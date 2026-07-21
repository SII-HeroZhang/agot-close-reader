#!/usr/bin/env python3
"""Build Chapter 9 (TYRION) close-reading Markdown."""

from pathlib import Path

from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter8_reader import VOCAB as BASE_VOCAB


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "Winterfell深处传来狼嚎，声音像一面哀悼的旗帜笼罩整座城堡。",
    "Tyrion从书中抬头并打寒战；狼嚎把他从温暖现实拖入被群狼追逐的黑暗想象。",
    "第二声狼嚎使Tyrion收起关于季节变化的古老论著，他意识到自己已在图书馆读了一整夜。",
    "Tyrion活动僵硬疼痛的短腿，路过趴在一本写高个王子的传记上熟睡的septon。",
    "他在冷空气中艰难走下图书馆塔狭窄螺旋石阶，下方已有骑士练武和人们交谈。",
    "Tyrion看见Sandor和Joffrey；Joffrey抱怨direwolf的叫声害他一夜无法睡觉。",
    "Sandor在披甲后表示可以让direwolf永远安静，并用长剑试重。",
    "Joffrey对派“狗”杀“狗”感到兴奋，并说Winterfell的狼多到Starks不会察觉少一只。",
    "Tyrion从最后一级跳下，讽刺Joffrey连六都数不清，Starks却能。",
    "Joffrey至少还知道脸红，说明他听懂了羞辱。",
    "Sandor装作没看见Tyrion，把他的声音称作来自空气精灵。",
    "Joffrey照例被这场演戏逗笑；习以为常的Tyrion只说自己在下面。",
    "Sandor低头假装刚发现Tyrion，又用“小领主”和没看见他继续嘲笑身高。",
    "Tyrion直言今天无意忍受冒犯，转而命Joffrey去安慰Eddard夫妇。",
    "Joffrey闹别扭地问，他的安慰对Starks能有什么用。",
    "Tyrion承认没有实际用处，但这是王子必须履行的礼仪，而且他的缺席已被注意。",
    "Joffrey说Bran与自己无关，他也无法忍受女人的哭号。",
    "Tyrion伸手重重打了Joffrey一耳光，使他的脸颊迅速发红。",
    "Tyrion警告Joffrey再说一个字，自己就会再打他。",
    "Joffrey马上威胁要告诉Mother。",
    "Tyrion实现警告，再打一次，使Joffrey两边脸颊都火辣发红。",
    "Tyrion允许Joffrey告状，但要求他首先跪在Starks面前，说出一整套合乎王子身份的慰问。",
    "Joffrey强忍眼泪点头，捂着脸逃出院子，Tyrion注视他离开。",
    "Sandor的巨大阴影覆住Tyrion，黑狗头盔下的人像悬崖一样压迫，但Tyrion没有退缩。",
    "Sandor警告Tyrion，王子会记住今天的羞辱。",
    "Tyrion说他正希望Joffrey记住，还用“好狗”反过来命令Sandor提醒主人，然后询问Jaime在哪里。",
    "Sandor告诉他，Jaime正与queen共进早餐。",
    "Tyrion草草点头后尽快离开，还用吹口哨掩饰紧张；他同情今天第一个与Sandor对练的骑士。",
    "Guest House的早餐气氛冰冷沉闷，Jaime、Cersei与孩子们在低声交谈。",
    "Tyrion未受邀请便入座，直接问Robert是否仍在睡觉。",
    "Cersei以一贯嫌恶的神情回答，Robert整夜未眠，正与Eddard一起并深深同情Starks。",
    "Jaime懒洋洋地讽刺Robert“心很大”；Tyrion知道哥哥很少认真，但也记得童年只有Jaime给过他爱与尊重。",
    "Tyrion点了大量食物和黑啤酒，然后观察穿着同样深绿、佩戴金饰的Jaime与Cersei，他们看起来极像一对双胞胎。",
    "Tyrion想象有个双胞胎的感受，又自嘲说每天在镜中看自己已够可怕，不想再有另一个自己。",
    "Tommen主动询问Uncle是否有Bran的新消息。",
    "Tyrion说自己昨夜去过病房，Bran没有变化，maester却把这视为希望迹象。",
    "Tommen怯生生地说不想Bran死；Tyrion认为他是善良的孩子，与Joffrey完全不同。",
    "Jaime想起Eddard也曾有一个叫Brandon的兄弟，被Targaryen杀死，因而称这个名字不吉利。",
    "Tyrion边撕黑面包边否定“Brandon”总是不幸的说法。",
    "Cersei立刻警惕地盯着Tyrion，追问他这句话的含义。",
    "Tyrion歪嘴笑着解释，maester认为Bran仍可能活下来，Tommen的希望也许会实现。",
    "Myrcella惊喜，Tommen紧张地笑；Tyrion却专门观察Jaime和Cersei，没有错过两人一闪而过的目光交换以及Cersei随后低头。",
    "Jaime要求Tyrion准确复述maester的原话。",
    "Tyrion故意一边慢慢嚼脆培根一边回答：如果Bran会死，四天无变化的时间让他本应早已死去。",
    "Myrcella进一步问Bran是否会恢复；Tyrion认为她有Cersei的美貌，却没有母亲的性情。",
    "Tyrion坦白Bran脊背和双腿已重伤，目前只靠蜂蜜水维生；即使醒来能进食，也永远无法再走路。",
    "Cersei重复“如果他醒来”，并追问这种可能性有多大。",
    "Tyrion说只有众神知道，maester也只是希望；他还怀疑守在窗外日夜嚎叫、每次被赶都返回的direwolf正维系Bran生命。",
    "Cersei对direwolves感到战栗，称它们不自然又危险，决定不让任何一只随队南下。",
    "Jaime提醒Cersei，direwolves总跟在Sansa和Arya身边，要阻止并不容易。",
    "Tyrion开始吃鱼，顺势询问王室队伍是否很快离开。",
    "Cersei说巴不得尽快离开，随后才意识到Tyrion说的是“你们”，吃惊地问他是否要留在Winterfell。",
    "Tyrion说Benjen将带Jon回Night’s Watch，他打算同行，亲眼看看人人谈论的Wall。",
    "Jaime开玩笑问，Tyrion是否准备穿上黑衣、加入Night’s Watch。",
    "Tyrion笑称自己不可能守独身誓，只想站在Wall顶端，对着世界边缘撒尿。",
    "Cersei立刻起身，说孩子不应听这种脏话，带着Tommen和Myrcella离开。",
    "Cersei离开后，Jaime认真审视Tyrion，认为Eddard不会在儿子生死未卜时离开Winterfell。",
    "Tyrion判断Robert会命令Eddard出发，而他留下也无法改变Bran的伤情。",
    "Jaime说Eddard可以结束Bran的痛苦；如果是自己的儿子，他会把安乐死当作仁慈。",
    "Tyrion建议Jaime不要向Eddard提这个意见，因为Eddard绝不会善意接受。",
    "Jaime认为Bran即使活下来也会成为残疾且畸形的人，所以自己宁要干净的死亡。",
    "Tyrion故意耸动扭曲的肩膀，以“代表畸形者”反驳：死亡无法挽回，生命却充满可能。",
    "Jaime笑称Tyrion是性情反常的小imp。",
    "Tyrion坦然承认，又说自己真希望Bran醒来，因为很想听听他会说什么。",
    "Jaime的笑容像酸奶一样凝固变质，他阴沉地说Tyrion有时会让人怀疑他站在哪一边。",
    "Tyrion用黑啤酒咽下面包和鱼，像狼一样朝Jaime露齿而笑，反讽说家人当然知道他多么爱自己的家族。",
]


KEY_NOTES = {
    1: "`flag of mourning`把声音视觉化：狼嚎不只表达一只动物的情绪，而是像丧旗一样向整座城堡公告灾难。",
    2: "图书馆的温暖与“心智中的黑森林”对照，显示理性而博学的Tyrion也会对direwolf声产生原始恐惧。",
    3: "一本讨论季节变化的百年古书建立Tyrion的求知欲，也让世界的异常季节成为当下可知的学术难题。",
    4: "熟睡者的书恰好写一位高个王子，与Tyrion艰难活动的身体形成一个无声、带苦味的笑话。",
    8: "Joffrey将Sandor也叫作`dog`，把人降为自己可驱使的动物；他的兴奋集中在语言游戏和杀戮上。",
    9: "Tyrion用数量而不是道德说教拆解Joffrey的话，一句便同时保护direwolves与羞辱王子。",
    11: "Sandor把Tyrion的身高当作固定表演；Joffrey“总是笑”说明这不是即兴玩笑，而是已建立的群体等级。",
    16: "Tyrion坦白慰问没有实际效用，但他仍重视礼仪：王子的公开行为会向他人表达王室如何看待Starks。",
    18: "身高有限的Tyrion必须“reach up”才能打到Joffrey；空间动作同时强调他的身体限制与他此刻掌握的权威。",
    21: "第二个耳光直接回应“再说一字”的条件，Tyrion用严格执行而不是音量建立威慑。",
    22: "这一长串慰问语与Joffrey的简短自私句形成反差；Tyrion几乎在为不合格的王储写一份礼仪脚本。",
    24: "Sandor被比作悬崖，铠甲还遮住阳光，身材和黑甲构成对Tyrion的物理压迫，但对话中的主动权仍在Tyrion手里。",
    26: "Tyrion用`good dog`将Sandor的Hound身份反过来作为贬称，他的语言成为抵消对方身体优势的武器。",
    28: "吹口哨显得轻松，但他“尽可能快”地离开并想到Sandor的坏脾气，说明Tyrion并未真正忽视威胁。",
    31: "Cersei对Tyrion的嫌恶被写成从他出生日开始从未改变，一句便将当下早餐的冷淡延伸到整个家庭历史。",
    32: "Tyrion知道Jaime轻佻，却因童年仅有的爱而宽恕他；这让兄弟关系比单纯互相怀疑更复杂。",
    33: "双胞胎穿同色衣服、佩同样金饰，外观上构成高度一致的一组；Tyrion则在餐桌上同时是手足与局外观察者。",
    34: "镜子笑话是Tyrion主动抢先说出对自己外貌的恶意评价，以自嘲掌控别人可能使用的伤害。",
    37: "Tyrion用Jaime/Tyrion反证Joffrey/Tommen：同一家庭的兄弟不会因血缘就具有相同性情。",
    40: "Cersei从冷淡立刻转为警惕，叙事没有解释原因，而是让读者像Tyrion一样通过反应推理。",
    42: "孩子们的喜悦与成人间短暂目光形成对照。**文本事实**只是Jaime和Cersei交换眼神；它的具体含义尚未证实。",
    44: "Tyrion先咬脆培根、慢慢咀嚼再回答，用餐节奏拉长Jaime和Cersei的等待，也测试他们对每一条消息的反应。",
    45: "`all of her mother’s beauty, and none of her nature`用对称句式同时赞美Myrcella外貌和贬低Cersei品性。",
    46: "Tyrion不用儿童化安慰欺骗Myrcella，而是坦白区分“活下来”、“醒来”与“恢复行走”三种不同结果。",
    48: "Tyrion用`I would swear`表示他对direwolf的判断是强烈直觉，不是医学证实；maester允许它留下的理由也是病人似乎有反应。",
    49: "Cersei的`unnatural`不是中立分类，而是将无法控制、无法解释的动物关系定义为威胁。",
    52: "Cersei回声重复`we`时才发现Tyrion把自己排除在南下队伍之外，短暂的语法错位暴露了计划分歧。",
    55: "Tyrion把Wall这个宏大、近乎神话化的边界地标转化为粗俗身体笑话，既抵抗庄严语气，也表达他真想站上最高处。",
    57: "当Cersei与孩子离开后，Jaime的语气立刻从懒散玩笑转为冷静计算，说明他并非真的什么都不认真。",
    59: "Jaime把杀死无法行走的儿子命名为`mercy`，正如他把自己的偏好`a good clean death`当作普遍标准。",
    62: "Tyrion不否认自己被他人视为`grotesque`，而是把这个侮辱转化成发言资格；他以自己的存在反证“死亡胜过残疾生命”。",
    64: "Tyrion说对Bran的话感兴趣，把病情问题重新变成“Bran是否看见或知道什么”的信息问题。",
    65: "笑容`curdled like sour milk`是可见的变质；Jaime的亲昵称呼未变，含义却从手足玩笑转为警告。",
    66: "`wolfishly`让Tyrion在一章始于狼嚎的章节末尾暂时获得狼的形象；“爱家人”与Jaime的质问同时保留亲情和威胁。",
}


STAGES = [
    (1, 13, "本段从狼嚎与图书馆塔写出Tyrion的博学、身体限制与被嘲笑日常，他以观察和语言对抗体格优势。"),
    (14, 28, "本段围绕Joffrey应否慰问Starks展开；Tyrion强迫王储履行公开义务，又与Sandor交换威胁。"),
    (29, 44, "本段转入Lannister家族早餐；Tyrion在闲谈、进食和亲情回忆中密切观察Jaime与Cersei对Bran生还消息的反应。"),
    (45, 56, "本段区分Bran存活、醒来与恢复的不同可能，同时交代Tyrion改道Wall的计划。"),
    (57, 66, "本段在孩子们离开后进入更尖锐的兄弟对话；残疾生命的价值、Bran可能的证言与家族立场彼此缠绕。"),
]


BACKGROUNDS = {
    3: "**文本事实：** Tyrion正读一位maester百年前撰写的季节变化论著，表明这个世界的学者也研究不规则季节。",
    7: "**文本事实：** Sandor Clegane被称为Hound，是Joffrey的近身护卫；此处他主动提议杀掉嚎叫的direwolf。",
    16: "**当前可知制度：** 王储对受灾高等贵族家庭表示慰问，属于公开礼仪和政治义务，不取决于它能否治疗伤者。",
    22: "**文本事实：** Bran坠落后仍昏迷，Eddard与Catelyn正守着他；Joffrey此前没有去慰问。",
    31: "**文本事实：** Robert为Bran的遭遇整夜未睡，当时正与Eddard在一起。",
    38: "**文本事实：** Eddard已故的兄弟也叫Brandon，他曾是Targaryen手中的人质并被杀死。",
    42: "**文本事实：** Tyrion观察到Jaime与Cersei短暂对视，Cersei随即低头。**合理推测：** 他正有意用Bran可能存活的消息测试两人，但眼神的确切意义尚未确认。",
    46: "**文本事实：** Bran脊背与腿部重伤，仍在昏迷，靠蜂蜜和水维持生命；Tyrion判断他即使醒来也不会再行走。",
    48: "**文本事实：** Bran的direwolf日夜守在病房窗外，被赶走后总会返回；maester认为它在场时Bran似乎更坚强。",
    53: "**文本事实：** Benjen将返回Night’s Watch，Jon将同行加入；Tyrion计划只作访客前往Wall。",
    54: "**术语：** `take the black`意为穿上Night’s Watch的黑衣、宣誓加入组织，其成员必须守独身等终身誓言。",
    62: "**文本事实：** Tyrion因身体被他人称为`grotesque`或`imp`；此处他以自身生活经验反驳Jaime对残疾生命的判决。",
    64: "**文本事实：** Bran坠落的原因尚未向Tyrion公开；Tyrion表示如果Bran醒来，他对Bran可能说出的事很感兴趣。",
}


EXTRA_VOCAB = [
    ("mourning", "/ˈmɔːrnɪŋ/", "n.", "哀悼；服丧", "`flag of mourning`比喻丧旗"),
    ("snug", "/snʌɡ/", "adj.", "温暖舒适的；紧凑的", "此处形容图书馆"),
    ("discourse", "/ˈdɪskɔːrs/", "n.", "论述；学术论著", "正式书面用词"),
    ("leatherbound", "/ˈleðərbaʊnd/", "adj.", "皮革装订的", "形容古书"),
    ("laborious", "/ləˈbɔːriəs/", "adj.", "费力的；艰难的", "与身体行动搭配"),
    ("corkscrew", "/ˈkɔːrkskruː/", "v.", "像螺旋起子般盘旋", "描述楼梯环绕塔身"),
    ("clangor", "/ˈklæŋər/", "n.", "铿锵声；连续金属撞击声", "文学性听觉词"),
    ("infested", "/ɪnˈfestɪd/", "adj.", "大量滋生有害生物的", "带强烈贬义"),
    ("mummer's farce", "/ˈmʌmərz fɑːrs/", "n.", "演员的滑稽闹剧", "此处指反复上演的身高嘲笑"),
    ("insolence", "/ˈɪnsələns/", "n.", "傲慢无礼；冒犯", "对权威者的不敬"),
    ("petulant", "/ˈpetʃələnt/", "adj.", "闹别扭的；急躁任性的", "常形容孩子气反应"),
    ("abide", "/əˈbaɪd/", "v.", "忍受；容忍", "`cannot abide`=无法忍受"),
    ("headlong", "/ˈhedlɔːŋ/", "adv.", "匆忙不顾一切地；一头向前", "描述逃走"),
    ("loom", "/luːm/", "v.", "高大逼近；阴森地笼罩", "制造身体威胁"),
    ("perfunctory", "/pərˈfʌŋktəri/", "adj.", "敷衍的；草率的", "`a perfunctory nod`"),
    ("briskly", "/ˈbrɪskli/", "adv.", "轻快地；敏捷地", "此处带尽快离开之意"),
    ("abed", "/əˈbed/", "adv.", "在床上；卧床", "古风用法"),
    ("distaste", "/dɪsˈteɪst/", "n.", "反感；嫌恶", "`faint distaste`"),
    ("tumble", "/ˈtʌmbəl/", "n.", "蓬松散落的一团", "此处描述时髦卷发"),
    ("contemplate", "/ˈkɑːntəmpleɪt/", "v.", "仔细思考；凝视", "正式书面用词"),
    ("timorously", "/ˈtɪmərəsli/", "adv.", "怯生生地；胆怯地", "表现Tommen的小心"),
    ("peas in a pod", "/piːz ɪn ə pɑːd/", "idiom", "像一个豆荚里的豆子；非常相像", "`less than` 表示远非相同"),
    ("warily", "/ˈwerəli/", "adv.", "警惕地；谨慎地", "防备潜在危险"),
    ("shatter", "/ˈʃætər/", "v.", "使粉碎；使严重破裂", "此处形容骨骼重伤"),
    ("celibate", "/ˈselɪbət/", "adj./n.", "独身禁欲的；独身者", "Night’s Watch誓言相关"),
    ("lingering", "/ˈlɪŋɡərɪŋ/", "adj.", "拖延的；迟迟不去的", "`lingering in the shadow of death`"),
    ("torment", "/ˈtɔːrment/", "n.", "严重痛苦；折磨", "身体或精神苦难"),
    ("grotesque", "/ɡroʊˈtesk/", "n./adj.", "畸形之人；怪诞可怕的", "此处是侮辱性人物标签"),
    ("perverse", "/pərˈvɜːrs/", "adj.", "故意反常的；乖张的", "指与常规价值判断相反"),
    ("curdle", "/ˈkɜːrdəl/", "v.", "凝结变质；使酸败", "比喻笑容突然变冷"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB


def main():
    blocks = extract_range(84, 89, "TYRION", "CH09")
    write_chapter(
        out=OUT, chapter=9, pov="TYRION", page_start=84, page_end=89,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观设定；重点在Tyrion的观察、讽刺、家族互动或对Bran伤情的判断。",
        vocab=VOCAB,
        guide="Bran坠落后的狼嚎笼罩Winterfell。Tyrion结束通宵阅读，在院中阻止Joffrey伤害direwolf，并强迫他去慰问Starks。随后的Lannister家族早餐看似只谈Bran的病情和南下安排，Tyrion却一直在观察Jaime与Cersei对“Bran可能醒来”的微妙反应。本章同时建立他前往Wall的计划，并用他自身经验反驳“残疾不如死亡”的判决。",
        people=[
            ("Tyrion Lannister", "本章视角人物；博学、善于讽刺和观察反应"),
            ("Joffrey Baratheon", "王储；抱怨direwolf并拒绝慰问Starks"),
            ("Sandor Clegane", "Joffrey的近身护卫，被称为Hound"),
            ("Cersei Lannister", "queen，Tyrion的姐妹；对Bran存活和direwolves表现警惕"),
            ("Jaime Lannister", "Tyrion的兄长、Cersei的双胞胎兄弟，Kingsguard成员"),
            ("Tommen / Myrcella", "Joffrey的弟弟和妹妹，真诚关心Bran的安危"),
        ],
        terms=[
            ("take the black", "宣誓加入Night’s Watch"),
            ("Wall", "北方边界的巨大冰墙，Tyrion打算亲眼参观"),
            ("Hound", "Sandor Clegane的绰号，也被Tyrion用来反讽他是受主人驱使的狗"),
            ("Guest House", "Winterfell中安置王室访客的建筑"),
        ],
        synthesis="Chapter 9的核心不只是展示Tyrion聪明，而是展示他如何将聪明变成生存工具。他无法与Sandor比较体格，便用语言夺回主动；他在家中长期遭受嫌弃，便用自嘲控制侮辱；他不知道Bran坠落的真相，便通过递出消息、拖延回答和观察短暂眼神收集线索。结尾的“生命充满可能”也表明，他对Bran的关心与自己的身体经验无法分开。",
        contrasts=[
            "**书本／狼嚎：** 理性研究的温暖室内，被无法解释的原始声音打断。",
            "**Sandor的身体／Tyrion的语言：** 一方以高大和铠甲威胁，另一方以反讽抵抗。",
            "**Joffrey／Tommen与Myrcella：** 同一家庭的孩子对Bran的同情完全不同。",
            "**孩子的欣喜／成人的对视：** Bran可能活下来的同一条消息引发相反反应。",
            "**干净的死／充满可能的生：** Jaime从健全者视角判决残疾，Tyrion则以残疾者身份反驳。",
        ],
        questions=[
            "Jaime和Cersei听说Bran可能醒来时，那次短暂对视意味着什么？",
            "Bran的direwolf是否真的影响了他的生命状态？",
            "Tyrion前往Wall只是出于好奇，还有其他需求？",
            "Bran若醒来，他可能说出什么？",
        ],
        extraction_notes="提取器已将 PDF pp.86–87 的双胞胎外貌描写保留为同一跨页段落",
    )
    print(f"Wrote Chapter 9 with {len(blocks)} paragraphs")


if __name__ == "__main__":
    main()
