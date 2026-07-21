#!/usr/bin/env python3
"""Build Chapter 1 (BRAN) close-reading Markdown with English personal names."""

from __future__ import annotations

import json
import re
from pathlib import Path

from build_agot_prologue_reader import VOCAB as BASE_VOCAB, english_names, term_present
from extract_chapter1 import PDF, extract


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "一个夏末寒冷的清晨，七岁的Bran随父亲和兄长出发观看处决；这是他第一次被认为已经大到可以承担这种见证。",
    "犯人在山中小堡被捕。Robb猜他是效忠墙外之王的野人，Bran因此想起Old Nan讲述的食人、巨人和异鬼等可怕炉边故事。",
    "被缚的老人瘦弱、冻伤严重，因耳朵和手指缺损而引起Bran害怕。",
    "犯人获释后被带到Lord Eddard Stark面前；Bran努力记住Jon关于控制小马和不要移开视线的提醒。",
    "Bran从父亲严肃的外表和冷峻目光中感到这一仪式与平日不同。",
    "父亲询问犯人、听取回答，随后下令将其按在铁树树桩上，并取来名为Ice的巨剑。",
    "Lord Eddard Stark脱下手套，双手握住Ice，郑重承担行刑动作。",
    "Jon Snow靠近Bran，再次提醒他稳住小马，并告诉他无论发生什么都不能移开目光。",
    "Bran照做，既控制住坐骑，也坚持直视。",
    "Lord Eddard Stark一剑斩首；鲜血喷在雪上，Bran的马受惊，但他没有移开眼睛。",
    "人头滚到Theon脚边，他把它踢开并笑，引出他轻浮、残酷的一面。",
    "Jon低声骂Theon，并用手安抚Bran；Bran把这种接触理解为认可。",
    "返程时Bran仍无法摆脱犯人的死亡和鲜血，明明太阳升高却觉得更冷。",
    "Robb认为逃兵死得勇敢，并由外貌描写呈现他更像母亲。",
    "Jon否认那是勇敢，认为犯人早已被恐惧击垮；他与Robb同龄，却在外貌、体格和观察力上形成对照。",
    "Robb用关于异鬼的咒骂回击，随后邀请Jon赛马。",
    "Jon抢先出发，Robb追上，两人把严肃争论迅速转成少年竞赛。",
    "Bran的小马追不上他们；他记得犯人的眼神，并思考真正让人疯狂的恐惧会是什么。",
    "Bran沉思到没有察觉父亲靠近；父亲询问他是否安好。",
    "Bran回答后仰望高大威严的父亲，觉得他不像一个能被轻易问倒的人。",
    "父亲反过来问Bran对刚才事情的看法。",
    "Bran提出本章的核心问题：人在害怕时还能不能勇敢。",
    "父亲回答，只有害怕时才谈得上勇敢，并问Bran是否理解他亲自行刑的原因。",
    "Bran依据Old Nan的故事，把犯人误认为会掳掠妇女、献给异鬼的野人。",
    "父亲温和纠正：那人是逃离守夜人的背誓者；任何守夜人都清楚逃跑的代价是死刑。",
    "Bran想不出答案，只指出King Robert可以让专门的刽子手行刑。",
    "父亲解释Stark遵循更古老的原则：判处死刑的人必须亲自挥剑、直视死者并听完遗言。",
    "父亲告诉Bran，未来他也可能掌管城堡、执行裁决；不能承担亲手杀人的责任，就不该轻易判人死。",
    "Jon在山顶重新出现，呼喊他们去看Robb发现的东西。",
    "Jory赶来询问是否有麻烦。",
    "Lord Eddard Stark带着一点父亲式幽默，判断儿子们多半又发现了某种麻烦。",
    "众人在桥北河岸找到Robb和Jon；积雪很深，Robb怀抱某物，男孩们显得兴奋。",
    "骑手小心穿过雪堆寻找落脚点，Jory最先察觉雪中的巨大黑影。",
    "Jory拔剑并让Robb远离那个东西，坐骑也受到惊吓。",
    "Robb展示怀里的小动物，说明巨大生物已经死亡，只剩幼崽。",
    "Bran好奇得想催马，却被父亲要求从容下马，体现贵族礼仪和自我控制。",
    "众人下马查看，Theon追问怪物是什么，Robb回答是一头狼。",
    "Robb直接说那是一头狼。",
    "Theon把它称作畸形怪物，并强调体形巨大。",
    "Bran穿过齐腰积雪靠近，心跳因好奇和紧张加快。",
    "雪中躺着一头巨大母兽，体形超过Bran的小马，喉咙处凝结着带血冰块。",
    "Jon纠正Theon：这不是普通狼的畸形，而是本就能长得更大的direwolf。",
    "Theon指出长城以南已有两百年没有人见过direwolf。",
    "Jon以简短反击指出，眼前事实比旧记录更有力。",
    "Bran注意到Robb怀里的幼崽；它睁不开眼却在寻找乳汁，令Bran又惊又怜。",
    "Jon把另一只幼崽递给Bran；温暖身体和微弱心跳让它从象征变成需要照顾的生命。",
    "马术总管Hullen把久违的direwolf视为不祥现象。",
    "Jory明确说这是一种征兆。",
    "父亲口头否认征兆说法，却显得不安，并开始查看母兽死因。",
    "Robb发现母兽喉部卡着东西，并为自己先于父亲找到答案而骄傲。",
    "父亲拔出一截折断的鹿角；母兽显然被它刺入喉咙。",
    "鹿角出现后所有人沉默不安，Bran虽然不懂含义，也感受到成人的恐惧。",
    "父亲抛开鹿角并洗手，惊讶母兽受此伤后还能活到生产。",
    "Jory提出更诡异的可能：幼崽也许是在母兽死亡后出生。",
    "另一人用“生于死亡”概括此事，并认为这预示坏运气。",
    "Hullen认为无论如何幼崽很快都会死。",
    "Bran因幼崽将死而发出无言的难过声。",
    "Theon赞成立刻杀死幼崽，并拔剑向Bran索要。",
    "幼崽在Bran怀中扭动，Bran强烈拒绝交出它。",
    "Robb命令Theon收剑，短暂表现出像父亲一样的权威。",
    "Harwin指出两个孩子实际上无法养活幼崽。",
    "Hullen认为趁早杀死它们反而是仁慈。",
    "Bran向父亲求助，但父亲承认幼崽没有母乳、可能饿死或冻死。",
    "Bran含泪再次拒绝，却不愿在父亲面前哭出来。",
    "Robb提出让刚生产的母犬哺乳，并以只有两只活犬崽为理由说明奶水足够。",
    "成年人反驳说母犬可能把陌生幼崽咬死。",
    "Jon正式称呼父亲为Lord Stark，指出幼崽恰好有五只：三公两母。",
    "父亲追问数量与决定之间有什么关系。",
    "Jon指出Lord Eddard Stark也恰有五名婚生子女，而direwolf正是House Stark的家徽；幼崽可以分别属于他们。",
    "Bran看见父亲与随从都被这个对应打动，并因Jon的机智而充满感激。",
    "父亲理解Jon主动把自己排除在外，柔声问他是否不想要幼崽。",
    "Jon强调direwolf属于House Stark，而自己因私生身份并不算Stark。",
    "父亲沉思；Robb趁沉默承诺亲自给幼崽喂奶。",
    "Bran立刻附和，也愿意承担照料责任。",
    "父亲警告，承诺容易、执行困难；若孩子让幼崽受苦，他会亲自结束它们的生命。",
    "Bran急切点头，怀中幼崽舔他的脸，加强两者已经形成的情感联系。",
    "父亲又要求他们亲自训练并照料direwolf，不许把责任推给马夫、仆人或养犬人。",
    "Bran答应。",
    "Robb也答应。",
    "父亲提醒，即使尽力，幼崽仍可能死亡。",
    "Robb坚持他们不会让幼崽死。",
    "父亲最终同意留下幼崽，并命人收集其余几只后返回Winterfell。",
    "上马返程后Bran才敢品尝胜利的喜悦，怀中的幼崽贴着他取暖。",
    "走到桥中央时，Jon突然停马。",
    "父亲询问Jon发现了什么。",
    "Jon反问众人是否听见某种声音。",
    "Bran只听见风、马蹄和幼崽声音；Jon却能从中辨出另一个声音。",
    "Jon循声返回雪地，从母兽尸体附近抱出第六只幼崽。",
    "Jon推测它是自己爬离其他幼崽的。",
    "父亲提出它也可能被排挤；第六只通体白色，眼睛已经睁开且呈红色。",
    "Theon用讽刺口吻称它为albino，并断言它会最先死。",
    "Jon以冰冷目光否定Theon，宣布这只幼崽属于自己。",
]


KEY_NOTES = {
    1: "章节以孩子第一次观看处决开场，把成长与死亡责任直接联系；`too young` 与 `old enough` 是成人世界的判断。",
    3: "残缺耳朵和手指与序章Gared的冻伤形成读者可见的联系，但Bran此刻并不知道前因。这里仅指出文本呼应。",
    6: "巨剑Ice在执行司法时出现，武器、家族权力与责任被绑定在同一个动作中。",
    8: "Jon不是叫Bran逃避，而是教他稳定身体并见证结果；这是一种保护，也是一种成长训练。",
    10: "红血与白雪形成强烈色彩对比；Bran没有移开目光，完成了父亲要求的第一次考验。",
    11: "Theon踢人头的动作没有必要性，因此主要用于展示他把死亡当成表演。",
    15: "Robb看重外在表现，Jon看见眼神里的恐惧；两人的判断差异也对应他们不同的观察方式。",
    18: "Bran真正关心的不是法律身份，而是犯人究竟看见了什么；这让本章与序章的信息产生错位。",
    22: "这是小说最著名的勇气定义之一：恐惧不是勇气的反面，而是勇气成立的前提。",
    27: "父亲的原则把司法从抽象命令变成身体责任：看眼睛、听遗言、亲手执行。",
    28: "这段既是对Bran的教育，也提前规定了Stark式权力应当承担的伦理成本。",
    39: "`freak` 是Theon先入为主的命名；Jon随后用准确物种名纠正他，知识与嘲笑形成对照。",
    41: "母兽体形超过小马，让direwolf的巨大不靠抽象数字，而通过Bran熟悉的尺度呈现。",
    43: "两百年未见使这次出现超出日常经验；本章人物因此把动物事实理解为政治或家族征兆。",
    44: "Jon的回答非常简短：传闻和历史记录不能否定眼前证据。",
    46: "触觉从“怪物”叙述切换到幼小生命：温暖、心跳和蠕动迅速改变Bran的立场。",
    49: "父亲嘴上坚持理性，身体反应却泄露不安；这与序章人物用常识压住恐惧的方式相似。",
    51: "direwolf死于鹿角，使House Stark的家徽与带鹿角的动物意象并置；人物将其视为征兆，但此处不解释未来含义。",
    52: "Bran不懂象征，却能准确读取成人的沉默，这保持了儿童视角的可信度。",
    60: "Robb模仿父亲的命令语气，显示孩子开始学习家族权力的表达方式。",
    67: "Jon用正式称呼把家庭请求转化成家族与纹章逻辑，因此父亲必须认真回应。",
    69: "五只幼崽与五名婚生子女的对应是论证核心；Jon不是只求同情，而是给出符合贵族象征体系的理由。",
    72: "Jon主动说 `I am no Stark`，揭示私生身份带来的排除感，也说明他为何愿意牺牲自己的份额。",
    75: "允许收养不是无条件奖励；父亲把生命照料转化为孩子必须亲自承担的责任。",
    80: "父亲保留失败和死亡的现实可能，Robb则以儿童式决心回答，形成成熟与希望的对照。",
    84: "Jon再次先于众人听见细微信号，延续他在前文“看见别人忽略之处”的人物特征。",
    90: "白毛红眼不仅标示albino，也让第六只幼崽在视觉上与五只灰色幼崽分离，对应Jon的家庭位置。",
    92: "结尾把Theon的死亡判断与Jon的认领正面对置；`belongs to me` 同时是保护和身份确认。",
}


STAGE_NOTES = [
    (1, 12, "本段通过Bran的儿童视角描写处决仪式，重点是他如何观察成人、控制恐惧并学习规则。"),
    (13, 28, "本段把处决后的困惑转化为父子对话，讨论勇气、司法与承担后果的原则。"),
    (29, 44, "本段由返程过渡到发现direwolf，借人物不同反应逐步把普通动物事件变成异常征兆。"),
    (45, 66, "本段把宏大的征兆缩小为幼崽能否存活的具体问题，让孩子的同情与成人的现实判断冲突。"),
    (67, 82, "本段通过家徽、婚生身份和数量对应完成说服，同时把收养与责任绑定。"),
    (83, 92, "本段用第六只幼崽完成第二次发现，并让它与Jon在家庭中的特殊位置形成对应。"),
]


BACKGROUNDS = {
    1: "**文本事实：** Bran七岁，随父亲观看领主司法；这不是娱乐活动，而是贵族继承人教育的一部分。",
    2: "**文本事实：** Bran关于wildlings的认识主要来自Old Nan的炉边故事；其中怪谈是儿童听闻，不应自动当成已经证实的事实。Mance Rayder被称为King-beyond-the-Wall。",
    6: "**文本事实：** Ice是House Stark的巨剑，Lord Eddard Stark用它亲自行刑。",
    8: "**文本事实：** Jon Snow是Bran的私生兄长；姓Snow在当前语境中标示北方的私生身份。",
    15: "**文本事实：** Jon与Robb同龄，是同父异母兄弟；两人的外貌差异被明确突出。",
    23: "**文本事实：** Lord Eddard Stark把勇气定义为在恐惧存在时仍采取正确行动。",
    25: "**文本事实：** 守夜人立誓终身服役；逃离被视为背誓，依法处死。",
    26: "**文本事实：** King Robert使用headsman代为行刑；Stark选择更古老的亲自行刑传统。",
    28: "**文本事实：** bannerman是向更高领主宣誓效忠、承担军事义务的封臣；keep是规模较小的城堡或据点。",
    31: "**文本事实：** Winterfell是House Stark的家堡，也是队伍的目的地。",
    42: "**文本事实：** direwolf是比普通狼更大的狼类，也是House Stark的家徽动物。",
    43: "**文本事实：** direwolf在长城以南已两百年没有可靠目击，因此这次发现被视为异常。",
    47: "**文本事实：** Hullen是master of horse，负责领主家的马匹、马厩及相关人员。",
    48: "**阅读提示：** 人物所说的“征兆”是他们的解释，不等于文本已经证明超自然预言成立。",
    51: "**文本事实：** 鹿角刺死direwolf。角色对其象征意义感到不安，但当前章节没有给出解释。",
    67: "**文本事实：** `Lord Stark`是正式身份称呼；Jon改变称呼，意味着他以封建家族逻辑而非私人亲情提出请求。",
    69: "**文本事实：** House Stark的sigil是direwolf；Lord Eddard Stark有五名婚生子女，恰与五只幼崽对应。",
    72: "**文本事实：** Jon因私生身份不被视为正式的Stark继承人；他因此没有把自己计入五名孩子。",
    90: "**文本事实：** albino指先天缺乏色素的个体，常见特征包括白色毛发和红色或浅色眼睛。",
}


EXTRA_VOCAB = [
    ("crispness", "/ˈkrɪspnəs/", "n.", "清冽；凉爽而干燥的感觉", "此处暗示夏末将尽"),
    ("set forth", "/set fɔːrθ/", "phr.", "出发；启程", "较正式、文学化"),
    ("holdfast", "/ˈhoʊldfæst/", "n.", "小型堡垒；坚固据点", "奇幻和历史语境常用"),
    ("prickle", "/ˈprɪkəl/", "v.", "刺痛；汗毛竖起", "此处是恐惧引起的皮肤感觉"),
    ("hearth tale", "/hɑːrθ teɪl/", "n.", "炉边故事；口耳相传的旧故事", "常含民间传说和夸张成分"),
    ("slaver", "/ˈsleɪvər/", "n.", "奴隶贩子", "从事捕捉或买卖奴隶的人"),
    ("consort with", "/kənˈsɔːrt wɪð/", "phr.", "与……结交；和……厮混", "常暗含不赞同"),
    ("ghoul", "/ɡuːl/", "n.", "食尸鬼；恶鬼", "民间怪物名称"),
    ("sire", "/saɪər/", "v.", "生育；成为……的父亲", "古风或动物繁殖语境"),
    ("scrawny", "/ˈskrɔːni/", "adj.", "干瘦的；骨瘦如柴的", "带弱小、不健康的观感"),
    ("frostbite", "/ˈfrɒstbaɪt/", "n.", "冻伤", "严寒导致组织损伤"),
    ("ragged", "/ˈræɡɪd/", "adj.", "破烂的；衣衫褴褛的", "此处形容毛皮服装"),
    ("hoarfrost", "/ˈhɔːrfrɒst/", "n.", "白霜；树霜", "空气水汽直接凝华形成"),
    ("haggard", "/ˈhæɡərd/", "adj.", "憔悴的；形容枯槁的", "常由疲惫、饥饿或惊恐造成"),
    ("bound hand and foot", "/baʊnd hænd ən fʊt/", "phr.", "手脚都被捆住", "也可比喻完全受制"),
    ("king’s justice", "/kɪŋz ˈdʒʌstɪs/", "n.", "国王依法施行的裁决", "封建司法表达"),
    ("ward", "/wɔːrd/", "n.", "受监护者；寄养的贵族子弟", "并非普通客人或囚犯"),
    ("solemnly", "/ˈsɒləmli/", "adv.", "庄严地；严肃地", "强调仪式性"),
    ("grim cast", "/ɡrɪm kɑːst/", "n.", "冷峻的神情", "`cast`指面部呈现出的固定样子"),
    ("don", "/dɒn/", "v.", "穿上；披上", "文学化，与take off相对"),
    ("Valyrian steel", "/vəˈlɪəriən stiːl/", "n.", "瓦雷利亚钢", "本书中的珍贵锻造材料"),
    ("spell-forged", "/ˈspel fɔːrdʒd/", "adj.", "以法术锻造的", "暗示锻造过程包含魔法"),
    ("warden", "/ˈwɔːrdən/", "n.", "守护者；军政长官", "此处为Warden of the North头衔"),
    ("bastard", "/ˈbɑːstərd/", "n./adj.", "私生子（的）", "历史语境中的法律身份，常带侮辱性"),
    ("flinch", "/flɪntʃ/", "v.", "畏缩；因疼痛或恐惧猛地退缩", "`do not flinch`"),
    ("stroke", "/stroʊk/", "n.", "一次挥击；一击", "此处指干净利落的一剑"),
    ("spray", "/spreɪ/", "v.", "喷溅；飞散", "描写血液瞬间散开"),
    ("queer", "/kwɪər/", "adj.", "奇怪的；异样的", "此处是较旧用法，不涉及性取向"),
    ("muscular", "/ˈmʌskjələr/", "adj.", "肌肉发达的", "与slender形成对照"),
    ("slender", "/ˈslendər/", "adj.", "修长纤细的", "不等于虚弱"),
    ("gallop", "/ˈɡæləp/", "v.", "策马飞奔", "马的快速步态"),
    ("deserter", "/dɪˈzɜːrtər/", "n.", "逃兵；擅离职守者", "本章犯人的法律身份"),
    ("disquieting", "/dɪsˈkwaɪətɪŋ/", "adj.", "令人不安的", "比 frightening 更含隐约不祥"),
    ("oathbreaker", "/ˈoʊθbreɪkər/", "n.", "背誓者", "违背正式誓言的人"),
    ("sworn", "/swɔːrn/", "adj.", "宣誓承担的；以誓言约束的", "`sworn to`"),
    ("headsman", "/ˈhedzmən/", "n.", "刽子手；斩首执行人", "专门代为执行死刑"),
    ("liege lord", "/liːdʒ lɔːrd/", "n.", "受宣誓效忠的领主", "封建义务关系中的上级领主"),
    ("pass the sentence", "/pɑːs ðə ˈsentəns/", "phr.", "作出判决；宣判", "此处sentence是法律判决"),
    ("bannerman", "/ˈbænərmən/", "n.", "封臣；旗臣", "向领主效忠并在战时随旗出征"),
    ("keep", "/kiːp/", "n.", "主堡；小型城堡", "此处不是动词“保持”"),
    ("mischief", "/ˈmɪstʃɪf/", "n.", "麻烦；恶作剧造成的乱子", "父亲口吻带幽默"),
    ("crest", "/krest/", "n.", "山顶；山脊最高处", "此处是Jon重新出现的位置"),
    ("root out", "/ruːt aʊt/", "phr.", "搜出；发现", "父亲幽默地说儿子们又找出了麻烦"),
    ("drift", "/drɪft/", "n.", "风吹堆积的雪堆", "`snowdrift`的简写语境"),
    ("footing", "/ˈfʊtɪŋ/", "n.", "立足处；脚下支撑", "`solid footing`"),
    ("rear", "/rɪər/", "v.", "（马）扬起前蹄", "受惊或反抗动作"),
    ("afire with curiosity", "/əˈfaɪər wɪð .../", "phr.", "好奇心炽盛", "把强烈好奇比作着火"),
    ("direwolf", "/ˈdaɪərwʊlf/", "n.", "冰原狼；巨型狼", "House Stark的家徽动物"),
    ("realm", "/relm/", "n.", "王国；领土", "历史和奇幻语境常用"),
    ("sigil", "/ˈsɪdʒəl/", "n.", "家徽；纹章标志", "代表贵族家族"),
    ("antler", "/ˈæntlər/", "n.", "鹿角", "通常指鹿科动物分叉的角"),
    ("tine", "/taɪn/", "n.", "叉齿；鹿角分叉", "较生僻的具体名词"),
    ("litter", "/ˈlɪtər/", "n.", "一窝幼崽", "同一胎出生的动物"),
    ("whelp", "/welp/", "v./n.", "产仔；幼犬", "古风动物繁殖用语"),
    ("dismay", "/dɪsˈmeɪ/", "n.", "惊愕与沮丧", "此处指听见幼崽将死后的痛苦"),
    ("furrowed", "/ˈfɜːroʊd/", "adj.", "皱起的；有深纹的", "`furrowed brow`表示忧虑"),
    ("squirm", "/skwɜːrm/", "v.", "蠕动；扭动", "幼小动物不安地动"),
    ("kennelmaster", "/ˈkenəlmɑːstər/", "n.", "养犬负责人", "管理领主家的犬舍"),
    ("trueborn", "/ˈtruːbɔːrn/", "adj.", "婚生的；合法婚姻所生的", "与bastard身份相对"),
    ("albino", "/ælˈbiːnoʊ/", "n.", "白化个体", "先天缺乏黑色素"),
    ("wry", "/raɪ/", "adj.", "挖苦的；带讽刺的", "`wry amusement`"),
    ("clatter", "/ˈklætər/", "n./v.", "连续的硬物碰撞声", "此处为马蹄踏木桥声"),
    ("whimper", "/ˈwɪmpər/", "n./v.", "呜咽；低声哀叫", "幼兽细弱的叫声"),
]

VOCAB = BASE_VOCAB + EXTRA_VOCAB


def stage_note(order: int) -> str:
    if order in KEY_NOTES:
        return KEY_NOTES[order]
    return next(note for start, end, note in STAGE_NOTES if start <= order <= end)


def vocab_for(text: str):
    return [entry for entry in VOCAB if term_present(entry[0], text)]


def background_for(order: int) -> str:
    return BACKGROUNDS.get(order, "本段没有新增必须补充的世界观设定；重点是人物反应、家庭关系或现场信息。")


def source_label(block):
    return f"PDF p.{block['page']}" if block["page"] == block["end_page"] else f"PDF pp.{block['page']}–{block['end_page']}"


def build_markdown(blocks):
    pages = {}
    for b in blocks:
        pages.setdefault(b["page"], []).append(b["id"])
    lines = [
        "# *A Game of Thrones* Chapter 1 — BRAN 逐段精读", "",
        "> **阅读模式：** 无剧透｜人物姓名保留英文｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        "> **文本范围：** 原 PDF 第 16–23 页，共 92 个正文段落", "",
        "## 本章导读", "",
        "七岁的Bran第一次随父亲Lord Eddard Stark观看处决。返程中，队伍发现一头死去的direwolf和一窝幼崽。本章把“成长”写成两种责任：先是见证司法与死亡，随后是选择是否照料弱小生命。Bran的儿童视角只理解眼前事件的一部分，读者则能看见它与序章的隐约呼应。", "",
        "## 人物表", "",
        "| 人物 | 当前身份 | 阅读重点 |", "|---|---|---|",
        "| Bran | 七岁的视角人物，Lord Eddard Stark之子 | 正在学习勇气、司法和责任 |",
        "| Lord Eddard Stark | House Stark领主，Bran之父 | 坚持判决者亲自行刑的古老原则 |",
        "| Robb Stark | Bran的兄长，Jon的同龄伙伴 | 自信、保护幼崽，并开始模仿父亲的权威 |",
        "| Jon Snow | Bran的私生兄长 | 观察敏锐，理解家族象征，也清楚自己的边缘身份 |",
        "| Theon Greyjoy | Lord Eddard Stark的ward | 习惯用嘲笑掩饰或展示优越感 |",
        "| Jory Cassel | 家庭卫队队长 | 负责安全，对异常动物保持戒备 |", "",
        "## 地名与专名", "",
        "| 英文 | 中文解释 |", "|---|---|",
        "| Winterfell | 临冬城；House Stark的家堡 |",
        "| House Stark | Stark家族；北方领主家族 |",
        "| the Wall | 长城；守夜人防线 |",
        "| the Night’s Watch | 守夜人；犯人宣誓服役后又逃离的组织 |",
        "| Ice | House Stark用于行刑的巨剑 |",
        "| direwolf | 冰原狼；House Stark的家徽动物 |",
        "| sigil | 贵族家族的家徽或纹章标志 |", "",
        "## 段落目录", "",
    ]
    for page, ids in pages.items():
        lines.append(f"- [PDF 第 {page} 页：{ids[0]}–{ids[-1]}](#{ids[0].lower()})")
    lines += ["", "---", "", "## 逐段精读", ""]
    for block, summary in zip(blocks, SUMMARIES, strict=True):
        order = block["order"]; bid = block["id"]; original = block["text"]
        lines += [f'<a id="{bid.lower()}"></a>', f"### {bid}", "", f"**来源：** {source_label(block)}", "", "**英文原段**", "", f"> {original}", "", "**难词与短语**", ""]
        vocab = vocab_for(original)
        if vocab:
            lines += ["| 词语 | 音标 | 词性 | 此处含义 | 用法提示 |", "|---|---|---|---|---|"]
            for term, ipa, pos, meaning, note in vocab:
                lines.append(f"| `{term}` | {ipa} | {pos} | {meaning} | {english_names(note)} |")
        else:
            lines.append("本段没有新增的四级以上重点词；重点留意语气和上下文。")
        lines += ["", "**这一段说了什么**", "", summary, "", "**值得注意的地方**", "", stage_note(order), "", "**背景与伏笔（无剧透）**", "", background_for(order), "", "[回到段落目录](#段落目录)", "", "---", ""]
    lines += [
        "## 本章整体梳理", "",
        "Chapter 1把Bran的成长教育分成两部分。处决现场教他：勇气只能在恐惧中存在，掌权者必须承担裁决的身体后果。direwolf幼崽则教他：同情不能停留在请求，选择保全生命就必须亲自照料。两部分都由Lord Eddard Stark把抽象原则变成具体责任。", "",
        "### 关键关系与意象", "",
        "- **Bran与Lord Eddard Stark：** 父亲不替孩子消除恐惧，而是教他如何在恐惧中行动。",
        "- **Robb与Jon：** Robb更直接、自信；Jon更敏锐，也更懂得用家族规则说服父亲。",
        "- **Jon与第六只幼崽：** 两者都处在原有群体边缘，白色幼崽成为Jon主动认领的对应物。",
        "- **血与雪：** 处决时红血落在白雪，后来direwolf也躺在血染的雪中，让死亡场景相互呼应。",
        "- **眼睛与观看：** Bran被要求不移开目光；Jon能从眼神和细微声音中看到或听到他人忽略的信息。",
        "- **剑与幼崽：** 前半章是承担夺走生命的责任，后半章是承担保护生命的责任。", "",
        "### 当前仍未解答的问题", "",
        "1. 逃兵究竟经历了什么，才会陷入Jon所说的极端恐惧？",
        "2. direwolf为何在消失两百年后出现在长城以南？",
        "3. 鹿角与direwolf的组合为何令成年人如此不安？",
        "4. 六只幼崽与Stark孩子们的对应只是巧合，还是人物所说的征兆？", "",
        "以上只作为继续阅读的观察点，不提供后文章节答案。", "",
        "## 词汇总表", "", "| 词语 | 音标 | 词性 | 核心释义 |", "|---|---|---|---|",
    ]
    all_text = " ".join(b["text"] for b in blocks)
    seen = set()
    for term, ipa, pos, meaning, _ in VOCAB:
        if term not in seen and term_present(term, all_text):
            lines.append(f"| `{term}` | {ipa} | {pos} | {meaning} |"); seen.add(term)
    lines += ["", "## 使用说明", "", "- 后续提问可直接引用段落编号，例如 `CH01-P018-022`。", "- 所有人物姓名保留原始英文；中文只用于解释身份、地点与设定。", "- “背景与伏笔”严格限制在当前阅读进度，不泄露后文。", ""]
    return "\n".join(lines)


def build_source_map(blocks):
    page_records = [{"page": p, "block_ids": [b["id"] for b in blocks if b["page"] <= p <= b["end_page"]]} for p in range(16, 24)]
    records = []
    for b, summary in zip(blocks, SUMMARIES, strict=True):
        o = b["order"]
        records.append({"id":b["id"],"page":b["page"],"end_page":b["end_page"],"type":"paragraph","order":o,"original_text":b["text"],"translation":"","paragraph_explanation_zh":summary,"reading_note_zh":stage_note(o),"background_note_zh":background_for(o),"bbox":[0,0,0,0],"confidence":"high","refs":[],"insert_after":b["id"]})
    all_text = " ".join(b["text"] for b in blocks)
    glossary = [{"term":t,"translation":m,"note":english_names(n)} for t,_,_,m,n in VOCAB if term_present(t,all_text)]
    return {"paper":{"title":"A Game of Thrones — Chapter 1 (BRAN)","author":"George R. R. Martin","source_type":"pdf","language":"en","source_path":str(PDF),"pdf_page_range":[16,23],"reader_mode":"spoiler-free close reading; English personal names"},"blocks":records,"pages":page_records,"figures":[],"glossary":glossary}


def main():
    blocks = extract()
    if len(blocks) != len(SUMMARIES): raise RuntimeError(f"Expected {len(SUMMARIES)} blocks, got {len(blocks)}")
    (OUT / "source_maps").mkdir(parents=True, exist_ok=True)
    (OUT / "notes").mkdir(parents=True, exist_ok=True)
    (OUT / "Chapter_01_BRAN_精读.md").write_text(build_markdown(blocks), encoding="utf-8")
    (OUT / "source_maps" / "Chapter_01_source_map.json").write_text(json.dumps(build_source_map(blocks),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (OUT / "notes" / "Chapter_01_notes.md").write_text("# Chapter 1 extraction notes\n\n- Source: selectable-text PDF pages 16–23.\n- 92 paragraph blocks after cross-page repair.\n- Personal names remain in their original English forms.\n- No full translation; commentary is spoiler-free.\n",encoding="utf-8")


if __name__ == "__main__": main()
