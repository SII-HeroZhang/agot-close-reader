#!/usr/bin/env python3
"""Build Chapter 33 (EDDARD) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter32_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"Eddard恳求Robert听清自己的命令本质：是在谋杀一个child。",2:"Robert因Daenerys怀孕暴怒，要求mother、unborn child和Viserys全部死亡。",3:"其他councillors假装置身事外，Eddard独自警告此举会永久羞辱Robert。",4:"Robert愿承担污名，只求消除悬在自己颈上的axe。",5:"Eddard说所谓axe只是二十年外的影子，甚至可能根本不存在。",6:"Varys轻声反问Eddard是否怀疑自己会向king和council带来lies。",7:"Eddard指出消息来自半个世界外的traitor Jorah，可能错误或撒谎。",8:"Varys说Jorah不敢骗自己，坚持princess怀孕。",9:"Eddard列出miscarriage、daughter、infant death等多种不构成威胁的可能。",10:"Robert追问若生下存活的boy怎么办。",11:"Eddard说narrow sea仍在，等Dothraki学会让马跑水上才值得害怕。",12:"Robert把等待描述成直到Targaryen army登陆才行动。",13:"Eddard强调所谓dragonspawn仍在腹中，连Aegon也是断奶后才征服。",14:"Robert骂Eddard像aurochs般固执，并逼其他councillors表态。",15:"Varys先承认谋杀vile，却以统治者为realm利益必须做恶来支持行动。",16:"Renly认为多年前就该杀Viserys与Daenerys，Jon的mercy是错误。",17:"Eddard以Robert救治敌将Barristan的旧事论证mercy从非错误，并暗问昔日高尚Robert去了哪里。",18:"Robert羞愧脸红，却辩称Barristan身份不同。",19:"Eddard反驳Daenerys只是十四岁girl，并问Rebellion若非为终止杀害children还有何意义。",20:"Robert答目的就是终结Targaryens。",21:"Eddard以Robert从不怕Rhaegar反讽他如今竟怕unborn child。",22:"Robert气紫脸，警告Eddard别忘谁是king。",23:"Eddard回问Robert自己是否忘了king应成为什么。",24:"Robert结束争论，要求每人直接投票。",25:"Renly明确赞成杀死Daenerys。",26:"Varys以悲伤姿态说别无选择。",27:"Barristan认为战场杀敌有honor，杀死母腹中敌人没有，因此支持Eddard。",28:"Pycelle以未来战争的士兵、城镇和children伤亡论证杀一人可救数万人。",29:"Varys赞同所谓kinder选择，并把Daenerys son与realm流血直接相连。",30:"Littlefinger用与ugly woman同床的粗俗比喻主张尽快完成不愉快任务。",31:"Barristan惊问kiss何意。",32:"Littlefinger答是steel kiss。",33:"Robert宣布Eddard与Barristan少数败北，转问由谁执行刺杀。",34:"Renly提醒Jorah渴望royal pardon。",35:"Varys说Vaes Dothrak拔刀会死，建议用tears of Lys伪装自然死亡。",36:"Pycelle骤然睁眼，怀疑地看向Varys。",37:"Robert嫌poison是coward武器。",38:"Eddard指责Robert雇刀杀十四岁girl却还计较honor，要求他按Stark原则亲自看着受刑者执行。",39:"Robert发现Eddard真心拒绝后砸空flagon，命令无论如何执行。",40:"Eddard拒绝在murder命令上加Hand seal。",41:"Robert起初无法理解defiance，随后以Hand必须服从否则换人威胁。",42:"Eddard摘下silver hand badge辞职，祝下一任成功，并说自己曾以为Robert更高尚。",43:"Robert命他滚回Winterfell，威胁若再相见就把头插上spike。",44:"Eddard鞠躬离开；门未关前已听见Pycelle提议Braavos的Faceless Men。",45:"Littlefinger抱怨Faceless Men刺杀princess费用高得胜过雇一支sellsword army。",46:"门关闭隔绝声音，守门Boros只好奇旁观。",47:"沉闷天气让Eddard想以雨洗净参与会议的污秽感；回Tower后他召Vayon。",48:"Eddard说明自己已不是Hand，准备全员返回Winterfell。",49:"Vayon估计整备需要两周。",50:"Eddard说可能连一天都没有，却仍相信Robert冷静后不会真伤害旧友。",51:"他忽然想到Robert对死去十五年的Rhaegar仍不消怒，加上Catelyn拘捕Tyrion即将曝光，安全判断动摇。",52:"Eddard决定带daughters与少量guards先走，要求Jory知情但在他们离开前保持秘密。",53:"Vayon领命。",54:"独处时Eddard既向往sons、Catelyn、新child、snow和wolfswood，又把离开解释成Robert替他做了选择。",55:"但未完成的财政、Lannister影响与Jon murder调查又令他愤怒；现有线索只是兽迹，尚未看见野兽本身。",56:"他想到乘船北返可途经Dragonstone询问Stannis；Stannis沉默使他更确信对方掌握Jon秘密。",57:"Eddard反问得到truth后怎么办，并把dagger、Bran与Jon秘密想成同一web的不同strand。",58:"Robert杀Daenerys的决定使Eddard首次怀疑king是否也可能涉入其他阴谋，并想起Catelyn说king已成陌生人。",59:"他再次召Vayon，命其秘密寻找只求快速安全、不求舒适的北行船。",60:"Vayon刚走，Tomard便报告Littlefinger来访。",61:"Eddard本想拒见，却认为自己尚未离开，仍须play their games。",62:"Littlefinger穿华服、带惯常mocking smile，仿佛早晨无事发生般进门。",63:"Eddard冷问来意。",64:"Littlefinger以Lady Tanda想嫁女和丰盛晚餐开玩笑，说自己宁娶suckling pig但爱lamprey pie。",65:"Eddard叫他去吃eels，并说此刻最不想见的就是他。",66:"Littlefinger列Varys、Cersei、Robert为更差对象，又转述Robert指责Eddard insolence与ingratitude。",67:"Eddard沉默且不让座，Littlefinger自行坐下，声称自己阻止雇Faceless Men，改由Varys悬赏lordship。",68:"Eddard厌恶用title奖励assassin。",69:"Littlefinger以titles cheap、Faceless Men expensive解释，并称低水平sellsword更可能失败，反而给Daenerys预警。",70:"Eddard质疑他council中赞同steel kiss、现在却自称保护girl的可信度。",71:"Littlefinger笑说自己确实把Eddard当巨大fool。",72:"Eddard问他是否总觉得murder好笑。",73:"Littlefinger说好笑的是Eddard像在rotten ice上治理，早晨已听见第一道裂纹。",74:"Eddard说那也是最后一道，自己已经受够。",75:"Littlefinger询问何时回Winterfell。",76:"Eddard答越快越好，并反问与他何干。",77:"Littlefinger说若Eddard黄昏仍在，就带他去Jory一直没找到的brothel，并拿Catelyn开玩笑。",
}
SUMMARIES = [S[i] for i in range(1, 78)]

KEY_NOTES = {
1:"Eddard拒绝用princess、heir或threat等政治词汇抽象受害者，先把命令还原为murdering a child。",
2:"Robert连续重复I want them dead，把恐惧转为绝对命令；把mother与胎儿并列也消除了等待事实发展的空间。",
3:"councillors的回避不是中立，他们随后都会表态；沉默首先表现出没人愿抢在king怒火前承担立场。",
5:"shadow of a shadow强调威胁经过血缘、时间、海洋与不确定未来多重折射，Eddard拒绝把可能性当迫近事实。",
7:"Eddard准确指出情报链含有incentivized source：Jorah有求于crown，因此既可能真报也可能迎合。",
9:"一串if展示风险树而非单一路径；他的伦理结论不只靠概率，但概率削弱“必须现在杀”的必要性。",
11:"horses run on water用讽刺把Dothraki陆战优势与narrow sea障碍具象化，也可能低估未来运输联盟。",
15:"Varys先承认vile再诉realm，是dirty hands论证：统治责任被用来允许私人道德禁止之事。",
17:"Barristan旧事把Robert自身最好行为变成反对当前Robert的证据；Would that man were here既怀念也指控。",
19:"Eddard把Rebellion正当性系于终止child murder；若胜者复制Aerys暴行，战争的道德叙事便坍塌。",
21:"unmanned与tremble直接攻击Robert男子气概，是危险但针对其核心自我形象的最后劝谏。",
23:"Have you?把“谁拥有权位”翻转成“是否履行king责任”；短句使政治不服从公开化。",
27:"Barristan把enemy保留为enemy，却要求战场面对，说明反刺杀不等于否认未来威胁。",
28:"Pycelle使用consequentialist calculus：确定杀一名无辜者换取避免假设性大规模伤亡；预测可靠性决定论证强弱。",
30:"Littlefinger把国家谋杀类比成不得不完成的性行为，以轻佻语言降低道德重量，并回避谁承担后果。",
35:"Varys刚在上一章称tears of Lys杀死Jon，此处立刻把同一毒药作为政策工具，Pycelle的睁眼反应因此值得注意但含义未明。",
38:"The man who passes the sentence should swing the sword把Winterfell justice原则带入远程刺杀争议：责任不能被distance和hired knife稀释。",
40:"seal把道德异议变成行政拒绝；没有Hand认证，Eddard不允许自己的office替命令提供合法外观。",
42:"摘badge是可见的身份解除，也把Jon亲手授予的office还回导致Jon调查死亡的制度。",
44:"讨论scarcely a pause显示Eddard辞职并未阻止policy machinery；个人道德退出与实际救下Daenerys并非同一成果。",
45:"Littlefinger先把murder转成price comparison，财政专业在此服务于刺杀方案优化。",
50:"Eddard以Robert rage always cool为安全模型；下一段用Rhaegar反例检验“always”并发现并不成立。",
51:"Catelyn/Tyrion消息把私人争吵连接到Stark–Lannister冲突；Eddard开始从离职规划转向撤离规划。",
54:"snow、sons与new child构成归家诱惑，但ought thank him显示他也在把被迫退场改写成主动释放。",
55:"spoor/beast把调查比作tracking：线索能证明猎物可能存在，却还不能识别、定位和捕获。",
56:"经Dragonstone返家把retreat与最后调查合并，是Eddard试图在安全和unfinished duty间找到路线。",
57:"他已经把Littlefinger所称dagger当the Imp’s knife，说明争议归属在内心语言中仍易固化成事实。",
58:"Robert当前明确命令杀child，使Eddard重新评估过去“不可能”判断；这是更新模型，不是发现Robert涉案证据。",
61:"play their games表明辞职没有立即使他退出court信息环境；身份过渡期仍有被观察与利用的风险。",
67:"Littlefinger声称把高成功率方案换成低成功率方案；结果可能确实降低即时风险，但动机与后续仍由他自述。",
69:"他以expected outcome为自己辩护：formal vote支持谋杀，implementation design却让失败更可能；道德与策略被刻意分离。",
70:"Eddard抓住public words与private claim矛盾，拒绝因聪明效果自动相信善意动机。",
73:"rotten ice比喻认为court规则表面可站、内部已腐坏；noble splash同时赞美Eddard高尚与预言其失败。",
77:"brothel邀请在Eddard即将离城时出现，正对应Jory调查Jon与Stannis曾访问的地点，迫使他在撤退前再做一次选择。",
}

STAGES = [
(1,14,"Robert要求杀死pregnant Daenerys、胎儿与Viserys；Eddard从情报不确定、海洋距离和道德污名三方面反对。"),
(15,33,"Varys、Renly、Pycelle与Littlefinger以realm安全支持刺杀，Barristan独自站在Eddard一边；投票后Robert转向执行。"),
(34,46,"council讨论Jorah、poison与Faceless Men；Eddard拒绝盖seal、摘下Hand badge离场，但刺杀规划没有停。"),
(47,59,"Eddard秘密安排daughters先行并找船返北，同时想经Dragonstone问Stannis，在归家渴望与未完调查间摇摆。"),
(60,77,"Littlefinger来访，声称用低成功率悬赏替代Faceless Men间接保护Daenerys，继而以brothel线索诱使Eddard暂缓离开。"),
]

BACKGROUNDS = {
2:"**Daenerys现状：** 十四岁、与Khal Drogo成婚并怀孕；性别尚由情报声称为boy，并非本章直接医学确认。",
7:"**Jorah Mormont：** Daenerys身边exile knight，向Varys传递消息并希望获得royal pardon，因此消息源有利益动机。",
11:"**narrow sea：** Westeros与Essos之间海域；Dothraki强于陆战，尚无本章可见的大规模渡海能力。",
17:"**Trident旧事：** Barristan为Aerys一方重伤后，Robert拒绝按Roose建议杀死他，反而派maester救治。",
19:"**Rebellion道德记忆：** Aerys阵营曾涉及对Stark及children的暴行；Eddard以此衡量胜利者当前行为。",
28:"**council分歧：** Renly、Varys、Pycelle、Littlefinger支持行动；Eddard与Barristan反对。Robert拥有最终命令权。",
35:"**Vaes Dothrak／tears of Lys：** sacred city按Dothraki custom不得拔blade流血；Varys因此建议据称clear、sweet且不留痕迹的毒药，也曾称Jon死于此毒。本段Pycelle明显警觉。",
42:"**Hand badge：** ornate silver hand象征office，由Robert任命、Jon曾亲自为Eddard佩上；辞还即拒绝继续任职。",
44:"**Faceless Men：** Braavos的神秘刺客组织，以高昂价格闻名；本章只讨论雇佣可能。",
51:"**迫近消息：** Yoren已告诉Eddard Catelyn拘捕Tyrion，且消息正在向Casterly Rock传播。",
56:"**Dragonstone：** Stannis所在的古Targaryen island fortress；他曾与Jon共同调查且未回应返council请求。",
67:"**执行方案：** council最终不雇Faceless Men，而由Varys散布“杀Daenerys者获lordship”的悬赏。",
77:"**brothel线索：** former stablehand称Jon与Stannis曾同去一家brothel；Jory一直未找到具体地点。",
}

EXTRA_VOCAB = [
("plead","/pliːd/","v.","恳求；申辩","Ned to Robert"),("thunderclap","/ˈθʌndərklæp/","n.","霹雳般巨响","fist on table"),("wring","/rɪŋ/","v.","绞扭双手","Varys gesture"),("miscarry","/ˌmɪsˈkæri/","v.","流产","risk branch"),("wean","/wiːn/","v.","使断奶","Aegon comparison"),("unctuous","/ˈʌŋktʃuəs/","adj.","油滑谄媚的","Varys smile"),("qualm","/kwɑːm/","n.","道德疑虑；不安","Ned’s objection"),("grievous","/ˈɡriːvəs/","adj.","严重痛苦的","news / wounds"),("caprice","/kəˈpriːs/","n.","反复无常；任性","gods"),("stifle","/ˈstaɪfəl/","v.","强忍；压住","yawn"),("aghast","/əˈɡæst/","adj.","惊骇的","Barristan"),("quibble","/ˈkwɪbəl/","v.","在细枝末节上争辩","honor"),("flagon","/ˈflæɡən/","n.","大酒壶","Robert throws it"),("defiance","/dɪˈfaɪəns/","n.","公开违抗","Ned refuses"),("clasp","/klæsp/","n.","扣饰","Hand badge"),("turn on one’s heel","/tɜːrn ɑːn wʌnz hiːl/","phr.v.","猛然转身离开","council exit"),("oppressive","/əˈpresɪv/","adj.","沉闷压迫的","weather"),("trifle","/ˈtraɪfəl/","n.","一点点","less unclean"),("fortnight","/ˈfɔːrtnaɪt/","n.","两周","travel preparation"),("spoor","/spʊr/","n.","兽迹；踪迹","murder clues"),("appointment","/əˈpɔɪntmənt/","n.","陈设设备（复数）","ship cabins"),("saunter","/ˈsɔːntər/","v.","悠闲踱入","Littlefinger"),("lamprey","/ˈlæmpri/","n.","七鳃鳗","pie"),("suckling pig","/ˈsʌklɪŋ pɪɡ/","n.","乳猪","dinner"),("wroth","/rɔːθ/","adj.","愤怒的（古风）","Robert"),("insolence","/ˈɪnsələns/","n.","无礼傲慢","Robert’s charge"),("ingratitude","/ɪnˈɡrætɪtuːd/","n.","忘恩负义","Robert’s charge"),("blithely","/ˈblaɪðli/","adv.","若无其事地；轻快地","Littlefinger"),("botch","/bɑːtʃ/","v./n.","笨拙搞砸","assassination"),("perchance","/pərˈtʃæns/","adv.","或许；碰巧（古风）","evenfall invitation"),("evenfall","/ˈiːvənfɔːl/","n.","黄昏","brothel trip"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def main():
    blocks = extract_range(324, 331, "EDDARD", "CH33")
    write_chapter(
        out=OUT, chapter=33, pov="EDDARD", page_start=324, page_end=331,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在预防性暴力的证据门槛、council责任、Eddard道德原则与撤离风险。",
        vocab=VOCAB,
        guide="small council收到Jorah经Varys传来的Daenerys怀孕消息。Robert把可能出生并渡海的Targaryen–Dothraki heir视为悬颈axe，要求杀死Daenerys、胎儿与Viserys；Eddard则把威胁称为二十年外的shadow，并坚持Rebellion若复制child murder便失去道德意义。Renly、Varys、Pycelle和Littlefinger支持刺杀，只有Barristan与Eddard反对。Eddard拒绝给命令加Hand seal，当场辞职，但门未关前council已继续讨论执行者。回Tower后他秘密筹划带daughters先走、乘船经Dragonstone问Stannis。Littlefinger随后声称自己用低成功率的lordship悬赏替代Faceless Men，效果可能降低即时风险，但动机未经证明；他又以Jory未找到的brothel线索让Eddard面临离城前最后一次调查诱惑。",
        people=[
            ("Eddard Stark","本章视角；反对刺杀Daenerys、辞去Hand并秘密筹划撤离"),
            ("Robert Baratheon","因潜在Targaryen–Dothraki heir下令预防性刺杀，与Eddard决裂"),
            ("Varys","提供Jorah情报、支持刺杀并建议tears of Lys与公开悬赏方案"),
            ("Barristan Selmy","唯一在表决中支持Eddard的councillor，强调战场honor"),
            ("Pycelle","以一人之死避免万人战争的后果论支持刺杀"),
            ("Renly Baratheon","认为早年就应杀死Viserys和Daenerys，并提出Jorah想要pardon"),
            ("Petyr Baelish","公开支持steel kiss，私下称自己用较低成功率方案减少Daenerys风险"),
            ("Vayon Poole","奉命秘密筹备daughters先行与快速北航船只"),
        ],
        terms=[
            ("preventive killing","以未来可能威胁为理由，在威胁尚未实现前杀死目标"),
            ("Hand’s seal","Hand对royal order的行政认证；Eddard拒绝使其office参与刺杀"),
            ("tears of Lys","可伪装自然死亡的罕见毒药，Varys同时把它与Jon死亡联系"),
            ("Faceless Men","Braavos高价刺客组织，council因成本放弃雇佣"),
            ("spoor","Eddard对现有Jon murder线索的比喻：看见踪迹，不等于看见或抓住真凶"),
        ],
        synthesis="Chapter 33把“为realm做必要的恶”放到证据与责任两道检验中。Robert一方把未来boy、成年、渡海、战争连成必然链，再用万人可能死亡为现在杀死girl辩护；Eddard则拆开每一个if，并要求下令者亲自面对受害者。表决结果说明道德少数无法靠纯粹正确阻止国家机器，辞职更保护了Eddard不成为共犯，却没有直接保护Daenerys。Littlefinger的私下解释又展示另一种宫廷伦理：公开顺从policy，暗中通过执行效率改变结果。其策略可能有效，但他是否为girl着想、是否还有别的目的，文本没有证明。",
        contrasts=[
            "**child／dragonspawn：** Eddard与Robert的命名分别唤起无辜与继承威胁。",
            "**shadow／axe：** 同一未来风险被描述成遥远投影或已悬颈武器。",
            "**battlefield honor／secret poison：** Barristan接受公开敌战，拒绝母腹刺杀。",
            "**个人辞职／机器继续：** Eddard离场后执行讨论几乎没有停顿。",
            "**Winterfell归家／unfinished duty：** 安全、家庭与snow吸引他，Jon truth和Stannis又拉住他。",
            "**public support／private mitigation：** Littlefinger在表决中赞成，却称自己在执行层降低成功率。",
        ],
        questions=[
            "lordship悬赏会吸引谁尝试刺杀Daenerys，是否真比Faceless Men更容易失败？",
            "Robert冷静后会撤回对Eddard的威胁，还是Catelyn/Tyrion消息会让冲突升级？",
            "Eddard能否在castle eyes and ears发现前带Sansa与Arya安全离开？",
            "Littlefinger为何此刻主动提供brothel位置，他希望Eddard发现什么？",
        ],
        extraction_notes="PDF pp.324–331共77段；正确合并3处跨页续段：pp.324–325、327–328与329–330。逐页复核未发现额外分页误切。",
    )
    print(f"Wrote Chapter 33 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
