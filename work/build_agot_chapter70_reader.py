#!/usr/bin/env python3
"""Build Chapter 70 (JON) close-reading Markdown."""
from pathlib import Path

from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter69_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

SUMMARIES = [
"Jon在寒冷stable给mare备鞍，烧伤手指仍僵硬，并召来Ghost。",
"Sam恳求Jon不要离开。",
"Jon上马面对夜色；月光把Sam的影子投得巨大，他命Sam让路。",
"Sam坚持不能放他走。",
"Jon威胁若不让开便骑马撞过去。",
"Sam相信Jon不会伤他，继续请求倾听。",
"Jon催马冲门；Sam到最后一刻才避开跌倒，mare从他上方跃出。",
"Jon趁Castle Black守望者面朝north而向south逃走，并用‘I warned him’减轻对Sam受伤的内疚。",
"Jon沿kingsroad疾驰，计划天亮后离路隐藏踪迹；目的地显然容易被猜到。",
"他估算Old Bear黎明起床前的时间，并相信Sam因友情不会主动告发。",
"Jon把Longclaw留在床上，因为deserter无权带走；此举仍会加深Mormont因Jorah蒙羞留下的伤口。",
"Jon无法确定何者才是honor，羡慕有septons解释神意的southron，而old gods沉默。",
"离开Castle Black灯火后他放慢速度，保护唯一坐骑以完成长途旅程。",
"全身black会暴露Night’s Watch身份；ravens传讯后连Winterfell也不能安全收留他。",
"尽管理性上不能去Winterfell，他仍清晰想念Bran、Old Nan、食物和旧房间。",
"Jon说自己终究是Eddard之子、Robb之弟；Longclaw不能使他成为Mormont，Aemon的三次选择也不能替他选择。",
"他接受自己是bastard、oathbreaker和终身逃亡者，只求活到与Robb并肩为Eddard复仇。",
"Jon幻想秘密现身Robb面前，却无法想象Robb会说什么。",
"Robb的笑容无法出现，取而代之的是Eddard处决Night’s Watch deserter的完整记忆。",
"Jon试图相信若deserter是Benjen，Eddard和Robb会作例外。",
"他拒绝继续想被Robb依法处决的可能，以狂奔压过疑虑，希望至少能像Stark一样战死。",
"Ghost先跟上奔马，随后按自己的节奏落在后方。",
"Jon穿过大多沉睡的Mole’s Town。",
"地下town与‘buried treasures’笑话使他想到兄弟们也会违背celibacy oath，却很少被追究。",
"Jon停下饮snowmelt，烧伤加剧；他反问若决定正确，为何身心如此痛苦。",
"他牵马恢复体力，并承认刚才狂奔愚蠢得像急于赴死。",
"林中动物尖叫使mare不安；Jon呼唤Ghost，只惊起owl。",
"Ghost迟迟不回，Jon担心它遇到bear或wolf pack。",
"Jon停下吃简陋食物，盘算今后狩猎会拖慢速度。",
"他吃完apple时听见北方追来的horses，判断距离太近无法骑马逃脱。",
"Jon把mare藏在sentinels后，希望来者只是夜行smallfolk；原文把Quiet排作Ouiet。",
"至少五六名骑手接近，谈话声穿过树林。",
"一名追踪者询问是否确定Jon走了这条路。",
"另一人承认无法确定。",
"有人推测Jon也可能东行或穿林。",
"同伴说黑夜穿林只会摔死或迷路。",
"Grenn认为可凭stars辨认south。",
"Pyp追问若多云怎么办。",
"Grenn说那样自己就不会出发。",
"Toad笑称若是自己会去Mole’s Town找‘buried treasure’，mare却因笑声发出鼻响。",
"Halder让所有人安静，说听见了动静。",
"骑手停下，有人否认听见任何东西。",
"同伴嘲笑其连自己放屁都听不见。",
"Grenn认真反驳。",
"Halder再次命令安静。",
"Jon屏息看见马腿，意识Sam没告发Mormont，却召集朋友追来；他们也可能因此被当作deserters。",
"长久静默后Pyp询问Halder听见什么。",
"Halder不确定，猜测是horse声。",
"有人断言这里什么也没有。",
"Ghost突然出现惊动mare，Halder立即发现藏身处。",
"另一人也确认听见。",
"Jon骂Ghost是traitor并试图撤离，但追兵迅速包围。",
"Pyp喊Jon名字。",
"Grenn要求停下，因为Jon不可能甩掉所有人。",
"Jon拔剑威胁，仍说不愿伤害他们。",
"七人散开合围，人数优势显著。",
"Jon质问他们目的。",
"Pyp说要把他带回真正属于他的地方。",
"Jon坚持自己属于Robb身边。",
"Grenn回答Night’s Watch成员如今才是他的brothers。",
"Toad紧张提醒逃兵会被砍头，又把Jon的行为比作Grenn式愚蠢。",
"Grenn否认，强调自己认真发过誓且不是oathbreaker。",
"Jon说自己同样真心发誓，但Eddard被杀、Robb正在战争中。",
"Pyp说明Sam已告诉他们全部消息。",
"Grenn对Eddard之死表示遗憾，却说words一经宣誓便不能因私事离开。",
"Jon仍说自己非走不可。",
"Pyp开始逐句复述Night’s Watch vow，提醒watch直到死亡才结束。",
"Grenn补上在岗位生死相守的句子。",
"Jon发怒说自己也熟知誓词，朋友只是在加重痛苦。",
"Halder庄重背出‘I am the sword in the darkness’。",
"Toad接上‘the watcher on the walls’。",
"他们无视咒骂，Pyp继续念抵御cold、带来dawn和守护realms的誓词。",
"Jon持剑警告Pyp别靠近，并意识到可轻易伤害未穿armor的朋友。",
"Matthar绕到背后加入合诵，重申life and honor归于Watch。",
"朋友从四面收紧包围，Jon只能原地转马。",
"Halder从左侧念出for this night。",
"Pyp完成and all nights to come，并给Jon二选一：杀他或一起回去。",
"Jon举剑又无力放下，咒骂所有人。",
"Halder询问是否需要捆手，还是Jon愿承诺和平返回。",
"Jon保证不逃，转而责怪把他暴露的Ghost。",
"Pyp催促赶在first light前回去，免得全体受罚。",
"返程在Jon记忆中很短；黎明前Castle Black重新出现，却不再像home。",
"Jon暗想朋友能带回却不能永远看守，已计划下次沿Wall或wildling mountain route再逃；提取中的wouid据页面修为would。",
"焦虑未眠的Sam在stable等候，并说庆幸找到Jon。",
"Jon直说自己并不庆幸。",
"Pyp让Sam帮忙安置horses，并抱怨Lord Snow让大家无眠。",
"Jon照常给Mormont送早餐，日常秩序仿佛没有中断。",
"他用冰冷lemon为Mormont调beer，细节强化既熟悉又紧张的serving routine。",
"Mormont以‘所爱之物总会毁掉我们’切入Eddard之死。",
"Jon阴沉确认记得，却不愿谈父亲。",
"Mormont要他记住hard truths，并直接问昨夜骑行是否疲惫。",
"Jon喉咙发干，惊问Mormont已经知道。",
"raven重复Know，使秘密暴露更具戏剧性。",
"跨页合并后Mormont说Aemon早料到Jon会走，自己则料到他会回来；honor让他出发，也让他被带回。",
"Jon纠正说是friends把自己带回。",
"Mormont反问自己何曾说是Jon本人的honor。",
"Jon质问父亲被杀，难道应无动于衷。",
"Mormont说他们预料到他会逃，并已派人监视；若朋友不带回，也会有Watch men截住。",
"Jon承认没有带翼的horse，感觉自己很蠢。",
"Mormont以玩笑说Watch倒很需要这种horse。",
"Jon准备好接受desertion死刑，声称不怕死。",
"raven尖叫Die。",
"Mormont希望他也不怕活，并指出尚未构成彻底desertion；但追问他是否仍计划以后逃跑。",
"Jon沉默，等同默认。",
"Mormont看穿他，问Eddard已死后Jon能否使其复生。",
"Jon闷闷回答不能。",
"Mormont用两人见过wight的经历把bring back反转成恐怖；又指出Robb有整个North，根本不缺Jon一把剑。",
"Jon无法回答，raven正啄开egg取食。",
"Mormont说自己也爱可能随Robb出征的Maege与其女儿，却因誓言留守，最后追问Jon的位置在哪里。",
"Jon心中仍以bastard、无权无名解释无处归属，口头只说不知道。",
"Mormont说自己知道：North出现elk、mammoths南迁、巨大足迹、废弃村庄、山火及Mance集结，失踪rangers远不止Benjen。",
"raven重复Ben Jen，把Jon最私人的北方牵挂嵌入大局。",
"Jon承认确有许多其他rangers失踪。",
"Mormont严厉问Robb的war是否比Watch的war更重要。",
"Jon迟疑时raven反复叫war。",
"Mormont说dead men夜猎时，Iron Throne归谁毫无意义。",
"Jon第一次从这种尺度思考，回答不重要。",
"Mormont说Eddard把Jon送来必有原因，虽无人能确定。",
"raven连续追问Why。",
"Mormont把Stark的First Men血统、Wall古老记忆与Ghost发现wights联系起来，认为Jon注定在此，并要带他越墙。",
"Jon因兴奋发冷，重复Beyond the Wall。",
"Mormont宣布亲自率Night’s Watch大举出境，寻找Benjen并调查Mance、Others与未知威胁；他要求Jon立即选择。",
"Jon请求Eddard、Robb、Arya和Bran原谅，承认这里才是自己的位置，并发誓不再逃。",
"Mormont接受答案，命他重新佩上sword。",
]

KEY_NOTES = {
1:"开场是安静准备而非冲动爆发，说明Jon已经认真计划desertion；scarred fingers不断把选择的痛转成身体感。",
3:"Sam的giant shadow与本人胆怯体型形成反差，他在道德上比自己的自我形象更勇敢。",
8:"Watch eyes朝north、Jon骑向south，是使命方向与私人忠诚的视觉对置。",
11:"留下Longclaw表明Jon仍接受某些honor界线，也让desertion并非简单抛弃一切价值。",
12:"old gods不回答不是证明没有道德，而是迫使Jon承担无法外包的判断责任。",
16:"‘不是Mormont，也不是Aemon’说明榜样和礼物都不能直接替代个人选择。",
17:"Jon用极端身份标签惩罚自己，同时把与Robb并肩想象成最后的belonging。",
19:"小说开篇deserter execution回返，使读者不能把Jon的行为只看作浪漫投奔家人。",
21:"四个sons的愿望仍是向Eddard索取死后的承认：Jon想以死亡获得生前欠缺的合法位置。",
24:"Mole’s Town的日常违誓与desertion死罪形成制度执行强度差异；并非所有oath breach同等处理。",
25:"烧伤手在每次疑虑时加剧，身体痛成为压抑冲突的叙事节拍。",
31:"Ouiet是页面可见排印异常，不是本文件误写；原文保留以维持来源忠实。",
46:"朋友冒险离营不是否定誓言，而是用brotherhood把Jon带回誓言内部。",
50:"Ghost像‘背叛’Jon，实际把他暴露给能阻止其自毁的朋友；animal agency保持可解释而不神化。",
60:"‘brothers now’重定义family，不抹去Robb，却要求Jon承认发誓后形成的新关系。",
67:"朋友不以长篇辩论说服，而让Jon亲口面对自己宣过的words。",
72:"誓词从cold、dawn到realms，把Jon的私人战争放回Watch保护全人类的尺度。",
77:"Kill me or come back把抽象oath转成Jon不愿支付的具体友情代价，因此真正阻止他的不是武力。",
82:"Castle Black暂时不像home，表明身体返回不等于心理选择完成。",
83:"Jon立刻筹划再逃，证明朋友只中断行动，尚未解决价值冲突；wouid是提取错误，依页面改为would。",
89:"Mormont重复的love命题与Aemon上一章教导呼应，但他会用军事现实而非抽象神学推进。",
94:"Mormont巧妙把honor拆成朋友的honor：Jon得以返回不是个人意志胜利，而是共同体替他承担。",
99:"Mormont早已布置截获，朋友行动改变的是Jon如何回来、是否亲手伤害brothers，而非Watch能否抓到他。",
104:"‘尚未deserted’是一种有意宽容的制度解释，也以未来选择为条件，不代表desertion规则消失。",
108:"bring back先指Eddard，再转wights，把Jon的复仇愿望与North真正的dead threat尖锐并置。",
110:"Mormont用自己对Maege的love证明duty不是因无感情才容易，而是在同类痛苦中仍选择岗位。",
112:"动物迁徙、footprints、弃村和集结分别来自不同报告；它们共同示警，但具体原因仍未完全确定。",
117:"Iron Throne问题把本书南方权力战争相对化：对会复活的dead而言，合法王位没有防御意义。",
121:"Mormont从Ghost行为推到‘meant to be’属于角色的purpose inference，不是文本已证实的命运机制。",
123:"最终问题故意用brother与bastard boy对立：Jon若只用出身解释自己，就永远无法选择成年身份。",
124:"Jon不是不再爱Starks，而是承认自己无法实际改变南方战局，并选择更需要他的岗位。",
}

STAGES = [
(1,21,"Jon夜间离开Castle Black，在family、honor与deserter死刑之间反复自辩，并把与Robb并肩视为获得Stark归属。"),
(22,52,"他穿过Mole’s Town后躲避追兵，却被Ghost暴露；追来的是Sam召集的Night’s Watch朋友。"),
(53,82,"Pyp、Grenn等以完整vow包围Jon，让他在杀朋友或回归间选择；他放下剑，被带回Castle Black。"),
(83,108,"Jon仍计划再次逃跑；Mormont表明一切早在监视中，并以Robb不缺一把剑、自己也有亲属参战反驳。"),
(109,124,"Mormont揭示Wall以北的大规模异常与远征计划；Jon重新衡量战争尺度，主动确认Night’s Watch身份。"),
]

BACKGROUNDS = {
11:"**Longclaw：** House Mormont的Valyrian steel bastard sword；Jon认为desertion使自己无权带走。",
14:"**black clothing：** Night’s Watch统一黑衣在North极易辨认；ravens可迅速把deserter特征传给各处。",
19:"**desertion penalty：** Night’s Watch誓言终身有效，擅离岗位可判死；Eddard在序章后第一章亲自执行过。",
24:"**Mole’s Town：** Castle Black以南最近聚落，大部分建筑和活动位于地下cellars。",
58:"**new brotherhood：** 发誓后Watch成员互称brothers，制度上要求新共同体优先于出生家族战争。",
67:"**Night’s Watch vow：** 规定watch终身、驻守岗位、奉献life and honor，并以抵御darkness/cold为使命。",
94:"**宽容边界：** Mormont把此次夜骑解释为尚未完成desertion，但明确若Jon再次逃离，判断可能不同。",
108:"**Robb’s force：** Robb已有North主要lords bannermen；Mormont以军事效用说明Jon个人参战几乎不能改变南方力量对比。",
110:"**Maege Mormont：** Old Bear的妹妹、Bear Island统治者，可能带女儿随Robb参战；Mormont同样承受family-duty冲突。",
112:"**northern reports：** Eastwatch、Shadow Tower与Gorge多路报告动物迁徙、弃村、山火和Mance集结，信息相互强化但原因未明。",
117:"**Watch priority：** Watch宣称守护realms of men，不效忠某一Iron Throne竞争者，因此应优先处理超越王位战争的威胁。",
121:"**First Men：** Stark血统与Wall建造传统相连；‘remember things otherwise forgotten’是传说性说法。",
123:"**great ranging：** Mormont计划不再零散派rangers，而由Lord Commander亲率主力越墙调查并寻找Benjen。",
}

EXTRA_VOCAB = [
("whicker","/ˈwɪkər/","v.","马轻声嘶鸣","mare"),("cinch","/sɪntʃ/","n./v.","马肚带；系紧","saddle"),("wheel","/wiːl/","v.","使马迅速转向","face the night"),("ungainly","/ʌnˈɡeɪnli/","adj.","笨拙不灵活的","Sam"),("strike out","/straɪk aʊt/","phr.","离开道路向新方向行进","overland"),("blown","/bloʊn/","adj.","马匹因过劳而喘竭的","mare"),("roughspun","/ˈrʌfspʌn/","adj.","粗纺布制的","breeches"),("jerkin","/ˈdʒɜːrkɪn/","n.","无袖紧身皮衣","leather"),("moleskin","/ˈmoʊlskɪn/","n.","厚实棉布；鼹鼠皮状织物","sword sheath"),("hauberk","/ˈhɔːbɜːrk/","n.","锁子甲长衫","ringmail"),("coif","/kɔɪf/","n.","锁甲头罩","armor"),("holdfast","/ˈhoʊldfæst/","n.","小型堡寨","road south"),("salt in the wound","/sɔːlt ɪn ðə wuːnd/","phr.","使旧伤更痛","Jorah disgrace"),("craven","/ˈkreɪvən/","adj./n.","怯懦的；懦夫","moral doubt"),("brigand","/ˈbrɪɡənd/","n.","强盗；匪徒","execution"),("raucous","/ˈrɔːkəs/","adj.","沙哑刺耳的","mule"),("privy","/ˈprɪvi/","n.","户外厕所","shack"),("runoff","/ˈrʌnɔːf/","n.","融雪径流","snowmelt"),("lathered","/ˈlæðərd/","adj.","马因出汗布满泡沫的","mare"),("pass abreast","/əˈbrest/","phr.","并排通过","road"),("filch","/fɪltʃ/","v.","顺手偷取","bacon"),("rasher","/ˈræʃər/","n.","一薄片培根","food"),("tart","/tɑːrt/","adj.","酸而爽口的","apple"),("peeved","/piːvd/","adj.","恼怒的","Grenn"),("brandish","/ˈbrændɪʃ/","v.","挥舞武器威吓","sword"),("intoned","/ɪnˈtoʊnd/","v.","庄重吟诵","vow"),("bide one's time","/baɪd wʌnz taɪm/","phr.","耐心等待时机","escape plan"),("perilous","/ˈperələs/","adj.","危险的","mountain route"),("flagon","/ˈflæɡən/","n.","大酒壶","beer"),("sullenly","/ˈsʌlənli/","adv.","闷闷不乐地","Jon"),("dumb as a stump","/dʌm æz ə stʌmp/","phr.","笨得像木桩","Mormont irony"),("fortnight","/ˈfɔːrtnaɪt/","n.","两星期","future escape"),("morsel","/ˈmɔːrsəl/","n.","一小口食物","egg"),("hoary","/ˈhɔːri/","adj.","白发年老的；古老的","Maege insult"),("misshapen","/ˌmɪsˈʃeɪpən/","adj.","畸形的","footprints"),("happenstance","/ˈhæpənstæns/","n.","偶然事件","Ghost warning"),("meekly","/ˈmiːkli/","adv.","温顺被动地","wait"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def extract_blocks():
    blocks = extract_range(701, 712, "JON", "CH70")
    # Merge the genuine pp.709–710 continuation split after “Night’s”.
    blocks[93]["text"] += " " + blocks[94]["text"]
    blocks[93]["end_page"] = blocks[94]["end_page"]
    del blocks[94]
    # The PDF image shows “would”; text extraction confused l with i.
    blocks[82]["text"] = blocks[82]["text"].replace("wouid follow", "would follow")
    for i, block in enumerate(blocks, 1):
        block["order"] = i
        block["id"] = f"CH70-P{block['page']:03d}-{i:03d}"
    return blocks

def main():
    blocks = extract_blocks()
    write_chapter(
        out=OUT, chapter=70, pov="JON", page_start=701, page_end=712,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须展开的设定；重点在Jon的desertion选择、Night’s Watch brotherhood、誓词效力与Wall以北威胁。",
        vocab=VOCAB,
        guide="Jon因Eddard被杀而夜间逃离Castle Black，想秘密加入Robb，却无法摆脱自己曾见Eddard处决deserter的记忆。他留下Longclaw，说明即使违誓也仍试图保留honor界线。Sam没有告发Mormont，而是召集Pyp、Grenn等人追赶。朋友们包围Jon，逐句背诵Night’s Watch vow，并把选择压缩为‘杀我，或跟我回去’；Jon无法伤害他们，只得返回。Mormont早知夜骑并已布置监视，却把返回机会保留给Jon。他指出Robb拥有整个North，并不缺Jon一把剑；自己也爱可能参战的Maege和她的女儿，却仍守在岗位。随后他列出Wall以北多路异常：动物南迁、巨大足迹、废弃村庄、山火、Mance集结和大量rangers失踪。面对会在夜里猎人的dead，Iron Throne归谁并不重要。Mormont宣布亲率great ranging寻找Benjen并调查威胁，Jon终于不再仅以bastard定义自己，承认Night’s Watch才是自己的位置。",
        people=[("Jon Snow","本章视角；短暂desertion后重新选择Night’s Watch"),("Samwell Tarly","冒险阻拦Jon并召集朋友追赶，却未直接向Mormont告发"),("Pyp / Grenn / Halder / Toad / Matthar","以brotherhood和完整vow迫使Jon面对选择"),("Lord Commander Mormont","早知逃离并安排监视，以现实战略和great ranging重新争取Jon"),("Ghost","跟随Jon出逃，又意外暴露其藏身处；此前曾发现wights"),("Robb Stark","Jon想投奔的brother，已有North主力支持"),("Eddard Stark","死亡触发Jon出逃，其处决deserter的记忆又构成约束"),("Maege Mormont","Mormont的妹妹，可能随Robb参战，证明Commander也承担亲情代价"),("Benjen Stark","失踪ranger；great ranging将寻找其生死")],
        terms=[("desertion","终身誓言下擅离Night’s Watch岗位，原则上可判死"),("new brothers","发誓后形成的Watch共同体，要求超越出生家族政治"),("the words","Night’s Watch vow；朋友以共同记忆而非单纯武力带Jon返回"),("northern migration signs","动物迁徙、弃村、山火与失踪共同构成异常预警"),("great ranging","Lord Commander亲率较大兵力越墙调查，而非零散巡逻")],
        synthesis="Chapter 70不是让Jon在family与honor之间突然停止痛苦，而是改变他衡量两者的尺度。出逃时，他把自己描述成motherless、friendless、damned，仿佛bastardy注定他只能靠为Robb战死来成为Eddard的‘第四个儿子’。但追来的七人本身反驳friendless：他们愿冒被视为deserter的风险，把Jon带回，并宣称‘We’re your brothers now.’ 誓词在这里不只是机构命令，而由朋友共同发声。Pyp的选择题之所以有效，不是Jon打不过，而是他不肯以杀死新brother作为投奔旧brother的代价。Mormont进一步拆解Jon的英雄幻想。Robb已有North诸侯，Jon一把剑几乎不能改变南方战争；Watch却正在失去rangers，并面对动物迁徙、弃村、Mance集结和复活dead。‘谁坐Iron Throne’与‘谁守住living realms’由此成为不同层级的问题。Mormont没有否认love，反以Maege说明自己也付出相同代价；他的宽容也不是取消规则，而是把Jon尚未完成的出逃解释为一次可收回的选择。结尾Jon说This is my place，不表示Stark亲情消失。他在心中逐一向Eddard、Robb、Arya、Bran道歉，正说明牺牲真实存在。成长发生在他不再让bastard身份替自己决定，而主动成为Mormont's man与Night’s Watch brother。",
        contrasts=["**north-facing guards／southbound Jon：** 共同使命方向与私人复仇方向相反。","**Longclaw left behind／oath abandoned：** Jon违背大誓，却仍维护一条honor界线。","**old family／new brothers：** Watch不抹去Starks，而要求新共同体拥有实际约束力。","**seven unarmored friends／one drawn sword：** 武力优势可能在Jon，决定性力量却是他不愿杀人。","**bring Eddard back／dead men come back：** 哀悼愿望被wight现实转成恐怖反问。","**Robb’s many swords／Watch’s scarcity：** Jon在两场战争中的边际作用不同。","**bastard boy／brother of the Watch：** 被动出身标签与主动承担身份对立。"],
        questions=["Mormont的great ranging将发现Benjen还是其他失踪rangers吗？","Mance为何把free folk集中到秘密stronghold？","巨大footprints与动物南迁分别指向什么威胁？","Jon能否在收到更多Stark消息时继续守住此次承诺？","Ghost与wights之间是否存在超出偶然的感知联系？"],
        extraction_notes="PDF pp.701–712校勘后共124段。6处跨页续段：pp.701–702、702–703、703–704、708–709、709–710（自动误拆后合并）、710–711。p.705页面本身排作‘Ouiet now’，按源文保留；p.708–709提取出的‘wouid’经页面图像确认应为‘would’，已修复；p.710页面可见‘you.,’异常标点，按源文保留。无需要安全占位的段落。",
    )
    print(f"Wrote Chapter 70 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
