#!/usr/bin/env python3
"""Build Chapter 17 (BRAN) close-reading Markdown."""

from pathlib import Path

from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter16_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

SUMMARY_BY_ORDER = {
    1: "Bran感觉自己仿佛已经坠落了许多年。",
    2: "黑暗中的声音要他飞，但他不知道如何飞，只能继续下坠。",
    3: "梦中Maester Luwin制作并从屋顶扔下一个穿Bran衣服的陶土男孩；Bran一边坠落一边坚持自己从不失足。",
    4: "地面仍在灰雾下很远处，但越来越近；Bran确信自己会像普通噩梦那样在撞地前醒来。",
    5: "声音反问：如果没有醒来呢？",
    6: "黑暗、寒冷和逼近的地面使Bran想哭。",
    7: "声音用押韵式命令纠正他：不要cry，而要fly。",
    8: "Bran反复说自己不会飞。",
    9: "声音问他从未尝试过，怎么能确定。",
    10: "Bran发现一只crow与自己一同盘旋下落，便向它求救。",
    11: "crow说自己正在帮忙，却突然问Bran有没有corn。",
    12: "Bran从口袋掏出金色谷粒，它们也在空中与他一起下坠。",
    13: "crow落在他的手上吃corn。",
    14: "Bran问它是否真的是crow。",
    15: "crow反问Bran是否真的在坠落。",
    16: "Bran以这一切只是梦来解释。",
    17: "crow质疑这个结论。",
    18: "Bran坚持撞地时自己会醒。",
    19: "crow冷静地说撞地意味着死亡，然后继续吃corn。",
    20: "Bran已能看见雪山、森林与银线般河流，于是闭眼哭泣。",
    21: "crow说哭没有用，答案是飞，并以自己能飞作为示范。",
    22: "Bran指出crow拥有翅膀。",
    23: "crow回答Bran也可能拥有翅膀。",
    24: "Bran摸索肩膀，寻找羽毛。",
    25: "crow解释翅膀不止一种。",
    26: "Bran注意到自己异常消瘦；灰雾中浮出金色发光的脸，重复把他推下塔前说过的话。",
    27: "这段记忆使Bran尖叫。",
    28: "crow叫他忘掉并收起那段记忆，又啄他使金色面孔消失。",
    29: "Bran下坠更快，哭着问crow究竟在对自己做什么。",
    30: "crow说是在教他飞。",
    31: "Bran仍坚持自己不会。",
    32: "crow说他此刻已经在飞；本PDF版本印作tight now，结合语境通常理解为right now。",
    33: "Bran认为自己只是在坠落。",
    34: "crow说每次飞行都始于一次坠落，并命他向下看。",
    35: "Bran承认自己害怕。",
    36: "crow以大写命令他必须往下看。",
    37: "Bran俯瞰整个世界；极度清晰的景象暂时取代恐惧。",
    38: "他从高空看见Winterfell众人和weirwood；城堡尺度缩小，weirwood却察觉凝视并回望他。",
    39: "向东看时，他看见Catelyn与Ser Rodrik乘船、桌上的血染匕首，以及他们尚未察觉的风暴。",
    40: "向南看时，他看见悲伤的Eddard、哭泣的Sansa和把秘密藏在心中的Arya。",
    41: "三道象征性阴影笼罩他们：hound面孔、金色太阳铠甲，以及内部只有黑暗与黑血的石甲巨人。",
    42: "Bran越过narrow sea看见Free Cities、Dothraki sea、Vaes Dothrak、Jade Sea与Asshai，那里有dragons在日出下苏动。",
    43: "最后他向北越过Wall和沉睡的Jon，看见无尽冰原，直到世界尽头光幕之外的heart of winter，恐惧得哭喊。",
    44: "crow说Bran现在已经知道自己为什么必须活下去。",
    45: "Bran仍不理解，边坠落边问为什么。",
    46: "crow用Stark家语回答：winter is coming。",
    47: "Bran发现crow有第三只眼；下方冰矛上刺着无数其他dreamers的骨骸。",
    48: "恐惧中，他想起自己曾问Eddard：害怕时还能不能勇敢。",
    49: "记忆中的Eddard回答，只有害怕时才谈得上勇敢。",
    50: "crow逼Bran立即选择：飞，或者死。",
    51: "死亡以尖叫着伸手的形象逼近。",
    52: "Bran张开双臂，终于飞了起来。",
    53: "看不见的翅膀承接风力，把他从冰刺上方拉起；飞行比攀爬更自由。",
    54: "Bran欣喜地宣布自己会飞了。",
    55: "three-eyed crow冷淡回应，随后拍翼遮眼并啄中Bran两眼之间，使他剧痛。",
    56: "Bran尖叫着问crow在做什么。",
    57: "灰雾像帷幕被撕开，crow变成黑发serving woman；Bran发现自己躺在Winterfell塔房，女人惊叫他醒了。",
    58: "Bran额心仍有灼痛却没有伤口；他虚弱眩晕，想下床时身体毫无反应。",
    59: "direwolf跃上他的双腿而Bran毫无感觉；狼已长大许多，身体的温暖包住他。",
    60: "Robb冲进房间时direwolf正舔Bran的脸；Bran平静地为它命名Summer。",
}

SUMMARIES = [SUMMARY_BY_ORDER[i] for i in range(1, 61)]

KEY_NOTES = {
    1: "years把昏迷期间的客观时间转成无尽主观坠落，章节开头没有先确认Bran是否活着。",
    3: "陶土替身把身体写成可烧硬、可破碎的物件；Bran说“从不坠落”与正在坠落构成梦的反讽。",
    4: "反复出现的instant before建立Bran用于安慰自己的梦境规则，下一句立即攻击这条规则。",
    7: "cry／fly只差一个辅音，crow把情绪反应改写成生存行动，形成全章反复的语言节奏。",
    11: "生死训导突然转成讨corn的滑稽口吻，使crow既神秘又顽皮，拒绝成为庄严导师的单一形象。",
    15: "反问把“crow是否真实”转回Bran自身处境：梦中形象真假不如坠落后果真假重要。",
    19: "死亡警告与继续啄食并置，crow把Bran最恐惧的事当作简单事实。",
    25: "different kinds of wings把飞行从身体器官转成尚未说明的能力或认知方式；当前不能确定具体机制。",
    26: "金色面孔和原句直接恢复Chapter 8结尾的压抑记忆；消瘦也表明外界已经过去一段时间。",
    28: "crow不是说记忆不真实，而是说Bran现在不需要它；生存训练暂时压过追问凶手。",
    32: "页面图像和文字层均印作tight now，并非提取器误认；结合Bran下一句，语义通常理解为right now。本文件保留源版措辞并注明疑似版本排印错误。",
    34: "every flight begins with a fall把事故重新组织成起点；它没有美化危险，而是要求Bran在危险中选择行动。",
    37: "恐惧因观看而暂时消失：look down既是面对死亡，也是获得超越个人身体的视野。",
    38: "俯瞰使人造城墙缩成泥地线条，weirwood却能回望；权力尺度与古老自然意识形成反差。",
    39: "读者已知匕首和航程；storm既可按画面理解为天气，也可能具有象征意味，不能提前锁定。",
    40: "三人分别以pleading、crying、holding secrets出现，把南方危机压缩成求情、哀伤和沉默。",
    41: "本段采用shadow而非姓名。hound与前文人物有明显联想，但三道影子的完整对应和未来含义仍不应定论。",
    42: "视野从家族危机扩展到世界地理；dragons stirred是梦中画面，不能据此断言现实中的具体状态。",
    43: "句中反复north推动视线越过已知地图；对heart of winter的恐惧是本章最明确的生存理由。",
    46: "家族格言在这里不再只是气候警告，而成为crow解释Bran必须活下去的答案。",
    47: "第三只眼象征一种可怕的知见；其他dreamers的骨骸说明训练具有失败和死亡风险。",
    48: "Bran用自己的童声回忆Chapter 1的问题，把父亲的伦理教导带入没有父亲在场的选择。",
    50: "Choose是转折核心：crow无法替Bran飞，导师能做的是逼他承认选择属于自己。",
    52: "极短句在长时间坠落后制造突然的解放；飞行首先是Bran接受行动，而非长出可见羽翼。",
    53: "“better than climbing”把新能力与Bran旧身份最热爱的活动连接，也暗示醒来后的Bran已不再是原来的攀爬者。",
    55: "crow先教会飞再啄额心，帮助带有疼痛和强制；第三眼位置与两眼之间的刺痛相互呼应。",
    57: "veil意象标记梦与清醒界面被撕开；serving woman的叫声把宇宙视野骤然拉回具体病房。",
    58: "没有外伤却有灼痛保留梦境的身体余波；“nothing happened”从普通失败逐步显露更严重事实。",
    59: "狼落在腿上却无感觉，是瘫痪状态最克制的揭示；与此同时狼的热量提供生命与陪伴。",
    60: "Summer与heart of winter、冰与死亡形成直接对照；命名说明Bran醒来后获得了新的确定性。",
}

STAGES = [
    (1, 19, "Bran在无尽梦境中坠落，three-eyed crow以fly／cry的语言游戏破坏他“撞地前会醒”的自我安慰。"),
    (20, 36, "crow让Bran承认死亡风险，并把被推下塔的记忆暂时移开，迫使他从寻找可见翅膀转向面对坠落。"),
    (37, 47, "Bran获得覆盖Winterfell、南方、东方和极北的梦中视野；heart of winter让生存使命第一次超出个人复仇。"),
    (48, 55, "Eddard关于勇气的旧话帮助Bran作出fly or die的选择；他飞起后又被crow啄中额心。"),
    (56, 60, "梦境撕开，Bran在Winterfell苏醒；腿部无感觉揭示身体代价，而direwolf的温暖与Summer之名提供反意象。"),
]

BACKGROUNDS = {
    3: "**前文联系：** Bran从塔上坠落后一直昏迷；陶土男孩是梦境形象，不是Maester Luwin现实中已被证实做过的仪式。",
    26: "**文本事实：** 金色面孔说出的原句与Chapter 8推Bran下塔前的话一致；Bran的意识正在触及被压住的记忆。",
    32: "**文本校勘：** 页面图像与文字层均为“flying tight now”，因此不是OCR错误；上下文语义通常应为“right now”。精读不擅改源文，只标注疑似版本排印错误。",
    38: "**专名：** weirwood是Winterfell godswood中心的心树；此前已写其树干有人脸。梦中它主动回望Bran。",
    39: "**前文联系：** Catelyn正携刺杀Bran所用的匕首前往King’s Landing，Ser Rodrik在海上晕船。",
    40: "**前文联系：** Eddard与Robert为Lady争执；Sansa失去Lady，Arya则经历Mycah之死和证词冲突。",
    41: "**事实／推测：** 这些都是梦中的shadow意象。可以依据hound、gold和stone建立联想，但当前文本没有给出完整、唯一的身份答案。",
    42: "**世界地理：** Free Cities和Dothraki sea位于narrow sea以东；Vaes Dothrak是Dothraki圣城，Asshai在已知世界遥远东方。",
    43: "**北方：** Wall以北仍有森林、海岸与冰原；光幕之外的heart of winter属于Bran梦中所见，地理与性质尚未解释。",
    46: "**家族格言：** “Winter is coming”是House Stark的words；在此被赋予超越普通季节变化的威胁语气。",
    47: "**称谓：** 直到本段读者才明确看见crow有三只眼；“three-eyed crow”由此成为稳定称呼。",
    58: "**身体事实：** Bran已经醒来，双腿无法按意愿动作；具体医学诊断和恢复可能性在当前段落尚未由Maester说明。",
    60: "**命名：** Bran的direwolf此前一直没有名字；Summer是他苏醒后的第一个明确决定，并与冬季意象对立。",
}

EXTRA_VOCAB = [
    ("brittle", "/ˈbrɪtəl/", "adj.", "硬而易碎的", "baked clay"),
    ("fling", "/flɪŋ/", "v.", "猛扔；抛掷", "flung him off a roof"),
    ("whirl", "/wɜːrl/", "v.", "旋转；打旋", "mists around Bran"),
    ("spiral", "/ˈspaɪrəl/", "v.", "盘旋升降", "crow spiraling down"),
    ("kernel", "/ˈkɜːrnəl/", "n.", "谷粒；玉米粒", "golden kernels"),
    ("grope", "/ɡroʊp/", "v.", "摸索", "grope for feathers"),
    ("taut", "/tɔːt/", "adj.", "绷紧的", "skin stretched taut"),
    ("caw", "/kɔː/", "v./n.", "乌鸦叫；鸦叫声", "the crow cawing"),
    ("plunge", "/plʌndʒ/", "v.", "猛冲；急坠", "plunge toward earth"),
    ("tapestry", "/ˈtæpəstri/", "n.", "挂毯；织锦般景象", "world spread below"),
    ("squat", "/skwɑːt/", "adj.", "低矮粗短的", "towers from above"),
    ("stubby", "/ˈstʌbi/", "adj.", "短粗的", "aerial perspective"),
    ("heft", "/heft/", "v.", "举起或掂量重物", "heft an anvil"),
    ("brood", "/bruːd/", "v.", "阴沉盘踞；沉思", "weirwood over the pool"),
    ("galley", "/ˈɡæli/", "n.", "桨帆船", "crossing the Bite"),
    ("heave", "/hiːv/", "v.", "剧烈起伏；作呕", "Ser Rodrik seasick"),
    ("loom", "/luːm/", "v.", "高大而阴森地逼近", "shadow over others"),
    ("visor", "/ˈvaɪzər/", "n.", "头盔面甲", "opened visor"),
    ("fabled", "/ˈfeɪbəld/", "adj.", "传说中的", "lands of Jade Sea"),
    ("cloak", "/kloʊk/", "v.", "覆盖；遮蔽", "forests cloaked in snow"),
    ("jagged", "/ˈdʒæɡɪd/", "adj.", "参差尖锐的", "ice spires"),
    ("spire", "/spaɪr/", "n.", "尖塔状物", "blue-white ice"),
    ("impale", "/ɪmˈpeɪl/", "v.", "刺穿并钉住", "bones on ice points"),
    ("pinion", "/ˈpɪnjən/", "n.", "鸟翼；翼端飞羽", "crow's wings"),
    ("falter", "/ˈfɔːltər/", "v.", "踉跄；动摇失稳", "falter in the air"),
    ("shrill", "/ʃrɪl/", "adj.", "尖厉刺耳的", "scream"),
    ("veil", "/veɪl/", "n.", "面纱；遮蔽物", "mist ripped like a veil"),
    ("enfold", "/ɪnˈfoʊld/", "v.", "包住；环抱", "wolf's warmth"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB


def main():
    blocks = extract_range(152, 156, "BRAN", "CH17")
    write_chapter(
        out=OUT, chapter=17, pov="BRAN", page_start=152, page_end=156,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增可确认的世界观事实；梦境语言允许建立意象联系，但不把象征推测写成后续情节结论。",
        vocab=VOCAB,
        guide="Bran在昏迷中经历一场无尽坠落梦。three-eyed crow不断用‘fly而不是cry’逼他放弃撞地前自然醒来的幻想，并让他直视整个realm：Winterfell、南行家人、narrow sea以东以及Wall之外的heart of winter。梦中视野把Bran个人受害经历放进更大的寒冷威胁，但许多shadow和远方画面仍只能作为象征或可能暗示。借助Eddard关于恐惧与勇气的旧话，Bran最终选择飞而不是死。醒来后，他发现双腿没有感觉，却也第一次为direwolf命名Summer。",
        people=[
            ("Bran Stark", "本章视角人物；在昏迷梦境中学习飞行并于Winterfell苏醒"),
            ("three-eyed crow", "梦中导师，以反问、嘲弄和强制引导Bran面对死亡与北方威胁"),
            ("Eddard Stark", "以记忆中的声音重申害怕时才需要勇气"),
            ("Catelyn Stark / Ser Rodrik Cassel", "Bran向东看见的航海者，携血染匕首前往King’s Landing"),
            ("Robb Stark", "留守Winterfell，Bran苏醒后最先冲入房间的家人"),
            ("Jon Snow", "Bran在Wall方向看见的bastard brother"),
            ("Summer", "Bran的direwolf；以体温包围失去腿部感觉的Bran，并在结尾获得名字"),
        ],
        terms=[
            ("three-eyed crow", "Bran梦中拥有第三只眼的crow，身份与能力当前未解释"),
            ("heart of winter", "Bran在世界极北光幕之外看到的恐怖中心，性质尚不明确"),
            ("Asshai by the Shadow", "遥远东方的传说城市，位于Jade Sea彼端"),
            ("weirwood", "godswood中的白色心树，梦中察觉并回望Bran"),
            ("Summer", "Bran为direwolf选择的名字，与全章冰、冬和死亡形成对照"),
        ],
        synthesis="Chapter 17把坠落从一次事故改写成一种认识方式。Bran最初依赖噩梦规则，认为自己无需选择；three-eyed crow则不断取消退路，让他承认地面、死亡和恐惧都可能是真的。只有向下看，他才获得超出身体的视野，也看见家族痛苦只是更大世界危机的一部分。飞行因此不是简单的超能力展示，而是面对恐惧后主动选择生存。醒来场景同时拒绝廉价奇迹：Bran活了下来，却失去双腿感觉。最后的Summer并未消除winter，而是在寒冷房间里提供另一种温度、陪伴与命名权。",
        contrasts=[
            "**fall／fly：** 同一个垂直运动既可被体验为被动死亡，也可在选择后成为主动飞行。",
            "**cry／fly：** crow用一个辅音差把恐惧反应转换成生存指令。",
            "**看不见的翅膀／无感觉的双腿：** 梦中获得移动自由，醒来却面对身体行动限制。",
            "**高空全景／塔房身体：** realm级视野最终收束到一张床和无法动作的双腿。",
            "**heart of winter／Summer：** 极北死亡中心与direwolf新名字构成最明确的季节反意象。",
            "**导师帮助／导师伤害：** crow既喂出知识，也以啄击、吼叫和死亡压力强迫学习。",
        ],
        questions=[
            "three-eyed crow是谁，它为何选择Bran？",
            "Bran梦中三道shadow分别对应什么，它们只是象征还是警告？",
            "heart of winter究竟是什么，为什么Bran必须为此活下去？",
            "Bran苏醒后双腿的状态是否会改变？",
            "Summer这个名字与Bran未来的选择会形成怎样的关系？",
        ],
        extraction_notes="PDF pp.152–156共60段，本章没有跨页合并段落；经页面图像复核，第32段源版确实印作tight，原样保留并标注其语义通常应为right",
    )
    print(f"Wrote Chapter 17 with {len(blocks)} paragraphs")


if __name__ == "__main__":
    main()
