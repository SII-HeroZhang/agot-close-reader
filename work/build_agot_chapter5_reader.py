#!/usr/bin/env python3
"""Build Chapter 5 (JON) close-reading Markdown."""

from __future__ import annotations

import json
from pathlib import Path

from agot_extract import PDF, extract_range
from build_agot_chapter4_reader import VOCAB as BASE_VOCAB
from build_agot_prologue_reader import english_names, term_present


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "Jon少数几次庆幸自己是bastard：被安排在低处反而让他能喝酒并从容观察王室宴会。",
    "他坐在年轻squires中不断饮酒，甜酒比平时更浓，使感官和情绪逐渐失去约束。",
    "Great Hall充满烟、烤肉、面包、啤酒和人声，宴会的丰盛与混乱由多种感官共同呈现。",
    "欢迎宴已进行四小时；Jon的兄弟姐妹坐在高台，而他因身份不能与家人同席。",
    "周围青年因他酒量而起哄，Jon把继续饮酒当成接近“成年男人”的证明。",
    "Ned陪Cersei入席；Jon承认王后美丽，也敏锐察觉她礼貌笑容中的冷淡。",
    "Robert与Catelyn随后出现；传说中的英雄如今肥胖醉态，让Jon深感失望。",
    "王室与Stark孩子依次入席；三岁的Rickon努力保持尊严，使正式礼仪带一点儿童喜剧。",
    "Arya陪Tommen，Sansa陪Joffrey；Jon注意到Joffrey的外貌与傲慢，也知道Sansa被他吸引。",
    "Jon更关注王后兄弟：Jaime步伐与外貌都像故事中的英雄骑士。",
    "Jon难以移开目光，心中认为Jaime才符合国王应有的外表。",
    "随后出现的Tyrion身材矮小、比例异常，与Jaime并肩时形成极强反差。",
    "最后入席的是Benjen Stark和Theon Greyjoy；Benjen向Jon微笑，Theon照例完全忽略他。",
    "Jon从那时开始饮酒，一直没有停下。",
    "Ghost在桌下蹭Jon的腿索食；Jon把鸡肉悄悄递给他。",
    "Jon眼睛刺痛，声称是烟造成并猛擦眼睛，实际也在压制被排除在家庭高台外的情绪。",
    "一只黑色杂种狗试图抢食，Ghost无声露齿便让更大的狗退走。",
    "Jon为Ghost的镇定与威慑力高兴，抚摸白毛，Ghost以红眼回应。",
    "熟悉声音询问这是否就是传闻中的direwolf。",
    "Jon高兴抬头，Benjen像Jon摸Ghost那样揉乱他的头发，亲近动作形成呼应。",
    "年轻squire让座给Benjen，他先称赞Ghost，又带笑指出Jon喝醉了。",
    "Jon只是微笑，没有否认。",
    "Benjen笑说自己第一次真正喝醉时可能比Jon更小，并随手拿起一只浸满肉汁的烤洋葱。",
    "Benjen外貌瘦削如山岩，黑衣朴素，却始终带着让Jon亲近的笑意。",
    "Jon解释Ghost不同于其他幼崽：他从不出声，因此得名；白色毛皮也与灰黑色同窝幼崽不同。",
    "Benjen说长城外仍有direwolves，巡逻时能听见；他随后询问Jon为何不坐在家人旁边。",
    "Jon平静回答Catelyn担心bastard与王室孩子同席会冒犯王后。",
    "Benjen看向远处高台，转而评论自己的哥哥Ned今晚似乎并不快乐。",
    "Jon早已注意到；作为bastard，他学会观察人们隐藏在言语后的真实态度。",
    "Benjen认真打量Jon，称赞他的观察力，并说守夜人需要他这样的人。",
    "Jon因称赞而自豪，列举自己在长剑、骑术等训练中胜过Robb的地方。",
    "Benjen用简短的“显著成就”回应，语气带着成人对少年自夸的保留。",
    "Jon突然请求随Benjen返回长城，认为父亲会同意他加入守夜人。",
    "Benjen仔细审视他，警告长城对一个男孩而言非常艰苦。",
    "Jon抗议自己即将十五岁，已接近成年，并以学识为证。",
    "Benjen承认他懂得不少，却拿走酒杯，暗示酒精正在夸大他的自信。",
    "Jon举Daeron Targaryen十四岁征服Dorne为例，证明少年也能建立功业。",
    "Benjen指出那场征服只维持一个夏天，付出大量生命，Daeron本人也早逝。",
    "Jon夸口自己记得一切；酒让他坐得更直、说得更大胆。",
    "Jon长期思考加入守夜人：Robb将继承Winterfell，弟弟妹妹各有位置，只有自己没有明确归属。",
    "Benjen说明守夜人是终身誓言兄弟会，成员不能有家庭，也不能生养子女。",
    "Jon坚持bastard同样可以拥有荣誉，并说自己已准备发誓。",
    "Benjen指出他只有十四岁，尚未真正了解女人与家庭，因此无法理解放弃它们的代价。",
    "Jon激烈声称自己不在乎那些生活。",
    "Benjen回答，只有知道誓言会夺走什么，Jon才可能真正作出选择。",
    "Jon的愤怒爆发，喊出自己并不是Benjen的儿子。",
    "Benjen起身，以`More’s the pity`回应Jon不是自己儿子，并让Jon等亲自生过几个bastards后再谈。",
    "Jon颤抖着发誓自己永远不会让任何孩子成为bastard，把这个身份的痛苦转成绝对誓言。",
    "他突然发现整桌人都安静注视自己，羞耻感取代愤怒。",
    "Jon维持最后一点尊严请求离席，随后转身逃离宴会。",
    "城堡院落安静空旷，只有守卫；冷夜与喧闹大厅形成强烈反差。",
    "音乐从窗内传来，却使Jon更难受；他强忍眼泪，Ghost无声跟随。",
    "一个声音叫住Jon，他转身寻找。",
    "Tyrion坐在大厅门上方的石檐，像怪兽雕像一样俯视Jon和Ghost。",
    "Jon介绍Ghost，并因Tyrion没有留在宴会而感到意外。",
    "Tyrion说宴会太热太吵、自己酒也喝多了，并用不该吐在哥哥身上的笑话解释离席，随后请求近看Ghost。",
    "Jon迟疑后点头，并半认真地问Tyrion是否需要梯子下来。",
    "Tyrion直接从高处跃下，以空翻稳稳落地，打破Jon对其身体能力的预期。",
    "Ghost不确定地后退。",
    "Tyrion拍去灰尘并道歉，笑说自己吓到了direwolf。",
    "Jon否认Ghost害怕，跪下呼唤并安抚他靠近。",
    "Ghost贴近Jon，却始终警惕盯着Tyrion，表现服从与自主戒备并存。",
    "Jon命Ghost坐下不动，并允许Tyrion触摸。",
    "Tyrion抚摸Ghost白毛，称赞他是好狼。",
    "Jon夸张声称自己若不在，Ghost会咬断Tyrion喉咙；他知道现在还做不到，却相信未来会。",
    "Tyrion顺着玩笑说Jon最好一直留在身边，介绍自己姓名，并用一双颜色不同的眼睛打量Jon。",
    "Jon承认自己知道Tyrion身份；站起来后发现自己比对方高，产生复杂不适。",
    "Tyrion直接问Jon是否是Ned Stark的bastard。",
    "这个词让Jon感到寒意，他抿紧嘴唇不回答。",
    "Tyrion问是否冒犯了他，并以自嘲说dwarfs无需委婉，因为多代小丑让他们获得这种特权。",
    "Jon僵硬承认Lord Eddard Stark是自己的父亲。",
    "Tyrion观察Jon面孔，认为他比其他兄弟更具北方特征。",
    "Jon纠正他们是half brothers；他因这句评价高兴，却努力不表现。",
    "Tyrion劝Jon永远不要忘记bastard身份，应把它当作盔甲，使别人无法再用它伤害他。",
    "Jon正在气头上，反问Tyrion懂什么bastard处境。",
    "Tyrion说在父亲眼中，所有dwarfs都是bastards。",
    "Jon反驳Tyrion明明是Lannister合法婚生子。",
    "Tyrion讽刺地让Jon去告诉自己的父亲；母亲因生他而死，而父亲似乎从未完全把他当作真正儿子。",
    "Jon坦白自己甚至不知道母亲是谁。",
    "Tyrion用一句悖论式玩笑结束：dwarfs在父亲眼中或许都是bastards，但bastards不必把自己活得渺小；随后返回宴会。",
]


KEY_NOTES = {
    1: "开篇把污名写成偶尔有利的观察位置；Jon的自由来自被排除，而非真正被接纳。",
    4: "高台座位把家庭关系空间化：兄弟姐妹在上方，Jon与squires在下方，身份差异无需解释便可看见。",
    6: "Jon能从礼貌笑容中读出冷淡，延续他作为边缘者必须发展出的观察能力。",
    7: "Robert的外表让Jon的英雄想象破裂，与Chapter 4中Ned的震惊形成不同年龄视角的呼应。",
    10: "Jaime先以视觉完成骑士理想，读者此刻只知道Jon看到的外表，不应提前代入后文评价。",
    12: "兄弟并行使身体差异无法被忽略；文本先展示Jon的观看，而不是要求读者立即下道德判断。",
    16: "`cursing the smoke`是自我掩饰；Jon宁愿把眼泪归因于烟，也不愿承认被家庭排除造成的痛。",
    17: "Ghost不吠不扑，只露齿便让大狗退开；无声控制与Jon在人群中的压抑形成对应。",
    25: "Ghost的名字来自沉默，而非颜色；`born with his eyes open`又强化他异常敏锐的形象。",
    29: "`read the truth that people hid behind their eyes`定义Jon的生存技能：没有明确地位的人必须比别人更会观察。",
    30: "Benjen一句称赞被Jon听成加入守夜人的许可，显示他早已等待一个归属出口。",
    33: "请求看似突然，实际是长期思考借酒说出口；真正突然的是表达，不是愿望。",
    38: "Benjen用伤亡与失败拆解少年英雄故事，区分被传颂的征服与真实代价。",
    40: "Jon把兄弟姐妹的未来逐一列出，说明加入守夜人首先源于家中没有位置，而不只是浪漫荣誉。",
    41: "守夜人誓言的关键不是冒险，而是永久放弃配偶、土地和子女；Benjen把被Jon忽略的成本说清。",
    43: "Benjen并非否定Jon能力，而是否定他在不了解人生选项时作出终身放弃的成熟度。",
    47: "`More’s the pity`同时表达亲情和界限：Benjen关心Jon，却不能以父亲身份替他决定。",
    48: "Jon厌恶的不是抽象私生制度，而是把自身痛苦复制给另一个孩子的可能。",
    50: "礼貌的`I must be excused`与随后的`bolted`形成反差：语言想保住尊严，身体只想逃跑。",
    52: "大厅的快乐声音在外面变成伤害，说明同一场宴会因归属位置不同而意义相反。",
    54: "Tyrion被比作gargoyle，看似怪物化，却是他主动选择的高处观察位置。",
    58: "空翻立即修正Jon和读者对Tyrion身体的单一想象；受限不等于没有技巧。",
    62: "Ghost接受Jon命令但持续盯住Tyrion，动物反应保持独立，不只是主人的道具。",
    68: "Tyrion直接说出Jon最敏感的身份，开启两名家族边缘者之间不舒服却诚实的对话。",
    70: "Tyrion把社会对dwarf的嘲笑转化成不必遵守礼貌的自由，是与Jon“盔甲”策略相同的逻辑。",
    74: "`wear it like armor`不是让Jon喜欢污名，而是让他主动控制叙述，使羞辱失去突然袭击的力量。",
    76: "Tyrion把dwarf与bastard类比的是父亲眼中的排斥，不是法律上的婚生身份。",
    78: "他用讽刺讲述母亲之死与父亲怨恨，笑话成为处理家庭创伤的防御机制。",
    80: "结尾重复核心建议，把一次偶遇变成Jon今后理解身份的可用原则。",
}


STAGES = [
    (1, 14, "本段借Jon在低处观看高台，展示宴会礼仪如何把合法子女、bastard、王室和家臣排列成可见等级。"),
    (15, 32, "本段通过Ghost与Benjen暂时缓解孤独，同时让Jon的观察力、骄傲和饮酒后的冲动逐步显现。"),
    (33, 50, "本段围绕加入守夜人争论：Jon把它视为荣誉和归属，Benjen强调终身誓言中尚未被少年理解的损失。"),
    (51, 67, "本段从喧闹大厅转入冷清院落，并通过Tyrion的空翻与Ghost反应打破彼此的第一印象。"),
    (68, 80, "本段让Jon与Tyrion直接谈论bastard、dwarf和父亲的排斥，形成两种边缘身份的对照。"),
]


BACKGROUNDS = {
    1: "**文本事实：** Jon是Ned的私生子，宴会礼法没有让他与Stark婚生子女及王室同坐高台。",
    7: "**文本事实：** Robert年轻时以强大战士闻名；Jon此前只从Ned的讲述建立英雄想象。",
    10: "**文本事实：** Jaime Lannister是Cersei的双胞胎弟弟和Kingsguard成员。",
    12: "**文本事实：** Tyrion Lannister是Cersei与Jaime的弟弟，因dwarf身体特征被称作Imp。",
    25: "**文本事实：** Jon的白色direwolf名为Ghost；他无声、红眼，并比其他幼崽更早睁眼。",
    26: "**文本事实：** Benjen是Ned的弟弟和守夜人游骑兵，会越过长城执行rangings。",
    27: "**文本事实：** Catelyn没有安排Jon与王室同席；本段呈现Jon对决定的理解。",
    37: "**文本事实：** Daeron I被称为Young Dragon，十四岁征服Dorne，但统治短暂且伤亡巨大。",
    41: "**文本事实：** 守夜人誓言要求终身服务，放弃婚姻、土地和子女。",
    47: "**文本事实：** Benjen是Jon的叔叔而非监护父亲，因此拒绝替他作出终身决定。",
    68: "**文本事实：** `Snow`标示Jon在北方的私生身份；社会会公开以bastard称呼他。",
    76: "**文本事实：** Tyrion是婚生Lannister；他的类比针对父亲态度和社会排斥，并非法律身份。",
}


EXTRA_VOCAB = [
    ("squire", "/ˈskwaɪər/", "n.", "骑士侍从；见习武士", "通常为年轻贵族"),
    ("raucous", "/ˈrɔːkəs/", "adj.", "喧闹刺耳的", "形容青年起哄"),
    ("hazy", "/ˈheɪzi/", "adj.", "烟雾朦胧的", "大厅被烟笼罩"),
    ("rafter", "/ˈrɑːftər/", "n.", "屋顶椽木；横梁", "Great Hall顶部结构"),
    ("waddle", "/ˈwɒdəl/", "v.", "摇摆蹒跚地走", "描述Tyrion步态"),
    ("stunted", "/ˈstʌntɪd/", "adj.", "发育受限的；矮小的", "旧式身体描述"),
    ("mongrel", "/ˈmʌŋɡrəl/", "n.", "杂种狗", "非纯种犬"),
    ("ruffle", "/ˈrʌfəl/", "v.", "揉乱；拨弄", "头发或毛皮"),
    ("bawdy", "/ˈbɔːdi/", "adj.", "粗俗色情的", "`bawdy story`"),
    ("crag", "/kræɡ/", "n.", "陡峭岩峰", "比喻Benjen瘦削面孔"),
    ("notable", "/ˈnəʊtəbəl/", "adj.", "值得注意的；显著的", "此处可能带保留或讽刺"),
    ("brotherhood", "/ˈbrʌðərhʊd/", "n.", "兄弟会；结义团体", "由共同誓言连接"),
    ("father a child", "/ˈfɑːðər ə tʃaɪld/", "phr.", "生育并成为孩子父亲", "此处讨论守夜人誓言"),
    ("battlement", "/ˈbætəlmənt/", "n.", "城墙垛口；防御墙顶", "守卫站立处"),
    ("gargoyle", "/ˈɡɑːrɡɔɪl/", "n.", "滴水兽；怪兽石像", "比喻高处的Tyrion"),
    ("ledge", "/ledʒ/", "n.", "狭窄的突出平台；岩架", "门上方坐处"),
    ("nuzzle", "/ˈnʌzəl/", "v.", "用鼻口亲昵地蹭", "Ghost靠近Jon"),
    ("tactful", "/ˈtæktfəl/", "adj.", "说话得体的；圆融的", "避免冒犯的能力"),
    ("sardonic", "/sɑːrˈdɒnɪk/", "adj.", "冷嘲的；讥讽的", "带痛苦或轻蔑的幽默"),
    ("counsel", "/ˈkaʊnsəl/", "n.", "忠告；建议", "较正式用语"),
]

VOCAB = BASE_VOCAB + EXTRA_VOCAB


def note(order):
    if order in KEY_NOTES: return KEY_NOTES[order]
    return next(t for s,e,t in STAGES if s <= order <= e)


def background(order):
    return BACKGROUNDS.get(order, "本段没有新增必须补充的世界观设定；重点在Jon的被排除感、守夜人选择或与Tyrion的交流。")


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
        "# *A Game of Thrones* Chapter 5 — JON 逐段精读","",
        "> **阅读模式：** 无剧透｜人物姓名保留英文｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        "> **文本范围：** 原 PDF 第 49–56 页，共 80 个正文段落","",
        "## 本章导读","",
        "Jon因私生身份被安排在王室欢迎宴的低处，与家人高台相隔。他借饮酒和观察压住受伤情绪，在Benjen一句称赞后请求加入守夜人，却被提醒终身誓言的真实代价。逃出大厅后，他遇见同样处于Lannister家族边缘的Tyrion。两人的交谈把身份污名从被动伤口转化成一种可能主动掌握的“盔甲”。","",
        "## 人物表","","| 人物 | 当前身份与关系 |","|---|---|",
        "| Jon Snow | 本章视角人物；Ned的私生子，十四岁 |",
        "| Benjen Stark | Jon的叔叔，守夜人游骑兵 |",
        "| Tyrion Lannister | Cersei与Jaime的弟弟，dwarf |",
        "| Ghost | Jon的白色direwolf，安静且红眼 |",
        "| Catelyn Stark | Winterfell女主人；Jon被排除在高台外的决定与她有关 |","",
        "## 主题词","","| 英文 | 中文解释 |","|---|---|",
        "| bastard | 私生子；法律与社会身份标签 |",
        "| dwarf | 侏儒；Tyrion受到排斥的身体身份 |",
        "| Night’s Watch oath | 守夜人终身誓言，放弃家庭、土地与子女 |",
        "| wear it like armor | 主动承认身份，使他人难以再用它羞辱自己 |","",
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
        "Chapter 5把“边缘位置”同时写成伤口和观察优势。Jon不能与家人同席，因此痛苦；也正因长期被排除，他更擅长从眼睛、座位和礼貌背后读取真实态度。他希望守夜人提供无须解释私生身份的新归属，却暂时只看到荣誉，没有理解终身放弃家庭的成本。Tyrion并不否认社会污名，而是提出控制它的策略：主动说出自己是谁，让侮辱失去突然袭击的力量。","",
        "### 关键对照","",
        "- **高台／低桌：** 合法身份与私生身份被宴会空间直接排列。",
        "- **喧闹大厅／寂静院落：** 家庭庆典在Jon听来既诱人又伤人。",
        "- **Jon／Ghost：** 两者都安静、警觉，并在原有群体边缘找到彼此。",
        "- **Jon／Tyrion：** 一个受私生身份排斥，一个因身体与父亲态度被排斥；两人处理伤口的方式不同。",
        "- **荣誉想象／誓言代价：** Jon向往守夜人荣耀，Benjen要求他理解永远失去的普通生活。","",
        "### 当前仍未解答的问题","",
        "1. Ned是否会允许Jon加入守夜人？",
        "2. Jon在清醒后是否仍会坚持这一选择？",
        "3. Jon的母亲是谁，为何无人向他说明？",
        "4. Tyrion关于把身份当盔甲的建议会如何影响Jon？","",
        "以上问题不使用后文章节答案。","","## 词汇总表","","| 词语 | 音标 | 词性 | 核心释义 |","|---|---|---|---|",
    ]
    all_text=' '.join(b['text'] for b in blocks); seen=set()
    for t,ipa,pos,m,_ in VOCAB:
        if t not in seen and term_present(t,all_text): lines.append(f"| `{t}` | {ipa} | {pos} | {m} |"); seen.add(t)
    lines += ["","## 使用说明","","- 人物姓名一律保留原始英文。","- 可使用如 `CH05-P056-074` 的段落编号继续提问。","- 背景讲解只采用截至当前段落可知的信息。",""]
    return '\n'.join(lines)


def build_map(blocks):
    records=[]
    for b,s in zip(blocks,SUMMARIES,strict=True):
        o=b['order']; records.append({"id":b['id'],"page":b['page'],"end_page":b['end_page'],"type":"paragraph","order":o,"original_text":b['text'],"translation":"","paragraph_explanation_zh":s,"reading_note_zh":note(o),"background_note_zh":background(o),"bbox":[0,0,0,0],"confidence":"high","refs":[],"insert_after":b['id']})
    all_text=' '.join(b['text'] for b in blocks); glossary=[]; seen=set()
    for t,_,_,m,n in VOCAB:
        if t not in seen and term_present(t,all_text): glossary.append({"term":t,"translation":m,"note":english_names(n)}); seen.add(t)
    return {"paper":{"title":"A Game of Thrones — Chapter 5 (JON)","author":"George R. R. Martin","source_type":"pdf","language":"en","source_path":str(PDF),"pdf_page_range":[49,56],"reader_mode":"spoiler-free close reading; English personal names"},"blocks":records,"pages":[{"page":p,"block_ids":[b['id'] for b in blocks if b['page']<=p<=b['end_page']]} for p in range(49,57)],"figures":[],"glossary":glossary}


def main():
    blocks=extract_range(49,56,'JON','CH05')
    if len(blocks)!=len(SUMMARIES): raise RuntimeError((len(blocks),len(SUMMARIES)))
    (OUT/'source_maps').mkdir(parents=True,exist_ok=True); (OUT/'notes').mkdir(parents=True,exist_ok=True)
    (OUT/'Chapter_05_JON_精读.md').write_text(build_markdown(blocks),encoding='utf-8')
    (OUT/'source_maps'/'Chapter_05_source_map.json').write_text(json.dumps(build_map(blocks),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'notes'/'Chapter_05_notes.md').write_text('# Chapter 5 extraction notes\n\n- Source: selectable-text PDF pages 49–56.\n- 80 paragraph blocks after cross-page repair.\n- Personal names remain in original English.\n- Commentary is spoiler-free; no full translation requested.\n',encoding='utf-8')


if __name__=='__main__': main()
