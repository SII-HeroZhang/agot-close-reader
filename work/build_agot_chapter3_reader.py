#!/usr/bin/env python3
"""Build Chapter 3 (DAENERYS) close-reading Markdown."""

from __future__ import annotations

import json
from pathlib import Path

from agot_extract import PDF, extract_range
from build_agot_chapter2_reader import VOCAB as BASE_VOCAB
from build_agot_prologue_reader import english_names, term_present


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "Viserys让Daenerys触摸Illyrio送来的华美长裙，命令式语气把礼物变成即将进行的交易准备。",
    "Daenerys感受丝织物如水般滑过手指；她从未拥有过如此精美的衣服，过去的漂泊生活由此显现。",
    "Viserys心情很好，称这套衣物是Magister Illyrio的礼物，并把Daenerys称为今晚的公主。",
    "Daenerys在心里重复“公主”，却发现自己几乎忘记这个身份是什么感觉。",
    "Viserys断言Illyrio并不愚蠢，会为了未来奖赏支持他们；他的紧张外貌与夸大的王者信心并存。",
    "Daenerys沉默怀疑：Illyrio富有且交易范围广，她看不出帮助流亡兄妹能给他什么利益。",
    "Viserys交代沐浴、香水和服饰细节，并警告她必须让Khal Drogo满意，因为这关系到夺回王冠。",
    "Viserys掐痛Daenerys，以“唤醒睡龙”威胁她，说明所谓龙的身份被他用作家庭暴力工具。",
    "Daenerys顺从地回答“不”，不敢反抗。",
    "Viserys恢复近似温柔的态度，幻想史书会称Daenerys为帮助他复位的美丽公主。",
    "哥哥离开后，Daenerys望向Pentos海湾，向往远处的自由与安静。",
    "夕阳彼端是Viserys所说的故国：绿色丘陵、河流和曾由dragonlords统治的城堡。",
    "Viserys声称龙会记得故国，但Daenerys没有记忆；她从未亲眼见过那个被称作家园的地方。",
    "长期听哥哥讲述后，她能想象King’s Landing、Red Keep、Dragonstone和Iron Throne，却清楚那只是借来的记忆。",
    "Daenerys出生于Dragonstone逃亡后的暴风雨中；母亲在生产中去世，家族舰队也被风暴摧毁。",
    "她同样不记得Dragonstone；在Robert的弟弟攻岛前，忠臣Ser Willem Darry把兄妹秘密带往Braavos。",
    "Daenerys依稀记得Ser Willem、红门房屋、草地和柠檬树；这些私人生活片段才是她真正的“家”记忆。",
    "Ser Willem去世后，仆人偷走钱财，兄妹被逐出红门之家，从此在自由城邦间漂泊。",
    "各地权贵最初欢迎最后的Targaryen，后来兴趣消退；Viserys只剩变卖母亲王冠所得的钱。",
    "Viserys承诺未来夺回王位与珠宝，但Daenerys看见他的手发抖，知道他真正渴望的是军队。",
    "Illyrio的三名奴隶进屋为Daenerys准备，其中包括老妇、女奴和太监；Pentos名义上禁止奴隶制却实际拥有奴隶。",
    "奴隶们准备热水与香油，老妇为她脱衣；Daenerys的瘦小身体暴露出她仍非常年幼。",
    "老妇洗梳Daenerys的银发；女奴称赞她的头发柔软且近似银色。",
    "她们为Daenerys擦干、梳发、涂抹香料，并给她穿上Illyrio送来的衣物与凉鞋。",
    "装扮完成后，女奴说她像公主；Daenerys看着镜中成熟的轮廓，却仍感到寒冷和不安。",
    "Viserys在池边检查她，命令她转身，并以审视商品般的目光评价外表。",
    "Illyrio出现并称她具有王者气质；他肥胖却动作轻巧，礼貌外表下仍带压迫感。",
    "Viserys嫌Daenerys太瘦，拉扯她的衣服检查胸部；Daenerys忍住眼泪。",
    "Illyrio指出Daenerys已经初潮，年龄足够嫁给khal，再次把身体成熟当作交易条件。",
    "Viserys以侮辱性想象嘲笑Dothraki的欲望，暴露他的偏见与粗俗。",
    "Illyrio提醒他不要在Khal Drogo面前说这种话。",
    "Viserys因被提醒而发怒，反问Illyrio是否把自己当傻瓜。",
    "Illyrio用恭维化解冲突：他说自己把Viserys当国王，而国王往往不像普通人那样谨慎。",
    "三人乘华丽palanquin穿过黑暗的Pentos；Daenerys从香料、声音和城市气息中观察陌生世界。",
    "Viserys躺在软垫上幻想海峡对岸的故国与等待他归来的人民。",
    "Illyrio迎合Viserys，说各地领主和百姓都秘密为真王举杯、缝制龙旗。",
    "Daenerys没有情报来源，只能判断哥哥相信这些话；她知道Viserys愿意听任何证明人民爱他的说法。",
    "Illyrio继续恭维，Daenerys却看见他胡须下的一点笑意，怀疑他并不完全认真。",
    "Khal Drogo的九塔宅邸坐落海湾旁，围墙和苍白树木营造富有而陌生的环境。",
    "宅门守卫粗暴掀开车帘检查；这名带Unsullied铜盔的无须守卫与Illyrio用Dothraki语交谈后才放行。",
    "Viserys紧握借来的剑，看起来与Daenerys同样害怕；等通过守卫后，他才低声辱骂对方为无礼太监。",
    "Illyrio用甜言蜜语解释严格安保：贵客都有敌人，Drogo必须保护他们，Robert也可能悬赏Viserys的人头。",
    "Viserys坚称Robert长期派刺客追杀自己，借此证明对方害怕合法王位继承人。",
    "palanquin停下，Daenerys接受奴隶搀扶下车，正式进入Khal Drogo的住所。",
    "宅内充满香料气味，门口的太监用Common Tongue欢迎他们。",
    "他们进入月光照亮的庭院；富商、王子、祭司和武士等各类宾客正在交谈。",
    "Illyrio低声介绍Drogo的bloodriders、Asshai来的shadowbinder以及流亡骑士Ser Jorah Mormont。",
    "Daenerys听见“骑士”便立刻追问，因为这是她与故国传统的直接联系。",
    "Illyrio确认Ser Jorah接受过High Septon主持的七油傅礼，是正式的七神骑士。",
    "Daenerys脱口问他为何会在这里，表现她对故国人物的强烈好奇。",
    "Illyrio解释Ser Jorah因贩卖偷猎者为奴而触法，逃离Ned Stark的审判，成为流亡者。",
    "Viserys决定稍后与Ser Jorah交谈；Daenerys从哥哥语气听出，他又在设想一支并不存在的军队。",
    "Daenerys仍观察这位故国骑士时，Illyrio触碰她并指向Khal Drogo。",
    "Daenerys本想逃走，但因害怕Viserys的惩罚，只能转身面对未来丈夫。",
    "她发现女奴所言不假：Drogo极其高大、强壮，皮肤和长发呈深色，佩戴金属饰物。",
    "Illyrio说自己先去行礼，让兄妹留在原地等待引见。",
    "Illyrio离开后，Viserys用力抓住Daenerys手臂，首先让她注意Drogo的长辫。",
    "Drogo的黑色发辫涂着香油、挂着细小铃铛，长度垂过腰臀，成为最醒目的身份标志。",
    "Viserys说明Dothraki战败会剪掉发辫，因此Drogo的长发象征他从未败北。",
    "Daenerys直视Drogo冷硬的脸与黑色眼睛，因恐惧请求回到Illyrio的住处。",
    "Viserys压低声音发怒，认为没有军队就不可能回到真正的“家”。",
    "Daenerys所说的家只是Illyrio宅中的房间；她意识到自己其实从未拥有真正家园。",
    "Viserys声明必须借Drogo的khalasar回国，并威胁即使让全部Dothraki甚至马匹侵犯她，也要换取王冠。",
    "Daenerys看见Illyrio正带Drogo走来，知道谈判的核心已经逼近。",
    "Viserys紧张命令她微笑、挺直身体，并让她刻意展示尚未成熟的胸部。",
    "Daenerys照做：她微笑并站直，以顺从姿态迎接决定自己命运的男人。",
]


KEY_NOTES = {
    1: "触觉先于政治解释出现：丝绸的柔软与Viserys的命令共同说明美丽服饰并不等于自由。",
    4: "Daenerys对“公主”感到陌生，揭示名义身份与实际生活经验之间的断裂。",
    6: "她没有公开质疑，只在心中计算Illyrio的利益；沉默不等于没有判断力。",
    8: "`wake the dragon`是Viserys为暴力创造的委婉说法，把受害者变成需要为施暴者愤怒负责的人。",
    10: "Viserys用未来史书美化当前交易，使Daenerys的牺牲服务于他的英雄叙事。",
    13: "同一个“家”对兄妹意义不同：Viserys记忆并执着于王国，Daenerys只继承了故事。",
    14: "列举地名制造完整故国图景，但反复出现的`Viserys had told her`提醒这些不是她的亲身记忆。",
    15: "出生、母亲死亡和舰队覆灭被压缩在同一场风暴中，使Daenerys的生命从一开始就与流亡相连。",
    17: "红门、草地和柠檬树是本章最温暖的记忆，也比王座与城堡更接近Daenerys真正理解的家。",
    19: "欢迎逐渐消失、财物逐渐卖掉，展示流亡王室身份如何在现实中不断贬值。",
    20: "Viserys的承诺与发抖的手并置；Daenerys能从身体细节识别语言背后的焦虑。",
    21: "“没有奴隶”与实际奴役并存，说明城市的法律标签和真实权力关系并不一致。",
    22: "沐浴场景不断提醒读者她的年龄，抵消其他人物把她当成可婚“女人”的说法。",
    25: "镜子呈现他人打造的公主外形，gooseflesh则保留她身体真实的恐惧。",
    28: "Viserys把妹妹的身体当成可检查资产；叙事不浪漫化这场婚姻安排。",
    29: "初潮在这里不是私人成人礼，而被男性谈判者直接转换成政治可用性。",
    33: "Illyrio的恭维非常精确：表面尊称国王，实际提醒Viserys缺乏谨慎而不正面得罪他。",
    34: "封闭palanquin把三人置于移动的谈判空间；Daenerys只能通过帘外感官碎片认识城市。",
    37: "Daenerys没有证据反驳，也没有证据相信；她转而观察谁需要相信什么。",
    38: "Illyrio的一点笑意是有限视角中的关键裂缝，暗示他的奉承可能服务于自身利益。",
    41: "借来的剑与紧握剑柄共同暴露Viserys的表演性：王者姿态依赖并不属于他的物件。",
    43: "Viserys把被追杀当作重要性的证明；这种解释既维护自尊，也无法由Daenerys验证。",
    47: "人物清单扩大世界范围，但Daenerys只被“来自故国的骑士”吸引，显示她仍在寻找可触及的家园联系。",
    51: "Ser Jorah的罪与Chapter 1中Will的偷猎形成制度对照：此处争议不在偷猎，而在把人卖作奴隶。",
    54: "她的逃跑冲动被对哥哥的恐惧压住；真正限制她行动的首先不是陌生khal，而是熟悉的家庭暴力。",
    58: "发辫是可见的战绩记录；Viserys借解释Dothraki习俗，强调自己选择的是强大盟友。",
    60: "Daenerys说`go home`时指眼前住处，表明她对家最现实的定义是暂时安全，而非王国。",
    63: "Viserys的极端威胁彻底说清交易逻辑：妹妹的身体价值低于他想象中的王冠。",
    66: "最后一句极短，表面顺从，情感上却冷硬；本章停在她把恐惧隐藏成合格公主姿态的瞬间。",
}


STAGES = [
    (1, 10, "本段通过服装、称呼和威胁建立兄妹权力关系：Viserys定义目标，Daenerys被要求用身体实现它。"),
    (11, 20, "本段把Viserys讲述的王国与Daenerys亲身记得的流亡生活并置，追问“家”究竟来自血统还是记忆。"),
    (21, 33, "本段以沐浴、装扮和男性审视完成婚姻交易的准备，Daenerys的身体被他人解释和安排。"),
    (34, 43, "本段在前往宴会的途中展示Viserys的复国幻想与Illyrio的奉承，让Daenerys通过微小表情判断可信度。"),
    (44, 53, "本段借宴会宾客扩展Pentos与流亡者世界，同时让Daenerys寻找与故国有关的人和信息。"),
    (54, 66, "本段让政治交易具体化为Daenerys面对Drogo的身体恐惧，并以Viserys不断升级的威胁收束。"),
]


BACKGROUNDS = {
    3: "**文本事实：** Illyrio是Pentos的magister和富商，目前收留Targaryen兄妹并安排今晚会面。",
    8: "**文本事实：** Viserys自称dragon，以`wake the dragon`指自己的暴怒；这是他的个人威胁用语。",
    12: "**文本事实：** narrow sea分隔Daenerys所在的Pentos与她家族曾统治的Seven Kingdoms。",
    14: "**文本事实：** Targaryen家族曾以dragonlords身份统治Seven Kingdoms，王权中心是King’s Landing与Iron Throne。",
    15: "**文本事实：** Daenerys出生于Dragonstone；其母在生产中去世，Robert一方当时正追击残余Targaryen。",
    16: "**文本事实：** Ser Willem Darry忠于Targaryen，把Daenerys和Viserys从Dragonstone带往Braavos。",
    18: "**文本事实：** Braavos、Myr、Tyrosh、Qohor、Volantis与Pentos均位于海峡东侧的自由城邦世界。",
    21: "**文本事实：** Pentos法律名义上禁止奴隶制，但Illyrio仍把受控制的仆役明确称为slaves。",
    29: "**文本事实：** khal是Dothraki首领称号；婚姻安排的目标是取得Khal Drogo的军事支持。",
    42: "**文本事实：** Robert Baratheon被Targaryen兄妹称为Usurper，因为他夺取了其家族王位。",
    47: "**文本事实：** bloodriders是khal最亲近的武士同伴；shadowbinder来自遥远Asshai，其具体能力当前未解释。",
    49: "**文本事实：** anointed knight接受七神仪式；Ser Jorah Mormont出身北方Bear Island。",
    51: "**文本事实：** Seven Kingdoms禁止把偷猎者卖作奴隶；Ser Jorah逃离了Ned Stark的司法追捕。",
    58: "**文本事实：** Dothraki战士败北时剪掉发辫；Drogo的长辫和铃铛表示他宣称从未被击败。",
    63: "**文本事实：** khalasar是由khal领导的Dothraki骑马群体与军队。",
}


EXTRA_VOCAB = [
    ("caress", "/kəˈres/", "v.", "轻抚；爱抚", "Viserys命令Daenerys触摸布料"),
    ("magister", "/ˈmædʒɪstər/", "n.", "潘托斯总督式尊称；显贵", "Illyrio的头衔"),
    ("dragonbone", "/ˈdræɡənbəʊn/", "n.", "龙骨", "本书中的珍贵材料"),
    ("subtle", "/ˈsʌtəl/", "adj.", "隐秘的；精巧的；难以察觉的", "`subtle things`暗指不明交易品"),
    ("tunic", "/ˈtjuːnɪk/", "n.", "束腰外衣；短袍", "中世纪常见衣物"),
    ("meekly", "/ˈmiːkli/", "adv.", "温顺地；怯弱顺从地", "表现恐惧下的服从"),
    ("wistfully", "/ˈwɪstfəli/", "adv.", "惆怅向往地", "想要却得不到的情绪"),
    ("usurper", "/juːˈzɜːrpər/", "n.", "篡位者；夺权者", "Targaryen对Robert的称呼"),
    ("treachery", "/ˈtretʃəri/", "n.", "背叛；不忠", "政治叙事中的道德定性"),
    ("fastness", "/ˈfɑːstnəs/", "n.", "要塞；坚固据点", "文学和历史用语"),
    ("parapet", "/ˈpærəpɪt/", "n.", "城墙女儿墙；护墙", "防御建筑顶部矮墙"),
    ("garrison", "/ˈɡærɪsən/", "n.", "守军；驻军", "驻守要塞的部队"),
    ("smuggle", "/ˈsmʌɡəl/", "v.", "秘密偷运；走私", "避开敌方封锁"),
    ("archon", "/ˈɑːrkɒn/", "n.", "执政官；城邦统治者", "自由城邦头衔"),
    ("brocade", "/brəˈkeɪd/", "n.", "锦缎；织锦", "有凸起花纹的华贵织物"),
    ("diaphanous", "/daɪˈæfənəs/", "adj.", "轻薄透明的", "常形容衣料"),
    ("gooseflesh", "/ˈɡuːsfleʃ/", "n.", "鸡皮疙瘩", "寒冷或恐惧造成"),
    ("regal", "/ˈriːɡəl/", "adj.", "有王者气质的；庄严华贵的", "Illyrio对Daenerys的评价"),
    ("ponderous", "/ˈpɒndərəs/", "adj.", "笨重缓慢的", "与Illyrio意外轻巧的动作对照"),
    ("pallid", "/ˈpælɪd/", "adj.", "苍白的；缺乏血色的", "常暗示不健康"),
    ("palanquin", "/ˌpælənˈkiːn/", "n.", "轿子；肩舆", "由人抬行的封闭乘具"),
    ("manse", "/mæns/", "n.", "大宅；豪宅", "此处指Drogo的宅邸"),
    ("eunuch", "/ˈjuːnək/", "n.", "太监；阉人", "宫廷或豪宅仆役身份"),
    ("bloodrider", "/ˈblʌdraɪdər/", "n.", "血盟卫；khal的亲密武士同伴", "Dothraki专名"),
    ("shadowbinder", "/ˈʃædəʊbaɪndər/", "n.", "缚影士", "来自Asshai的神秘术士称号"),
    ("trifling", "/ˈtraɪflɪŋ/", "adj.", "微不足道的", "Illyrio淡化Ser Jorah的罪"),
    ("affront", "/əˈfrʌnt/", "n.", "公然侮辱；冒犯", "对名誉或权威的冒犯"),
    ("mercenary", "/ˈmɜːrsəneri/", "n./adj.", "雇佣兵（的）", "为报酬作战"),
    ("khal", "/kɑːl/", "n.", "Dothraki部族首领", "本书专名"),
    ("khalasar", "/ˌkɑːləˈsɑːr/", "n.", "由khal统领的Dothraki群体与军队", "本书专名"),
    ("submissive", "/səbˈmɪsɪv/", "adj.", "顺从的；服从支配的", "权力关系用语"),
    ("onyx", "/ˈɒnɪks/", "n.", "缟玛瑙；黑玛瑙", "比喻Drogo深黑眼睛"),
]

VOCAB = BASE_VOCAB + EXTRA_VOCAB


def note(order):
    if order in KEY_NOTES: return KEY_NOTES[order]
    return next(t for s,e,t in STAGES if s <= order <= e)


def background(order):
    return BACKGROUNDS.get(order, "本段没有新增必须补充的世界观设定；重点在Daenerys的感受、流亡记忆或交易推进。")


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
        "# *A Game of Thrones* Chapter 3 — DAENERYS 逐段精读","",
        "> **阅读模式：** 无剧透｜人物姓名保留英文｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        "> **文本范围：** 原 PDF 第 31–39 页，共 66 个正文段落","",
        "## 本章导读","",
        "十三岁的Daenerys被哥哥Viserys装扮成“公主”，准备与Khal Drogo见面。章节一面补足Targaryen兄妹的流亡经历，一面揭示复国计划的真实代价：Viserys试图用妹妹的婚姻和身体换取Dothraki军队。全章严格贴近Daenerys的有限视角，她很少公开反驳，却持续观察语言、表情和利益之间的裂缝。","",
        "## 人物表","","| 人物 | 当前身份与关系 |","|---|---|",
        "| Daenerys Targaryen / Dany | 本章视角人物；流亡的Targaryen公主 |",
        "| Viserys Targaryen | Daenerys的哥哥，自认合法国王 |",
        "| Magister Illyrio | Pentos富商与显贵，收留兄妹并安排婚事 |",
        "| Khal Drogo | Dothraki首领，Daenerys被安排的未来丈夫 |",
        "| Ser Jorah Mormont | 来自Seven Kingdoms的流亡骑士 |","",
        "## 专名与设定","","| 英文 | 中文解释 |","|---|---|",
        "| Pentos | 潘托斯；兄妹目前居住的自由城邦 |",
        "| Dragonstone | 龙石岛；Daenerys出生地 |",
        "| King’s Landing / Red Keep | Targaryen曾经的王都／王宫 |",
        "| Dothraki | 以骑马与战斗文化著称的游牧群体 |",
        "| khal / khalasar | Dothraki首领／其统领的群体和军队 |",
        "| wake the dragon | Viserys对自己暴怒与惩罚的威胁说法 |","",
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
        "Chapter 3围绕“谁有权定义Daenerys”展开。Viserys称她为公主，却把公主身份变成交换军队的工具；Illyrio以礼物、奴仆和恭维安排交易；Drogo尚未与她说话，权力已通过身形、战绩和众人反应抵达。Daenerys外表顺从，但她能区分哥哥的故事、自己的记忆和Illyrio可能虚假的奉承。她对“家”的理解也与Viserys根本不同：他要的是王位，她怀念的是红门、草地与暂时安全。","",
        "### 关键意象与关系","",
        "- **丝绸与掐痕：** 华美装扮和家庭暴力同时作用于Daenerys的身体。",
        "- **龙：** 对Viserys而言是血统与威胁语言；对Daenerys而言首先是哥哥随时可能爆发的愤怒。",
        "- **家：** Viserys把家等同于Seven Kingdoms和Iron Throne，Daenerys的真实记忆却停留在Braavos红门。",
        "- **微笑：** Illyrio的微笑可能隐藏利益，Daenerys最后的微笑则是被要求呈现的顺从。",
        "- **借来的剑／未剪的发辫：** Viserys的权力依靠表演，Drogo的地位则由可见战绩支撑。","",
        "### 当前仍未解答的问题","",
        "1. Illyrio帮助Targaryen兄妹真正想得到什么？",
        "2. 海峡对岸是否真的有人秘密等待Viserys归来？",
        "3. Khal Drogo会如何看待这场婚姻安排？",
        "4. Ser Jorah接近Targaryen兄妹的目的是什么？",
        "5. Daenerys能否在哥哥与婚姻交易之外形成自己的选择？","",
        "以上问题不使用后文章节答案。","","## 词汇总表","","| 词语 | 音标 | 词性 | 核心释义 |","|---|---|---|---|",
    ]
    all_text=' '.join(b['text'] for b in blocks); seen=set()
    for t,ipa,pos,m,_ in VOCAB:
        if t not in seen and term_present(t,all_text): lines.append(f"| `{t}` | {ipa} | {pos} | {m} |"); seen.add(t)
    lines += ["","## 使用说明","","- 人物姓名一律保留原始英文。","- 可使用如 `CH03-P038-058` 的段落编号继续提问。","- 背景讲解只采用截至当前段落可知的信息。",""]
    return '\n'.join(lines)


def build_map(blocks):
    records=[]
    for b,s in zip(blocks,SUMMARIES,strict=True):
        o=b['order']; records.append({"id":b['id'],"page":b['page'],"end_page":b['end_page'],"type":"paragraph","order":o,"original_text":b['text'],"translation":"","paragraph_explanation_zh":s,"reading_note_zh":note(o),"background_note_zh":background(o),"bbox":[0,0,0,0],"confidence":"high","refs":[],"insert_after":b['id']})
    all_text=' '.join(b['text'] for b in blocks); glossary=[]; seen=set()
    for t,_,_,m,n in VOCAB:
        if t not in seen and term_present(t,all_text): glossary.append({"term":t,"translation":m,"note":english_names(n)}); seen.add(t)
    return {"paper":{"title":"A Game of Thrones — Chapter 3 (DAENERYS)","author":"George R. R. Martin","source_type":"pdf","language":"en","source_path":str(PDF),"pdf_page_range":[31,39],"reader_mode":"spoiler-free close reading; English personal names"},"blocks":records,"pages":[{"page":p,"block_ids":[b['id'] for b in blocks if b['page']<=p<=b['end_page']]} for p in range(31,40)],"figures":[],"glossary":glossary}


def main():
    blocks=extract_range(31,39,'DAENERYS','CH03')
    if len(blocks)!=len(SUMMARIES): raise RuntimeError((len(blocks),len(SUMMARIES)))
    (OUT/'source_maps').mkdir(parents=True,exist_ok=True); (OUT/'notes').mkdir(parents=True,exist_ok=True)
    (OUT/'Chapter_03_DAENERYS_精读.md').write_text(build_markdown(blocks),encoding='utf-8')
    (OUT/'source_maps'/'Chapter_03_source_map.json').write_text(json.dumps(build_map(blocks),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'notes'/'Chapter_03_notes.md').write_text('# Chapter 3 extraction notes\n\n- Source: selectable-text PDF pages 31–39.\n- 66 paragraph blocks after cross-page repair.\n- Personal names remain in original English.\n- Commentary is spoiler-free; no full translation requested.\n',encoding='utf-8')


if __name__=='__main__': main()
