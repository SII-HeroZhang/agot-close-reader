#!/usr/bin/env python3
"""Build Chapter 36 (DAENERYS) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter35_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"Vaes Dothrak的Horse Gate由两匹百英尺高bronze stallions构成尖拱。",2:"无城墙、暂看不见建筑的城市却有巨大gate；Drogo与bloodriders带khalasar进入godsway。",3:"Daenerys随行并回顾Viserys因不懂Dothraki嘲弄而获Sorefoot King、Cart King称号，自己费力说服Drogo让他重返队首。",4:"她过gate后只见grass、road与历代掠来的monuments，询问city在哪里。",5:"Jorah说在前方mountain下。",6:"道路两侧陈列失名gods、stone kings、maidens与来自各地的dragons、griffins、manticores等战利品。",7:"Daenerys感叹数量和来源地域之广。",8:"Viserys称其为dead cities垃圾，只承认Dothraki会steal和kill，并因Common Tongue没人懂而放肆。",9:"Daenerys说Dothraki如今也是自己people，请他别叫savages。",10:"Viserys以dragon可随意说话回应，还故意嘲笑guards听不懂并催促Drogo交army。",11:"Jorah说princess须先被引见给dosh khaleen。",12:"Viserys轻蔑称crones与prophecy为mummer show，厌恶horsemeat、气味和自己旅途破烂衣服。",13:"Jorah说Western Market有Free Cities食物，并提醒khal会按自己时间兑现promise。",14:"Viserys坚持自己被许golden crown，警告dragon不可受mockery，随后去看奇异statue。",15:"Daenerys虽松口气仍焦虑，祈祷Drogo别让哥哥等太久。",16:"Jorah说Viserys本应留Pentos，因为khalasar无其位置，Illyrio也警告过。",17:"Daenerys仍说拿到ten thousand后他就会走，Drogo答应golden crown。",18:"Jorah解释Dothraki把Daenerys视为gift而非sale，khal会回gift但不能被demand。",19:"Daenerys不知为何仍替哥哥辩护，并转述他自称能以一万screamers横扫Seven Kingdoms。",20:"Jorah讥讽Viserys即使用一万brooms也扫不了stable。",21:"Daenerys没有假装惊讶，试探若由更strong的人率领，Dothraki能否征服Westeros。",22:"Jorah回忆初流亡时把Dothraki视为half-naked barbarians，以为少量knights即可驱散他们。",23:"Daenerys追问现在看法。",24:"Jorah说他们骑术、勇气、horse archery和数量都可怕，Drogo单独有四万mounted warriors。",25:"Daenerys问四万是否真多。",26:"Jorah以Rhaegar Trident全军同量、knights仅十分之一作比较，预测四万screamers冲锋会击溃普通兵。",27:"Daenerys认同传统军队撑不久、防不好。",28:"Jorah补充Dothraki不善siege，明智lords可守castle；但Robert可能愚蠢地在open field迎战。",29:"Daenerys问Robert是否fool。",30:"Jorah说Robert性格像Dothraki，强勇却rash；Stannis、Tywin、Eddard等谋臣则可能选择不同策略。",31:"Daenerys指出Jorah憎恨Eddard。",32:"Jorah说Eddard为poachers和honor夺走自己一切，痛苦仍在，随后指向Vaes Dothrak转移话题。",33:"城市既最大又最小：面积远超Pentos，grass streets广阔，却古老、傲慢而空旷。",34:"建筑风格彼此完全不同，有stone pavilions、grass manses、wood towers、pyramids与open halls。",35:"Jorah承认Dothraki不build，这些建筑由被掳slaves按各自文化建造。",36:"Daenerys见多数halls空置，询问居民去向。",37:"Jorah说只有dosh khaleen与servants常住，城市按prophecy预留足够容纳所有khalasars的空间。",38:"Drogo在Eastern Market附近停下；所谓两百房palace其实是巨大wood hall、可升降silk roof与成百earthen houses。",39:"所有riders连Drogo都交出weapons；Mother of Mountains视线内禁止blade和free man blood，敌对khalasars也必须休战。",40:"Drogo最年长bloodrider Cohollo来传话；叙述回顾他曾救幼年Drogo并终身绑定。",41:"bloodriders不只是guards，而是khal brothers、shadows和共享生命者；khal死后须复仇并随死，部分古俗还共享tent、wine、wives但不共享horses。",42:"Daenerys庆幸Drogo不共享wife；Cohollo友善，Haggo与Qotho却可怕，Qotho还经常伤害handmaids。",43:"她只能接受bloodriders，并幻想future son也需这类忠诚者，因为Aerys的Kingsguard曾背叛或转投Robert。",44:"Cohollo说Drogo当夜须登Mother of Mountains献祭安全归来。",45:"Daenerys知道只有men可登山，答自己等待他；pregnancy使她易累，也使Drogo对她需求增加。",46:"Doreah带她进准备好的hollow hill，Daenerys命Jhiqui准备hot bath，并庆幸可暂停骑行。",47:"洗浴时Daenerys决定当晚送Viserys gifts，让他在sacred city像king；她派Doreah邀请、Irri买非horse食物。",48:"Irri坚持horse最好、能使man强壮。",49:"Daenerys说Viserys讨厌horsemeat。",50:"Irri服从。",51:"handmaids准备goat、果蔬；Daenerys铺开white linen、sandals、bronze belt、dragon vest与cloak，希望改善Viserys形象并修复grass事件。",52:"Viserys拖着被打红眼的Doreah进来，怒称她是传命whore并把她推倒。",53:"Daenerys被怒火惊住，问Doreah究竟说了什么。",54:"Doreah道歉，说自己按吩咐告诉Viserys Daenerys commanded他来晚餐。",55:"Viserys说无人能command dragon，并威胁本该送回Doreah head。",56:"Doreah害怕；Daenerys安抚她，向Viserys改称礼貌邀请并展示gifts。",57:"Viserys怀疑这些东西是什么。",58:"Daenerys羞涩说是为他定做new raiment。",59:"Viserys讥称Dothraki rags，指责妹妹想dress自己。",60:"Daenerys试图解释穿当地衣服更舒适且能获尊重，却怕waking dragon而说不完整。",61:"Viserys讽刺下一步是否要给自己braid。",62:"Daenerys说他没有victories，因此无权braid。",63:"Viserys暴怒却因handmaids和khas不敢打她，只拿cloak羞辱说当horse blanket。",64:"Daenerys受伤地说Doreah特制，这是适合khal的衣服。",65:"Viserys拒绝像grass savage，抓痛Daenerys手臂，并以pregnancy不能保护她相威胁。",66:"Daenerys瞬间退回child恐惧，却抓起准备送他的bronze medallion belt全力挥击。",67:"belt割破Viserys脸，Daenerys命他离开，否则叫khas拖走，并以Drogo报复警告。",68:"Viserys起身威胁将来复国会让她后悔，捂伤离开且不拿gifts。",69:"他的blood溅污sandsilk cloak；Daenerys抱布坐在sleeping mats上。",70:"Jhiqui说晚餐已好。",71:"Daenerys疲惫悲伤地拒食，让handmaids分享并送Jorah一份，随后要一枚dragon egg。",72:"Irri取来green-bronze egg；Daenerys侧卧抱在pregnant belly与胸前，觉得stone dragons给予strength和courage。",73:"胎儿移动像在回应egg中的dragon；Daenerys称son为true dragon，带着home之梦入睡。",
}
SUMMARIES = [S[i] for i in range(1, 74)]

KEY_NOTES = {
1:"无wall城市却有monumental gate，说明入口首先是ritual boundary与身份宣告，而非单纯军事防御。",
2:"bronze horses框住purple mountain，建筑把Dothraki最核心的horse与sacred landscape对齐。",
3:"Sorefoot/Cart King的讽刺依赖Viserys不懂custom；Daenerys保护他不知真相，也在延长其自我幻觉。段中关系背景非露骨，未扩写。",
6:"被掠statues仍保留原文化形态，却失去names和context；Vaes Dothrak通过收集他者神圣物展示征服规模。",
8:"Viserys只因语言屏障才敢辱骂，所谓dragon自由依赖听众听不懂，并非真正无惧。",
9:"my people now标志Daenerys身份重心变化：她不再只以exile Targaryen看Dothraki。",
12:"衣服腐败把Viserys停留在Pentos华服/king形象的失败物质化；他越坚持旧身份，外表越像beggar。",
15:"她担忧的仍是两个男性权威碰撞，试图通过安抚双方维持脆弱关系。",
18:"sale/gift不是词语差异，而是交换制度冲突：Viserys认为已交货可催款，Drogo认为回礼时机属于giver。",
20:"stable/brooms双关把宏大复国claim压到最基础管理能力，Jorah否定的是leader而非Dothraki战力。",
21:"someone stronger故意不命名；Daenerys已经把army可能性与Viserys分离，开始想象其他leadership。",
24:"Jorah修正自己早期偏见的依据是具体能力：mounted archery、range、mobility、fearlessness和numbers。",
26:"比较四万总兵与四万mounted warriors强调composition差异；Jorah仍用假设战场预测，不是必然结果。",
28:"siegecraft是结构性弱点；Dothraki优势取决于Westerosi commanders是否接受open battle。",
30:"Robert与Dothraki共享valor code，使文化陌生不妨碍性格预测；Jorah认为councillors可能抵消其rashness。",
32:"Jorah把法律处罚叙述成Eddard为lice-ridden poachers毁掉自己，省略自身slaving责任；这是self-justifying视角。",
33:"largest/smallest悖论区分physical area与resident density；city为未来汇聚而建，日常却近乎空。",
35:"不同建筑不是Dothraki审美多元主动选择，而是enslaved builders留下的征服地图。",
37:"预言反过来塑造城市容量：因为相信所有khalasars终将齐聚，空置空间也具有目的。",
39:"no blood rule创造跨khalasar sacred truce；禁止blade并不意味着没有coercion或其他暴力形式。",
41:"bloodrider忠诚比Kingsguard更total，也更可怕：个人生命与khal绑定，institution由kinship language维系。",
42:"Daenerys明确庆幸不被shared；Qotho对handmaids的伤害说明Drogo身边绝对忠诚者未必对弱者安全。",
43:"她只从Aerys被Jaime杀和Barristan转投理解Kingsguard，尚不了解完整政治情境；未来设计基于partial history。",
45:"pregnancy疲劳与Drogo需求并置，显示她期待独处休息；正文未描写露骨行为，讲解也不作扩展。",
47:"new clothes是Daenerys的soft power方案：通过可见文化适应替Viserys重建Dothraki respect。",
51:"礼物每一件都按Dothraki环境设计，却保留dragon motif；她试图创造Targaryen与Dothraki的混合身份。",
52:"Viserys先伤Doreah再谈command，把对妹妹地位上升的恐惧转移到权力更弱的servant身上。",
54:"commanded可能是Doreah按Khaleesi正常权威翻译，到了Viserys耳中却成为篡夺king地位的证据。",
56:"Daenerys立刻改写为ask/if it pleases，仍先尝试用礼仪修补而非对抗。",
60:"waking his dragon仍控制她语言，说明社会权力已改变，童年恐惧反射却未立刻消失。",
62:"braid必须由victories赢得；Daenerys用已内化的Dothraki标准直接否认Viserys象征资格。",
63:"he dared not strike her表明约束来自witnesses和khas，而非突然尊重；Daenerys保护已成为可见政治事实。",
66:"belt本为礼物与地位修复工具，瞬间变成自卫weapon；她用想交给他的权威象征反击其旧权威。",
67:"the one who forgets himself翻转Viserys惯用训斥；她不再只躲dragon，而以Khaleesi身份规定边界。",
69:"blood on cloak把失败和解留下物质痕迹；Daenerys抱住它说明反击成功并未消除亲情悲伤。",
72:"egg是无生命stone却提供心理strength；是否有超自然作用，本段只通过Daenerys感受表达。",
73:"brother to brother把胎儿与egg内dragon想象成blood kin，同时把true dragon称号从Viserys转移给unborn son。",
}

STAGES = [
(1,15,"khalasar穿Horse Gate与掠夺monuments进入Vaes Dothrak；Viserys持续辱骂Dothraki并催要army，Daenerys开始称其为my people。"),
(16,32,"Jorah解释gift制度、否定Viserys领导力，又从horse archery、兵力与siege弱点评估Dothraki征服Westeros的条件。"),
(33,46,"Vaes Dothrak以被掳建筑、空置容量和sacred truce组织；bloodrider制度与Kingsguard形成忠诚对照，Drogo夜登Mother。"),
(47,63,"Daenerys准备衣食礼物帮助Viserys融入；他因Doreah说commanded而施暴，拒绝Dothraki服饰并再次威胁妹妹。"),
(64,73,"Viserys抓痛她后，Daenerys以gift belt反击并驱逐；亲情修复失败，她转向dragon egg与unborn son寻找strength和home。"),
]

BACKGROUNDS = {
3:"**Dothraki称号：** Khal Rhae Mhar意为Sorefoot King，Khal Rhaggat意为Cart King；两者都是对Viserys无能与不懂custom的嘲弄。",
6:"**godsway：** Horse Gate通往sacred city的主路，两侧陈列历代Dothraki从被征服地区掠来的monuments。",
11:"**dosh khaleen：** 由历任khal widows组成、常住Vaes Dothrak的女性权威群体，将为Daenerys pregnancy作prophecy仪式。",
18:"**gift norm：** Drogo视Daenerys为Viserys给他的gift，因此回报也应是自愿gift；Viserys却按sale/debt理解。",
24:"**Drogo兵力：** Jorah估算khalasar含四万mounted warriors；此数不包括所有随行population。",
26:"**Trident比较：** Rhaegar约带四万人，但knights约十分之一，其余含archers、freeriders与infantry。",
28:"**军事限制：** mounted archers适合open field与机动作战，不善攻Westerosi stone castles。",
32:"**Jorah exile原因：** Eddard因Jorah把poachers卖给slavers而判罪；Jorah本段把重点放在失去家园和honor冲突。",
37:"**Vaes Dothrak人口：** 仅dosh khaleen与servants常住，巨大容量用于所有khalasars可能同时回归的预言。",
39:"**sacred peace：** Mother of Mountains视线内不得携blade或流free man blood，敌对khalasars也须停战。",
41:"**bloodriders：** khal最亲密的三名兄弟式warriors，共享生死并在khal被杀后先复仇再殉死。",
43:"**Daenerys所知历史：** 她知道Jaime杀Aerys、Barristan转投Robert，但对Rebellion因果的认识来自Targaryen流亡叙事。",
47:"**服饰计划：** Daenerys以Dothraki-cut衣物配dragon装饰，试图让Viserys既保留Targaryen符号又符合当地尊重标准。",
62:"**braid：** Dothraki warrior以胜利后不剪发braid象征未败战绩；Viserys没有获得相应资格。",
72:"**dragon eggs：** Illyrio婚礼赠礼，被认为已经石化；Daenerys常通过触摸获得情绪力量。",
}

EXTRA_VOCAB = [
("rear","/rɪr/","v.","（马）扬起前蹄","bronze stallions"),("godsway","/ˈɡɑːdzweɪ/","n.","神道；仪式大道","Vaes Dothrak"),("linger","/ˈlɪŋɡər/","v.","逗留拖延","waiting"),("monolith","/ˈmɑːnəlɪθ/","n.","巨型独石碑","roadside spoil"),("sachet","/sæˈʃeɪ/","n.","香囊","Viserys sleeve"),("bide one’s time","/baɪd wʌnz taɪm/","phr.","等待合适时机","Pentos"),("outrange","/ˌaʊtˈreɪndʒ/","v.","射程超过","bows"),("shieldwall","/ˈʃiːldwɔːl/","n.","盾墙","foot archers"),("pike","/paɪk/","n.","长枪","infantry"),("rabble","/ˈræbəl/","n.","乌合之众（贬义）","Jorah’s army view"),("siegecraft","/ˈsiːdʒkræft/","n.","攻城技术","Dothraki weakness"),("rash","/ræʃ/","adj.","鲁莽的","Robert"),("piper","/ˈpaɪpər/","n.","风笛手；引申影响决策者","different tune"),("poacher","/ˈpoʊtʃər/","n.","偷猎者","Jorah crime"),("sprawl","/sprɔːl/","v.","无边界铺展开","city"),("languorously","/ˈlæŋɡərəsli/","adv.","慵懒舒展地","Vaes Dothrak"),("rickety","/ˈrɪkəti/","adj.","摇摇欲坠的","wood towers"),("cavernous","/ˈkævərnəs/","adj.","洞穴般巨大空旷的","hall"),("rough-hewn","/ˌrʌf ˈhjuːn/","adj.","粗凿粗制的","timber walls"),("billowing","/ˈbɪloʊɪŋ/","adj.","鼓胀翻涌的","silk roof"),("unbelt","/ʌnˈbelt/","v.","解下腰带上的物品","arakh"),("exempt","/ɪɡˈzempt/","adj.","被豁免的","Drogo not exempt"),("mace","/meɪs/","n.","战锤","Cohollo wound"),("glower","/ˈɡlaʊər/","v.","怒目而视","Haggo"),("hollow hill","/ˈhɑːloʊ hɪl/","n.","中空土丘式住所","Drogo dwelling"),("scalding","/ˈskɔːldɪŋ/","adj.","滚烫的","bathwater"),("haunch","/hɔːntʃ/","n.","动物后腿肉","goat"),("firepod","/ˈfaɪərpɑːd/","n.","辛辣豆荚状香料","cooking"),("raiment","/ˈreɪmənt/","n.","衣服服饰（古风）","gifts"),("quail","/kweɪl/","v.","畏缩发抖","Doreah"),("rue","/ruː/","v.","后悔；悔恨","future threat"),("spatter","/ˈspætər/","v.","飞溅","blood on cloak"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def extract_blocks():
    blocks = extract_range(354, 362, "DAENERYS", "CH36")
    # One quoted paragraph continues from p.359 to p.360 with capitalized “Doreah”.
    blocks[46]["text"] = str(blocks[46]["text"]) + " " + str(blocks[47]["text"])
    blocks[46]["end_page"] = blocks[47]["end_page"]
    del blocks[47]
    for order, block in enumerate(blocks, 1):
        block["order"] = order
        block["id"] = f"CH36-P{int(block['page']):03d}-{order:03d}"
    return blocks

def main():
    blocks = extract_blocks()
    write_chapter(
        out=OUT, chapter=36, pov="DAENERYS", page_start=354, page_end=362,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Dothraki custom、军事能力、Viserys权威困境与Daenerys逐步建立边界。",
        vocab=VOCAB,
        guide="Daenerys进入无wall却有巨大Horse Gate的Vaes Dothrak。沿godsway的被掠gods与各式建筑把Dothraki征服史变成城市景观；常住人口极少，空间按所有khalasars终将齐聚的prophecy预留。Jorah解释Viserys把婚姻视为sale，而Drogo把它视为gift，不能被催讨；他又认为四万mounted archers在open field极其危险、却不善siege，真正弱点是Viserys根本无领导能力。Daenerys准备Dothraki服饰与非horse晚餐，希望修复哥哥尊严。Viserys却因Doreah说commanded而施暴、拒绝文化适应并再次抓痛妹妹。Daenerys用本为礼物的bronze belt反击，以Khaleesi身份驱逐他；和解失败后，她从dragon egg与unborn son获得力量，并把true dragon称号从哥哥移向下一代。",
        people=[
            ("Daenerys Targaryen","本章视角；认同Dothraki为my people，并首次以实际武力制止Viserys"),
            ("Viserys Targaryen","不懂gift custom与Dothraki荣誉，因地位流失而侮辱、施暴并拒绝礼物"),
            ("Jorah Mormont","解释Vaes Dothrak、gift规范与Dothraki军事优劣，也暴露对Eddard的怨恨"),
            ("Khal Drogo","遵守sacred city交武器规则，夜登Mother of Mountains献祭"),
            ("Doreah / Irri / Jhiqui","Daenerys handmaids；Doreah因传达commanded遭Viserys殴打"),
            ("Cohollo / Haggo / Qotho","Drogo bloodriders；忠诚绝对，但后两人尤其Qotho令Daenerys与handmaids害怕"),
            ("dosh khaleen","常住sacred city的khal widows，将解释Daenerys unborn child prophecy"),
        ],
        terms=[
            ("Vaes Dothrak","Mother of Mountains下的sacred city，无walls、面积巨大、常住人口很少"),
            ("gift economy","Drogo认为Daenerys与未来回报均为gift，giver决定时间；Viserys误按商业债务催收"),
            ("bloodriders","与khal共享生死、复仇和兄弟身份的终身companions"),
            ("sacred truce","Vaes Dothrak内不得携blade或流free man blood，敌对khalasars暂时合一"),
            ("warrior braid","以未败胜绩取得的Dothraki象征，Viserys尚无资格"),
        ],
        synthesis="Chapter 36写权威如何从自称转向被承认。Viserys不断说king、dragon、promised crown，却不懂language、gift规则、braid资格或战士体系；Daenerys则会Dothraki、能调动khas、理解服饰与ritual，也能保护Doreah。她的权力不是一句宣言突然出现，而是旅程中学会的文化知识、关系与行动累积。belt转成weapon尤其清楚：原本用来替Viserys制造合法外观的礼物，被他拒绝后反而成为Daenerys维护自身边界的工具。",
        contrasts=[
            "**无walls／巨大gate：** Vaes Dothrak以ritual而非城防界定城市。",
            "**sale／gift：** Viserys认为被欠army，Drogo认为回礼不能被demand。",
            "**open-field strength／siege weakness：** Dothraki mobility与数量强大，却难攻stone castles。",
            "**Kingsguard oath／bloodrider life bond：** 前者在Daenerys记忆中会betray，后者忠诚更彻底也更残酷。",
            "**gift belt／self-defense weapon：** 和解象征因Viserys暴力被反转。",
            "**自称dragon／true dragon转移：** Viserys靠威胁维持称号，Daenerys把它给unborn son。",
        ],
        questions=[
            "dosh khaleen会如何解释Daenerys unborn child，prophecy将怎样影响Drogo？",
            "Viserys会不会理解自己已失去命令妹妹和khalasar的实际权力？",
            "Jorah的军事评估是否会推动Daenerys想象由谁领导Dothraki渡海？",
            "dragon eggs带来的strength只是心理安慰，还是还存在尚未理解的性质？",
        ],
        extraction_notes="PDF pp.354–362校勘后共73段；自动提取曾把pp.359–360间同一段中以Doreah开头的续句误切，已合并。共5处跨页续段：pp.354–355、356–357、357–358、358–359与359–360。涉及未成年Daenerys的非露骨关系背景按原文保留，不扩写或情色化；本章无须新增敏感占位符。",
    )
    print(f"Wrote Chapter 36 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
