#!/usr/bin/env python3
"""Build the spoiler-free Chinese close-reading companion for the AGOT prologue."""

from __future__ import annotations

import json
import re
from pathlib import Path

from extract_prologue import PDF, extract


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


SUMMARIES = [
    "加里德催促队伍返回，并断言他们追踪的野人已经死亡。夜色与“死人”从第一句就建立危险气氛。",
    "威玛以带笑的反问试探加里德是否害怕死人。",
    "加里德拒绝被激怒，凭经验坚持死者不值得继续调查。",
    "威玛追问死亡是否得到证实，表现出他对证据的执着。",
    "加里德相信威尔的侦察判断，说明威尔在追踪方面很可靠。",
    "威尔被迫加入争论，只能引用一句民间俗语缓和局面。",
    "威玛轻蔑地否定乳母的俗话，认为死人同样能提供线索。",
    "加里德从返程距离和天色出发，再次提出撤退的现实理由。",
    "威玛嘲笑他怕黑，把审慎解释成怯懦。",
    "威尔看出加里德既愤怒又恐惧；后者的资历让这种恐惧格外可信。",
    "威尔回忆自己已习惯长城外的巡逻，本以为那些旧故事不再能吓到他。",
    "但今晚的黑暗异常压迫；风、树声和被窥视感让两名老手都想逃回长城。",
    "短句补充：他们尤其不愿向威玛这样的指挥官承认恐惧。",
    "本段介绍威玛的贵族出身、年龄、坐骑和精良装备，并暗示他经验不足。",
    "他的奢华黑斗篷曾被同袍嘲笑，说明他尚未赢得真正的威望。",
    "威尔意识到，私下嘲笑过威玛使服从他的命令变得更难。",
    "加里德援引任务已经完成、天气恶化和返程艰难等理由继续劝返。",
    "威玛无视情绪争执，要求威尔重新准确描述现场。",
    "威尔原是偷猎者，被迫在断手与加入守夜人之间选择；他的林地本领因此成为队伍所需的技能。",
    "威尔详述野人营地：八名成年人静止不动、没有火，姿态像死者。",
    "威玛首先询问是否有血迹。",
    "威尔承认没有看见血。",
    "威玛继续询问武器，像是在系统排除遭袭的可能。",
    "威尔说明武器仍在死者手边，现场不像发生过搏斗。",
    "威玛进一步追问尸体姿势。",
    "威尔描述有人倚石而坐、其余倒地，坚持他们是倒下而非休息。",
    "威玛提出另一解释：他们也许只是睡着了。",
    "威尔提到树上的女哨兵也完全不动；他的颤抖表明自己并不相信那只是睡眠。",
    "威玛察觉威尔发冷。",
    "威尔把颤抖归因于风，隐藏真正的恐惧。",
    "威玛转向经验丰富的加里德，直接问这些人可能如何死亡。",
    "加里德详细描述冻死的过程：先疼痛，继而麻木、虚弱、嗜睡，最后平静死亡。",
    "威玛用讽刺口吻称赞加里德的口才。",
    "加里德展示冻伤造成的残缺，并讲到兄弟冻死的经历，证明自己的判断来自亲历。",
    "威玛用一句“穿暖些”轻率打发这段惨痛经验。",
    "加里德被激怒；威尔开始注意到天气与尸体状态之间存在矛盾。",
    "威尔试图替加里德辩护，却被威玛打断。",
    "威玛问威尔最近是否值过长城上的守夜。",
    "威尔回答肯定，并疑惑威玛究竟要证明什么。",
    "威玛问长城当时是什么状态。",
    "威尔意识到长城正在融水；若气温足以融冰，就不足以迅速冻死八名有装备的人。",
    "威玛完成推理，命令威尔带路，决意亲眼查看尸体。",
    "命令下达后，荣誉和军纪迫使两名下属服从。",
    "威尔领路；积雪掩盖坑洼，而威玛高大的战马与奢华斗篷都不适合密林。",
    "天色从紫黑变成彻底的夜，月光下积雪与威玛的斗篷形成鲜明黑白对照。",
    "威玛嫌行进速度太慢。",
    "恐惧让威尔罕见地顶撞，反问威玛是否愿意亲自领路。",
    "威玛不屑回应，维持贵族式的冷淡。",
    "远处狼嚎为即将发生的危险增加听觉信号。",
    "威尔在一棵古老铁树下停马。",
    "威玛询问停下的原因。",
    "威尔建议最后一段步行，因为营地就在山脊另一侧。",
    "威玛首次认真感受周围异常；风、马匹和树林的反应都显得不安。",
    "加里德再次明确说此地不对劲。",
    "威玛仍以轻蔑反问回应。",
    "加里德要求他不要只听具体声音，而要感受黑暗整体的不自然。",
    "威尔完全同意；四年巡逻经验也无法解释这种前所未有的恐惧。",
    "威玛把危险感拆成普通声响并继续嘲笑；随后拔出华丽但未经实战的长剑。",
    "威尔提醒密林会缠住长剑，短刀更实用。",
    "威玛拒绝建议，命令加里德留下看守马匹。",
    "加里德提出生火。",
    "威玛认为火会暴露位置，因此严厉斥责。",
    "加里德指出火能驱赶熊、冰原狼以及他不敢说出口的“其他东西”。",
    "威玛明确禁止生火。",
    "加里德一度像要违抗甚至攻击威玛，但长久形成的服从最终占了上风。",
    "加里德低头重复“不要火”，接受命令却并不认同。",
    "威玛把沉默当作顺从，催促威尔继续领路。",
    "威尔凭猎人技巧安静攀上山脊，威玛的盔甲、长剑和斗篷却不断发出声响并被树枝牵扯。",
    "威尔钻到山脊顶的哨兵树下，俯视下方营地。",
    "营地的火坑、棚屋、岩石与溪流都和几小时前完全一致；这种准确对应让威尔确信自己没有找错地方。",
    "原先看到的全部尸体都消失了。",
    "威玛笨拙地砍开树枝来到山脊，并因空营地而愤怒。",
    "威尔急促要求他伏低，确认危险仍在附近。",
    "威玛把尸体消失解释成威尔看错，并公开嘲弄他。",
    "威尔无法解释眼前矛盾，却确信自己没有看错，也没有弄错地点。",
    "威玛命令威尔起身，不许他继续躲藏。",
    "威尔不情愿地服从。",
    "威玛担心首次巡逻以失败告终，坚持搜索并命令威尔爬树观察火光。",
    "威尔停止争辩，攀树前拔出短刀；寒铁的味道给他一点心理安慰。",
    "下方的威玛突然挑战未知者；威尔从他的声音里听出了不确定。",
    "树林只传来树叶、溪水和雪鸮等自然声音。",
    "真正的“异鬼”却完全无声。",
    "威尔瞥见苍白身影在林间滑行，甲胄颜色随环境变化，使它几乎无法被锁定。",
    "威玛在空地里转身搜寻，终于放弃从容姿态，公开呼唤威尔。",
    "严寒骤然加强；树液似乎冻结，威尔嘴边的呼吸结霜，说明这不是普通夜寒。",
    "一个高瘦、苍白、仿佛由旧骨构成的身影走到威玛面前。",
    "威玛虽然声音发颤，仍拔剑摆出战斗姿态；他的斗篷暴露在月光下。",
    "异鬼无声逼近，手中的剑呈半透明晶体状，极薄且泛着幽蓝光。",
    "威玛勇敢应战，用“与我共舞”发出挑战；这一刻他真正成为守夜人战士。",
    "异鬼观察威玛的剑，眼睛像燃烧的冰；威尔短暂希望它也会畏惧人类武器。",
    "更多异鬼无声包围威玛；威尔明白出声既是职责，也几乎等于送死，最终选择沉默。",
    "异鬼率先挥出苍白长剑。",
    "两剑相击没有金属声，而发出近似动物痛苦的尖鸣；威玛因此感到恐惧。",
    "其他异鬼像观众一样耐心围观，甲胄继续随林影变化。",
    "连续交锋使威玛精疲力竭、流血，铠甲结霜，战斗声也越来越尖厉。",
    "威玛一次格挡稍迟，异鬼的剑穿过环甲，在腋下割伤他。",
    "异鬼用未知语言说话并似乎嘲弄；它的声音被比作冬湖冰裂。",
    "威玛因愤怒重新振作，高喊效忠国王劳勃并发动最后攻击。",
    "两剑再次相撞，人类钢剑瞬间碎裂。",
    "碎片像针雨飞散，一片刺入威玛左眼；他跪地惨叫。",
    "围观者一同上前，以绝对安静的方式反复砍杀威玛，随后发出冰冷笑声。",
    "许久之后，威尔才敢重新睁眼；山脊下已经空无一物。",
    "威尔在树上等到月亮移动很远，终于因肌肉僵硬和加里德的缺席而决定下去。",
    "威玛的尸体俯卧雪中，华丽斗篷和精良环甲都被轻易破坏。",
    "威尔捡起断剑残片，发现其边缘薄得像削刃；这可作为异常遭遇的物证。",
    "威尔起身时，本应死亡的威玛已经站在他身后。",
    "复起的威玛衣脸尽毁、左眼被碎片贯穿，右手仍握着断剑。",
    "他睁开的右眼已经燃烧着与异鬼相同的蓝光，并且正在注视威尔。",
    "断剑落下，威尔闭眼祈祷；威玛冰冷的双手随即扼住他的喉咙。",
]


KEY_NOTES = {
    1: "开篇没有解释世界观，而让“死人”在普通争执中出现；读者先感到不安，再逐步理解危险。",
    3: "`Dead is dead` 的重复看似坚定，也暴露加里德正在用常识压住无法言说的恐惧。",
    7: "威玛的粗俗与轻蔑建立了阶级冲突：他掌握军衔，却尚未取得老兵的尊敬。",
    10: "叙事严格贴近威尔的观察；我们不是直接知道加里德害怕，而是从表情与身体反应推断。",
    11: "先说旧故事已失去力量，再用 `Until tonight` 推翻它，是典型的恐怖叙事转折。",
    12: "自然景物被写成有生命、有敌意的存在，恐惧还没有实体，却已经控制感官。",
    14: "坐骑和服装不是装饰性清单：它们把贵族身份、经济差距和“不适合密林实战”同时写出来。",
    15: "`soft as sin` 让斗篷兼具诱惑与不祥；后来它也会成为视觉上最醒目的目标。",
    18: "威玛并非完全无能。他要求复述细节，显示出调查意识，只是傲慢妨碍他理解老兵的直觉。",
    19: "守夜人吸纳罪犯，并让其过去的技能服务边境；这是制度功能，也是威尔身份不安的来源。",
    20: "尸体没有外伤、火已熄灭、姿势异常，这些细节构成一个暂时无法由常识解释的谜。",
    24: "武器仍触手可及，削弱了“遭普通敌人袭击”的解释。",
    28: "树上的哨兵本应最警觉，她的静止让“所有人只是睡着”显得更不可能。",
    32: "冻死过程被写得逐步而具体，使“寒冷”从天气变成能侵入人体的敌人。",
    34: "伤残是比口头资历更强的证据；威玛仍不接受，突出知识与权力的错位。",
    41: "`the Wall was weeping` 是形象化说法：冰墙融水像流泪，同时提供气温证据。",
    42: "这一推理让威玛显出聪明和责任感，人物因此不只是单纯的傲慢贵族。",
    43: "`honor bound them` 表明悲剧并非因为所有人都判断错误，而是正确判断无法战胜等级和职责。",
    45: "天空像旧伤瘀青，是颜色描写也是暴力预示；黑白意象此后不断加强。",
    53: "马匹常先于人感知危险。此处威玛的停顿说明他的理性自信第一次出现裂缝。",
    56: "`Listen to the darkness` 不是要听某个声音，而是注意正常环境中不该出现的沉寂与压迫。",
    58: "华丽长剑“看起来很新”暗示它缺乏实战历史，与加里德身上的旧伤构成对照。",
    63: "省略的 `other things` 比直接命名更有效：加里德害怕承认旧传说可能是真的。",
    65: "这里的对峙把军纪写成一种近乎本能的力量；加里德看见危险，却无法越过身份秩序。",
    68: "威尔无声、威玛有声的并置，把经验差异转化为可以听见的细节。",
    71: "两个极短句把节奏骤然压紧；此前细密铺垫在这里变成一个清晰、无法回避的异常事实。",
    75: "恐怖来自证据冲突：地点完全正确，记忆也清晰，但世界不再遵守熟悉的因果。",
    79: "短刀的味觉细节把读者拉回威尔的身体，也显示他只能依赖微小、熟悉的实物获得安全感。",
    81: "自然界有声，异鬼无声；沉默因此不再是空白，而成为它们的标志。",
    83: "`gliding` 和会变色的甲胄让它们不像普通步行的人，也解释了威尔为何难以持续看清。",
    85: "骤降的温度与异鬼出现同步，把加里德早先关于“真正敌人是寒冷”的话转化为现实。",
    86: "描写避免直接给出完整答案，只以骨、乳白与肉的比喻拼出非人的身体感。",
    88: "异鬼之剑同时像晶体、冰和光；作者用互相矛盾的材质感强调它不属于普通锻造体系。",
    89: "威玛此前的傲慢没有被洗白，但在真正危险面前，他确实选择迎战，人物获得悲剧性的尊严。",
    90: "“冰在燃烧”是矛盾修辞，把极寒写成具有主动能量的存在。",
    91: "威尔在职责与求生之间选择沉默；文本不简单裁决他，而让读者感受这个选择的代价。",
    93: "声音先于伤口暴露力量差异：人类钢铁面对异鬼武器时，连熟悉的金属规则都失效。",
    94: "围观姿态暗示这不是势均力敌的战斗，更像观察、试探或仪式性的猎杀。后两种属于阅读推测。",
    97: "异鬼不仅能行动，也有语言和类似笑声的交流，这使其比无意识怪物更令人不安。",
    98: "`For Robert` 表明威玛在绝境中仍以王国与誓约定义自己。此处不展开劳勃的后续背景。",
    99: "单句成段让“钢剑碎裂”成为全场最干脆的力量判决。",
    101: "`cold butchery` 既指残酷屠杀，也把“冷”从温度扩展为施暴者的无情。",
    105: "威尔想带走证物，说明他仍希望让不可置信的经历进入可验证的现实。",
    106: "生与死的界线在一个五词短句中被推翻，呼应开头加里德的 `Dead is dead`。",
    108: "眼睛颜色成为状态改变的明确视觉证据；文本只展示变化，不在序章内解释机制。",
    109: "结尾不直接写死亡结果，而停在触觉与窒息动作上，使威尔的命运在感官层面封闭。",
}


STAGE_NOTES = [
    (1, 18, "本段继续通过军衔、经验和恐惧之间的冲突塑造三人关系，并延迟揭示威胁。"),
    (19, 42, "本段以侦察细节或推理推进谜团，让常识解释逐渐显得不足。"),
    (43, 68, "本段让错误的指挥决定一步步转化为空间上的深入，悬念随距离缩短。"),
    (69, 80, "本段利用空营地、消失的尸体和人物反应，把预感转化为可观察的异常。"),
    (81, 91, "本段主要依靠声音、温度、颜色和运动方式描写未知生物，保留解释空白。"),
    (92, 101, "本段用短句和感官比喻加快战斗节奏，并持续强调人类武器的劣势。"),
    (102, 109, "本段在战斗后的寂静中制造第二次反转，使开篇关于死亡的争论获得残酷回应。"),
]


BACKGROUNDS = {
    1: "**文本事实：** 三人正在长城以北追踪野人。`wildlings` 是长城外人群的称呼，并不等于超自然生物。",
    6: "**文本事实：** 威尔处在两名地位更高者的争论之间；俗语来自母亲，反映普通人的生活智慧。",
    10: "**文本事实：** 加里德在守夜人服役四十年。老兵异常恐惧本身就是重要警报。",
    11: "**文本事实：** `the Wall` 是守夜人的边境据点核心；`rangings` 指越过长城执行的巡逻侦察。",
    14: "**文本事实：** 威玛来自古老贵族家族，作为幼子缺乏主要继承机会；加入守夜人可能为他提供独立身份。最后一点是基于本段的合理推断。",
    17: "**文本事实：** Mormont 是给他们下达追踪任务的上级；本段不需要知道更多身份细节。",
    19: "**文本事实：** `take the black` 指加入守夜人。威尔因偷猎面临断手刑罚，选择以服役替代。",
    31: "**文本事实：** `man-at-arms` 是受训练、受雇或隶属于贵族武装体系的职业战士，不等同于有爵位的骑士。",
    34: "**文本事实：** Maester Aemon 曾处理加里德的冻伤；`maester` 可先理解为城堡或组织中的学者、医者与顾问。",
    41: "**文本事实：** 长城主体为冰，表面融水能作为温度变化的直观指标。",
    43: "**文本事实：** 守夜人有明确的指挥链与服从义务；个人经验不能自动推翻上级命令。",
    58: "**文本事实：** `castle-forged` 强调武器出自条件良好的锻造场所，象征品质与身份，但不保证使用者有经验。",
    63: "**当前可知：** direwolf 是体形巨大的狼类；加里德停顿后的“其他东西”尚未被可靠命名。",
    78: "**文本事实：** Castle Black 是他们返回后要报告的守夜人据点；威玛把首次巡逻的成败与个人名誉相连。",
    81: "**文本事实：** 本段第一次把这些存在称为 `the Others`。中文常译“异鬼”；在当前进度只应把它视为未知、非人的北方威胁。",
    86: "**当前可知：** 异鬼具有实体、装备和主动行动能力；关于来源、种族和目的，序章尚无答案。",
    88: "**当前可知：** 异鬼武器并非威尔熟悉的人类金属剑；其材料与制造方式仍未知。",
    98: "**文本事实：** Robert 是威玛效忠的国王。为保持无剧透，本篇不补充其政治史。",
    108: "**当前可知：** 蓝眼与复起同时出现，表明威玛已发生超自然改变；本篇不提前命名或解释该状态。",
}


VOCAB = [
    ("wildling", "/ˈwaɪldlɪŋ/", "n.", "野人；长城外居民", "奇幻专名，在人物话语中带有边境内部人的称呼色彩"),
    ("rise to the bait", "/raɪz tə ðə beɪt/", "phr.", "上钩；被挑衅激怒", "把言语挑衅比作钓饵"),
    ("lordling", "/ˈlɔːrdlɪŋ/", "n.", "年轻小贵族；贵族小子", "常带轻蔑或讽刺"),
    ("quarrel", "/ˈkwɒrəl/", "n.", "争论；口角", "比普通 disagreement 更带情绪冲突"),
    ("wet nurse", "/ˌwet ˈnɜːrs/", "n.", "乳母；奶妈", "替别人的婴儿哺乳并照料孩子的女性"),
    ("unman", "/ʌnˈmæn/", "v.", "使失去勇气；吓破胆", "古风且带性别羞辱意味"),
    ("suppress", "/səˈpres/", "v.", "压住；抑制", "`barely suppressed anger` 指几乎压不住的愤怒"),
    ("perilous", "/ˈperələs/", "adj.", "危险的；接近危险程度的", "`come perilous close to` 表示危险地接近"),
    ("unease", "/ʌnˈiːz/", "n.", "不安；忧虑", "比 fear 更含模糊、未明的担忧"),
    ("bowels had turned to water", "/ˈbaʊəlz .../", "idiom", "吓得腿软、肚子发虚", "生动的身体化恐惧表达"),
    ("ranging", "/ˈreɪndʒɪŋ/", "n.", "远程巡逻；越墙侦察", "本书中守夜人的任务用语"),
    ("southron", "/ˈsʌðrən/", "n./adj.", "南方人（的）", "古风拼写，近似 southern"),
    ("implacable", "/ɪmˈplækəbəl/", "adj.", "无法安抚的；不留情的", "强调敌意不会缓和"),
    ("hellbent", "/ˈhelbent/", "adj./adv.", "不顾一切地；拼命地", "`ride hellbent` 指策马狂奔"),
    ("heir", "/eər/", "n.", "继承人", "`too many heirs` 暗示幼子继承机会有限"),
    ("destrier", "/ˈdestriər/", "n.", "中世纪骑士战马", "比普通乘用马高大昂贵"),
    ("garron", "/ˈɡærən/", "n.", "苏格兰高地矮马", "适合崎岖地形的结实小马"),
    ("ringmail", "/ˈrɪŋmeɪl/", "n.", "环甲；环状金属甲", "本书盔甲用语"),
    ("moleskin", "/ˈmoʊlskɪn/", "n.", "鼹鼠皮；厚实棉布", "此处指手套材质"),
    ("boiled leather", "/bɔɪld ˈleðər/", "n.", "煮制硬革", "经处理后变硬，可作护甲"),
    ("sable", "/ˈseɪbəl/", "n./adj.", "黑貂皮；深黑色的", "贵重毛皮，也强化全黑形象"),
    ("in your cups", "/ɪn jər kʌps/", "idiom", "喝醉时；酒后", "古风表达"),
    ("fortnight", "/ˈfɔːrtnaɪt/", "n.", "两星期", "英式常用时间单位"),
    ("cocksure", "/ˌkɒkˈʃʊər/", "adj.", "过分自信的", "通常含贬义"),
    ("poacher", "/ˈpoʊtʃər/", "n.", "偷猎者", "未经许可猎取他人土地上的猎物"),
    ("caught red-handed", "/kɔːt ˌred ˈhændɪd/", "idiom", "当场抓获；抓个正着", "强调作案时被发现"),
    ("take the black", "/teɪk ðə blæk/", "phr.", "披上黑衣；加入守夜人", "本书制度用语"),
    ("lean-to", "/ˈliːn tuː/", "n.", "单坡简易棚", "通常倚靠岩石、墙或树搭建"),
    ("firepit", "/ˈfaɪərpɪt/", "n.", "火坑；篝火坑", "营地中生火的位置"),
    ("far-eyes", "/ˈfɑːr aɪz/", "n.", "远望哨；侦察哨", "从语境可知是负责观察远处的人"),
    ("grizzled", "/ˈɡrɪzəld/", "adj.", "头发灰白的；饱经风霜的", "常暗示年龄和经验"),
    ("man-at-arms", "/ˌmæn ət ˈɑːrmz/", "n.", "职业武装侍从；披甲战士", "并不必然拥有骑士头衔"),
    ("eloquence", "/ˈeləkwəns/", "n.", "雄辩；有感染力的表达", "此处称赞带讽刺"),
    ("stump", "/stʌmp/", "n.", "残端；树桩", "此处指冻伤后缺失耳朵留下的部位"),
    ("flurry", "/ˈflɜːri/", "n.", "短暂小雪；阵雪", "`a flurry of snow`"),
    ("clad", "/klæd/", "adj.", "穿着……的", "文学化用法，`clad in fur and leather`"),
    ("undergrowth", "/ˈʌndərɡroʊθ/", "n.", "林下灌木；矮树丛", "影响骑行与视线"),
    ("unwary", "/ʌnˈweəri/", "adj.", "不警觉的；粗心的", "与 `careless` 并列"),
    ("insolent", "/ˈɪnsələnt/", "adj.", "无礼的；顶撞的", "尤指对上级不敬"),
    ("deign", "/deɪn/", "v.", "屈尊；俯就", "常用于 `deign to do`，带讽刺"),
    ("gnarled", "/nɑːrld/", "adj.", "扭曲多节的", "常形容古树或老人的手"),
    ("disdainful", "/dɪsˈdeɪnfəl/", "adj.", "轻蔑的；鄙视的", "比冷淡更明确地表现优越感"),
    ("sheath", "/ʃiːθ/", "n.", "刀鞘；剑鞘", "`draw ... from its sheath`"),
    ("hilt", "/hɪlt/", "n.", "剑柄", "包括护手与握柄部分"),
    ("acquiescence", "/ˌækwiˈesəns/", "n.", "默许；勉强顺从", "没有真正赞同，只是不再反抗"),
    ("thicket", "/ˈθɪkɪt/", "n.", "灌木丛；密林", "枝条密集、难以穿行"),
    ("sentinel", "/ˈsentɪnəl/", "n.", "哨兵；守望者", "此处把树拟人化为守卫"),
    ("slither", "/ˈslɪðər/", "n./v.", "窸窣滑动声；滑行", "此处写环甲摩擦声"),
    ("dirk", "/dɜːrk/", "n.", "长匕首；短剑", "适合近身或林地使用"),
    ("perch", "/pɜːrtʃ/", "n.", "栖身处；高处落脚点", "此处指威尔在树上的位置"),
    ("gaunt", "/ɡɔːnt/", "adj.", "瘦削憔悴的", "常带不健康、骷髅般的感觉"),
    ("milkglass", "/ˈmɪlkɡlæs/", "n.", "乳白玻璃", "用来比喻异鬼苍白半透明的身体"),
    ("longsword", "/ˈlɔːŋsɔːrd/", "n.", "长剑", "中世纪武器名称"),
    ("defiant", "/dɪˈfaɪənt/", "adj.", "反抗的；蔑视威胁的", "强调迎战姿态"),
    ("translucent", "/trænzˈluːsənt/", "adj.", "半透明的", "允许部分光线穿过"),
    ("keening", "/ˈkiːnɪŋ/", "n.", "尖厉哀鸣", "原指哭丧般的长声"),
    ("parry", "/ˈpæri/", "n./v.", "格挡；挡开攻击", "剑术动作"),
    ("butchery", "/ˈbʊtʃəri/", "n.", "残酷屠杀", "比 killing 更强调冷酷和血腥"),
    ("shard", "/ʃɑːrd/", "n.", "尖锐碎片", "常指玻璃、金属或陶器碎片"),
    ("transfix", "/trænsˈfɪks/", "v.", "刺穿；钉住", "`a shard ... transfixed the pupil`"),
    ("pupil", "/ˈpjuːpəl/", "n.", "瞳孔", "此处不是“学生”"),
    ("nerveless", "/ˈnɜːrvləs/", "adj.", "无力的；失去知觉的", "`nerveless fingers` 指手指失去控制"),
]


def stage_note(order: int) -> str:
    if order in KEY_NOTES:
        return KEY_NOTES[order]
    for start, end, note in STAGE_NOTES:
        if start <= order <= end:
            return note
    raise ValueError(order)


def vocabulary_for(text: str) -> list[tuple[str, str, str, str, str]]:
    found = []
    for entry in VOCAB:
        term = entry[0]
        if term_present(term, text):
            found.append(entry)
    return found


def term_present(term: str, text: str) -> bool:
    """Match glossary lemmas as well as simple English inflections."""
    escaped = re.escape(term.lower())
    if re.fullmatch(r"[a-z]+", term.lower()):
        escaped += r"(?:s|es|ed|ing)?"
    special = {
        "unman": r"unman(?:s|ned|ning)?",
        "hearth tale": r"hearth tales?",
        "consort with": r"consort(?:s|ed|ing)? with",
        "pass the sentence": r"pass(?:es|ed|ing)? the sentence",
        "root out": r"root(?:s|ed|ing)? out",
    }.get(term.lower(), escaped)
    return bool(re.search(r"(?<![a-z])" + special + r"(?![a-z])", text.lower()))


def background_for(order: int) -> str:
    return BACKGROUNDS.get(order, "本段没有新增必须补充的世界观设定；理解重点在人物反应与现场信息。")


def english_names(text: str) -> str:
    """Honor the reader's preference: never translate personal names."""
    replacements = [
        ("威玛·罗伊斯爵士", "Ser Waymar Royce"),
        ("威玛·罗伊斯", "Waymar Royce"),
        ("伊蒙学士", "Maester Aemon"),
        ("莫尔蒙", "Mormont"),
        ("加里德", "Gared"),
        ("威尔", "Will"),
        ("威玛", "Waymar"),
        ("劳勃", "Robert"),
    ]
    for chinese, english in replacements:
        text = text.replace(chinese, english)
    for duplicate in ["Will（Will）", "Gared（Gared）", "Ser Waymar Royce（Ser Waymar Royce）", "Mormont（Mormont）", "Maester Aemon（Maester Aemon）"]:
        text = text.replace(duplicate, duplicate.split("（", 1)[0])
    return text


def source_label(block: dict[str, object]) -> str:
    start = int(block["page"])
    end = int(block["end_page"])
    return f"PDF p.{start}" if start == end else f"PDF pp.{start}–{end}"


def build_markdown(blocks: list[dict[str, object]]) -> str:
    page_ranges: dict[int, list[str]] = {}
    for block in blocks:
        page_ranges.setdefault(int(block["page"]), []).append(str(block["id"]))

    lines = [
        "# *A Game of Thrones* 序章逐段精读",
        "",
        "> **阅读模式：** 无剧透｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        "> **文本范围：** 原 PDF 第 6–15 页，共 109 个正文段落  ",
        "> **定位说明：** 每段都有稳定编号；跨页段落会同时标出起止页。",
        "",
        "## 序章导读",
        "",
        "三名守夜人越过长城追踪一队野人。老兵加里德坚信现场有危险，年轻贵族指挥官威玛·罗伊斯则要求用证据验证“尸体已经死亡”的判断，猎人出身的威尔夹在两者之间。本章的核心并不是单纯的怪物袭击，而是经验、理性、阶级与军纪如何共同把三人推向无法回头的地点。",
        "",
        "本篇只解释读到当前段落时能够知道的内容。出现伏笔时会说明它与本章前文的呼应，但不揭示小说后续答案。",
        "",
        "## 人物表",
        "",
        "| 人物 | 身份与当前信息 | 阅读时留意 |",
        "|---|---|---|",
        "| Will（威尔） | 叙事视角人物；原为偷猎者，加入守夜人约四年 | 林地经验可靠，但军阶较低，常压下自己的判断 |",
        "| Gared（加里德） | 在守夜人服役四十年的老兵 | 身体保存着严寒造成的伤，恐惧来自经验而非传闻 |",
        "| Ser Waymar Royce（威玛·罗伊斯爵士） | 十八岁的贵族幼子，入守夜人不足半年，本次指挥官 | 傲慢且缺乏经验，但会观察证据，也重视职责与荣誉 |",
        "| Mormont（莫尔蒙） | 给小队下达追踪命令的上级 | 序章只需知道其指挥关系 |",
        "| Maester Aemon（伊蒙学士） | 曾处理加里德的冻伤 | `maester` 兼具学者、医者和顾问职能 |",
        "",
        "## 地名与专名",
        "",
        "| 英文 | 本篇译名 | 当前可知含义 |",
        "|---|---|---|",
        "| the Night’s Watch | 守夜人 | 驻守长城并执行边境巡逻的组织，成员常穿黑衣 |",
        "| the Wall | 长城 | 巨大的冰墙，也是队伍想返回的安全边界 |",
        "| Castle Black | 黑城堡 | 守夜人的据点 |",
        "| wildlings | 野人／长城外居民 | 威尔等人正在追踪的北方人群，不是本段中的超自然存在 |",
        "| haunted forest | 鬼影森林 | 长城以北的森林；`haunted` 体现南方人的恐惧想象 |",
        "| the Others | 异鬼 | 序章中出现的未知非人存在；来源与目的暂不解释 |",
        "| direwolf | 冰原狼 | 体形巨大的狼类 |",
        "| take the black | 披上黑衣 | 加入守夜人 |",
        "",
        "## 段落目录",
        "",
    ]
    for page in sorted(page_ranges):
        ids = page_ranges[page]
        lines.append(f"- [PDF 第 {page} 页：{ids[0]}–{ids[-1]}](#{ids[0].lower()})")

    lines.extend(["", "---", "", "## 逐段精读", ""])

    for block, summary in zip(blocks, SUMMARIES, strict=True):
        order = int(block["order"])
        block_id = str(block["id"])
        original = str(block["text"])
        lines.extend(
            [
                f'<a id="{block_id.lower()}"></a>',
                f"### {block_id}",
                "",
                f"**来源：** {source_label(block)}",
                "",
                "**英文原段**",
                "",
                f"> {original}",
                "",
                "**难词与短语**",
                "",
            ]
        )
        vocab = vocabulary_for(original)
        if vocab:
            lines.extend(["| 词语 | 音标 | 词性 | 此处含义 | 用法提示 |", "|---|---|---|---|---|"])
            for term, ipa, pos, meaning, note in vocab:
                lines.append(f"| `{term}` | {ipa} | {pos} | {meaning} | {note} |")
        else:
            lines.append("本段没有新增的四级以上重点词；重点留意语气和上下文。")
        lines.extend(
            [
                "",
                "**这一段说了什么**",
                "",
                summary,
                "",
                "**值得注意的地方**",
                "",
                stage_note(order),
                "",
                "**背景与伏笔（无剧透）**",
                "",
                background_for(order),
                "",
                "[回到段落目录](#段落目录)",
                "",
                "---",
                "",
            ]
        )

    lines.extend(
        [
            "## 序章整体梳理",
            "",
            "序章的故事线非常简单：三人追踪野人，发现尸体消失，遭遇异鬼，威玛被杀后又以异常状态起身袭击威尔。真正复杂的是人物为何明知危险仍继续前进。加里德掌握经验却没有权力；威玛掌握权力，也能进行合理推理，却轻视无法量化的经验；威尔最了解现场，但阶级和军纪让他只能执行。悲剧来自超自然威胁，也来自信息与权力没有落在同一个人身上。",
            "",
            "### 人物关系",
            "",
            "- 威玛是正式指挥官；加里德与威尔必须服从。",
            "- 加里德资历最深，却因身份较低且长期被嘲弄，无法让警告变成命令。",
            "- 威尔既相信加里德，又畏惧威玛的权力；最后还必须独自面对职责与求生的选择。",
            "- 威玛的形象有意保持复杂：他傲慢、粗鲁、判断失误，却在真正遭遇敌人时勇敢迎战。",
            "",
            "### 关键意象",
            "",
            "| 意象 | 在序章中的作用 |",
            "|---|---|",
            "| cold / 寒冷 | 从天气、冻伤记忆逐渐变成具有主动敌意的力量 |",
            "| silence / 沉默 | 自然界有声而异鬼无声；沉默成为危险存在的证据 |",
            "| black and white / 黑与白 | 守夜人的黑衣、白雪、苍白武器构成视觉对抗 |",
            "| eyes / 眼睛 | 谁能看见、谁拒绝看见贯穿全章；蓝眼标记最后的异常改变 |",
            "| sword / 剑 | 威玛华丽的新剑象征贵族身份，碎裂则宣告人类秩序和技术的失效 |",
            "| `Dead is dead` | 开头的常识判断在结尾被彻底推翻，形成首尾闭环 |",
            "",
            "### 当前仍未解答的问题",
            "",
            "1. 野人最初为何集体倒下，又为何全部消失？",
            "2. 异鬼为何在此出现，它们是否有明确目的？",
            "3. 异鬼的甲胄与武器由什么制成？",
            "4. 威玛死亡后为何能够起身，蓝眼意味着什么？",
            "5. 加里德去了哪里，他是否察觉或躲过了这场袭击？",
            "",
            "这些问题只作为继续阅读的观察点；本篇不提供后文答案。",
            "",
            "## 词汇总表",
            "",
            "| 词语 | 音标 | 词性 | 核心释义 |",
            "|---|---|---|---|",
        ]
    )
    used_text = " ".join(str(block["text"]) for block in blocks)
    for term, ipa, pos, meaning, _ in VOCAB:
        if term_present(term, used_text):
            lines.append(f"| `{term}` | {ipa} | {pos} | {meaning} |")

    lines.extend(
        [
            "",
            "## 使用说明",
            "",
            "- 后续提问可直接引用段落编号，例如“解释 `PRO-P013-088` 的武器描写”。",
            "- 本篇不等同于逐句直译；“这一段说了什么”负责解释信息，“值得注意的地方”负责分析写法。",
            "- 背景栏只采用当前读者可知信息。标为“合理推断”或“阅读推测”的内容并非文本明说。",
            "",
        ]
    )
    return english_names("\n".join(lines))


def build_source_map(blocks: list[dict[str, object]]) -> dict[str, object]:
    pages = []
    for page in range(6, 16):
        pages.append(
            {
                "page": page,
                "block_ids": [str(b["id"]) for b in blocks if int(b["page"]) <= page <= int(b["end_page"])],
            }
        )
    block_records = []
    for block, summary in zip(blocks, SUMMARIES, strict=True):
        order = int(block["order"])
        block_records.append(
            {
                "id": str(block["id"]),
                "page": int(block["page"]),
                "end_page": int(block["end_page"]),
                "type": "paragraph",
                "order": order,
                "original_text": str(block["text"]),
                "translation": "",
                "paragraph_explanation_zh": english_names(summary),
                "reading_note_zh": english_names(stage_note(order)),
                "background_note_zh": english_names(background_for(order)),
                "bbox": [0, 0, 0, 0],
                "confidence": "high",
                "refs": [],
                "insert_after": str(block["id"]),
            }
        )
    glossary = [
        {"term": term, "translation": english_names(meaning), "note": english_names(note)}
        for term, _, _, meaning, note in VOCAB
        if term_present(term, " ".join(str(b["text"]) for b in blocks))
    ]
    return {
        "paper": {
            "title": "A Game of Thrones — Prologue",
            "author": "George R. R. Martin",
            "source_type": "pdf",
            "language": "en",
            "source_path": str(PDF),
            "pdf_page_range": [6, 15],
            "reader_mode": "spoiler-free close reading; no full Chinese translation",
        },
        "blocks": block_records,
        "pages": pages,
        "figures": [],
        "glossary": glossary,
    }


def main() -> None:
    blocks = extract()
    if len(blocks) != len(SUMMARIES):
        raise RuntimeError(f"Expected {len(SUMMARIES)} blocks, extracted {len(blocks)}")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "AGOT_Prologue_精读.md").write_text(build_markdown(blocks), encoding="utf-8")
    (OUT / "source_map.json").write_text(
        json.dumps(build_source_map(blocks), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (OUT / "translation_notes.md").write_text(
        "# Extraction and reading notes\n\n"
        "- Source format: selectable-text PDF (`pdf-text`).\n"
        "- Scope: PDF pages 6–15, the complete Prologue.\n"
        "- Paragraph count after cross-page repair: 109.\n"
        "- Cross-page paragraphs were merged before IDs were assigned.\n"
        "- The source file apparently omits the opening quotation mark in the first paragraph; it was preserved rather than silently rewritten.\n"
        "- No full Chinese translation was requested; `translation` fields are intentionally empty.\n"
        "- No figures or tables occur in this scope.\n"
        "- Background commentary is spoiler-free and does not use later-book revelations.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
