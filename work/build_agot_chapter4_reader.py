#!/usr/bin/env python3
"""Build Chapter 4 (EDDARD) close-reading Markdown."""

from __future__ import annotations

import json
from pathlib import Path

from agot_extract import PDF, extract_range
from build_agot_chapter3_reader import VOCAB as BASE_VOCAB
from build_agot_prologue_reader import english_names, term_present


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "王室队伍像金银与钢铁组成的河流涌入Winterfell，规模与色彩先于个人面孔展示王权。",
    "Ned认出Jaime Lannister和烧伤面孔的Sandor Clegane，并据位置辨认出王储Joffrey与Tyrion Lannister。",
    "队伍前方体形巨大的国王Robert仍认得Ned，先用响亮笑声和旧日昵称打破正式场面。",
    "Ned回想十五年前两人并肩作战时，Robert精瘦强壮、挥舞战锤，是令人生畏的战士。",
    "如今Robert依然高大，却因饮食享乐变得肥胖、气喘，香水也掩不住衰败感。",
    "尽管心中震惊，Ned记得Robert既是朋友也是国王，只以正式礼仪欢迎他进入Winterfell。",
    "Cersei Lannister带着孩子下车，王室与Stark家庭完成公开问候，众人都在观看。",
    "礼节刚结束，Robert便要求Ned带他去crypt祭拜，显示他仍把Lyanna置于首要位置。",
    "Ned因Robert记得Lyanna而感动，取灯亲自领路，不让随从陪同。",
    "两人走下曲折石阶进入crypt；Ned发现身边的国王已与记忆中的朋友大不相同。",
    "Ned礼貌询问Robert旅途是否顺利。",
    "Robert抱怨北方只有沼泽、森林和差劲旅店，还打趣一路没见到传说中的女人。",
    "Ned以玩笑回应，说她们也许害羞躲着；地下寒气正逐渐增强。",
    "Robert继续抱怨夏末下雪，用夸张语气嘲笑北方气候。",
    "Ned解释夏末小雪很常见，通常不造成大麻烦。",
    "Robert咒骂所谓“小雪”，无法想象真正冬天，并问Ned为何愿意居住在这种地方。",
    "Ned承认冬季严酷，却说Stark总能坚持下去。",
    "Robert邀请Ned到南方感受夏天，热烈描绘Highgarden、Oldtown、Arbor等温暖丰饶之地。",
    "Ned记得Robert一向欲望旺盛、懂得享乐；他自己性情不同，因此只简短回应。",
    "Ned礼貌提醒他们来到地下是为Lyanna，并用灯光照出crypt中的石像。",
    "Ned在前引路，Robert沉默跟随，在地下寒气中发抖。",
    "历代Lord of Winterfell石像膝上横放铁剑，用来安抚亡灵；最古老坟墓的剑已锈蚀消失。",
    "Ned停在crypt深处，前方仍有为未来死亡者预留的空墓穴。",
    "Robert在Lyanna墓前跪下低头默哀。",
    "相邻三座墓分别属于Ned的父亲Rickard、兄长Brandon和妹妹Lyanna，石像保存家族死亡。",
    "Brandon二十岁时奉Mad King Aerys之命被勒死，原本属于他的婚姻和继承都随之中断。",
    "Lyanna十六岁去世，石像无法还原她的美；Ned对她的爱与悲伤仍然强烈。",
    "Robert说Lyanna本人比石像更美，并抱怨她不该被安葬在阴冷地下。",
    "Ned回答Lyanna属于Winterfell，这里就是她应在的位置。",
    "Robert想象她应该葬在有阳光、雨水和花香的山丘上，反映他理想化的悼念方式。",
    "Ned提醒Robert，自己在Lyanna临终时陪伴她；回到父兄身旁是她明确的愿望。",
    "Robert轻触石像脸颊，回忆曾发誓杀死Rhaegar，为Lyanna复仇。",
    "Ned提醒Robert，他确实完成了这个誓言。",
    "Robert苦涩回答，自己只杀了Rhaegar一次，仍不足以消解仇恨。",
    "叙述回顾Trident之战：Robert用战锤击碎Rhaegar胸甲，红宝石散入河水。",
    "Robert承认自己每晚在梦中再次杀死Rhaegar，即使千次死亡也嫌不够。",
    "Ned无法回应这种执念，转而建议回去，因为王后正在等待。",
    "Robert厌恶地咒骂妻子，却开始沿原路返回，脚步让crypt回声震动。",
    "Ned说自己没有忘记Jon Arryn，随后询问他的病情与死亡经过。",
    "Robert说Jon Arryn发病极快，前不久还健康地观看tourney，两周后便去世。",
    "Ned提到两人都如同失去父亲，并询问Lysa如何承受悲痛。",
    "Robert说Lysa几乎被悲伤逼疯，拒绝让儿子由Tywin Lannister收为ward，并连夜逃回Eyrie。",
    "Ned认为把孩子交给Tywin极不安全，但没有公开说出，以免旧伤再次引发争执。",
    "Robert抱怨六岁且体弱的Robert Arryn如今继承Eyrie，认为由Tywin教养能使他坚强。",
    "Ned主动提出由自己收养男孩，认为Lysa与Catelyn的姐妹关系会让她接受。",
    "Robert称赞提议，却说为时已晚：Tywin已同意，Lysa的拒绝令Lannister家族蒙羞。",
    "Ned明确表示自己更关心外甥的安危，而非Lannister的骄傲。",
    "Robert用关于婚姻的粗俗玩笑回应，笑声在墓穴中回荡。",
    "两人继续穿过石柱；Robert搂住Ned肩膀，开始解释自己为何远道而来。",
    "Ned其实已有猜测，却以玩笑说Robert只是为了享受他的陪伴。",
    "Robert说长城已屹立数千年，Mance Rayder不足为惧；他真正关心的是Jon Arryn死后留下的职位。",
    "Ned刚想提Jon Arryn的儿子。",
    "Robert打断：男孩只继承Eyrie和收入，不能自动继承父亲的王国职位。",
    "Ned惊讶地停步，指出House Arryn历来担任Warden of the East，这个头衔应与Eyrie领地相连。",
    "Robert说等男孩成年或许归还荣誉，但当前必须交给能指挥军队的人。",
    "Ned主张和平时期头衔主要是荣誉，应为Jon Arryn的儿子保留，至少以此回报其父的服务。",
    "Robert不悦，认为Jon的服务本就是臣子义务，而自己不能让半数王国军队由病弱幼童名义统领。",
    "Ned说自己永远服从国王；这是身份要求他说的话，而非内心完全认同。",
    "Robert几乎没听见，转而怀念两人在Eyrie的少年岁月，感叹身边无人真正理解自己。",
    "Ned温和表示理解。",
    "Robert确认Ned可能是唯一理解他的人，正式提出任命Ned为Hand of the King。",
    "Ned单膝跪下；这个邀请并不意外，因为他早已猜到Robert来访的真正目的。",
    "但成为Hand是Ned最不想要的结果。",
    "Ned以自己不配为由试图推辞。",
    "Robert说这不是荣誉性奖励，而是需要Ned治理王国、约束国王并阻止其愚行。",
    "Ned引用俗语：国王负责梦想，Hand负责把梦想建成现实。",
    "Robert用低俗版本改写这句俗语，自己大笑，却发现Ned没有笑。",
    "Robert的笑声渐止，Ned仍然跪着；Robert抱怨他连配合笑一下都不肯。",
    "Ned平静地用北方严寒会让笑声冻结在喉咙里的故事解释Stark为何缺少幽默。",
    "Robert邀请Ned南下共同守住王国，并提出让Joffrey与Sansa订婚，以完成自己与Lyanna未能建立的家族联结。",
    "这项婚约才真正让Ned意外；他首先指出Sansa只有十一岁。",
    "Robert说十一岁已足以订婚，婚礼可以等待几年，并催Ned起身答应。",
    "Ned礼貌表示荣幸，却请求时间考虑这些突然而重大的安排。",
    "Robert允许他与Catelyn商量，但催促不要拖太久，并粗鲁有力地把Ned拉起。",
    "Ned在crypt中产生强烈不祥预感：他属于北方与Winterfell，不愿离开，石像的盲眼仿佛正在注视。",
]


KEY_NOTES = {
    1: "`river of gold and silver and polished steel`把车队写成流动财富与武力，王室权力先以物质规模抵达。",
    3: "Robert第一声笑让Ned认出旧友，随后外貌差异才展开；声音比身体更保留过去。",
    5: "重复的`perfume`与体重描写故意破坏英雄形象，Ned看到的是时间和享乐留下的痕迹。",
    6: "Ned压下真实反应，选择合乎礼法的话；私人友谊已经被君臣关系包围。",
    8: "Robert把祭拜Lyanna置于王后、孩子和宴会之前，显示这段旧爱仍支配他的情感秩序。",
    10: "`this king he scarcely recognized`同时指外貌陌生与身份变化：朋友已经成为需要礼貌应对的国王。",
    17: "Stark的自我定义不是不受苦，而是`endure`；家族箴言在这里转化为生存态度。",
    18: "Robert列举南方景色和女人，语言丰盛外放，与crypt的寒暗和Ned的克制形成对照。",
    22: "铁剑既象征领主身份，也被认为能约束亡灵；锈蚀消失让古老秩序显出脆弱。",
    23: "为未来领主预留的空墓把政治邀请置于死亡时间轴中，Ned的任何选择最终都通向这里。",
    25: "三座并列墓穴把Ned的私人失去集中可视化，也解释他为何对旧战争不愿轻易浪漫化。",
    28: "Robert爱的是记忆中的Lyanna，甚至想替她选择墓地；Ned掌握她临终意愿，两种哀悼因此冲突。",
    31: "`promise me`未在本段解释内容；无剧透阅读应保留这个未完成信息，而不是提前填答案。",
    35: "红宝石散入河水把历史战役压缩成传奇画面，Robert却仍停留在无法结束的私人仇恨中。",
    36: "反复梦杀说明复仇没有治疗失去；胜利结束了战斗，却没有结束Robert的心理时间。",
    40: "Jon Arryn从健康到死亡只隔两周，速度本身构成疑问，但当前人物把它描述为疾病。",
    42: "Lysa的夜逃既可视为悲伤失控，也可视为保护孩子；本章没有足够信息裁定。",
    43: "Ned的内心判断与公开沉默分开，显示他知道旧政治创伤可能因一句话重新流血。",
    48: "Robert用笑话化解关于儿童监护与Lannister权力的严重分歧，是他常见的逃避方式。",
    51: "Robert主动降低Mance威胁的重要性，是为了把谈话转向他真正需要Ned解决的王国职位。",
    53: "Robert明确区分世袭财产与国王任命：儿子继承领地，不自动继承父亲的国家权力。",
    58: "`words he had to say`让效忠誓言出现裂缝：形式绝对，内心仍保留判断。",
    61: "任命在友情语言中提出，但Hand是国家最高责任之一；私人信任与政治负担被绑在一起。",
    63: "单句独段直接切开礼仪：Ned知道邀请合理，却明确不想接受。",
    65: "Robert不是给Ned体面职位，而是公开承认自己需要有人替他工作并限制他。",
    67: "低俗俗语把宏大的王权分工拉回身体需求，既表现Robert的幽默，也暴露他对统治的懒散。",
    71: "Hand任命后紧接婚约，使Ned的公共职责和家庭未来同时被王权重新安排。",
    72: "Robert把婚姻理解为修复自己未能与Lyanna成婚的方式，孩子因而承受上一代未完成愿望。",
    75: "终段把Ned的归属感放在墓穴中表达：离开北方不仅是旅行，而像走向已经预留的空墓。",
}


STAGES = [
    (1, 9, "本段以Ned视角比较记忆中的Robert与眼前国王，让私人重逢始终受到礼仪和权力约束。"),
    (10, 24, "本段借进入crypt的空间移动对照南北性格，并让活人逐步走入Stark家族的死亡记忆。"),
    (25, 38, "本段围绕Lyanna、Rhaegar与旧战争展示两种哀悼：Ned尊重遗愿，Robert反复沉浸于复仇。"),
    (39, 51, "本段从Jon Arryn的病逝转向遗属、监护和职位问题，私人悲痛迅速显出政治后果。"),
    (52, 61, "本段区分世袭领地与王室任命，并通过Robert的怀旧逐步引出真正请求。"),
    (62, 75, "本段围绕Hand任命与婚约展开；Robert用友情和家庭愿景邀请，Ned则以不祥预感回应。"),
]


BACKGROUNDS = {
    2: "**文本事实：** Jaime Lannister属于Kingsguard；Sandor Clegane担任王子Joffrey的护卫。",
    6: "**文本事实：** Robert既是Ned的旧友也是国王，公开场合必须以`Your Grace`等君臣礼仪相待。",
    8: "**文本事实：** Lyanna Stark是Ned的妹妹，也是Robert未能成婚的旧日未婚妻。",
    22: "**文本事实：** Winterfell的crypt安葬历代Stark领主，石像与铁剑属于古老丧葬习俗。",
    25: "**文本事实：** Rickard、Brandon和Lyanna是Ned在旧战争前后失去的父亲、兄长与妹妹。",
    26: "**文本事实：** Aerys Targaryen下令处死Brandon；Catelyn原本与Brandon订婚，后来嫁给Ned。",
    31: "**文本事实：** Ned在Lyanna临终时陪伴她，并按其意愿把遗体带回Winterfell。承诺内容当前未说明。",
    35: "**文本事实：** Robert在Trident之战中亲手杀死Rhaegar Targaryen，这场胜利是旧战争的关键节点。",
    42: "**文本事实：** Lysa是Jon Arryn遗孀；其六岁儿子Robert Arryn继承Eyrie。",
    44: "**文本事实：** ward由另一贵族家族抚养，可兼具教育、结盟与政治控制意义。",
    51: "**文本事实：** Jon Arryn生前同时担任Hand of the King与Warden of the East；两者都是国王授予的重要职位。",
    53: "**文本事实：** Eyrie与收入可世袭；Warden of the East涉及军事统帅权，需国王任命。",
    61: "**文本事实：** Hand of the King是国王最重要的行政代理，可制定法律、指挥军队并代王处理事务。",
    71: "**文本事实：** Joffrey是Robert的继承人，Sansa是Ned十一岁的长女；此处提出的是未来婚约。",
}


EXTRA_VOCAB = [
    ("flank", "/flæŋk/", "v.", "位于……两侧；护卫侧翼", "军事与队列用语"),
    ("girth", "/ɡɜːrθ/", "n.", "腰围；腹围", "此处委婉指Robert肥胖"),
    ("scarcely", "/ˈskeəsli/", "adv.", "几乎不；勉强", "`scarcely recognized`"),
    ("crypt", "/krɪpt/", "n.", "地下墓室", "Winterfell家族墓穴"),
    ("bog", "/bɒɡ/", "n.", "沼泽；泥炭地", "Robert抱怨北方地貌"),
    ("jest", "/dʒest/", "v./n.", "开玩笑；笑谈", "较文学化"),
    ("endure", "/ɪnˈdjʊər/", "v.", "忍受并坚持；熬过", "Stark面对冬季的态度"),
    ("subterranean", "/ˌsʌbtəˈreɪniən/", "adj.", "地下的", "形容crypt寒气"),
    ("unsealed", "/ʌnˈsiːld/", "adj.", "未封闭的", "为未来死亡者预留的空墓"),
    ("surpassing", "/səˈpɑːsɪŋ/", "adj.", "非凡的；无比的", "`surpassing loveliness`"),
    ("linger", "/ˈlɪŋɡər/", "v.", "停留；久久不离", "目光或情绪持续"),
    ("ford", "/fɔːrd/", "n.", "浅滩；可涉水过河处", "Trident战场地形"),
    ("warhammer", "/ˈwɔːrhæmər/", "n.", "战锤", "Robert的标志性武器"),
    ("sicken", "/ˈsɪkən/", "v.", "患病；病情加重", "`sicken quickly`"),
    ("tourney", "/ˈtʊərni/", "n.", "比武大会", "tournament的古风缩写"),
    ("wardship", "/ˈwɔːrdʃɪp/", "n.", "受监护状态；监护安排", "贵族儿童政治安排"),
    ("brusquely", "/ˈbrʌskli/", "adv.", "唐突生硬地", "Robert打断Ned"),
    ("unbidden", "/ʌnˈbɪdən/", "adj./adv.", "未经邀请地；不由自主地", "话语或记忆自行涌出"),
    ("dispense justice", "/dɪˈspens ˈdʒʌstɪs/", "phr.", "主持司法；施行裁决", "Hand代王行使权力"),
    ("foreboding", "/fɔːrˈbəʊdɪŋ/", "n.", "不祥预感", "尚无具体证据的强烈担忧"),
    ("betrothal", "/bɪˈtrəʊðəl/", "n.", "订婚；婚约", "贵族家族政治安排"),
]

VOCAB = BASE_VOCAB + EXTRA_VOCAB


def note(order):
    if order in KEY_NOTES: return KEY_NOTES[order]
    return next(t for s,e,t in STAGES if s <= order <= e)


def background(order):
    return BACKGROUNDS.get(order, "本段没有新增必须补充的世界观设定；重点在Ned与Robert的关系、旧战争记忆或职位谈判。")


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
        "# *A Game of Thrones* Chapter 4 — EDDARD 逐段精读","",
        "> **阅读模式：** 无剧透｜人物姓名保留英文｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        "> **文本范围：** 原 PDF 第 40–48 页，共 75 个正文段落","",
        "## 本章导读","",
        "King Robert率王室队伍抵达Winterfell，却立即要求Ned陪他前往Stark家族crypt祭拜Lyanna。两位旧友在墓穴中谈论旧战争、Jon Arryn之死与王国职位，Robert最终邀请Ned出任Hand of the King，并提出Joffrey与Sansa的婚约。本章核心是记忆中的友谊如何被现实王权重新塑形：Robert用亲情和怀旧提出请求，Ned却在家族死者之间感到强烈不祥。","",
        "## 人物表","","| 人物 | 当前身份与关系 |","|---|---|",
        "| Eddard “Ned” Stark | 本章视角人物；Lord of Winterfell |",
        "| Robert Baratheon | King；Ned的旧友与君主 |",
        "| Lyanna Stark | Ned已故妹妹，Robert一直怀念的人 |",
        "| Jon Arryn | 两人共同的foster father、前任Hand，刚去世 |",
        "| Cersei Lannister | Robert的王后 |","",
        "## 专名与职位","","| 英文 | 中文解释 |","|---|---|",
        "| crypt | Winterfell地下家族墓穴 |",
        "| Hand of the King | 国王之手；协助并代理国王处理政务的最高职位 |",
        "| Warden of the East | 东境守护；涉及东部军队统帅权 |",
        "| Kingsguard | 御林铁卫；保护王室的誓言骑士 |",
        "| betrothal | 贵族婚约；Robert提议Joffrey与Sansa订婚 |","",
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
        "Chapter 4把政治任命放在家族墓穴中完成。Robert从外表到性格都与Ned记忆中的英雄不同，却仍真诚依赖这位旧友；Ned仍爱Robert，却无法忽略君臣身份、Lannister影响与旧战争伤口。Hand任命和子女婚约表面上把两家结合得更紧，实际上要求Ned离开最能定义他的北方空间。终段的foreboding不是已被解释的预言，而是人物对归属被撕动的身体直觉。","",
        "### 关键对照","",
        "- **记忆中的Robert／眼前的Robert：** 战士英雄变成肥胖国王，但笑声和对Lyanna的执念没有改变。",
        "- **南方夏景／北方crypt：** Robert向往享乐与温暖，Ned把身份建立在严冬、祖先和坚持之上。",
        "- **友情／君臣：** 两人说旧日笑话，Ned却必须跪下并使用礼仪语言。",
        "- **荣誉／负担：** Robert称Hand为需要完成工作的位置，Ned准确感到它会重塑整个家庭。",
        "- **婚约／旧爱：** Joffrey与Sansa的未来被用来完成Robert未能与Lyanna建立的家族连接。","",
        "### 当前仍未解答的问题","",
        "1. Jon Arryn为何在短短两周内从健康转为死亡？",
        "2. Lysa为何如此坚决地拒绝Tywin的wardship并连夜返回Eyrie？",
        "3. Robert准备把Warden of the East交给谁？",
        "4. Ned是否会接受Hand任命和婚约？",
        "5. Ned最后的不祥预感来自哪些尚未被他说清的担忧？","",
        "以上问题不使用后文章节答案。","","## 词汇总表","","| 词语 | 音标 | 词性 | 核心释义 |","|---|---|---|---|",
    ]
    all_text=' '.join(b['text'] for b in blocks); seen=set()
    for t,ipa,pos,m,_ in VOCAB:
        if t not in seen and term_present(t,all_text): lines.append(f"| `{t}` | {ipa} | {pos} | {m} |"); seen.add(t)
    lines += ["","## 使用说明","","- 人物姓名一律保留原始英文。","- 可使用如 `CH04-P046-061` 的段落编号继续提问。","- 背景讲解只采用截至当前段落可知的信息。",""]
    return '\n'.join(lines)


def build_map(blocks):
    records=[]
    for b,s in zip(blocks,SUMMARIES,strict=True):
        o=b['order']; records.append({"id":b['id'],"page":b['page'],"end_page":b['end_page'],"type":"paragraph","order":o,"original_text":b['text'],"translation":"","paragraph_explanation_zh":s,"reading_note_zh":note(o),"background_note_zh":background(o),"bbox":[0,0,0,0],"confidence":"high","refs":[],"insert_after":b['id']})
    all_text=' '.join(b['text'] for b in blocks); glossary=[]; seen=set()
    for t,_,_,m,n in VOCAB:
        if t not in seen and term_present(t,all_text): glossary.append({"term":t,"translation":m,"note":english_names(n)}); seen.add(t)
    return {"paper":{"title":"A Game of Thrones — Chapter 4 (EDDARD)","author":"George R. R. Martin","source_type":"pdf","language":"en","source_path":str(PDF),"pdf_page_range":[40,48],"reader_mode":"spoiler-free close reading; English personal names"},"blocks":records,"pages":[{"page":p,"block_ids":[b['id'] for b in blocks if b['page']<=p<=b['end_page']]} for p in range(40,49)],"figures":[],"glossary":glossary}


def main():
    blocks=extract_range(40,48,'EDDARD','CH04')
    if len(blocks)!=len(SUMMARIES): raise RuntimeError((len(blocks),len(SUMMARIES)))
    (OUT/'source_maps').mkdir(parents=True,exist_ok=True); (OUT/'notes').mkdir(parents=True,exist_ok=True)
    (OUT/'Chapter_04_EDDARD_精读.md').write_text(build_markdown(blocks),encoding='utf-8')
    (OUT/'source_maps'/'Chapter_04_source_map.json').write_text(json.dumps(build_map(blocks),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'notes'/'Chapter_04_notes.md').write_text('# Chapter 4 extraction notes\n\n- Source: selectable-text PDF pages 40–48.\n- 75 paragraph blocks after cross-page repair.\n- Personal names remain in original English.\n- Commentary is spoiler-free; no full translation requested.\n',encoding='utf-8')


if __name__=='__main__': main()
