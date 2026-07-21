#!/usr/bin/env python3
"""Build Chapter 6 (CATELYN) close-reading Markdown."""

from __future__ import annotations

import json
from pathlib import Path

from agot_extract import PDF, extract_range
from build_agot_chapter5_reader import VOCAB as BASE_VOCAB
from build_agot_prologue_reader import english_names, term_present


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "Catelyn的bedchamber是Winterfell主堡中最温暖的房间，她很少需要生火，石墙内的温泉管道提供热量。",
    "持续温暖让她想起Riverrun的阳光；即使多年生活在北方，她仍会借身体感觉返回故乡。",
    "夫妻亲密结束后，Ned像往常一样起身开窗，让刺骨夜风进入温暖房间。",
    "Ned赤身站在黑暗与寒风前，Catelyn裹紧毛皮看着他；两人对冷热的不同需求形成性格对照。",
    "Ned转身宣布自己会拒绝Robert的Hand任命，声音疲惫却坚定。",
    "Catelyn立刻坐起，强调他不能、也不应该拒绝。",
    "Ned说自己的责任在北方，个人也完全不想成为Hand。",
    "Catelyn警告国王不是普通朋友；拒绝可能被理解为轻蔑，连婚约等“荣誉”也可能变成危险。",
    "Ned不相信Robert会伤害自己家人，依赖两人过去比兄弟更亲密的关系。",
    "Catelyn区分过去的男人与现在的国王，并想到direwolf和鹿角，认为Ned低估了改变。",
    "Ned苦笑着重复“荣誉”，显然把任命视为负担。",
    "Catelyn说至少在Robert看来，这些确实是荣誉。",
    "Ned反问Catelyn自己是否也如此看。",
    "Catelyn愤怒承认：国王让继承人与Sansa联姻、让Ned代行王权，是家族难得的提升。",
    "Ned再次指出Sansa只有十一岁，并对Joffrey明显有所保留。",
    "Catelyn替他说完：Joffrey是王储；她自己十二岁时也已与Brandon订婚。",
    "Brandon的名字让Ned苦涩，觉得死去的兄长更适合处理权力和荣耀。",
    "Catelyn说Brandon已死，责任之杯已经传到Ned手中，他必须饮下。",
    "Ned转向窗外，沉默凝视黑暗，月光照在他身上。",
    "Catelyn因看见丈夫痛苦而软化；她回想自己原本要嫁Brandon，却依习俗嫁给Ned并逐渐建立爱情。",
    "她正要走近Ned，突然而响亮的敲门打断私密谈话。",
    "守卫Desmond在门外报告Maester Luwin请求紧急觐见。",
    "Ned询问守卫是否已转达不得打扰的命令。",
    "Desmond确认转达，但Luwin仍坚持。",
    "Ned只得允许他进入。",
    "Ned穿上厚袍；Catelyn这才意识到房间已经很冷，也穿衣并要求关窗。",
    "Ned心不在焉地点头，Maester Luwin被带进房间。",
    "Luwin身材矮小、通身灰色，目光敏锐；maester锁链由不同金属环组成，象征所学领域。",
    "门关后Luwin才说，有一件东西被秘密留给Catelyn。",
    "Ned不悦地追问是谁送来、是否有骑手，为何自己没有收到报告。",
    "Luwin说没有骑手，只有一个木雕盒趁他睡觉时被放在observatory桌上。",
    "Catelyn确认他说的是木盒。",
    "盒内是一块来自Myr的精良新镜片，制作精美且价值不低。",
    "Ned没有耐心听工艺细节，追问镜片为何与自己妻子有关。",
    "Luwin说自己也问了同一问题，显然礼物表面之下另有含义。",
    "Catelyn在毛皮下发抖，想到lens能帮助人看得更清楚。",
    "Luwin同意这个象征，并触摸maester锁链，确认送礼者想让他们看见被遮蔽的信息。",
    "Catelyn的不安再次升起，问对方究竟想让他们看清什么。",
    "Luwin取出藏在盒内的卷纸，说明真正信息就在镜片之外。",
    "Ned伸手要求查看信件。",
    "Luwin没有递给他，因为信件标明也不是写给Ned，而是只供Catelyn阅读。",
    "Catelyn紧张点头；Luwin把带蓝色封蜡的卷纸放在床边，随后准备退出。",
    "Ned命令Luwin留下，并从Catelyn脸色看出她害怕，追问信件为何让她发抖。",
    "Catelyn承认恐惧，赤身取过信件并认出蓝蜡上的House Arryn月鹰纹章，已经顾不上遮掩身体。",
    "Ned脸色变沉，命令她打开。",
    "Catelyn掰开封印。",
    "文字起初毫无意义，随后她认出Lysa使用了姐妹儿时共同发明的秘密语言。",
    "Ned询问她能否读懂。",
    "Catelyn承认可以。",
    "Ned要求她把内容说出来。",
    "Luwin提出自己或许应回避姐妹间的私密信息。",
    "Catelyn让他留下，因为接下来需要他的判断；她起身准备生火。",
    "Luwin移开视线，连Ned也惊讶她在maester面前赤身行动。",
    "Catelyn解释自己只是点火，随后披上dressing gown跪到壁炉前。",
    "Ned刚想以Luwin在场提醒她。",
    "Catelyn说Luwin接生过她所有孩子，现在不是讲虚假羞耻的时候，并开始烧掉信件。",
    "Ned抓住她手臂拉起，急切追问信中内容。",
    "Catelyn僵住，低声把它定义为一项需要足够智慧才能听懂的警告。",
    "Ned搜索她的表情，催她继续。",
    "Catelyn说Lysa声称Jon Arryn遭到谋杀。",
    "Ned手指收紧，立即追问凶手。",
    "Catelyn回答是Lannisters，尤其是王后。",
    "Ned松手，Catelyn手臂已留下红印；他震惊到声音微弱。",
    "Catelyn认为Lysa虽冲动，但秘密语言、盒子和焚信安排都经过精心策划。",
    "她说Lysa冒如此风险必有超越怀疑的依据，并由此得出Ned必须南下调查的结论。",
    "Ned却得出相反结论：他只信任眼前的家人和北方，南方处处是谎言与危险。",
    "Luwin提醒Hand必须拥有强大力量；若Jon Arryn被杀，新任Hand更应查清真相。",
    "Ned无助地环顾房间；Catelyn心疼他，却知道自己不能代他逃避决定。",
    "Ned咒骂两人把他推向南方，转身望窗外。",
    "Luwin提醒这是不同的时代、不同的国王，暗示Ned不必重复父兄命运。",
    "Ned低落接受现实，并开始安排Catelyn留守Winterfell，与Robb和Rickon同在。",
    "Catelyn听见要分离，心中像灌入冷风，立刻拒绝。",
    "Ned用不容争辩的语气说明她必须代为治理北方，并教导Robb将来继承。",
    "Luwin低声希望Ned真正继位不会发生在许多年内。",
    "Ned要求Luwin像支持自己一样支持Catelyn，成为她处理大小事务的顾问。",
    "Luwin郑重点头；沉默后，Catelyn鼓起勇气询问其他孩子如何安排。",
    "Ned抱住她，先说Rickon太小，必须留在Winterfell。",
    "Catelyn颤抖着说自己无法承受与更多孩子分离。",
    "Ned坚持必须这样：Sansa需南下完成婚约，Arya也要同行学习宫廷生活，Bran则能接触南方骑士。",
    "Catelyn认为Sansa会在南方发光，Arya确实需要礼仪训练，但想到失去他们仍然痛苦。",
    "Ned说自己八岁便被送往Eyrie；Bran可缓和Robb与Joffrey的紧张，且这次随王室车队南下比海路更安全。",
    "Catelyn承认他有道理，却仍难以接受自己将同时失去四个孩子。",
    "Ned吻去她将落的眼泪，感谢她接受这项痛苦安排，并承认事情确实很难。",
    "Luwin询问Jon Snow应当如何安排。",
    "Catelyn听见名字立即绷紧；Ned察觉她的愤怒并松开拥抱。",
    "Catelyn知道许多贵族有bastards，甚至为他们提供生活；真正刺痛她的是Ned把Jon带回婚姻家庭。",
    "Ned不仅承认Jon，还让他与婚生子女同桌、同训；这使Catelyn每天都面对丈夫不忠的证据。",
    "更深伤口来自Ned拒绝透露Jon母亲身份；城堡流言说她可能是Ashara Dayne。",
    "Catelyn唯一一次追问Ashara时，Ned罕见地吓到她，命令她永远不要再问Jon。",
    "她由Ned的沉默推断他曾强烈爱过Jon母亲，并长期无法说服他把Jon送走。",
    "Ned说Jon与Robb感情亲近，原本希望Jon能留在Winterfell。",
    "Catelyn打断并拒绝：Jon是Ned的儿子，不是她的，她不会在Ned离开后让Jon留下。",
    "Ned露出痛苦神情，指出自己不能带Jon去宫廷，那里不会给bastard位置。",
    "Catelyn硬起心肠，用Robert把bastards留在宫廷之外作比较，拒绝被Ned无声恳求动摇。",
    "Ned愤怒反驳：Robert的孩子正是被Cersei挡在宫廷外；他不愿同样抛开Jon。",
    "Ned还想继续争吵，Luwin及时提出另一种解决办法。",
    "Luwin透露Jon希望加入守夜人，Ned对此十分震惊。",
    "Catelyn沉默让Ned自行判断，却在心中因可能摆脱Jon而感到带罪恶感的释然。",
    "Luwin强调在长城服役具有很高荣誉。",
    "Ned想到bastard也能在守夜人晋升，且誓言会阻止Jon留下可能威胁Robb后代的子嗣。",
    "Luwin承认这是艰难牺牲，但当前时代艰难，而且Jon的道路未必比Ned为婚生孩子安排的更残酷。",
    "Catelyn想到自己将失去三个南下孩子，在此刻很难继续沉默。",
    "Ned长久望窗思考，最终叹息同意Jon的选择。",
    "Luwin询问何时告诉Jon。",
    "Ned说等必要时再告诉；出发准备需两周，他希望Jon先享受最后几天童年，因为夏天和童年都会很快结束。",
]

# The PDF page break between pp.61–62 falls inside one continuous paragraph.
SUMMARIES[63] = (
    "Catelyn认为Lysa虽冲动，但秘密语言、盒子和隐藏方式都经过精心策划；"
    "冒死传信说明她自认掌握的不只是怀疑，因此Catelyn得出Ned必须南下调查的结论。"
)
del SUMMARIES[64]


KEY_NOTES = {
    1: "温泉管道让私人房间成为南方般温暖的避难所，后续政治消息不断把寒冷重新带进来。",
    3: "亲密结束后立刻进入政治争论，说明Hand任命无法留在公共空间，已经进入婚姻核心。",
    8: "Catelyn把`friend`与`king`分开：私人情感不能自动约束拥有制度权力的人。",
    10: "`You knew the man. The king is a stranger`概括本章争论，也回应Chapter 4中Ned几乎认不出Robert。",
    14: "Catelyn并非单纯追逐地位；她把王室“荣誉”理解为家族安全与无法轻易拒绝的政治现实。",
    18: "`the cup has passed`把继承责任写成必须饮下的苦酒，Brandon的死亡仍在决定Ned的人生。",
    20: "婚姻起于替代已故兄长，却在多年共同生活中变成真实爱情；这让即将分离更有重量。",
    28: "Luwin的灰色外貌与多金属锁链并置：个人低调，知识范围却广。",
    33: "lens既是昂贵实物，也是阅读指令：不要只看盒子表面，而要寻找隐藏信息。",
    36: "Catelyn首先读出象征含义，显示她在家庭政治与暗示解读上比Ned更敏锐。",
    41: "信件只给Catelyn且使用秘密方式，使信息权暂时不属于领主Ned，而属于姐妹关系。",
    44: "她赤身取信不是情色描写，而是恐惧压过羞耻；身体防御和社交礼节同时被放弃。",
    47: "姐妹童年密码把私人亲密变成政治保密工具，家庭记忆获得情报功能。",
    56: "烧信保护Lysa和收信者，也意味着此后判断依赖记忆与信任，失去可反复核验的原件。",
    60: "`Jon Arryn was murdered`用极短句改变此前所有关于自然病逝的理解，但仍只是Lysa的指控。",
    62: "指控对象从广义Lannisters收束到queen，使Robert的婚姻与Jon Arryn之死潜在相连。",
    64: "Catelyn以传递方式证明Lysa认真谨慎，这是可信度论证，却仍不能替代直接证据。",
    65: "同一警告导出相反策略：Catelyn认为必须进入权力中心调查，Ned认为应远离危险。",
    67: "Luwin把Hand权力解释成调查工具，从而把职位负担转化为保护家族的可能手段。",
    71: "Ned一旦接受南下，立即从情绪转入治理安排；职责思维帮助他承受个人不愿。",
    73: "Catelyn被要求成为北方实际治理者，说明她不是留在家中的被动配偶，而是权力代理人。",
    79: "孩子安排被政治逻辑逐一解释；父母的爱不能取消继承、婚约和教育要求。",
    83: "Ned感谢的是Catelyn承担分离与治理，不只是同意他的决定。",
    86: "Catelyn段落坦率承认她能容忍bastard存在，却不能容忍Jon被放进自己的家庭中心。",
    88: "未知母亲比已知不忠更具威胁，因为Catelyn无法衡量Ned曾经的感情。",
    89: "Ned唯一一次令Catelyn恐惧发生在Jon母亲问题上，这种异常反应加深她多年不安。",
    92: "`your son, not mine`为Catelyn划出明确边界，也把Jon再次变成无人愿意承担的孩子。",
    94: "Catelyn`armored her heart`说明她看见Ned痛苦，却主动压下同情；这是防御，不是无知。",
    98: "她的释然与羞耻同时存在，文本允许角色拥有不体面的真实感受而不替她粉饰。",
    100: "Ned同时看见守夜人的上升机会和誓言对子嗣的限制，家族继承风险进入判断。",
    103: "沉默思考后才同意，说明Ned并未把Jon送走视为轻松解决方案。",
    105: "Ned推迟告知是为了保留最后两周家庭平静，也意味着Jon的个人未来由成人在他缺席时决定。",
}


STAGES = [
    (1, 20, "本段在温暖bedchamber中展开Hand争论，Catelyn强调政治风险与家族机会，Ned强调北方职责与私人不愿。"),
    (21, 42, "本段用秘密木盒、lens和只给Catelyn的信逐层揭开隐藏信息，悬念来自物件与阅读权限。"),
    (43, 65, "本段从身体恐惧进入密信内容；Lysa的谋杀指控改变夫妻选择，却尚未得到独立证实。"),
    (66, 83, "本段把南下决定转换成北方治理与孩子分离方案，政治行动直接重排家庭。"),
    (84, 105, "本段集中处理Jon的归属：Ned的父爱、Catelyn的伤口和守夜人制度共同决定少年的道路。"),
]


BACKGROUNDS = {
    1: "**文本事实：** Winterfell建在温泉之上，热水通过墙内管道为部分房间供暖。",
    14: "**文本事实：** Hand任命和Joffrey–Sansa婚约会显著提高House Stark在王国政治中的位置。",
    16: "**文本事实：** Catelyn十二岁时与Brandon Stark订婚；Brandon死后她依习俗嫁给Ned。",
    28: "**文本事实：** maester锁链由不同金属环组成，每种金属对应其研究和掌握的领域。",
    33: "**文本事实：** Myr以精密lens工艺闻名；镜片在本章被用作“看清隐藏真相”的暗号。",
    42: "**文本事实：** House Arryn纹章为月鹰；封印说明信件声称来自Lysa。",
    47: "**文本事实：** Lysa与Catelyn幼年共同创造秘密语言，因此只有Catelyn能直接阅读。",
    60: "**当前证据：** Lysa在密信中声称Jon Arryn遭谋杀。此时尚无独立证据证明指控。",
    62: "**当前证据：** 密信把责任指向Lannisters与Cersei；这是指控，不是已被查实的事实。",
    73: "**文本事实：** Ned离开后Catelyn将代为治理北方，并培养Robb承担继承责任。",
    79: "**文本事实：** Sansa因婚约必须南下；Arya接受宫廷礼仪训练；Bran学习南方骑士文化。",
    86: "**文本事实：** 贵族可能承认并供养bastards，但把私生子带入婚生家庭共同抚养并不常见。",
    88: "**传闻：** Winterfell曾流传Ashara Dayne可能是Jon母亲；Ned从未确认。",
    99: "**文本事实：** 守夜人服务被视为荣誉道路，也接受bastards和其他缺乏继承位置的人。",
    100: "**文本事实：** 守夜人不得生育子女，因此Jon未来不会产生可与Robb后代竞争的合法家族支系。",
}


EXTRA_VOCAB = [
    ("bedchamber", "/ˈbedtʃeɪmbər/", "n.", "卧室；寝室", "较古风表达"),
    ("brook no argument", "/brʊk nəʊ ˈɑːɡjəmənt/", "phr.", "不容争辩", "brook作动词表示容忍"),
    ("observatory", "/əbˈzɜːrvətɔːri/", "n.", "观测室；天文台", "maester观察天空的房间"),
    ("lenscrafter", "/ˈlenzkrɑːftər/", "n.", "镜片工匠", "制作精密光学镜片"),
    ("seeming", "/ˈsiːmɪŋ/", "n.", "表象；外观", "`more than the seeming`"),
    ("avert", "/əˈvɜːrt/", "v.", "移开；避开", "`avert one’s eyes`"),
    ("false modesty", "/fɔːls ˈmɒdəsti/", "n.", "虚假的羞怯；不合时宜的矜持", "Catelyn拒绝社交遮掩"),
    ("cipher", "/ˈsaɪfər/", "n.", "密码；密文", "姐妹秘密书写方式"),
    ("impulsive", "/ɪmˈpʌlsɪv/", "adj.", "冲动的", "行动快于深思"),
    ("chafe", "/tʃeɪf/", "v.", "摩擦擦伤；磨痛", "锁链磨颈"),
    ("govern in my stead", "/ˈɡʌvərn ɪn maɪ sted/", "phr.", "代我治理", "stead表示位置或代理身份"),
    ("mute appeal", "/mjuːt əˈpiːl/", "n.", "无声恳求", "通过眼神而非话语"),
    ("solace", "/ˈsɒləs/", "n.", "安慰；慰藉", "常用于痛苦中的情感补偿"),
    ("refinement", "/rɪˈfaɪnmənt/", "n.", "礼仪教养；文雅训练", "此处指宫廷式行为规范"),
]

VOCAB = BASE_VOCAB + EXTRA_VOCAB


def note(order):
    source_order = order if order <= 64 else order + 1
    if source_order in KEY_NOTES: return KEY_NOTES[source_order]
    return next(t for s,e,t in STAGES if s <= source_order <= e)


def background(order):
    source_order = order if order <= 64 else order + 1
    return BACKGROUNDS.get(source_order, "本段没有新增必须补充的世界观设定；重点在夫妻决策、密信可信度、孩子安排或Jon的归属。")


def extract_blocks():
    blocks = extract_range(57,65,'CATELYN','CH06')
    left, right = blocks[63], blocks[64]
    if not (left['id'] == 'CH06-P061-064' and str(right['text']).startswith('To risk so much')):
        raise RuntimeError('Expected pp.61–62 cross-page paragraph was not found')
    left['text'] = str(left['text']) + ' ' + str(right['text'])
    left['end_page'] = right['end_page']
    del blocks[64]
    for order, block in enumerate(blocks, start=1):
        block['order'] = order
        block['id'] = f"CH06-P{int(block['page']):03d}-{order:03d}"
    return blocks


def vocab_for(text):
    seen=set(); out=[]
    for v in VOCAB:
        if v[0] not in seen and term_present(v[0],text): out.append(v); seen.add(v[0])
    return out


def source_label(b):
    return f"PDF p.{b['page']}" if b['page']==b['end_page'] else f"PDF pp.{b['page']}–{b['end_page']}"


def build_markdown(blocks):
    pages={}
    for b in blocks: pages.setdefault(b['page'],[]).append(b['id'])
    lines=[
        "# *A Game of Thrones* Chapter 6 — CATELYN 逐段精读","",
        "> **阅读模式：** 无剧透｜人物姓名保留英文｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        "> **文本范围：** 原 PDF 第 57–65 页，共 104 个正文段落","",
        "## 本章导读","",
        "Ned准备拒绝Hand任命，Catelyn则认为拒绝国王既危险又会错失家族机会。Maester Luwin带来的秘密木盒和Lysa密信改变争论：信中声称Jon Arryn遭Lannisters谋杀。夫妻最终决定Ned南下、Catelyn留守北方，并逐一安排孩子去留。最后，Jon加入守夜人的请求成为解决其归属冲突的艰难方案。","",
        "## 人物表","","| 人物 | 当前身份与作用 |","|---|---|",
        "| Catelyn Stark | 本章视角人物；主张Ned南下调查并接受Hand |",
        "| Eddard “Ned” Stark | 不愿离开北方，但必须作出家族与王国决定 |",
        "| Maester Luwin | Winterfell的maester，传递密信并参与决策 |",
        "| Lysa Arryn | Catelyn的妹妹，秘密写信指控Jon Arryn遭谋杀 |",
        "| Jon Snow | 未参与谈话，但其未来由三名成人讨论决定 |","",
        "## 关键物件与制度","","| 英文 | 中文解释 |","|---|---|",
        "| Myrish lens | Myr制造的镜片；既是礼物也是“看清真相”的提示 |",
        "| secret letter | 使用姐妹秘密语言、只供Catelyn阅读的密信 |",
        "| Hand of the King | 既带来危险，也提供调查Jon Arryn之死的权力 |",
        "| Night’s Watch | Jon可能获得荣誉与位置、但必须付出终身誓言的组织 |","",
        "## 段落目录","",
    ]
    for p,ids in pages.items(): lines.append(f"- [PDF 第 {p} 页：{ids[0]}–{ids[-1]}](#{ids[0].lower()})")
    lines += ["","---","","## 逐段精读",""]
    for b,s in zip(blocks,SUMMARIES,strict=True):
        o=b['order']; bid=b['id']; original=b['text']
        lines += [f'<a id="{bid.lower()}"></a>',f"### {bid}","",f"**来源：** {source_label(b)}","","**英文原段**","",f"> {original}","","**难词与短语**",""]
        v=vocab_for(original)
        if v:
            lines += ["| 词语 | 音标 | 词性 | 此处含义 | 用法提示 |","|---|---|---|---|---|"]
            for t,ipa,pos,m,n in v: lines.append(f"| `{t}` | {ipa} | {pos} | {m} | {english_names(n)} |")
        else: lines.append("本段没有新增的四级以上重点词；重点留意语气和上下文。")
        lines += ["","**这一段说了什么**","",s,"","**值得注意的地方**","",note(o),"","**背景与伏笔（无剧透）**","",background(o),"","[回到段落目录](#段落目录)","","---",""]
    lines += [
        "## 本章整体梳理","",
        "Chapter 6把一个任命问题变成全家的重新布局。Lysa密信并未直接证明谋杀，却让不接受Hand也不再等于安全：远离King’s Landing可能失去调查和自保能力。Ned与Catelyn从相反立场出发，最终共同承担不同职责——Ned南下进入风险中心，Catelyn留守治理北方。孩子们则被婚约、教育、继承和私生身份分别分配道路，几乎没有人能完全按个人愿望生活。","",
        "### 关键对照","",
        "- **温暖房间／寒冷窗风：** 私人安全不断被外部政治侵入。",
        "- **lens／密信：** 看清真相的象征与未经验证的指控同时出现。",
        "- **北方安全／南方权力：** Ned相信远离谎言更安全，Catelyn与Luwin认为必须拥有权力才能调查。",
        "- **婚生孩子／Jon：** 每个孩子都被安排未来，但Jon的选择同时被当作家族继承问题。",
        "- **父母决定／孩子意愿：** Jon主动提出守夜人，却仍由未让他在场的成人决定何时告知。","",
        "### 当前仍未解答的问题","",
        "1. Lysa的谋杀指控依据是什么？",
        "2. 密信和Myrish lens由谁秘密送入Winterfell？",
        "3. Ned接受Hand后将如何调查Lannisters？",
        "4. Jon得知成人已经接受其请求后会如何反应？",
        "5. 分居和孩子分离会如何改变Stark家庭？","",
        "以上问题不使用后文章节答案。","","## 词汇总表","","| 词语 | 音标 | 词性 | 核心释义 |","|---|---|---|---|",
    ]
    all_text=' '.join(b['text'] for b in blocks); seen=set()
    for t,ipa,pos,m,_ in VOCAB:
        if t not in seen and term_present(t,all_text): lines.append(f"| `{t}` | {ipa} | {pos} | {m} |"); seen.add(t)
    lines += ["","## 使用说明","","- 人物姓名一律保留原始英文。","- 可使用如 `CH06-P061-060` 的段落编号继续提问。","- 密信内容均标为人物指控，不提前当作已证实事实。",""]
    return '\n'.join(lines)


def build_map(blocks):
    records=[]
    for b,s in zip(blocks,SUMMARIES,strict=True):
        o=b['order']; records.append({"id":b['id'],"page":b['page'],"end_page":b['end_page'],"type":"paragraph","order":o,"original_text":b['text'],"translation":"","paragraph_explanation_zh":s,"reading_note_zh":note(o),"background_note_zh":background(o),"bbox":[0,0,0,0],"confidence":"high","refs":[],"insert_after":b['id']})
    all_text=' '.join(b['text'] for b in blocks); glossary=[]; seen=set()
    for t,_,_,m,n in VOCAB:
        if t not in seen and term_present(t,all_text): glossary.append({"term":t,"translation":m,"note":english_names(n)}); seen.add(t)
    return {"paper":{"title":"A Game of Thrones — Chapter 6 (CATELYN)","author":"George R. R. Martin","source_type":"pdf","language":"en","source_path":str(PDF),"pdf_page_range":[57,65],"reader_mode":"spoiler-free close reading; English personal names"},"blocks":records,"pages":[{"page":p,"block_ids":[b['id'] for b in blocks if b['page']<=p<=b['end_page']]} for p in range(57,66)],"figures":[],"glossary":glossary}


def main():
    blocks=extract_blocks()
    if len(blocks)!=len(SUMMARIES): raise RuntimeError((len(blocks),len(SUMMARIES)))
    (OUT/'source_maps').mkdir(parents=True,exist_ok=True); (OUT/'notes').mkdir(parents=True,exist_ok=True)
    (OUT/'Chapter_06_CATELYN_精读.md').write_text(build_markdown(blocks),encoding='utf-8')
    (OUT/'source_maps'/'Chapter_06_source_map.json').write_text(json.dumps(build_map(blocks),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'notes'/'Chapter_06_notes.md').write_text('# Chapter 6 extraction notes\n\n- Source: selectable-text PDF pages 57–65.\n- 104 paragraph blocks after cross-page repair.\n- The paragraph crossing PDF pp.61–62 was manually merged before stable IDs were assigned.\n- Personal names remain in original English.\n- Lysa’s allegations are labelled as claims, not verified facts.\n',encoding='utf-8')


if __name__=='__main__': main()
