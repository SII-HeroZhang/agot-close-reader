#!/usr/bin/env python3
"""Build Chapter 46 (DAENERYS) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter45_reader import VOCAB as BASE_VOCAB

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"/"AGOT_逐章精读"

S={
1:"Drogo把刚取出的raw stallion heart放到Daenerys面前，bloodriders持stone knives跪在尸体旁。",
2:"Daenerys摸着孕腹，在dosh khaleen注视下以blood of dragon鼓励自己咬下heart。",
3:"她忍住温血与恶心吞咽；Dothraki相信吃完整颗heart才能让son强壮，失败预示stillbirth、畸弱或female。",
4:"handmaids事先用半凝blood、dried horseflesh和禁食训练她适应味道与份量。",
5:"Vaes Dothrak禁steel，Daenerys只能用牙与指甲撕muscle，忍住胃部翻涌继续。",
6:"Drogo硬脸俯视；Daenerys每次力竭便看他，反复chew and swallow，最后似乎看见他的pride。",
7:"她终于吞下最后部分，手脸黏血，才重新看向dosh khaleen。",
8:"Daenerys用练习多日的Dothraki宣布prince正在体内骑行。",
9:"独眼老crone举臂回应prince is riding。",
10:"其余women齐声宣告是strong boy。",
11:"bells、warhorn、chant与brazier香烟启动预言仪式；Dothraki把stars看作fire horses。",
12:"烟升chant止，crone闭眼看future，全场在lake与torch声中静候。",
13:"Drogo握Daenerys手臂时手指紧张，显示强大khal也畏惧dosh khaleen预言。",
14:"crone睁眼说看见胎儿面孔并听见hooves thunder。",
15:"其他women回声重复thunder。",
16:"crone预言prince迅疾、khalasar无数、敌人恐惧，将成为stallion who mounts world。",
17:"围观者反复高喊这一title，声音响彻night。",
18:"独眼crone问这位world-stallion叫什么。",
19:"Daenerys站起宣布Rhaego，保护性摸孕腹，Dothraki以roar重复name。",
20:"Drogo领她出pit，dosh khaleen procession随后；叙述说明每名crone曾是khaleesi，widowed后被强制留城统治nation。",
21:"其后是其他khals、wives、leaders、handmaids、servants、slaves；沿godsway的stolen gods在黑暗中注视。",
22:"Drogo用Daenerys教的Common Tongue问Rhaego含义，虽学得快但口音令Jorah、Viserys听不懂。",
23:"Daenerys说以未曾见过的brother Rhaegar命名，Jorah称其last dragon。",
24:"Drogo似乎微笑，以生涩Common Tongue认可名字并称她moon of life。",
25:"队伍到Womb of the World湖；传说first man从湖中骑first horse出现。",
26:"本段含十四岁Daenerys在公众仪式中的裸露与露骨身体描写；不逐字复录。",
27:"本段含十四岁Daenerys被成人伴侣性化注视及露骨身体/性唤起描写；不逐字复录。",
28:"本段含成人Drogo与十四岁Daenerys的露骨性行为；不逐字复录。",
29:"仪式后Drogo整装并叫horses，Cohollo扶Daenerys上silver，两人月下沿godsway疾驰。",
30:"Drogo hall卷起roof silk、三座firepit高燃；Daenerys骑入时全场评论孕腹并高呼world-stallion。",
31:"drums、horns、dancers、fruit和醉men充满宴会，但sacred city禁blade与bloodshed。",
32:"Drogo居high bench，Jommo、Ogo与各bloodriders、wives按rank就座。",
33:"Daenerys下马后寻找Viserys，却没看见其显眼银发与破旧服装。",
34:"她在低位席间没找到brother，却见Jorah因剑术获尊重座位，召他到自己身旁。",
35:"Daenerys拍cushion请Jorah坐下聊天。",
36:"Jorah称受honor，坐下取slave盘中fig。",
37:"Daenerys问Viserys为何还未来feast。",
38:"Jorah说早晨见他要去Western Market找wine。",
39:"Daenerys知道Viserys常去bazaar同caravan traders喝wine，似乎觉得他们比她更congenial。",
40:"Jorah说Viserys还想从caravan sellswords招army，边说边吃blood pie。",
41:"Daenerys担心他无gold、会被betray，并责Jorah未履sworn sword保护。",
42:"Jorah提醒Vaes Dothrak不许带blade或shed blood。",
43:"Daenerys指出仍有人死亡，traders可让eunuchs用silk勒死thieves以绕过no blood规则。",
44:"Jorah说希望Viserys别偷东西，随后透露他曾想拿dragon eggs，自己以砍手阻止。",
45:"Daenerys震惊，强调eggs是Illyrio给自己的bride gift且只是stone。",
46:"Jorah解释dragon eggs比gems更稀有，卖掉三枚足以买大量sellswords。",
47:"Daenerys仍说若brother需要便应给他，他只需开口，因为他是brother与true king。",
48:"Jorah只认可brother身份，没有认可true king。",
49:"Daenerys解释父母、Rhaegar早亡，只有Viserys给她家族names与陪伴，他曾是全部。",
50:"Jorah说那只是once；如今她属于Dothraki，womb中是world-stallion。",
51:"Daenerys因horse heart拒绝mare’s milk，问prophecy含义。",
52:"Jorah解释是古代khal of khals预言，将统一Dothraki、骑至world ends，把所有人当herd。",
53:"Daenerys小声回应，并说自己给他取名Rhaego。",
54:"Jorah说此名会令Usurper血冷。",
55:"Doreah急拉Daenerys手肘，低声提醒brother来了。",
56:"Daenerys看见Viserys醉步走近，判断wine给了他某种假courage。",
57:"Viserys穿污损scarlet silk、破旧boots并佩longsword；Dothraki怒视禁weapon，music紧张停顿。",
58:"Daenerys恐惧，命Jorah阻止并愿给dragon eggs换Viserys放弃冲突。",
59:"Viserys醉喊自己是king、辱骂Daenerys并要求feast服从。",
60:"他在firepit旁看五千Dothraki，虽多数听不懂Common Tongue，醉态一望即知。",
61:"Jorah低声劝并拉他手臂，Viserys挣脱，声称无人可未经许可touch dragon。",
62:"Daenerys焦虑看high bench，Jommo与Ogo因Drogo的话大笑。",
63:"笑声吸引Viserys，他近乎礼貌称自己来feast，踉跄想上high bench。",
64:"Drogo指向后方低位席；Jorah翻译Viserys不配high bench。",
65:"Viserys看到unblooded boys、老人、disabled等最低席，宣称不适合king。",
66:"Drogo用新学Common Tongue叫他Sorefoot King，并命给Cart King拿cart。",
67:"五千人哄笑；Jorah与Viserys扭打，最终把他撞倒。",
68:"Viserys拔出sword。",
69:"借来的blade在fire中红亮；他挥剑威胁，Dothraki从四面咒骂。",
70:"Daenerys无声恐叫，因为知道sacred city拔剑意味着什么。",
71:"Viserys因她声音终于看见她，挥剑穿过无人阻拦的通道逼近。",
72:"Daenerys求他丢blade、共享food drink，并再次愿交dragon eggs。",
73:"Jorah叫Viserys听从，否则会害死所有人。",
74:"本段含Viserys以剑对十四岁Daenerys胸腹实施性化威胁，并明确威胁剖出胎儿；不逐字复录。",
75:"Jhiqui哭着不敢translate，怕Drogo严惩；Daenerys反而安慰她并决定亲自翻译。",
76:"Daenerys词汇有限但说清威胁；Drogo下high bench，Viserys开始畏缩问其回应。",
77:"hall寂静只闻Drogo hair bells；Daenerys冷透，翻译说他会得到令众人颤抖的splendid golden crown。",
78:"Viserys误信字面，放低sword微笑说只要承诺之物；这smile日后最令Daenerys心痛。",
79:"Daenerys靠住Drogo；bloodriders制伏Viserys、折腕夺剑，他仍喊自己是dragon、必须被crowned。",
80:"Drogo解下gold medallion belt，让slaves倒空stew pot、将gold放入火中熔化。",
81:"Viserys面对死亡尖叫挣扎，Jorah到Daenerys旁劝她转身。",
82:"Daenerys拒绝，双臂保护孕腹。",
83:"Viserys最后向sister求救，请她让众人停下。",
84:"Drogo用mittens取出半熔gold pot，宣布给Cart King crown并倒在Viserys头上。",
85:"Viserys惨叫、动作逐渐停止；molten gold使silk冒烟，却遵守不spill blood的字面禁令。",
86:"Daenerys异常平静地判断他不是dragon，因为fire不能杀dragon。",
}
SUMMARIES=[S[i] for i in range(1,87)]

KEY_NOTES={
1:"heart steaming把生命刚离体的时间感置于仪式开端；torch使blood变black，神圣与恐怖同时出现。",
2:"must not flinch是公开权力测试：Daenerys不只是进食，也在dosh khaleen、Drogo与khalasar前证明khaleesi资格。",
3:"female与stillborn/deformed并列，清楚暴露Dothraki预兆体系的性别贬抑；这是文化信念，不是医学事实。",
4:"成功看似瞬间意志奇迹，实则由handmaids数月训练、饮食适应与禁食共同准备。",
5:"no steel规则让teeth/nails成为仪式工具，身体本身必须承担文化纯洁性要求。",
6:"chewed and swallowed三次重复模拟机械坚持；Drogo可能的pride仍用thought/glimpsed保留Daenerys不确定。",
8:"背诵练习显示语言能力也是政治表演基础；正确一句Dothraki让她主动宣布而非被他人命名。",
11:"stars as fire horses把天象纳入horse culture，prophecy不是孤立迷信，而嵌入整个宇宙想象。",
12:"关闭视觉才能peer future形成paradox；全场静音把crone interpretation塑成唯一权威声音。",
13:"Drogo fingers泄露的fear比face更可读；powerful leader仍受religious institution约束。",
16:"预言以敌妻血泪赞美conquest，world-stallion既是统一希望也是对外部people的灾难想象。",
19:"Rhaego把未见brother Rhaegar、未来son与Targaryen restoration连结；protective touch同时有母性与政治意味。",
20:"dosh khaleen拥有超越khals的authority，却来自widow被强制留城；制度把女性个人自由兑换为集体权威。",
21:"stolen heroes/dead gods让Vaes Dothrak成为被征服文化的仓库；monuments保存外形，却失去原社区。",
22:"Daenerys教Drogo Common Tongue形成双向学习，不再只是她单方面被迫适应Dothraki。",
23:"Rhaegar身份来自Jorah转述与Viserys故事；Daenerys用name继承一个从未亲见的family past。",
24:"Dan Ares wife展示Drogo仍在拆分陌生音节；不完美语言却承担亲密认可。",
25:"Womb of World与pregnancy呼应，把个人孕腹置入Dothraki creation myth。",
26:"本段涉及未成年公开裸露与露骨身体细节，不逐字复录。其叙事功能是通过water cleansing完成blood-to-sacred transition。",
27:"本段含成人对十四岁Daenerys的露骨性化注视与唤起，不复录。公开仪式与private sexuality在群体目光下无缝连接。",
28:"本段含成人与十四岁未成年人的露骨性行为，不逐字复录。文本把prophecy title带入行为语言，强化son、sex与conquest绑定。",
30:"hall roof开放让moon延续ritual space；群众对孕腹的喊声把Daenerys body变成公共政治象征。",
31:"no blade/no blood并不等于no violence；后文Viserys会误把规则字面当绝对安全。",
34:"Dothraki respect Jorah sword prowess，即使此城禁sword；能力的社会价值超出当下能否使用。",
39:"Viserys转向traders不是建立独立外交，而是从sister/khalasar失势后寻找愿听其king story的新观众。",
41:"Daenerys仍以sworn sword规则要求Jorah保护Viserys，说明她尚在努力维持brother king架构。",
43:"silk strangling是legal loophole：禁止shed blood被遵守字面却不阻止杀人，预演gold crown。",
44:"Jorah以威胁阻止egg theft，保护Daenerys property，却没有先告诉她；保护与替她决定边界重叠。",
47:"Daenerys第一反应仍是主动让渡财富，brother/true king的旧忠诚压过property betrayal。",
48:"Jorah只重复brother，沉默删去true king；这是一种精确而不直接冒犯的否认。",
49:"He is all I have用过去孤立解释现在忠诚：Viserys既施虐，也是她童年唯一family archive与companion。",
50:"Once/no longer把身份支点从blood brother转向Dothraki husband、child和title；也可能推动危险情感切断。",
52:"all people as herd揭示prophecy不是单纯伟大领导，而把world population降为被驱赶所有物。",
56:"wine提供的something that passed for courage明确否定其真正勇气，把醉意写成冒险冲动。",
57:"scarlet silks与longsword试图恢复king appearance，却因污损、禁令和集体怒视反而凸显beggar status。",
59:"No one eats before king是他用旧court hierarchy向完全不承认该rank的社会发令，performative authority失效。",
60:"原自动提取在p.455–456把同段误切，已合并；听不懂words仍能读drunken body，非语言信息压过title。",
64:"Drogo不直接杀，先公开分配Viserys社会位置；羞辱从空间等级开始。",
65:"叙述用lowest of low复现Dothraki等级观；disabled与old被系统性贬低，精读不把此排序当客观价值。",
66:"Sorefoot/Cart King把Viserys此前步行受伤与乘cart的屈辱固化为公共称号，反夺其自封king语言。",
68:"极短句让blade crossing taboo成为不可逆转点；此前仍可能被escort away，此后整个hall必须回应。",
70:"Daenerys wordless cry显示语言训练在极端恐惧下短暂失效，也触发Viserys终于把她当目标。",
72:"她连续提供cushions、drink、food、eggs，尽量让他拥有不丢面子的退出路径。",
74:"本段含针对十四岁Daenerys胸腹与胎儿的性化身体威胁，不逐字复录。Viserys把她、eggs、fetus都当交易财产。",
75:"Daenerys在自己被blade威胁时安慰Jhiqui，显示khaleesi责任已从被保护者转向保护subordinate。",
77:"golden crown在语义上兑现Viserys demand，splendid/tremble同时隐藏致命双关；Daenerys已听懂结果。",
78:"smile之所以最sad，是Viserys最后一刻仍把promise fulfillment当作恢复自我故事，没有理解关系已彻底断裂。",
79:"the man who had been her brother把亲属身份转成过去式；不是生物关系消失，而是Daenerys内心不再承认原角色。",
80:"Drogo沉默熔gold把财富、promise与处刑工具合一；等待过程延长公开恐惧。",
81:"Jorah建议turn away提供保护选择，Daenerys拒绝见证；拒绝不等于无创伤。",
84:"crown从longed-for sovereignty变成execution device，是全章最残酷的literalization。",
85:"no blood spilled揭示sacred law被形式遵守而实质violence达到极端；与silk strangling完全同构。",
86:"Fire cannot kill a dragon是Daenerys用family myth处理brother death的逻辑：死亡反向证明Viserys从未配title。",
}

STAGES=[
(1,19,"Daenerys完成stallion-heart测试，dosh khaleen从smoke预言其son为统一Dothraki、征服world的stallion，并命名Rhaego。"),
(20,30,"procession解释dosh khaleen widow authority，Drogo学习Common Tongue；Womb of World cleansing后众人回hall公开庆祝pregnancy。"),
(31,50,"feast中Daenerys寻找Viserys；Jorah揭露他想卖dragon eggs招sellswords，Daenerys仍以唯一family为由愿意给他。"),
(51,70,"Jorah解释prophecy时醉酒Viserys佩禁剑闯入，拒绝低位席、受全场嘲笑并最终拔blade触犯sacred rule。"),
(71,86,"Viserys以Daenerys与fetus逼Drogo兑现crown；Daenerys翻译后Drogo以molten gold处刑，Daenerys由death否定其dragon身份。"),
]

BACKGROUNDS={
1:"**stallion-heart rite：** pregnant khaleesi公开吃完整颗raw stallion heart，以Dothraki信仰为胎儿获取strength与omens。",
3:"**文化／医学区分：** heart与胎儿性别、畸形、stillbirth间的因果是Dothraki belief，不是医学事实；female被视作bad omen反映性别等级。",
8:"**khalakka：** khal之子、prince；Dany练习Dothraki句子公开确认胎儿male身份。",
11:"**dosh khaleen：** deceased khals widows组成的wise-women council，居Vaes Dothrak并拥有连khals也尊重的预言与政治权威。",
16:"**stallion who mounts world：** 古预言中的khal of khals，将统一所有Dothraki并把world people视为herd。",
20:"**widow rule：** khaleesi在khal死后必须加入dosh khaleen，不以本人意愿为转移；权威与强制同时存在。",
21:"**godsway：** Vaes Dothrak中央grass road，两侧立有Dothraki从被征服people带来的heroes与gods。",
25:"**Womb of World：** Dothraki creation lake，传说first man骑first horse由此出现。",
26:"**安全说明：** 本段含十四岁Daenerys公开裸露与露骨身体描写；保留cleansing仪式作用与定位，不复录细节。",
27:"**安全说明：** 本段含成人对十四岁Daenerys的露骨性化注视与身体反应；不逐字复录。",
28:"**安全说明：** 本段含成人Drogo与十四岁Daenerys的露骨性行为；保留prophecy、权力与仪式衔接分析。",
31:"**Vaes Dothrak law：** sacred city内禁止携带blade、shed blood；规则可被不流血的杀法绕过。",
44:"**dragon eggs：** Illyrio给Daenerys的bride gifts，虽已石化仍极稀有昂贵，可兑换大批sellswords。",
49:"**family history：** Daenerys出生时mother死亡，Aerys与Rhaegar更早死；Viserys抚养并讲述她不曾亲见的family。",
57:"**Viserys sword：** Illyrio借给他用于kingly appearance；在Vaes Dothrak佩带本身已是严重禁忌。",
66:"**Khal Rhaggat：** Dothraki称Viserys的Sorefoot/Cart King绰号，源自他被迫步行与乘cart的屈辱。",
74:"**安全说明：** 本段含针对十四岁Daenerys与胎儿的性化身体暴力威胁；保留事件性质、动机与定位，不复录原句。",
85:"**formal compliance：** molten gold杀人却不流血，使Drogo在字面上没有违反sacred-city bloodshed ban。",
}

EXTRA_VOCAB=[
("stallion","/ˈstæliən/","n.","成年公马","heart ritual"),("crone","/kroʊn/","n.","老妪（常带贬义或神秘色彩）","dosh khaleen"),("flint","/flɪnt/","n.","燧石","eyes simile"),("stringy","/ˈstrɪŋi/","adj.","多筋难嚼的","heart flesh"),("gag","/ɡæɡ/","v.","作呕；噎住","blood taste"),("retch","/retʃ/","v.","干呕；呕吐","omen"),("stillborn","/ˈstɪlbɔːrn/","adj.","死产的","child"),("clotted","/ˈklɑːtɪd/","adj.","凝结成块的","blood or milk"),("confines","/ˈkɑːnfaɪnz/","n.","范围；界限","sacred city"),("roil","/rɔɪl/","v.","翻腾；搅动","stomach"),("medallion","/məˈdæliən/","n.","大奖章形金属饰片","gold belt"),("clangor","/ˈklæŋər/","n.","连续铿锵声","bells"),("brazier","/ˈbreɪʒər/","n.","火盆","sacred smoke"),("ascend","/əˈsend/","v.","上升","smoke"),("wavery","/ˈweɪvəri/","adj.","颤抖不稳的","voice"),("rend","/rend/","v.","撕裂","grief"),("cadence","/ˈkeɪdəns/","n.","有节奏的拍子","procession"),("brood","/bruːd/","v.","阴沉笼罩；沉思","stolen gods"),("fringe","/frɪndʒ/","n.","边缘带","reeds"),("gingerly","/ˈdʒɪndʒərli/","adv.","小心翼翼地","enter water"),("curdled","/ˈkɜːrdəld/","adj.","凝乳状的","mare’s milk"),("conspicuous","/kənˈspɪkjuəs/","adj.","显眼的","Viserys"),("frayed","/freɪd/","adj.","磨损起毛的","rugs"),("esteem","/ɪˈstiːm/","v.","敬重","sword prowess"),("congenial","/kənˈdʒiːniəl/","adj.","意气相投的；合意的","traders"),("wisp","/wɪsp/","n.","一缕；细束","silk"),("opal","/ˈoʊpəl/","n.","蛋白石","fire opal"),("prophecy","/ˈprɑːfəsi/","n.","预言","khal of khals"),("lurch","/lɜːrtʃ/","n./v.","踉跄；猛晃","drunken step"),("scabbard","/ˈskæbərd/","n.","剑鞘","longsword"),("presume","/prɪˈzuːm/","v.","擅自；胆敢","eat without king"),("guffaw","/ɡəˈfɔː/","v.","哄然大笑","Khal Ogo"),("grapple","/ˈɡræpəl/","v.","扭打","Jorah and Viserys"),("brusque","/brʌsk/","adj.","简短生硬的","Drogo reply"),("chime","/tʃaɪm/","v.","发出清脆铃声","hair bells"),("ornate","/ɔːrˈneɪt/","adj.","华丽繁复的","medallions"),("mitten","/ˈmɪtən/","n.","连指手套","horsehair"),("upend","/ʌpˈend/","v.","倒置；掀翻","pot"),("smolder","/ˈsmoʊldər/","v.","闷烧冒烟","silk"),("literalization","/ˌlɪtərələˈzeɪʃən/","n.","将比喻按字面实现","golden crown"),
]
VOCAB=BASE_VOCAB+EXTRA_VOCAB

def extract_blocks():
    blocks=extract_range(449,458,"DAENERYS","CH46")
    # p.453 continues p.452's sentence with capitalized “Dany”.
    blocks[29]["text"]=str(blocks[29]["text"])+" "+str(blocks[30]["text"])
    blocks[29]["end_page"]=blocks[30]["end_page"]
    del blocks[30]
    # p.456 continues p.455's sentence with capitalized “Dothraki”.
    blocks[59]["text"]=str(blocks[59]["text"])+" "+str(blocks[60]["text"])
    blocks[59]["end_page"]=blocks[60]["end_page"]
    del blocks[60]
    for order,block in enumerate(blocks,1):
        block["order"]=order
        block["id"]=f"CH46-P{int(block['page']):03d}-{order:03d}"
    blocks[25]["text"]="[原文含十四岁Daenerys在公众仪式中的裸露与露骨身体描写，此处不逐字复录。请参见源 PDF p.452 对应段落。]"
    blocks[26]["text"]="[原文含成人Drogo对十四岁Daenerys的露骨性化注视、身体反应与脱衣描写，此处不逐字复录。请参见源 PDF p.452 对应段落。]"
    blocks[27]["text"]="[原文含成人Drogo与十四岁Daenerys之间的露骨性行为，此处不逐字复录。请参见源 PDF p.452 对应段落。]"
    blocks[73]["text"]="[原文含Viserys以剑对十四岁Daenerys胸腹实施性化身体威胁，并明确威胁其胎儿；此处不逐字复录。请参见源 PDF p.457 对应段落。]"
    return blocks

def main():
    blocks=extract_blocks()
    write_chapter(
        out=OUT,chapter=46,pov="DAENERYS",page_start=449,page_end=458,
        blocks=blocks,summaries=SUMMARIES,key_notes=KEY_NOTES,stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Dothraki ritual authority、prophecy、Daenerys身份转移与Viserys触犯sacred law。",
        vocab=VOCAB,
        guide="Daenerys以数月准备和公开自控完成stallion-heart仪式，dosh khaleen据smoke宣告腹中Rhaego将成为统一Dothraki、征服世界的stallion who mounts the world。这个预言既提升她的政治地位，也把她的身体、胎儿与future conquest变成全khalasar公共象征。Womb of the World后的未成年露骨段落使用安全占位。宴会上，Jorah揭露Viserys企图偷dragon eggs买sellswords；Daenerys仍愿把eggs给唯一的童年family。醉酒Viserys却佩禁剑闯入、要求high honor，并以Daenerys与胎儿逼Drogo兑现crown。Drogo最终用molten gold在不流血的字面规则内处刑。Daenerys把死亡解释为‘fire不能杀dragon’，完成对Viserys自封身份的心理否定。",
        people=[
            ("Daenerys Targaryen","本章视角；约十四岁pregnant khaleesi，完成heart rite并见证Viserys死亡"),
            ("Khal Drogo","Daenerys adult husband与khal，认可Rhaego预言并以molten gold处刑Viserys"),
            ("Viserys Targaryen","Daenerys brother；醉酒佩禁剑闯宴，以sister和fetus索要crown"),
            ("Rhaego","Daenerys未出生son，以Rhaegar命名并被预言为stallion who mounts world"),
            ("dosh khaleen","widowed khaleesi组成的wise-women council，主持仪式并宣告prophecy"),
            ("Ser Jorah Mormont","Daenerys adviser；阻止egg theft、解释prophecy并试图制止Viserys"),
            ("Jhiqui / Irri / Doreah","Daenerys handmaids，协助语言、仪式、照护与危机翻译"),
            ("Qotho / Haggo / Cohollo","Drogo bloodriders，制伏Viserys并执行khal命令"),
        ],
        terms=[
            ("stallion-heart rite","pregnant khaleesi吞食raw stallion heart以求male child强壮与吉兆的仪式"),
            ("dosh khaleen","居Vaes Dothrak、由deceased khals widows构成的最高女性宗教政治机构"),
            ("stallion who mounts the world","预言中统一Dothraki并把世界人群视作herd的khal of khals"),
            ("Womb of the World","Dothraki first-man/first-horse creation myth的圣湖"),
            ("Khal Rhaggat","Viserys的Dothraki绰号，意为Sorefoot/Cart King"),
        ],
        synthesis="Chapter 46以三种‘兑现’组织权力转移。Daenerys兑现仪式要求：她依靠handmaids训练而非纯粹天命吃完heart，于是获得prophecy与公共地位。Viserys要求Drogo兑现golden crown，却把妹妹、eggs和未出生child都当作买卖标的；Drogo用最残酷的字面方式兑现，既满足crown语言又绕过no blood law。Daenerys最终兑现自己的dragon判断：曾经由Viserys垄断的family myth被她拿来否定Viserys。这里的成长伴随严重暴力与情感切断，不能只当‘爽快逆袭’。Viserys长期施虐、当场威胁是真实的；他最后微笑、求救与Daenerys事后被那smile刺痛也同样真实。",
        contrasts=[
            "**个人身体／公共prophecy：** Daenerys独自吞咽，结果却被整个khalasar当作征服未来。",
            "**widow authority／widow compulsion：** dosh khaleen极有权威，却由不得拒绝的终身安排组成。",
            "**no blood law／极端杀人：** 禁令约束形式，不阻止silk strangling或molten gold。",
            "**brother and true king／brother only：** Daenerys仍维护双重身份，Jorah精确删去后者。",
            "**promised crown／molten crown：** Viserys的王权符号按字面成为死亡工具。",
            "**dragon claim／fire death：** Daenerys用Viserys自己的myth标准反向取消其身份。",
        ],
        questions=[
            "Rhaego预言会如何改变Drogo khalasar与其他khals对Daenerys的态度？",
            "Daenerys失去最后一个blood-family companion后会如何重建Targaryen identity？",
            "dragon eggs将继续只是昂贵stones，还是具有Viserys未理解的其他意义？",
            "Viserys之死会如何影响Jorah对Daenerys和Targaryen restoration的选择？",
            "stallion-who-mounts-world预言究竟会以何种方式被理解或实现？",
        ],
        extraction_notes="PDF pp.449–458校勘后共86段。自动提取曾把p.452末尾As与p.453开头Dany rode…误切，并把p.455末尾faces of the与p.456开头Dothraki误切，均已合并。校勘后共8处跨页续段：pp.449–450、450–451、451–452、452–453、453–454、455–456、456–457与457–458。第26–28段及第74段涉及未成年裸露、露骨性内容或性化身体威胁，保留定位与分析但以安全占位替代原文。",
    )
    print(f"Wrote Chapter 46 with {len(blocks)} paragraphs")

if __name__=="__main__":
    main()
