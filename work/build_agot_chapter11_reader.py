#!/usr/bin/env python3
"""Build Chapter 11 (DAENERYS) close-reading Markdown."""

from pathlib import Path

from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter10_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

SUMMARIES = [
    "Daenerys怀着恐惧，在Pentos城外的露天草地与Khal Drogo成婚；Dothraki认为人生大事必须在天空下完成。",
    "Drogo召来整个khalasar，包括四万武士及无数家属和奴隶；庞大营地与畜群令Pentos居民越来越不安。",
    "Illyrio说Pentos已经扩充城卫；Drogo回到khalasar后，把自己的庄园暂时留给婚前的Daenerys和Viserys。",
    "Ser Jorah玩笑说应尽快成婚，免得Pentos耗费巨资雇人防卫；这名流亡骑士已经向Viserys献剑效忠。",
    "Viserys只关心Drogo何时支付政治对价；他看向Daenerys时，她只能低下眼睛。",
    "Illyrio保证交易已经谈妥，Drogo承诺的王冠最终会交给Viserys。",
    "Viserys立刻追问承诺究竟何时兑现。",
    "Illyrio列出婚后行程：先成婚，再横越草原向Vaes Dothrak的dosh khaleen展示新娘，之后若战争征兆吉利才可能行动。",
    "Viserys蔑视Dothraki征兆，抱怨Usurper仍占据父亲的王位，自己已经等得太久。",
    "Illyrio反问，Viserys几乎等了一生，再等数月或数年又有什么不同。",
    "去过Vaes Dothrak的Ser Jorah劝他耐心：Dothraki会守信，但按自己的时间行事；可以请求khal，不可呵斥。",
    "Viserys因“较低等的人”一词发怒，威胁割掉Jorah的舌头，并宣称dragon不会乞求。",
    "Jorah恭敬低眼，Illyrio含义不明地笑着进食；Daenerys在心中想世上已没有dragons，却不敢说出口。",
    "Daenerys梦见Viserys再次施暴，但在痛苦、血与火中，一条dragon出现并取代了他；她在极度恐惧中惊醒。",
    "Daenerys以为自己从未如此害怕，直到婚礼日真正来临。",
    "婚礼从黎明持续到黄昏，充满宴饮、歌舞与打斗；Daenerys与Drogo坐在高台，俯视坚持古老服饰、饮食和狂欢方式的Dothraki人海。",
    "Viserys虽获高贵席位，却因坐在Daenerys下方、只能吃新人拒绝的食物而愤恨，只能不断品味自己的怨气。",
    "Daenerys在人海中极度孤独；她按Viserys命令强笑到脸疼，不敢哭，也因紧张而无法进食。",
    "Drogo只与bloodriders谈笑，几乎不看Daenerys；两人没有共同语言，Illyrio和Viserys又坐得太远，她无人可谈。",
    "Daenerys只能抱着蜂蜜酒在心中重复自己的血统和头衔，用Aegon the Conqueror后裔的身份给自己撑胆。",
    "太阳刚升起不久，她便看到婚礼上的第一个死者；舞者在鼓声中表演，Drogo偶尔抛下铜章让她们争抢。",
    "一名武士当众与舞者发生性接触；Illyrio曾解释，khalasar不把这类亲密行为视为私密或羞耻。",
    "Daenerys试图移开视线，但更多武士加入后已无法回避；两人争夺同一女子，arakhs立刻出鞘，无人干预。",
    "决斗迅速结束，一名武士被杀；胜者随即转向另一名女子，奴隶搬走尸体，舞蹈照常继续。",
    "Illyrio曾说少于三人死亡的Dothraki婚礼会被视为乏味；这场婚礼最终死了十二人。",
    "恐惧不断增长：Daenerys害怕陌生而暴力的Dothraki，害怕令Viserys失望，更害怕婚后与Drogo独处。",
    "Daenerys再次以“我是dragon之血”压制恐惧。",
    "黄昏时Drogo拍手，宴饮骤停；他拉起Daenerys，婚礼进入bride gifts环节。",
    "Daenerys知道礼物之后便是first ride与完婚，无法排除恐惧，只能抱紧自己抑制颤抖。",
    "Viserys送她三名handmaids，但费用其实来自Illyrio；Irri教骑术、Jhiqui教语言、Doreah教亲密知识，Viserys还以轻薄言辞谈论Doreah。",
    "Ser Jorah因礼物不贵重而道歉，但他送的是Common Tongue写成的Seven Kingdoms历史与歌谣，Daenerys由衷感谢。",
    "Illyrio送来装满高级织物的雪松箱，箱中有三枚色彩各异、布满鳞片、像石头般沉重的巨蛋，Daenerys惊叹其美丽。",
    "Illyrio说它们是来自Asshai之外Shadow Lands的dragon’s eggs，漫长岁月使其石化，但美丽仍在。",
    "Daenerys答应永远珍藏；她也明白Illyrio之所以能慷慨，是因为他已从这场婚姻中获得大量马匹和奴隶。",
    "Drogo的三名bloodriders按传统赠送长鞭、arakh与dragonbone弓；Daenerys依仪式以女性身份谢绝，让丈夫代为使用。",
    "其他Dothraki送来衣物、珠宝、香料等海量物品，甚至有千张鼠皮制成的长袍，礼物多到她无法使用。",
    "最后Drogo亲自取礼物，期待的寂静扩展到整个khalasar；人群分开，他牵来一匹马。",
    "这是一匹年轻而非同寻常的母马，身体像冬日海水般灰，鬃毛像银色烟雾。",
    "Daenerys犹豫地抚摸马颈和银鬃；Drogo说它的银色是为配她的银发。",
    "Daenerys轻声赞叹这匹马很美。",
    "Illyrio说它是khalasar的骄傲，习俗要求khaleesi拥有与身份相配的坐骑。",
    "Drogo轻松把Daenerys举上Dothraki马鞍；无人预告她要当众试骑，她不安地询问该怎么做。",
    "Ser Jorah回答，只要拿住缰绳骑出去，不必走远。",
    "Daenerys骑术普通，过去更多乘船、车和palanquin；她祈祷别摔下丢脸，只敢轻轻催马。",
    "这一刻Daenerys数小时来第一次忘记害怕，甚至可能是一生第一次。",
    "银灰母马对细微指令敏锐回应；Daenerys从快步到飞驰，以兴奋取代恐惧，面对火坑时放开缰绳。",
    "银马像长出翅膀一样跃过火焰。",
    "Daenerys让Illyrio告诉Drogo，他送给她的是风；Drogo听后第一次对她微笑。",
    "日落后Drogo准备婚后骑行；Viserys却靠近并用手掐她的腿，威胁她必须取悦Drogo，否则会“唤醒dragon”。",
    "Viserys的话使恐惧立刻回来；Daenerys再次觉得自己只是十三岁、孤立无援且没有准备好的孩子。",
    "星辰升起时二人离开营地；Daenerys跟在沉默的Drogo身后，反复念“我是dragon之血”，试图维持勇气。",
    "他们在天黑后停在小溪旁；Daenerys感到像玻璃般易碎、四肢无力，终于在Drogo的注视下哭泣。",
    "Drogo看着她的眼泪，说了一个“No”，再用长满老茧的拇指略显粗糙地擦去泪水。",
    "Daenerys惊讶地以为Drogo会说Common Tongue。",
    "Drogo只再次重复“No”。",
    "Daenerys猜他也许只会这一个词，但他的语气和轻触头发的动作带有她未曾预期的温暖，使她略微安心。",
    "Drogo托起Daenerys的下巴，让她与自己对视。",
    "Drogo把Daenerys放在溪边圆石上，自己盘腿坐在地上，使两人的脸处于同一高度，然后又说“No”。",
    "Daenerys问他是否只会这一个词。",
    "Drogo没有回答，而是逐个解下辫中银铃；Daenerys主动帮忙，又按手势慢慢拆开他的辫子。",
    "拆辫子用了很久；解开后，他油亮浓黑的长发像黑色河流般铺开。",
    "随后Drogo开始帮Daenerys脱下婚服，场景进入婚姻亲密环节。",
    "Drogo动作比她预想的轻柔；她因羞怯回避目光、遮挡身体，他则以“No”和动作让她继续看着自己。",
    "Daenerys重复Drogo的“No”，开始在极有限的共同词汇中回应。",
    "Drogo继续完成亲密行为前的准备；Daenerys因寒冷和恐惧发抖，他暂时只是安静观察。",
    "Drogo以缓慢、循序的身体接触使Daenerys逐渐放松；文本强调其力量强大，却没有在此刻令她疼痛。",
    "亲密接触继续加深，Daenerys逐渐出现身体反应；此处不复录涉及未成年角色的露骨细节。",
    "Drogo停下并把“No”说成问句，Daenerys理解他在寻求她对继续亲密行为的回应。",
    "Daenerys以“Yes”和主动动作表达愿意继续；此处仅保留叙事功能与同意结构，不复录露骨细节。",
]

def extract_blocks():
    blocks = extract_range(97, 105, "DAENERYS", "CH11")
    for block in blocks:
        if block["order"] >= 62:
            block["text"] = (
                f"[原文涉及明确未成年角色的性内容，此处不逐字复录。"
                f"请参见源 PDF p.{block['page']} 中对应段落。]"
            )
    return blocks

KEY_NOTES = {
    1: "“fear and barbaric splendor”并置主观恐惧与宏大视觉：婚礼不是纯美庆典，也不是单一色调的暴力场景。",
    4: "Jorah的玩笑把Pentos的恐惧翻译成财政问题，而“Daenerys被卖给Drogo”直接命名了婚姻的交易属性。",
    5: "Viserys说Drogo可以“拿走她”，在语法上把Daenerys当作对价，而非具有意志的家人。",
    8: "Illyrio列出Dothraki的完整时间表，说明Viserys无法命令这个新盟友，也不会在婚后立即得到军队。",
    12: "Viserys只回应“lesser man”造成的自尊伤害；“dragon不乞求”成为他拒绝现实规则的口号。",
    13: "Daenerys心中“没有dragons了”的反驳，比在场成年人更直接，却仍只能保持沉默。",
    14: "梦中Viserys反复声称自己是dragon，真正出现的dragon却取代了他，显示Daenerys的潜意识开始分离二者。",
    15: "独立半句以省略号把噩梦恐惧直接缝合到婚礼现实，说明现实威胁比梦更近。",
    17: "Viserys形式上获得高席，却只感到低于妹妹和吃剩食的侮辱；“nurse resentment”把怨恨写成被主动喂养之物。",
    18: "庞大人群没有削弱孤独，反因无人能交流而放大隔绝；“笑到流泪”使服从命令成为身体劳动。",
    19: "婚姻在仪式上联结二人，语言上却几乎完全分离；沟通障碍是本章后半的核心限制。",
    20: "Daenerys把完整头衔当成内心护甲：它能给她勇气，却不能给她对话者或决定权。",
    21: "“第一个死者”在太阳初升时便出现，序数词已经暗示不会是最后一个。",
    23: "叙事严格跟随Daenerys视线：她试图转头，人群和冲突又迫她观看；无人干预使暴力显得属于公共秩序。",
    24: "死亡、搬尸与恢复舞蹈之间没有情绪间隔，这种迅速归于常态比决斗本身更突出文化距离。",
    25: "“especially blessed”是黑色反语；按婚礼习俗死亡多代表热闹，在Daenerys视角中却只加深恐怖。",
    26: "恐惧由外到内排列：陌生群体、熟悉兄长、即将独处的丈夫；最后一项被放在情绪顶点。",
    30: "Viserys把三名女子当作自己挑选的礼物，Daenerys却立即识别经济来源；轻薄言辞也暴露这些女性在交易中的位置。",
    31: "Jorah称书是“小东西”，Daenerys却“全心”感谢；礼物的情感价值与市场价格明显分离。",
    32: "龙蛋描写从珠宝、瓷器和玻璃的误认，逐步转向异常重量、鳞片与金属光泽，让读者与Daenerys同步辨认。",
    34: "Daenerys在感到奇迹时仍记得Illyrio从“卖她”中获利，说明她没有被礼物的美完全迷惑。",
    35: "传统拒辞要求Daenerys公开说“我只是女人”，将赠给她的军事力量转交丈夫；性别权力已写进仪式。",
    37: "寂静从中心向外波动，让Drogo的礼物在出现前便获得与众不同的重量。",
    38: "银灰色与Daenerys的头发呼应，使马不像通用财物，而像按她个人特征识别的伙伴。",
    42: "成人细致教她如何拒收武器，却没人预告公开试骑；对礼仪外表的准备与对她个人感受的忽略形成对照。",
    45: "“或许是一生第一次”把数小时的婚礼恐惧扩展到整个童年，暗示Viserys的统治一直以恐惧为基础。",
    46: "马对微小动作的即时回应给Daenerys罕见的控制感；她短暂从被安排者变成能发出指令的骑手。",
    47: "极短独立句把跃火设为情绪高峰；“像有翅膀”把地面的逃离转成短暂飞翔。",
    48: "“你送给我风”描述的是自由感而非价格或血统；Drogo首次微笑，表明他理解了这一回应。",
    49: "Viserys在Daenerys刚获得自由感时用触碰和熟悉威胁将她拉回控制关系。",
    50: "文本明确Daenerys只有十三岁，要求读者不能被Princess、khaleesi和华丽婚礼忘记她是未成年人。",
    51: "“dragon从不害怕”是Daenerys强加给自己的不可能标准；需要重复三次，恰好证明恐惧仍在。",
    52: "玻璃、水、婚绸和眼泪共同把Daenerys写成失去支撑的身体，与白天骑马的行动自由形成反差。",
    53: "Drogo的第一个Common Tongue词是“No”，但它是制止、安慰还是否定，对Daenerys并不清楚。",
    56: "Daenerys无法理解词义，只能从语气辨认温暖；沟通从词汇转向声音、触摸与手势。",
    58: "Drogo通过坐低使二人脸部等高，但年龄、力量和婚姻决定权的不平等并未因此消失。",
    60: "解铃和拆辫是一项无需共同语言的合作任务；Daenerys从被动观察转为主动帮助。",
    61: "“黑暗河流”将白天由铃铛和辫子表示的公开武士身份，转成私密场景中的自然形态。",
    63: "文本同时写Drogo动作轻柔与Daenerys的不动、避视和遮挡；不能用一个形容词替整场权力关系辩护。",
    64: "Daenerys首次主动说出两人唯一的共同词，但此时只是回声，并非对整场政治婚姻的自由选择。",
    66: "本段以力量与没有造成疼痛作对照，改变她对即时暴力的预期；年龄与婚姻非自主性仍不可忽略。",
    67: "本段通过时间拉长和身体反应表现恐惧逐渐转为参与；因角色明确未成年，不重述露骨细节。",
    68: "“No?”把反复出现的单词转成问句，形式上索取回应；局部交流不能倒推出她曾自由选择整场婚姻。",
    69: "结尾以“Yes”回应“No?”，让语言障碍在最小问答中暂时打开；仍须区分局部回应和结构性强迫。",
}

STAGES = [
    (1, 15, "本段交代婚姻的军事交易与Dothraki时间表；Viserys以dragon自称，Daenerys却在梦中开始把dragon与他分开。"),
    (16, 29, "本段用婚礼的感官过载、语言孤立和公共暴力累积Daenerys的恐惧，礼物环节则成为婚夜倒计时。"),
    (30, 37, "本段以handmaids、书、龙蛋、武器和奢侈品展示不同赠礼者如何定义Daenerys的身份。"),
    (38, 48, "本段让银马成为第一件真正给Daenerys带来自由和行动权的礼物，跃火完成情绪转折。"),
    (49, 61, "本段让Viserys的威胁打断骑行带来的勇气，随后用有限词汇、语气和合作动作建立Daenerys与Drogo的初步沟通。"),
    (62, 69, "本段进入婚姻亲密场景；精读只保留非露骨的叙事功能、局部问答与权力关系，不复录未成年角色的露骨细节。"),
]

BACKGROUNDS = {
    1: "**文本事实：** Dothraki认为人生重大事件必须露天举行，因此婚礼在Pentos城墙外举办。",
    2: "**术语：** khalasar是由khal统领的Dothraki迁徙群体，也包括家属、奴隶和畜群。",
    4: "**文本事实：** Ser Jorah Mormont是流亡骑士，已经向Viserys献剑效忠。",
    8: "**习俗：** 婚后Drogo须在Vaes Dothrak将Daenerys展示给dosh khaleen；战争还取决于Dothraki认可的征兆。",
    13: "**文本事实：** 活着的dragons被普遍认为已经消失；这是Daenerys当时对Viserys自我神话的内心反驳。",
    19: "**语言背景：** Daenerys不懂Dothraki；Drogo只懂少量bastard Valyrian，不懂Common Tongue。",
    22: "**视角限制：** “Dothraki像畜群动物”的概括来自Illyrio，不应自动当成对每个个体的完整客观描述。",
    25: "**文本事实：** Illyrio称少于三人死亡的婚礼会被视为乏味；本场婚礼死亡十二人。",
    30: "**文本事实：** Irri、Jhiqui和Doreah分别负责骑术、Dothraki语与婚姻亲密知识。",
    32: "**文本事实：** Illyrio送出三枚石化dragon’s eggs，声称来自Asshai之外的Shadow Lands。",
    35: "**婚礼习俗：** bloodriders赠新娘三件武器，新娘按仪式谢绝并让丈夫代用。",
    41: "**术语：** khaleesi是khal的妻子与女性配偶头衔，需有与身份相配的坐骑。",
    49: "**文本事实：** Viserys长期以“唤醒dragon”威胁Daenerys，指自己即将施加的愤怒和暴力。",
    50: "**年龄与权力：** Daenerys明确只有十三岁，婚姻由成人安排为政治交易，这是后续场景不可忽略的结构性强迫背景。",
    58: "**文本事实：** Drogo坐在地上使两人的脸等高；这不取消年龄、力量与婚姻决定权的不平等。",
    62: "**安全说明：** 从本段起因涉及明确未成年角色的性内容，不逐字复录原文；稳定编号和PDF定位仍保留。",
    68: "**阅读区分：** 当下问句寻求Daenerys回应，与她从未自由选择是否进入政治婚姻，是两个层次的事实。",
}

EXTRA_VOCAB = [
    ("barbaric", "/bɑːrˈbærɪk/", "adj.", "野蛮的；粗犷华丽的", "此处与splendor并置"),
    ("splendor", "/ˈsplendər/", "n.", "辉煌；壮丽", "强调视觉规模"),
    ("sellsword", "/ˈselsɔːrd/", "n.", "雇佣兵", "奇幻语境中的雇佣剑士"),
    ("procession", "/prəˈseʃən/", "n.", "队列行进；仪式性巡行", "婚后横越草原"),
    ("omen", "/ˈoʊmən/", "n.", "征兆；预兆", "决定战争是否吉利"),
    ("berate", "/bɪˈreɪt/", "v.", "严厉斥责", "不可对khal如此说话"),
    ("enigmatically", "/ˌenɪɡˈmætɪkli/", "adv.", "神秘难解地", "表情意义不明"),
    ("ungainly", "/ʌnˈɡeɪnli/", "adj.", "笨拙难看的", "梦中身体失去控制"),
    ("fermented", "/fərˈmentɪd/", "adj.", "发酵的", "马奶酒制作"),
    ("roil", "/rɔɪl/", "n./v.", "翻滚；混乱涌动", "形容紧张的胃部"),
    ("scythe", "/saɪð/", "n.", "长柄大镰刀", "arakhs形状类比"),
    ("consummation", "/ˌkɑːnsəˈmeɪʃən/", "n.", "完婚；婚姻的正式完成", "正式法律或文学用词"),
    ("handmaid", "/ˈhændmeɪd/", "n.", "贴身女侍", "负责个人服务和教导"),
    ("damask", "/ˈdæməsk/", "n.", "锦缎；花纹丝织品", "高级织物"),
    ("enamel", "/ɪˈnæməl/", "n.", "珐琅；搪瓷", "龙蛋材质猜测"),
    ("burnished", "/ˈbɜːrnɪʃt/", "adj.", "擦亮的；有光泽的", "金属色斑点"),
    ("lavish", "/ˈlævɪʃ/", "adj.", "奢华慷慨的", "赠礼花费巨大"),
    ("in my stead", "/ɪn maɪ sted/", "phr.", "代替我", "正式、古风表达"),
    ("filly", "/ˈfɪli/", "n.", "年轻母马", "通常指四岁以下"),
    ("stirrup", "/ˈstɪrəp/", "n.", "马镫", "骑马时的脚部支撑"),
    ("palanquin", "/ˌpælənˈkiːn/", "n.", "轿子；肩舆", "人力抬行的交通工具"),
    ("give a horse its head", "/ɡɪv ə hɔːrs ɪts hed/", "idiom", "放松缰绳，让马自由奔跑", "也可比喻放手行事"),
    ("callused", "/ˈkæləst/", "adj.", "长满老茧的", "常年劳动或使用武器"),
    ("deft", "/deft/", "adj.", "灵巧熟练的", "手部动作"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def main():
    blocks = extract_blocks()
    write_chapter(
        out=OUT, chapter=11, pov="DAENERYS", page_start=97, page_end=105,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观设定；重点在Daenerys的恐惧、Viserys的控制、Dothraki婚礼习俗或礼物的象征功能。",
        vocab=VOCAB,
        guide="Daenerys与Khal Drogo的婚礼既是跨文化庆典，也是Viserys用妹妹换取军事支持的政治交易。婚礼中的庞大人群、语言隔绝与公共暴力使Daenerys越来越害怕，而书、dragon’s eggs、武器和银马则显示不同赠礼者如何定义她。银马第一次给她带来自由与行动权，但Viserys的威胁很快让恐惧回归。末段以年龄、结构性强迫、有限语言和局部回应为中心，不将温柔动作简化为对整场婚姻权力关系的辩护。",
        people=[
            ("Daenerys Targaryen", "本章视角人物，十三岁；在政治安排下与Drogo成婚"),
            ("Khal Drogo", "Dothraki khalasar的领袖与Daenerys的新婚丈夫"),
            ("Viserys Targaryen", "Daenerys的兄长，将婚姻视为换取王冠和军队的交易"),
            ("Illyrio Mopatis", "Pentos magister，婚姻中介与大量礼物的提供者"),
            ("Ser Jorah Mormont", "效忠Viserys的流亡骑士，熟悉Dothraki习俗"),
            ("Irri / Jhiqui / Doreah", "赠给Daenerys的handmaids，分别教骑术、语言和婚姻亲密知识"),
        ],
        terms=[
            ("khalasar", "由khal统领的Dothraki迁徙群体"),
            ("dosh khaleen", "居于Vaes Dothrak、按习俗接受新娘觐见的女性群体"),
            ("bloodriders", "与khal有严格忠诚纽带的近身武士"),
            ("arakhs", "Dothraki弯刃武器，形似剑与镰刀的结合"),
            ("dragon’s eggs", "Illyrio赠送的三枚石化龙蛋"),
            ("khaleesi", "khal的妻子和女性配偶头衔"),
        ],
        synthesis="Chapter 11的主线是Daenerys如何在几乎没有决定权的婚礼中寻找最小的主体空间。Viserys把她当作王冠价格，Dothraki仪式把她置于显赫却陌生的高位，众多礼物又按赠礼者的需要定义她。真正的变化发生在骑上银马时：她给出细小指令，马立即回应，恐惧首次被行动取代。但章末仍不能脱离她只有十三岁、婚姻由兄长安排的事实。Drogo的局部温柔与寻求回应改变了她对当下场景的感受，却不能倒推整个政治婚姻具有充分自由选择。",
        contrasts=[
            "**庞大人群／极度孤独：** 宾客越多，Daenerys因语言和权力隔绝反而越孤单。",
            "**Viserys的dragon／Daenerys梦中的dragon：** 前者是暴力威胁，后者开始显现与兄长不同的力量形象。",
            "**奢华礼物／个人价值：** 书的市价不高却最真诚，银马则因带来自由而超越普通财物。",
            "**骑马时的行动权／婚姻中的被安排：** 一方是指令与即时回应，一方是成人替她决定未来。",
            "**无共同语言／有限问答：** 二人先靠语气、手势和合作交流，最终以No?/Yes形成最小对话。",
        ],
        questions=[
            "Daenerys梦中取代Viserys的dragon代表什么？",
            "Illyrio为何愿意送出三枚珍贵的dragon’s eggs？",
            "银马带来的自由感会如何影响Daenerys适应Dothraki生活？",
            "Drogo与Daenerys的语言障碍能否逐步被打破？",
        ],
        extraction_notes="提取器正确保留4个跨页段落；第62–69段因涉及明确未成年角色的性内容，保留稳定定位但不逐字复录露骨英文细节",
    )
    print(f"Wrote Chapter 11 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()

