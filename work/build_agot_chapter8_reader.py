#!/usr/bin/env python3
"""Build Chapter 8 (BRAN) close-reading Markdown."""

from __future__ import annotations

import json
from pathlib import Path

from agot_extract import PDF, extract_range
from build_agot_chapter7_reader import VOCAB as BASE_VOCAB
from build_agot_prologue_reader import english_names, term_present


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "国王一行黎明出发猎野猪；Robb也随行，这是南下前最后一次狩猎。",
    "Bran被留在Winterfell，他不理解Jon近来的愤怒，还认为去Night’s Watch并不比南下差。",
    "Bran原本极度期待骑真马走kingsroad、住进King’s Landing的红堡；恐怖传说只增加了他的兴奋。",
    "Bran梦想成为Kingsguard，并如数家珍地回想传说中的白袍骑士与古老战争。",
    "他比较随行的三名Kingsguard，认为Jaime最像故事里的骑士，又期待到王都见到Ser Barristan Selmy。",
    "真到离别前一天，Bran却感到失落；他试图向城堡中熟悉的人一一道别。",
    "在马厩看见即将留下的小马后，他差点哭出来，放弃道别，转而和direwolf独处。",
    "Bran还没给direwolf找到合适名字，他美慕Ghost这个名，也评论兄弟姐妹各自的命名。",
    "他玩腻投棍后决定去爬broken tower，把它当作离开前最后一次探险。",
    "Bran绕开令他害怕的heart tree，命令direwolf留在sentinel tree下。",
    "direwolf先服从命令，却在Bran爬到半途时起身嚎叫。",
    "Bran因狼的注视感到寒意，但仍把警告当成烦人阻拦，继续爬上屋顶。",
    "Winterfell的屋顶是Bran的第二个家；Catelyn甚至说他先会爬才会走。",
    "在孩子眼中，Winterfell是不规则生长的灰色石迷宫，像一棵扭曲的巨树。",
    "登高后Bran可俯瞰整座城堡的日常，这使他拥有一种连Robb也不懂的领主感。",
    "爬行还让Bran掌握Winterfell的暗道、桥梁和错层结构，他相信有些秘密连Maester Luwin也不知道。",
    "Catelyn害怕他失足身亡，曾迫他保证留在地面；Bran只忍了近两周便偷偷违约。",
    "Bran因内疚坦白后被罚在godswood反省，结果第二天被发现睡在最高的树上。",
    "Eddard再生气也忍不住发笑，戏称Bran是松鼠，并默许他继续爬，只别让母亲看见。",
    "Old Nan用雷击和乌鸦啄眼的故事吓他，但Bran用自己喂乌鸦的经验否定这种警告。",
    "Maester Luwin把穿Bran衣服的陶偶抛下城墙演示后果，Bran却坚信自己不是陶土，也绝不会掉落。",
    "守卫后来追逐屋顶上的Bran，却总是输给他；他也发现人们很少抬头，因而爬高几乎等于隐身。",
    "Bran详细感受赤脚攀爬的触感、肌肉酸痛、高处冷空气与栖息的鸟类。",
    "他最喜欢的是到达旁人无法去的地方，拥有一座只属于自己视角的Winterfell。",
    "broken tower是他最爱的去处；它百年前被雷火摧毁，如今只有Bran和乌鸦能到达崩坏顶部。",
    "Bran知道两条路，但不喜欢直接爬松动、砂浆已烧毁的塔墙。",
    "更好的路线需穿过树、屋顶、First Keep与石像鬼，最后荡到broken tower；叙述展示他娴熟的身体地图。",
    "Bran在石像鬼间移动时听见空置多年的First Keep传出人声，惊得几乎脱手。",
    "一名女子表示不喜欢当前局势，认为对话的男人本应成为Hand。",
    "男人懒洋洋拒绝这份荣誉，因为Hand的工作太多。",
    "Bran悬在窗上方偷听，又担心移动时脚会被对方看见。",
    "女子强调Eddard受Robert手足般喜爱，认为他成为Hand会带来危险。",
    "男人用Robert不喜欢自己亲兄弟作玩笑，还讽刺Stannis令人消化不良。",
    "女子区分Robert的兄弟与Eddard，懊悔没有坚持推举对话的男人。",
    "男人认为Eddard至少是honorable enemy，比Littlefinger这类有野心的候选人更容易应付。",
    "Bran意识到他们在谈Father，因此冒险留下，想听得更多。",
    "女子说必须密切监视Eddard。",
    "男人把政治担忧转成调情，说自己更想看她。",
    "女子认为Eddard长年不理南方事务，此次离开根基必然是要对付他们。",
    "男人列举责任、荣誉、留名、逃离妻子或追求温暖等普通动机，消解阴谋解读。",
    "女子指出Eddard的妻子是Lysa Arryn的姐妹，并担心Lysa的指控。",
    "Bran研究窗下狭窄凸沿，想靠近却发现距离太远。",
    "男人轻蔑地称Lysa只是受惊的母牛。",
    "女子提醒他，Lysa与Jon Arryn同床，可能知道秘密。",
    "男人认为若Lysa知情，逃离King’s Landing前本会告诉Robert。",
    "女子反驳：Lysa的儿子原将被送往Casterly Rock，他会成为迫她沉默的人质；如今孩子在Eyrie才可能大胆。",
    "男人咒骂母亲都疯了，又宣称Lysa无论知道什么都没有证据，但随即也显出一丝不确定。",
    "女子担心Robert根本不会要求证据，因为他并不爱她。",
    "男人反问这是谁的错，并称她为sweet sister，暴露两人是姐弟或兄妹。",
    "Bran考虑冒险落到窗台上，他虽不懂内容，却知道这些话不该被自己听到。",
    "女子骂男人像Robert一样盲目。",
    "男人借“看到同一件事”反驳，认为Eddard宁死也不会背叛Robert。",
    "女子以Eddard曾背叛旧王反驳，并担心Robert死后Joffrey继位时Eddard的立场；她还嫉妒Robert对Lyanna的旧情。",
    "Bran终于害怕，想找兄弟求助，又意识到自己必须先看清说话者身份。",
    "男人叫女子少想未来，多享受眼前的快乐。",
    "Bran听见肉体拍击声、女子制止和男人笑声，却无法正确理解。",
    "他爬过石像鬼上屋顶，绕到对话房间正上方。",
    "男人嫌政治谈话乏味，再次命令姐妹靠近并安静。",
    "Bran头朝下挂在石像鬼上，倒置的世界与下方湿滑庭院制造眩晕与危险感。",
    "Bran终于从窗口望进房间。",
    "他看到一对赤裸男女在“摔跤”，因视线被挡还认不出他们。",
    "孩子误把性行为理解为男人在弄疼女人，只通过接吻、呻吟和金发看到零碎线索。",
    "女人的脸露出后，Bran认出她是queen。",
    "Bran可能发出了声音；queen突然睁眼直视他并尖叫。",
    "惊慌中Bran失去固定点，向下坠落后勉强单手抓住窗沿，撞在墙上悬空。",
    "两张脸出现在Bran上方的窗口。",
    "Bran看清queen身边的男人，两人长得像镜中倒影。",
    "女人尖声说Bran看见了他们。",
    "男人冷静承认事实。",
    "Bran手指滑落时，男人伸手叫他抓住，免得坠落。",
    "Bran抓紧男人手臂被拉回窗沿；女人不理解男人在做什么。",
    "男人把Bran立在窗台上，询问他的年龄。",
    "Bran如释重负地回答七岁，还为自己在对方手臂抓出深痕而难为情。",
    "男人看向女人，厌恶地说出“我为爱做的事”，随即把Bran推出窗外。",
    "Bran尖叫着坠向空无一物的庭院，再没有可以抓住的支点。",
    "远处传来狼嚎，乌鸦在broken tower上盘旋等待玉米，与前面的警告和童话形成冷酷回声。",
]


KEY_NOTES = {
    1: "“最后一次狩猎”与“明日南下”让本章从一开始就带有过渡时刻的不可逆感。",
    3: "Bran用骑士、鬼魂和龙头构建王都，这是儿童英雄故事的King’s Landing，不是成人政治中的王都。",
    4: "名字“like music”显示Bran对骑士的认识首先来自歌谣；古老内战在他心中也已经被美化成传奇。",
    5: "Jaime外貌最像传奇骑士，却因弑旧王不被Robb认可；外形、誓言和行为在此出现缝隙。",
    6: "期待在离别成为现实时突然反转成失落，这是儿童对“去新地方”和“失去家”的第一次同时感知。",
    7: "被遗留的小马将抽象离别变成可见的损失；Bran逃走是为了不被他人看见眼泪。",
    10: "heart tree的眼睛和手形叶子被儿童视角重新陌生化，使熟悉的godswood也带有被观察感。",
    12: "direwolf的嚎叫是明确警告；Bran把它类比为Mother的唠叨，正显示他如何忽略危险信号。",
    14: "城堡被比作“monstrous stone tree”，建筑不再是静态布局，而是几个世纪累积生长的活物。",
    15: "俯瞰让Bran感到自己比继承人Robb更像城主；他的权力来自视角和无人知晓的在场。",
    18: "惩罚要求Bran在godswood的地面反思，他却睡到最高的树上，用空间行动完成了无声反驳。",
    20: "Old Nan故事中的雷击、坠落、乌鸦与眼睛集中出现，本章结尾会让这些意象变得不再只是吓孩子。",
    21: "“我不是陶土”在逻辑上没错，却避开了演示的真正命题；这是儿童对自身例外性的坚信。",
    22: "“People never looked up”是Bran的优势，也是悬念机制：他可以看见别人，别人却忘记他可能存在。",
    23: "这一长串触觉、味觉与肌肉感觉让“他爱爬高”成为身体经验，而不只是性格标签。",
    27: "路线的精密描述先证明Bran几乎从不失手，从而使后面的坠落不能被简化为普通攀爬事故。",
    28: "一直空置的First Keep突然有声音，日常冒险在一句中转向政治悬念。",
    35: "“honorable enemies”与“ambitious ones”的对照说明：对话者并不把Eddard看作朋友，只是把他视为行为可预测的对手。",
    40: "Bran身体上想靠近窗口，叙事上也在靠近他无法完全理解的成人秘密。",
    46: "“她没有证据”后的停顿与反问泄露了男人的不安，这比直接承认恐惧更有效。",
    48: "sweet sister突然明确两人的手足关系，也使前面的调情语气变得异常。",
    52: "女人把Eddard的忠诚限定在Robert生前，担心的是王位继承后的权力重组。",
    53: "Bran从好奇转为害怕，但“必须看清是谁”又把他留在危险中；识别身份是求助的前提。",
    58: "倒悬视角把世界在字面上翻转；这时Bran即将看见与官方亲族和骑士形象相反的私密真相。",
    61: "文本严格留在七岁孩子的理解边界：读者懂得性行为，Bran却只能用“弄疼她”解释。",
    64: "“Everything happened at once”后动词密集加速，从看见、惊叫到失足几乎没有思考空间。",
    66: "两人“like reflections in a mirror”是Bran用外貌相似确认亲缘的瞬间，也将窗口变成一面暴露秘密的镜子。",
    69: "男人先伸手救Bran，延长了安全幻觉，也使他随后的选择明确成为决定，而非失手。",
    73: "“The things I do for love”把暴力包装成爱的代价；“with loathing”则使这句话完全没有浪漫意味。",
    76: "狼的预警、Old Nan的乌鸦故事、Bran喂鸟的玉米与真实坠落在末句重合，将温柔日常变成不祥回声。",
}


STAGES = [
    (1, 12, "本段从南下前的兴奋转向离别伤感，direwolf的异常嚎叫为Bran的最后一次攀爬蒙上警示。"),
    (13, 27, "本段交代Bran的攀爬技术、家庭争论和对Winterfell的秘密视角，为后面的高处偷听建立可信性。"),
    (28, 48, "本段由空置城堡中的声音引出政治秘谈；Bran只听懂零碎人名，读者则能辨认对Eddard和Lysa的恐惧。"),
    (49, 61, "本段让偷听从政治疑惧滑向亲密秘；Bran为确认身份越靠越近，却无法理解眼前行为。"),
    (62, 76, "本段从身份暴露迅速转入失足、获救和被推落；章首的狼嚎与乌鸦意象在结尾合拢。"),
]


BACKGROUNDS = {
    1: "**文本事实：** Robert在南下前举行最后一次狩猎，Joffrey、Robb、Benjen、Theon、Jory、Ser Rodrik和Tyrion随行。",
    4: "**当前可知设定：** Kingsguard由七名白袍骑士组成，终身服务君主，不婚不育。Bran提及的古人多来自歌谣与传奇。",
    5: "**文本事实：** Jaime Lannister是Kingsguard成员，但他曾杀死自己誓言保护的旧王，因此其骑士名誉存在争议。",
    8: "**文本事实：** 狼名分别包括Grey Wind、Lady、Nymeria、Shaggydog与Ghost；Bran的direwolf此时仍未命名。",
    14: "**文本事实：** Winterfell是几百年间分期扩建的古老城堡，所以地面、楼层和建筑并不规整。",
    25: "**文本事实：** broken tower约在百年前被雷击烧毁，顶部坍塌后从未重建。",
    35: "**文本事实：** Hand of the King是国王最高级的执政代理人；Eddard获任命会改变王都的权力关系。",
    41: "**文本事实：** Lysa Arryn是Catelyn的姐妹、已故Jon Arryn的妻子；她已带儿子离开King’s Landing回到Eyrie。",
    45: "**阅读推测：** 对话者认为Lysa可能因儿子的安全而保持沉默；这是他们的判断，尚非已证实事实。",
    52: "**文本事实：** Lyanna是Eddard已故的妹妹，Robert曾深爱她；女子担心这段记忆影响自己的王后地位。",
    66: "**文本事实：** queen与男人有极强外貌相似，且对话中已用`sister`确认手足关系。",
    73: "**文本事实：** 男人在已将Bran拉回窗台后主动将他推落；这不是攀爬失足。",
}


EXTRA_VOCAB = [
    ("morrow", "/ˈmɑːroʊ/", "n.", "明日；翌日", "古风、文学用词"),
    ("dungeon", "/ˈdʌndʒən/", "n.", "地牢", "城堡语境"),
    ("sworn sword", "/swɔːrn sɔːrd/", "n.", "宣誓效忠的武装护卫", "封建忠诚关系"),
    ("jowly", "/ˈdʒaʊli/", "adj.", "下颌肉松垮的", "外貌描写"),
    ("droopy", "/ˈdruːpi/", "adj.", "下垂的；耷拉的", "形容眼睛"),
    ("wolfling", "/ˈwʊlfɪŋ/", "n.", "幼狼", "文学性构词"),
    ("fortnight", "/ˈfɔːrtnaɪt/", "n.", "两周", "英式常用"),
    ("sentinel", "/ˈsentɪnəl/", "n.", "守卫；哨兵", "此处也是树种名"),
    ("labyrinth", "/ˈlæbərɪnθ/", "n.", "迷宫；错综复杂的空间", "城堡比喻"),
    ("gnarled", "/nɑːrld/", "adj.", "多节扭曲的", "常形容老树或手"),
    ("gargoyle", "/ˈɡɑːrɡɔɪl/", "n.", "石制怪兽滴水嘴；石像鬼", "中世纪建筑元素"),
    ("rookery", "/ˈrʊkəri/", "n.", "鸦巢处；此处指信鸦塔", "城堡通信设施"),
    ("crevice", "/ˈkrevɪs/", "n.", "裂缝；窄缝", "攀爬落手处"),
    ("haunt", "/hɔːnt/", "n.", "常去之处", "此处不是“闹鬼”"),
    ("mortar", "/ˈmɔːrtər/", "n.", "砂浆；灰浆", "固定砖石的材料"),
    ("shinny", "/ˈʃɪni/", "v.", "用手脚夹住迅速爬", "常与up/down连用"),
    ("eyrie", "/ˈɪəri/", "n.", "鹰巢；高处栖所", "比喻断塔顶部"),
    ("fret", "/fret/", "v.", "烦恼；过度担忧", "`fret too much`"),
    ("foster", "/ˈfɔːstər/", "v.", "寄养；交由他家教养", "贵族政治与教育安排"),
    ("hostage", "/ˈhɑːstɪdʒ/", "n.", "人质；用来施压的人", "此处强调政治控制"),
    ("insipid", "/ɪnˈsɪpɪd/", "adj.", "乏味的；平淡无趣的", "带贬义的人物评价"),
    ("astride", "/əˈstraɪd/", "adv./prep.", "跨坐着", "双腿分开在两侧"),
    ("vertigo", "/ˈvɜːrtɪɡoʊ/", "n.", "眩晕；高处头晕", "坠落时的身体感受"),
    ("lurch", "/lɜːrtʃ/", "n.", "突然摇晃或下坠", "失重感"),
    ("shrilly", "/ˈʃrɪlli/", "adv.", "尖声地；刺耳地", "紧张语气"),
    ("unyielding", "/ʌnˈjiːldɪŋ/", "adj.", "坚硬不动的；不屈的", "此处形容石头"),
    ("gouge", "/ɡaʊdʒ/", "n./v.", "深凹痕；挖出深痕", "指甲造成的伤痕"),
    ("sheepishly", "/ˈʃiːpɪʃli/", "adv.", "尴尬难为情地", "意识到自己造成小麻烦"),
    ("loathing", "/ˈloʊðɪŋ/", "n.", "厌恶；憎恨", "`with loathing`"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB


def extract_blocks():
    raw = extract_range(75, 83, "BRAN", "CH08")
    # The Ser Barristan paragraph is split only by the PDF page break (pp.75–76).
    raw[4]["text"] += " " + raw[5]["text"]
    raw[4]["end_page"] = raw[5]["end_page"]
    del raw[5]
    for order, block in enumerate(raw, 1):
        block["order"] = order
        block["id"] = f"CH08-P{block['page']:03d}-{order:03d}"
    return raw


def note(order):
    if order in KEY_NOTES:
        return KEY_NOTES[order]
    return next(text for start, end, text in STAGES if start <= order <= end)


def background(order):
    return BACKGROUNDS.get(order, "本段没有新增必须补充的世界观设定；重点在Bran的儿童理解、攀爬空间、偷听信息或危险升级。")


def vocab_for(text):
    seen, out = set(), []
    for item in VOCAB:
        if item[0] not in seen and term_present(item[0], text):
            out.append(item)
            seen.add(item[0])
    return out


def source_label(block):
    if block["page"] == block["end_page"]:
        return f"PDF p.{block['page']}"
    return f"PDF pp.{block['page']}–{block['end_page']}"


def build_markdown(blocks):
    pages = {}
    for block in blocks:
        pages.setdefault(block["page"], []).append(block["id"])
    lines = [
        "# *A Game of Thrones* Chapter 8 — BRAN 逐段精读", "",
        "> **阅读模式：** 无剧透｜人物姓名保留英文｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        "> **文本范围：** 原 PDF 第 75–83 页，共 76 个正文段落", "",
        "## 本章导读", "",
        "南下前夕，Bran由期待转为不舍，决定最后一次攀爬Winterfell的broken tower。他的direwolf不断嚎叫警告，Bran却仍继续前行。在废弃的First Keep外，他偶然听见一对男女谈论Eddard、Jon Arryn、Lysa与王位继承，并冒险探查他们的身份。一场儿童冒险由此突然撞上成人世界最危险的秘密。", "",
        "## 人物表", "", "| 人物 | 当前身份与作用 |", "|---|---|",
        "| Bran Stark | 本章视角人物；七岁，擅长攀爬并梦想成为Kingsguard |",
        "| Eddard Stark | Bran的父亲，即将南下担任Hand of the King |",
        "| Robert Baratheon | 国王；王室南下前参加最后一次狩猎 |",
        "| Cersei Lannister | queen；Bran在窗内认出的女人 |",
        "| Jaime Lannister | Kingsguard成员；与queen外貌极为相似 |",
        "| Bran的direwolf | 此时仍未命名，在Bran攀爬时反复嚎叫 |", "",
        "## 地名与专名", "", "| 英文 | 中文解释 |", "|---|---|",
        "| Kingsguard | 七名宣誓终身保卫君主的白袍骑士 |",
        "| First Keep | Winterfell最古老的主堡，当前已废弃 |",
        "| broken tower | 百年前被雷火摧毁的断塔 |",
        "| Eyrie | House Arryn的高山堡垒，Lysa和儿子已回到那里 |", "",
        "## 段落目录", "",
    ]
    for page, ids in pages.items():
        lines.append(f"- [PDF 第 {page} 页：{ids[0]}–{ids[-1]}](#{ids[0].lower()})")
    lines += ["", "---", "", "## 逐段精读", ""]
    for block, summary in zip(blocks, SUMMARIES, strict=True):
        order, bid, original = block["order"], block["id"], block["text"]
        lines += [f'<a id="{bid.lower()}"></a>', f"### {bid}", "", f"**来源：** {source_label(block)}", "", "**英文原段**", "", f"> {original}", "", "**难词与短语**", ""]
        vocab = vocab_for(original)
        if vocab:
            lines += ["| 词语 | 音标 | 词性 | 此处含义 | 用法提示 |", "|---|---|---|---|---|"]
            for term, ipa, pos, meaning, usage in vocab:
                lines.append(f"| `{term}` | {ipa} | {pos} | {meaning} | {english_names(usage)} |")
        else:
            lines.append("本段没有新增的四级以上重点词；重点留意语气和上下文。")
        lines += ["", "**这一段说了什么**", "", summary, "", "**值得注意的地方**", "", note(order), "", "**背景与伏笔（无剧透）**", "", background(order), "", "[回到段落目录](#段落目录)", "", "---", ""]
    lines += [
        "## 本章整体梳理", "",
        "Chapter 8用一条非常精密的链条完成转折：离别伤感促使Bran去做最爱的事；攀爬技术让他拥有无人能及的视角；无人抬头的习惯让他得以偷听；对Father的关心和对身份的好奇又使他不肯离开。因此结尾不是偶然惊吓，而是人物性格、城堡空间和成人秘密的必然碰撞。", "",
        "### 关键意象", "",
        "- **高处／地面：** 高处原本给Bran自由、隐身与控制感，最后却成为致命的暴露位置。",
        "- **眼睛／观看：** heart tree似乎在看他，Bran从高处看所有人，最终queen突然回看。",
        "- **direwolf嚎叫：** 狼在危险发生前已经警告，结尾的远方狼嚎使警告变成悲哀。",
        "- **乌鸦与玉米：** Old Nan的吓人故事与Bran喂乌鸦的温柔日常，在坠落瞬间同时回归。",
        "- **传奇骑士／现实行为：** Bran在章首向往Kingsguard，章末却面对一名Kingsguard成员的真实选择。", "",
        "### 当前仍未解答的问题", "",
        "1. Bran坠落后会发生什么？",
        "2. 那对男女害怕Lysa知道的究竟是什么？",
        "3. Eddard成为Hand为何会让他们如此不安？",
        "4. Bran的direwolf为何在他爬高时反复嚎叫？", "",
        "以上问题不使用后文章节答案。", "", "## 词汇总表", "", "| 词语 | 音标 | 词性 | 核心释义 |", "|---|---|---|---|",
    ]
    all_text = " ".join(block["text"] for block in blocks)
    seen = set()
    for term, ipa, pos, meaning, _ in VOCAB:
        if term not in seen and term_present(term, all_text):
            lines.append(f"| `{term}` | {ipa} | {pos} | {meaning} |")
            seen.add(term)
    return "\n".join(lines) + "\n"


def build_source_map(blocks):
    return {
        "work": "A Game of Thrones",
        "section": "Chapter 8 — BRAN",
        "source_file": str(PDF),
        "source_format": "pdf-text",
        "page_range": [75, 83],
        "block_count": len(blocks),
        "name_policy": "Personal names remain in original English.",
        "spoiler_policy": "Only information available through each current paragraph is used.",
        "pages": [{"page": p, "first_id": next(b["id"] for b in blocks if b["page"] == p), "last_id": [b["id"] for b in blocks if b["page"] == p][-1]} for p in sorted({b["page"] for b in blocks})],
        "blocks": [{
            "id": b["id"], "page": b["page"], "end_page": b["end_page"], "type": "paragraph", "order": b["order"],
            "original_text": b["text"], "translation": "", "explanation_zh": SUMMARIES[b["order"] - 1],
            "literary_note_zh": note(b["order"]), "background_zh": background(b["order"]), "bbox": [0, 0, 0, 0],
            "confidence": "high", "refs": [], "insert_after": None,
        } for b in blocks],
    }


def build_notes(blocks):
    return f"""# Chapter 8 生成说明

- 范围：PDF pp.75–83
- 视角：Bran
- 段落数：{len(blocks)}
- 人名策略：保留原始英文
- 剧透策略：严格限于当前段落已知信息
- 翻译策略：不提供逐段完整中译，仅提供中文段意和精读
- 提取修复：合并了跨 PDF pp.75–76 的 Ser Barristan Selmy 段落
"""


def main():
    blocks = extract_blocks()
    assert len(blocks) == len(SUMMARIES) == 76
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "source_maps").mkdir(exist_ok=True)
    (OUT / "notes").mkdir(exist_ok=True)
    (OUT / "Chapter_08_BRAN_精读.md").write_text(build_markdown(blocks), encoding="utf-8")
    (OUT / "source_maps" / "Chapter_08_source_map.json").write_text(json.dumps(build_source_map(blocks), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "notes" / "Chapter_08_notes.md").write_text(build_notes(blocks), encoding="utf-8")
    print(f"Wrote Chapter 8 with {len(blocks)} paragraphs")


if __name__ == "__main__":
    main()
