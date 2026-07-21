#!/usr/bin/env python3
"""Build Chapter 7 (ARYA) close-reading Markdown."""

from __future__ import annotations

import json
from pathlib import Path

from agot_extract import PDF, extract_range
from build_agot_chapter6_reader import VOCAB as BASE_VOCAB
from build_agot_prologue_reader import english_names, term_present


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "Arya的针脚再次歪斜，第一句便把她放在一项反复失败、也不喜欢的女性训练中。",
    "她沮丧地比较Sansa整齐精美的刺绣；Sansa周围的女孩都在称赞她，Arya更显孤立。",
    "Arya担心Septa Mordane看出自己的不满，却发现septa正向Princess Myrcella展示Sansa作品。",
    "她尝试补救针脚后放下针，听见Sansa与Jeyne、Beth低声谈论某事。",
    "Arya突然插话，直接询问她们在谈什么。",
    "Jeyne吃惊后发笑，Sansa尴尬，Beth脸红，没人立刻回答。",
    "Arya再次坚持要她们告诉自己。",
    "Jeyne先确认Septa Mordane没在听，说明话题带有少女私密和越界意味。",
    "Sansa用温柔语气说她们在谈王子。",
    "Arya知道是Joffrey；她回想宴会座位，Sansa与王储同席，自己只陪年幼Tommen。",
    "Jeyne说Joffrey喜欢Sansa，还以自己似乎参与此事的口气感到骄傲。",
    "Beth梦想Joffrey会娶Sansa，使她成为整个王国的王后。",
    "Sansa优雅脸红；Arya苦涩地觉得姐姐连脸红都比自己漂亮。",
    "Arya引用Jon的评价，说Joffrey看起来像女孩。",
    "Sansa同情式地说Jon因bastard身份嫉妒Joffrey。",
    "Arya过于响亮地反驳Jon是她们的brother，声音打破塔楼安静。",
    "Septa Mordane抬头，严厉目光和天生适合皱眉的面孔让Arya感到压力。",
    "Sansa精准纠正Jon只是half brother，并向septa解释她们在谈王室婚约。",
    "Septa Mordane认可婚约是全家的荣誉，Myrcella则对紧张气氛有些不确定。",
    "Arya恼怒Sansa引来septa注意，索性把失败针线交给她检查。",
    "Septa Mordane反复说作品不合格，公开表示失望。",
    "所有人注视Arya；Sansa没有笑，Jeyne却窃笑，Arya羞耻到起身逃离。",
    "Septa Mordane在身后命令她回来，警告会告诉Catelyn，并说她在王室公主前让家族蒙羞。",
    "Arya在门口咬唇回头，泪水已流下，却仍没有返回座位。",
    "Myrcella不知如何反应，Septa Mordane则继续命令Arya立刻回来。",
    "Arya甜甜地说自己得去给马钉蹄铁，用不符合贵族女孩身份的工作故意刺激septa后离开。",
    "她觉得一切不公平：Sansa年龄更大、从母亲处得到美貌与才能，自己似乎只剩失败。",
    "Nymeria在楼梯下等她，听见脚步立刻起身，提供无条件欢迎。",
    "Arya解开Nymeria，幼狼兴奋轻咬她手；黄色眼睛在阳光中像两枚金币。",
    "Arya知道septa会告状，不能回房；她决定去看Robb和王子们练武，Nymeria紧跟。",
    "她想起连接armory与Great Keep的covered bridge有一扇能俯瞰练武场的窗。",
    "Arya气喘吁吁赶到时，Jon已懒散坐在窗台，Ghost在旁安静躺着。",
    "Jon好奇问她此刻是否应该练针线。",
    "Arya做鬼脸，说自己想看男孩们打斗。",
    "Jon微笑，邀请她过来一起看。",
    "Arya爬上窗台坐在Jon旁，下面练武场传来击打声、喘息和Ser Rodrik的喊声。",
    "让她失望的是只有年幼男孩练习；Bran和Tommen穿着厚重护具，用木质武器交手。",
    "Jon说这项活动只比针线稍微累一点，故意调侃她。",
    "Arya回敬说也比针线有趣一点；Jon笑着揉乱她的头发。",
    "Arya询问Jon为何不在场下练武。",
    "Jon半笑着说bastards不被允许弄伤年轻王子。",
    "他补充，王子在练武场受的瘀伤必须来自trueborn的剑。",
    "Arya惭愧自己没有想到；她一天内第二次意识到生活并不公平。",
    "她看Bran攻击Tommen，自信自己也能做得一样好，甚至比Bran更强。",
    "Jon以十四岁少年的权威打量她，说她太瘦，并捏了捏她手臂。",
    "Arya抽回手瞪他，Jon又揉乱她头发；两人继续观看，Bran一度占上风。",
    "Jon让Arya注意Prince Joffrey。",
    "Arya起初没看到，随后发现Joffrey与Robb在阴影下休息，正被随从围绕。",
    "Jon提示她观察Joffrey练习服上的纹章。",
    "Arya看见盾形刺绣把Baratheon王冠鹿与Lannister金狮并列。",
    "Jon说Lannisters骄傲到觉得单用王室纹章还不够，必须同时展示母系狮子。",
    "Arya反驳母亲一方同样重要。",
    "Jon笑着建议她也把Tully与Stark纹章结合，让父母两家同时出现在自己盾牌上。",
    "Arya想象狼叼鱼的滑稽图案，并指出女孩反正不能使用真正纹章作战。",
    "Jon总结两人的不公平：女孩拥有家徽却没有剑，bastards有剑却没有家徽；他相信Arya会比自己更擅长缝两家纹章。",
    "场下突然有人喊叫，Tommen穿着厚护具仰面倒地，像翻不过身的乌龟，Bran高兴绕圈。",
    "Ser Rodrik叫停并扶起Tommen，随后邀请Robb与Joffrey再比一场。",
    "刚练过一场、满身汗水的Robb立即欣然应战。",
    "Joffrey走进阳光，金发闪耀；他虽疲倦，却以王子姿态拒绝显弱。",
    "Theon Greyjoy突然嘲笑两人仍是children。",
    "Joffrey说Robb也许是孩子，自己却是prince，并厌烦用木剑拍打Starks。",
    "Robb反击Joffrey挨打更多，并问他是不是害怕。",
    "Joffrey以讽刺口气假装恐惧，拿Robb年龄开玩笑，Lannister随从随之发笑。",
    "Jon皱眉看着场下，直截了当地告诉Arya：Joffrey确实是个讨厌鬼。",
    "Ser Rodrik若有所思地问Joffrey究竟想提出什么。",
    "Joffrey要求使用live steel。",
    "Robb立即接受并警告Joffrey会后悔。",
    "Ser Rodrik按住Robb，拒绝使用真剑，愿意提供钝化的tourney blades。",
    "Arya不认识的烧伤黑发高大男人替Joffrey说话，嘲弄Winterfell的master-at-arms。",
    "Ser Rodrik报出自己的正式职位，警告Sandor Clegane不要忘记。",
    "Sandor讥讽Ser Rodrik是不是在训练女人，并以强壮身体施压。",
    "Ser Rodrik强调自己训练的是knights，只有准备好的人才会获得钢剑。",
    "Sandor转向Robb询问年龄。",
    "Robb回答十四岁。",
    "Sandor说自己十二岁已杀过人，而且用的不是钝剑，以血腥经历羞辱Robb。",
    "Arya看见Robb因自尊受伤而竖起防备，再次请求Ser Rodrik允许真剑决斗。",
    "Ser Rodrik坚持让Robb用tourney blade击败Joffrey即可。",
    "Joffrey耸肩拒绝，嘲笑Robb长大后再来找他，随从大笑着准备离开。",
    "Robb在场中咒骂，Arya震惊捂嘴；Theon抓住他防止冲上去。",
    "Joffrey假装打哈欠，叫Tommen离开，称玩耍时间已结束。",
    "Lannisters再次发笑，Robb继续咒骂，Ser Rodrik气得面红；孩子较量已变成家族侮辱。",
    "Jon目送他们离开，Arya观察Jon；他的脸像godswood黑水池一样静止，隐藏情绪。",
    "Arya不觉得好笑，突然用力说自己憎恨needlework，一切都不公平。",
    "Jon回答没有什么是公平的，最后揉乱她头发，与Ghost一起离开；Nymeria一度想跟随。",
    "Arya不情愿地转向相反方向，准备面对自己的惩罚。",
    "实际情况比Jon预想更糟：她房里不仅有Septa Mordane，还有Catelyn。",
]


KEY_NOTES = {
    1: "极短首句像老师批语，先让Arya被失败定义，再逐步展示她不适合的其实是一套单一标准。",
    2: "针脚差异立即变成姐妹比较；Arya不是单纯讨厌缝纫，而是不断在姐姐优势旁被衡量。",
    9: "Sansa语气`soft as a kiss`把王子话题浪漫化，Arya随后用更尖锐观察打破这种氛围。",
    13: "`She did everything prettily`既是羡慕也是怨气；Arya承认Sansa优势，却把它体验成自己的失败。",
    15: "Sansa把Jon的评价归因于嫉妒，避免正面判断Joffrey，也把bastard身份变成解释一切的缺陷。",
    16: "Arya用`our brother`优先表达情感关系，Sansa随后用`half brother`恢复法律与礼仪精确性。",
    20: "Arya主动交出针线近似挑衅：既然已经被注意，她宁愿让冲突立刻发生。",
    22: "Sansa没有笑而Jeyne笑，细节避免把姐妹矛盾简单写成Sansa故意羞辱。",
    26: "`shoe a horse`用被视为男性或仆役的工作挑战贵族女孩规范；甜美语气让反抗更尖。",
    27: "Arya把才能分配想象成母亲在出生时已经用完，显示儿童如何把长期比较内化为宿命。",
    28: "Nymeria无需Arya表现优雅便欢迎她，动物关系提供家庭评价体系之外的安全感。",
    32: "Jon与Ghost已经占据观看边缘位置；Arya逃离女孩课堂后自然来到另一个边缘者身边。",
    37: "厚护具让男孩练武也显得笨拙，暂时拆解“男孩天生擅长、女孩天生不擅长”的假设。",
    41: "Jon用玩笑说出严肃等级规则：王子的身体只能被社会认可的trueborn身体碰伤。",
    43: "Arya一天两次发现不公平——自己因女孩身份被排除，Jon因bastard身份被排除。",
    50: "一面盾牌同时展示父系王权与母系家族，纹章成为血统政治的可视化。",
    54: "狼叼鱼的荒谬图像让Arya笑，但笑后问题仍在：她不能把纹章转化为持剑权利。",
    55: "Jon的总结精确交换两种缺失：Arya有arms纹章却无arms武器，英文双关强化结构性不公平。",
    59: "Joffrey的外貌光彩与言语挑衅并置，继续区分“像王子”与“如何行动”。",
    61: "`I am a prince`不是反驳自己年幼，而是用身份宣布普通年龄标准不适用于他。",
    64: "Jon的粗话提供章节最直接的Joffrey评价，但仍来自Jon个人判断。",
    66: "`live steel`只有两词，骤然把练习从游戏提升到可能致命的真实暴力。",
    68: "Ser Rodrik拒绝并非懦弱，而是训练责任：十四岁少年的自尊不能替代安全判断。",
    71: "Sandor以性别侮辱挑战训练方法，把谨慎等同女性化，迫使Robb在荣誉压力下冒险。",
    75: "十二岁杀人被Sandor当作成熟证明，显示其价值体系把暴力经验置于训练与年龄之上。",
    78: "Joffrey先要求真剑，再以对方不能使用真剑为由拒绝钝剑，目标更像羞辱而非公平较量。",
    82: "Jon脸部静止与Ghost沉默相似；他比Arya更早学会把愤怒藏在无法读取的表面下。",
    84: "`Nothing is fair`没有安慰Arya，而是承认共同现实；兄妹亲昵动作仍提供有限支持。",
    86: "结尾把外部练武冲突切回家庭纪律，Arya不能永久逃离对她的女性规范要求。",
}


STAGES = [
    (1, 22, "本段以缝纫课堂展示Arya与Sansa的才能、礼仪和婚姻想象差异，羞耻在集体注视中不断累积。"),
    (23, 39, "本段让Arya逃离评价空间，经由Nymeria来到Jon身边；边缘人物与direwolves组成暂时安全的小群体。"),
    (40, 55, "本段用练武资格和纹章讨论对照女孩与bastard的制度限制，并通过arms双关把血统和武器连接。"),
    (56, 70, "本段从儿童练习升级到Joffrey与Robb的身份对抗，live steel要求暴露较量背后的家族自尊。"),
    (71, 86, "本段让Sandor以真实杀人经验施压，Ser Rodrik坚持训练边界；冲突结束后Arya仍须回去面对家庭惩罚。"),
]


BACKGROUNDS = {
    3: "**文本事实：** Septa Mordane负责Stark女孩的七神礼仪与女红教育；Myrcella是王室公主。",
    11: "**文本事实：** Jeyne Poole是Winterfell steward之女，也是Sansa最亲近的朋友。",
    18: "**文本事实：** Jon与Arya、Sansa同父异母；`half brother`在血缘上准确，但人物选择何种称呼也表达亲疏。",
    28: "**文本事实：** Arya的direwolf名为Nymeria，黄眼，性格活跃。",
    41: "**文本事实：** Jon因bastard身份未被允许与王子进行可能造成伤痕的正式练习。",
    50: "**文本事实：** Joffrey的纹章同时包含House Baratheon crowned stag与House Lannister lion。",
    53: "**文本事实：** Arya母亲出身House Tully，其家徽为trout；父亲House Stark家徽为direwolf。",
    55: "**语言提示：** `arms`既可指纹章，也可指武器；此处用双关概括Arya和Jon各自被剥夺之物。",
    66: "**文本事实：** live steel指开刃或可致伤的真实钢制武器，与木剑、钝化练习剑相对。",
    69: "**文本事实：** 烧伤面孔的男人是Sandor Clegane，担任Joffrey的护卫。",
    70: "**文本事实：** Ser Rodrik Cassel是Winterfell master-at-arms，负责武术训练与安全。",
}


EXTRA_VOCAB = [
    ("crooked", "/ˈkrʊkɪd/", "adj.", "歪斜的；不直的", "形容针脚"),
    ("stitch", "/stɪtʃ/", "n.", "针脚；一针", "缝纫基本单位"),
    ("furtively", "/ˈfɜːrtɪvli/", "adv.", "偷偷地；鬼祟地", "担心被发现"),
    ("salvage", "/ˈsælvɪdʒ/", "v.", "挽救；抢救", "试图补救失败作品"),
    ("abashed", "/əˈbæʃt/", "adj.", "尴尬惭愧的", "因被指出或意识到失误"),
    ("well-bred", "/ˌwel ˈbred/", "adj.", "有良好教养的", "贵族礼仪评价"),
    ("disgrace", "/dɪsˈɡreɪs/", "n.", "耻辱；丢脸", "公开失败造成的羞耻"),
    ("shoe a horse", "/ʃuː ə hɔːrs/", "phr.", "给马钉蹄铁", "铁匠或马匹工作"),
    ("sill", "/sɪl/", "n.", "窗台；门槛", "Jon坐的位置"),
    ("languidly", "/ˈlæŋɡwɪdli/", "adv.", "懒洋洋地；倦怠地", "姿态放松"),
    ("surcoat", "/ˈsɜːrkoʊt/", "n.", "罩在盔甲外的无袖外衣", "常展示纹章"),
    ("embroider", "/ɪmˈbrɔɪdər/", "v.", "刺绣；绣上", "制作纹章图案"),
    ("derisively", "/dɪˈraɪsɪvli/", "adv.", "嘲弄地；轻蔑地", "Theon的笑"),
    ("swat", "/swɒt/", "v./n.", "拍打；猛击", "Joffrey贬低木剑练习"),
    ("whiskers", "/ˈwɪskərz/", "n.", "胡须；络腮胡", "Ser Rodrik白胡子"),
    ("bristle", "/ˈbrɪsəl/", "v.", "因愤怒而竖起戒备", "像动物毛发竖立"),
    ("blunt", "/blʌnt/", "adj.", "钝的；未开刃的", "练习武器"),
    ("feign", "/feɪn/", "v.", "假装；佯作", "`feigned a yawn`"),
]

VOCAB = BASE_VOCAB + EXTRA_VOCAB


def note(order):
    if order in KEY_NOTES: return KEY_NOTES[order]
    return next(t for s,e,t in STAGES if s <= order <= e)


def background(order):
    return BACKGROUNDS.get(order, "本段没有新增必须补充的世界观设定；重点在Arya的自我比较、性别规范、血统资格或练武冲突。")


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
        "# *A Game of Thrones* Chapter 7 — ARYA 逐段精读","",
        "> **阅读模式：** 无剧透｜人物姓名保留英文｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        "> **文本范围：** 原 PDF 第 67–74 页，共 86 个正文段落","",
        "## 本章导读","",
        "Arya在缝纫课上再次被Sansa的优雅与自己的失败对照，羞愤逃离后带着Nymeria去找Jon。兄妹从高处观看Bran、Tommen、Robb与Joffrey练武，并谈到女孩与bastards分别被允许拥有的纹章和武器。Joffrey要求与Robb使用live steel，Sandor Clegane又以杀人经历煽动少年自尊，训练场由游戏变成家族和身份的较量。","",
        "## 人物表","","| 人物 | 当前身份与作用 |","|---|---|",
        "| Arya Stark | 本章视角人物；不擅长也不喜欢传统贵族女红 |",
        "| Sansa Stark | Arya的姐姐，擅长礼仪、刺绣并向往Joffrey |",
        "| Jon Snow | Arya亲近的half brother，与她共同观察练武 |",
        "| Joffrey Baratheon | 王储，挑衅Robb使用live steel |",
        "| Robb Stark | Arya的兄长，因自尊接受挑战 |",
        "| Nymeria / Ghost | Arya与Jon各自的direwolves |","",
        "## 主题词","","| 英文 | 中文解释 |","|---|---|",
        "| needlework | 女红；Arya被要求掌握却排斥的贵族女孩技能 |",
        "| trueborn | 婚生身份；决定谁有资格与王子正式练武 |",
        "| arms | 同时表示纹章与武器，本章核心双关 |",
        "| live steel | 可真正致伤的钢制武器 |","",
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
        "Chapter 7并不是简单说明Arya“不像女孩”，而是展示她不断被单一贵族女性标准判为失败。逃到Jon身边后，她发现男孩世界同样受身份限制：Jon有剑术却因bastard不能碰伤王子，Arya有合法家徽却因女孩不能持剑。练武场冲突进一步显示荣誉如何被挑衅操控——Joffrey提出危险条件，Sandor把谨慎羞辱成女性化，Robb便更难退让。","",
        "### 关键对照","",
        "- **Sansa／Arya：** 一个适应贵族女性规则，一个在规则中持续失败；两人并非简单善恶对立。",
        "- **Nymeria／课堂女孩：** 幼狼提供无需表现“漂亮”的接纳。",
        "- **女孩／bastard：** Arya和Jon被不同制度剥夺武器或纹章资格。",
        "- **木剑／live steel：** 安全训练被转化为对勇气与男性气概的测试。",
        "- **观看／参与：** Arya与Jon都坐在高处看别人做自己想做却不被允许做的事。","",
        "### 当前仍未解答的问题","",
        "1. Catelyn会如何处理Arya逃课和顶撞？",
        "2. Joffrey与Robb的敌意是否会继续升级？",
        "3. Arya能否获得真正学习剑术的机会？",
        "4. Jon为何在Joffrey离开后变得异常安静？","",
        "以上问题不使用后文章节答案。","","## 词汇总表","","| 词语 | 音标 | 词性 | 核心释义 |","|---|---|---|---|",
    ]
    all_text=' '.join(b['text'] for b in blocks); seen=set()
    for t,ipa,pos,m,_ in VOCAB:
        if t not in seen and term_present(t,all_text): lines.append(f"| `{t}` | {ipa} | {pos} | {m} |"); seen.add(t)
    lines += ["","## 使用说明","","- 人物姓名一律保留原始英文。","- 可使用如 `CH07-P071-055` 的段落编号继续提问。","- 背景讲解只采用截至当前段落可知的信息。",""]
    return '\n'.join(lines)


def build_map(blocks):
    records=[]
    for b,s in zip(blocks,SUMMARIES,strict=True):
        o=b['order']; records.append({"id":b['id'],"page":b['page'],"end_page":b['end_page'],"type":"paragraph","order":o,"original_text":b['text'],"translation":"","paragraph_explanation_zh":s,"reading_note_zh":note(o),"background_note_zh":background(o),"bbox":[0,0,0,0],"confidence":"high","refs":[],"insert_after":b['id']})
    all_text=' '.join(b['text'] for b in blocks); glossary=[]; seen=set()
    for t,_,_,m,n in VOCAB:
        if t not in seen and term_present(t,all_text): glossary.append({"term":t,"translation":m,"note":english_names(n)}); seen.add(t)
    return {"paper":{"title":"A Game of Thrones — Chapter 7 (ARYA)","author":"George R. R. Martin","source_type":"pdf","language":"en","source_path":str(PDF),"pdf_page_range":[67,74],"reader_mode":"spoiler-free close reading; English personal names"},"blocks":records,"pages":[{"page":p,"block_ids":[b['id'] for b in blocks if b['page']<=p<=b['end_page']]} for p in range(67,75)],"figures":[],"glossary":glossary}


def main():
    blocks=extract_range(67,74,'ARYA','CH07')
    if len(blocks)!=len(SUMMARIES): raise RuntimeError((len(blocks),len(SUMMARIES)))
    (OUT/'source_maps').mkdir(parents=True,exist_ok=True); (OUT/'notes').mkdir(parents=True,exist_ok=True)
    (OUT/'Chapter_07_ARYA_精读.md').write_text(build_markdown(blocks),encoding='utf-8')
    (OUT/'source_maps'/'Chapter_07_source_map.json').write_text(json.dumps(build_map(blocks),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'notes'/'Chapter_07_notes.md').write_text('# Chapter 7 extraction notes\n\n- Source: selectable-text PDF pages 67–74.\n- 86 paragraph blocks after cross-page repair.\n- Personal names remain in original English.\n- Commentary is spoiler-free; no full translation requested.\n',encoding='utf-8')


if __name__=='__main__': main()
