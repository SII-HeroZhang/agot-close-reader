#!/usr/bin/env python3
"""Build Chapter 37 (BRAN) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter36_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"轻雪中Bran骑在马上等portcullis升起，努力压住第一次出城的紧张。",2:"Robb问他是否ready。",3:"Bran点头隐藏fear，决心像knight般骄傲骑出fall后一直未离开的Winterfell。",4:"Robb先骑过gate。",5:"Bran用声音和触碰让特训filly Dancer前行；oversize saddle与两周独骑练习使他逐渐大胆。",6:"Summer、Grey Wind、Theon、四名guards、Joseth和骑donkey的Luwin随行；Bran虽想兄弟独处，成人坚持医疗保护。",7:"队伍穿过大多空置的winter town；天气转冷后farmer families会迁入，long summer终结已近。",8:"villagers已渐习惯direwolves，对boys跪礼，Robb以lordly nod回应。",9:"Bran无法夹马，起初随sway不稳；高背saddle与straps支撑后，节奏变自然、焦虑转成笑容。",10:"Theon当街向Kyra调情，并开始讲带性暗示的成人故事。",11:"Robb提醒别让Bran听。",12:"Bran假装没听见，却感到Theon在笑；Robb喜欢Theon，Bran却始终不亲近他。",13:"Robb靠近夸Bran骑得好。",14:"Bran要求更快。",15:"Robb同意小跑，wolves与其余骑手追上。",16:"Dancer顺滑转入gallop，Bran赶上Robb并喊自己会骑了，感觉近似flying。",17:"Robb开玩笑怕比赛会输，却掩不住内心忧虑。",18:"Bran不想race，询问昨夜Summer howling。",19:"Robb说Grey Wind也不安，觉得wolves能感知某些事，又苦恼Bran太小难以告知全部。",20:"Bran强调自己已八岁、仅比十五岁小七年，且是Robb之后的Winterfell heir。",21:"Robb承认，随后说昨夜King’s Landing来raven，Luwin叫醒了他。",22:"Bran回顾Benjen失踪、Catelyn拘捕Tyrion、Lannister触发的身体恐惧和Robb向north发commands等一连串dark words。",23:"他仍希望新信来自Mother并宣布回家。",24:"Robb说Alyn来信：Jory、Wyl、Heward被Jaime杀死，并为他们祈祷。",25:"Bran像遭拳击，回忆Jory从小陪伴、追他爬roof和Great Hall玩笑，不懂为何有人杀他。",26:"Robb又说Eddard在fight中leg shattered、服milk of the poppy且不知何时醒；他握sword切换到Lord voice，保证不让此事被遗忘。",27:"Bran被语气吓得更深，问Robb要做什么；Theon此时赶到。",28:"Robb说Theon建议call the banners。",29:"Theon不笑，以blood for blood支持报复。",30:"Bran指出只有lord能call banners。",31:"Theon说若Eddard死，Robb就是Lord of Winterfell。",32:"Bran尖叫Eddard不会死。",33:"Robb安慰却说north honor已在自己手中，记得父亲要求为Bran与Rickon坚强，自己也almost man grown。",34:"Bran发抖想要Mother回来，并问Luwin是否也赞成call banners。",35:"Theon辱称maester像old woman般timid。",36:"Bran提醒Eddard与Catelyn一向听Luwin counsel。",37:"Robb坚持自己会听所有人。",38:"Bran骑行的joy像脸上snow融尽；过去会兴奋的war如今只带dread，他说冷、想回去。",39:"Robb说仍须找wolves，问能否再撑一会。",40:"Bran不愿在brother面前承认saddle sore风险，说能走和他一样久。",41:"兄弟离kingsroad进wolfswood寻找hunters，Theon与guards在后方说笑。",42:"林中感官让久困castle的Bran像首次重见熟悉世界，细察pine、leaves、musk、squirrel和spider web。",43:"后队越来越远，兄弟到stream时Bran流泪。",44:"Robb问怎么了。",45:"Bran想起Jory曾带自己、Robb、Jon来此钓trout。",46:"Robb也悲伤地记得。",47:"Bran说自己空手而Jon把fish给他，问是否还会再见Jon。",48:"Robb以Benjen曾来访类比，保证Jon也会来。",49:"stream水高流急，Robb往返牵Dancer过ford；喷雾让Bran一瞬觉得strong、whole并梦想再次climb trees。",50:"两只direwolves的howl先后从林中传来，Bran认出Summer。",51:"Robb判断它们kill成功，叫Bran原地等Theon等人，自己去带回。",52:"Bran想同行。",53:"Robb说独自更快，策马消失。",54:"Robb离开后woods仿佛合拢；雪、紧strap、湿冷手套与失去感觉的legs令Bran意识到自己独处不适。",55:"树叶声响起时，他以为是同伴，却出现ragged strangers。",56:"Bran紧张问候，立即看出他们非farmer/forester，也意识到自己富贵衣物显眼。",57:"最大bald man假装关怀他是否迷路。",58:"Bran说brother刚离开、guards将至，并发现前后共六人。",59:"grey-stubbled man盯上silver pin，嘲问guards保护的是什么。",60:"持长spear的高瘦woman称pin漂亮。",61:"bald man要近看。",62:"Bran从两人破烂black cloth认出Night’s Watch deserters，并记起Eddard说亡命者因必死而最危险。",63:"bald man伸手索要pin。",64:"短黄发woman又要horse，拔出锯齿knife命他下马；源页形容词印作fiat。",65:"Bran脱口说自己不能。",66:"Stiv抓住reins，威胁无论如何都要他下来。",67:"Osha注意Bran被strapped，认为他说不能可能是真的。",68:"Stiv拔dagger说可割断straps。",69:"短woman问他是否cripple。",70:"Bran被激怒，报出Brandon Stark身份并威胁让他们全死。",71:"grey-stubbled man笑说果然是Stark，只有Stark会在聪明人求饶时愚蠢威胁。",72:"短woman以针对八岁Bran的明确性化身体伤害威胁要求让他闭嘴；不逐字复录。",73:"Osha骂她愚蠢，认为Bran活着可作为Benjen blood送给Mance换取价值。",74:"Stiv拒绝回north，反问white walkers是否在乎hostage，随后割Bran thigh strap。",75:"刀锋也切开Bran腿；他看见blood却完全无pain，Stiv因此惊讶。",76:"Robb出现，要求对方放weapon，承诺quick painless death。",77:"Bran绝望中看到Robb骑马带elk carcass；威胁力度被其紧张破音削弱。",78:"grey man认出是brother。",79:"Hali嘲Robb是否真敢一对六。",80:"Osha劝Robb下马弃剑，以horse和venison换兄弟安全离开。",81:"Robb吹whistle，Grey Wind与Summer从雪枝下现身并growl。",82:"Hali惊叫wolves。",83:"Bran纠正是direwolves，并依据头、腿、snout等特征解释；Grey Wind muzzle已有fresh blood。",84:"Stiv轻蔑称dogs，想取wolfskins，下令攻击。",85:"Robb喊Winterfell冲锋，一剑杀axe man；Grey Wind扑倒grey deserter并拖入stream。",86:"Robb与Osha在水中交战，挡下多次spear thrust，趁她失衡骑马撞倒。",87:"Summer躲过Hali刀，咬住calf，再将其撞倒撕咬腹部。",88:"第六人逃跑，Grey Wind追上咬断腿筋并扑向throat。",89:"只剩Stiv；他割断Bran chest strap把人拉落，dagger抵喉，以杀Bran逼Robb退后。",90:"Robb立刻停马放低sword。",91:"Bran看见Summer继续攻击Hali、Osha爬向spear、Grey Wind逼近；Stiv要求叫回wolves。",92:"Robb命Grey Wind、Summer回来。",93:"Grey Wind回Robb，Summer仍守着Bran盯住Stiv，满嘴血而眼神燃烧。",94:"Osha用spear撑起；Bran闻到Stiv fear，Stiv命她杀wolves取sword。",95:"Osha拒绝靠近这些monsters。",96:"Stiv失去办法、手发抖，刀划出Bran颈血，转问Robb名字。",97:"Robb报自己是Winterfell heir。",98:"Stiv确认Bran是否其brother。",99:"Robb答yes。",100:"Stiv以Bran性命命Robb下马。",101:"Robb短暂犹豫后缓慢下马，仍持sword。",102:"Stiv再命他杀wolves。",103:"Robb不动。",104:"Stiv逼他在wolves与boy之间选择。",105:"Bran尖叫阻止，因为一旦wolves死，Stiv仍会杀两兄弟。",106:"Stiv扭Bran头发令他痛哭并命令闭嘴。",107:"林后弓弦低响，Theon的broadhead从Stiv胸口穿出。",108:"dagger离喉，Stiv倒进stream，blood随水流走。",109:"Eddard guards出现，Osha丢spear向Robb求mercy。",110:"guards被屠杀现场与wolves吓白；Summer返回尸体进食令Joseth呕吐，Luwin短暂震惊后立即检查Bran。",111:"Bran说腿被割却无感觉。",112:"Luwin检查时，Bran看到Theon持bow微笑，六箭备地却只用一箭；Theon称dead enemy很美。",113:"Robb引用Jon说Theon是ass，并威胁把他绑起来让Bran练箭。",114:"Theon说Robb应感谢自己救命。",115:"Robb逐项质问miss、只伤Stiv、惊动其手或误中Bran的风险，以及看不见breastplate的未知。",116:"Theon笑容消失，闷闷耸肩并逐支收箭。",117:"Robb转向guards，质问为何不紧跟。",118:"Quent尴尬解释先等Luwin donkey，随后欲言又止看向Theon。",119:"Theon承认看见turkey而偏离，反问怎知Robb会独留Bran。",120:"Robb以从未见过的怒意看Theon，却不再说，转问Luwin伤势。",121:"Luwin说只是scratch，又指出死者两人穿black。",122:"Robb判断是Night’s Watch deserters，认为敢近Winterfell很愚蠢。",123:"Luwin说folly与desperation常难区分。",124:"Quent问是否burial。",125:"Robb说敌人不会埋他们，命砍heads送Wall、尸体留carrion crows。",126:"Quent指Osha问如何处理。",127:"Robb走近，Osha虽更高仍跪下，以效忠交换生命。",128:"Robb问oathbreaker能有什么用。",129:"Osha说自己从未发Night’s Watch oath，只有Stiv与Wallen逃Wall，women不能加入black crows。",130:"Theon建议把她给wolves；Osha与guards看向Hali残骸都感不适。",131:"Robb只说她是woman，拒绝立刻如此处置。",132:"Bran补充她是wildling，曾提议把自己交给Mance Rayder。",133:"Robb问名字。",134:"她不情愿报Osha。",135:"Luwin建议先审问。",136:"Robb明显松口气，接受maester建议，命Wayn绑手带回Winterfell，生死取决于供词truth。",
}
SUMMARIES = [S[i] for i in range(1, 137)]

KEY_NOTES = {
1:"snow像gentlest rain，先以温柔触感覆盖Bran焦虑；同一场雪随后会融去joy、遮蔽危险。",
3:"proud as any knight是Bran的新目标：身体条件改变后，他仍用旧英雄语言组织第一次出行。",
5:"Dancer、custom saddle与循序训练共同创造mobility；独立不是意志奇迹，而是动物、工艺和照护协作成果。",
6:"Bran厌烦escort却确实需要医疗与安全支持；想要privacy和客观risk可同时成立。",
7:"winter town以季节迁徙扩容，Winter is coming在此是具体人口与住房制度，而非抽象口号。",
9:"straps既是保护也会在伏击时成为束缚；相同装置的功能取决于环境。",
10:"Theon的adult sexual talk在公共街道测试Robb保护弟弟的边界，也延续Bran对他不信任。",
12:"world as secret joke概括Theon姿态：不断smile既显魅力，也让Bran无法判断何时认真。",
16:"almost as good as flying让骑行替代climbing/flying愿望，暂时恢复Bran失去的自主感。",
17:"Bran能读出smile beneath trouble，说明children并非只接收成年人明确告知的内容。",
19:"Robb希望Bran older是信息照护困境：保护他免真相冲击也会让他更无力理解正在变化的world。",
22:"Lannister记忆触发dizziness和stomach clench而非图像，创伤以身体反应保留被意识封锁的信息。",
24:"snow melted on cheeks模糊snow与tears，Robb保持仪式化祈祷却无法完全隐藏grief。",
25:"Bran用日常动作回忆Jory，而不是战士荣耀；死亡首先破坏的是熟悉生活结构。",
26:"句子在when he…处中断，再由hoofbeats迫使改成when he will wake；Robb避免说death，同时握剑进入Lord persona。",
29:"Blood for blood把复杂政治压成对称报复，Theon的hungry look显示war对他具有吸引力。",
30:"Bran用法律身份反驳Theon，却无意中触碰Eddard可能死亡才会让Robb成为lord的恐惧。",
33:"Robb说almost man grown既是自我鼓励也是制度压力；十五岁被迫在father absence中承担house honor。",
36:"Bran维护Luwin counsel，说明八岁child反而在报复情绪中保留institutional memory。",
38:"过去想象war只含banners与adventure，现在Jory死亡和Eddard伤势给同一词加入真实成本。",
40:"不承认weakness使Bran错过身体安全反馈；反抗过度照护可能滑向证明自己无需任何照护。",
42:"嗅觉与微小观察恢复他对world的参与，林地不只是背景，而是康复后的感官重新占有。",
45:"stream从今日路径变成共同记忆地点，Jory死亡使空间突然储存loss。",
47:"Jon让出fish是small kindness；Bran担心的不只Night’s Watch距离，而是熟悉家庭持续散开。",
49:"feel strong and whole来自水雾、骑行和Robb帮助，并非腿恢复；whole在心理经验上可暂时成立。",
54:"Robb一离开，woods close in，展示Bran独立感仍高度依赖附近可靠者；身体不适也重新进入意识。",
56:"rich clothing在Winterfell象征身份与保护，面对穷困亡命者却标记为可掠夺目标。",
62:"Bran用Eddard处刑日学到的deserter lesson识别危险；Prologue之后的知识在此转成现场判断。",
64:"源页确实印作broad fiat face，疑似排印错误；为遵守原文不擅改，仅在notes标注。",
70:"Bran用Stark name威胁，是从领主环境学来的权力语言；在人数劣势下，身份既有价值也可能提高hostage价值。",
71:"跨页连续句把Stark courage与Stark foolishness绑定：同一不求饶姿态可被看成honor或无效挑衅。",
72:"本段以针对未成年人的性化身体伤害威胁制造残酷升级；稳定定位保留，但不复录原句。",
73:"Osha首先提出hostage value而非伤害，显示她比Hali更能做strategic calculation。",
74:"white walkers在Stiv口中是拒绝北返的理由；结合Prologue可知威胁值得重视，但其具体经历尚未讲明。",
75:"blood without pain将Bran paralysis变成对袭击者的诡异场面，也提醒无pain不等于无injury。",
76:"Robb模仿Eddard式sentence voice，却因少年紧张破音；权威语言已学会，身体尚暴露年龄。",
81:"whistle不是临时召唤野兽，而是已有训练与bond的战术信号；此前wolves失踪其实在附近hunt。",
83:"Bran在刀伤与包围中仍精确解释direwolf anatomy，以知识重新获得片刻叙述控制。",
84:"Stiv低估direwolves为dogs，也把它们只看成pelts；错误分类立刻导致战术灾难。",
85:"Robb喊Winterfell把个人救弟行动转成house battle cry，同时也是他第一次近距离杀人。",
89:"straps从防fall安全装置变成Stiv能快速解除、夺取hostage的弱点，呼应第9段双重功能。",
91:"Bran的全景观察在极端恐惧中异常清晰；hostage视角迫使战斗突然冻结成静态棋局。",
93:"Summer对Robb command部分服从却留守Bran，暗示bond不是普通obedience，仍以保护Bran为优先。",
94:"Bran闻到fear后发现Stiv并非绝对强者；嗅觉与心理判断让权力差距开始变化。",
105:"Bran比Robb更快识别Stiv incentive：若wolves死，对方就不再需要兑现承诺。",
107:"箭声先于Theon出现，和此前Crack/whip一样让介入以声音突发；broadhead一次解决hostage deadlock。",
112:"Theon把kill审美化成beauty，与Robb立即想到miss风险形成性格对照。",
115:"Robb列出counterfactuals，说明结果成功不等于decision合理；他评估的是发箭当时可知风险。",
119:"Theon的turkey解释把escort failure归为狩猎分心，也反推为何Bran等不到后队。",
123:"Luwin拒绝只叫deserters fools，把行为放回hunger、fear与逃亡绝境；解释不等于免罪。",
125:"Robb命decapitation/report Wall模仿Eddard justice，却同时拒绝burial，愤怒让程序更严酷。",
129:"Osha准确区分deserter与wildling woman：她未发oath，因此不能按同一oathbreaking罪名定义。",
131:"She’s a woman是Robb最初拒绝wolf execution的直觉界线，仍需Luwin提供可执行替代方案。",
136:"Robb对questioning建议显出relief，说明他并不想即刻杀Osha，却需要maester把mercy转成符合lord duty的理由。",
}

STAGES = [
(1,16,"Bran借Dancer与special saddle第一次离开Winterfell，穿过winter town后加速追上Robb，重获近似flying的自由感。"),
(17,38,"Robb告知Jory等被杀、Eddard重伤，并在Theon催促下考虑call banners；Bran对war的旧兴奋转为真实dread。"),
(39,75,"兄弟进wolfswood找direwolves并回忆Jory、Jon；Robb离开片刻后，Bran被六名贫困亡命者包围并割伤。"),
(76,109,"Robb与direwolves救援，战斗很快压倒对手；Stiv挟Bran逼Robb杀wolves，Theon以高风险一箭解除僵局。"),
(110,136,"战后Robb质问Theon与guards、辨认deserters并决定送heads到Wall；在Luwin建议下留下wildling Osha审问。"),
]

BACKGROUNDS = {
5:"**Dancer与saddle：** Tyrion设计高背大鞍，以胸腿straps固定Bran；Dancer经训练响应voice、rein和touch。",
7:"**winter town：** Winterfell外季节性聚落，long winter时farmer families迁入，平日多数房屋空置。",
22:"**north preparations：** Catelyn自Eyrie传来Tyrion被捕消息后，Robb已派riders传令并谈及Moat Cailin。",
24:"**King’s Landing消息：** Alyn报告Jaime截路后杀死Jory、Wyl、Heward并使Eddard重伤。",
28:"**call the banners：** lord命vassal houses集结兵力的封建动员；Eddard尚活且Robb只是acting heir。",
49:"**身体事实：** Bran双腿无感觉且无法自行夹马；骑行依赖Dancer、saddle、straps与他人协助过水。",
62:"**Night’s Watch desertion：** deserter被捕依法处死；Bran从Eddard此前处刑Gared学到其亡命风险。",
64:"**源页校勘：** PDF p.369页面原图印作broad fiat face，语义疑应为flat，但精读不擅改原文。",
72:"**安全说明：** 本段含针对八岁Bran的明确性化身体伤害威胁；保留编号、页码与作用分析，不逐字复录。",
73:"**Mance Rayder：** wildlings的King-beyond-the-Wall；Osha认为Benjen nephew可作hostage。",
74:"**white walkers：** Stiv称其为不愿回north的重要原因；Prologue已出现相似超自然威胁，但本章未核实他的经历。",
83:"**direwolf：** 比common wolf头更大、腿更长、snout与jaw更瘦长；Summer与Grey Wind尚未完全成年。",
115:"**decision audit：** Theon一箭实际救下Bran；Robb评估的是miss、armor与hostage reflex等事前风险，不否认结果。",
122:"**deserters：** Luwin从black clothing判断两名男子曾属Night’s Watch；Robb识别Stiv等靠近Winterfell的异常。",
129:"**Osha身份：** 她自称wildling、未加入Night’s Watch，因此不是oathbreaker；是否可信仍待审问。",
}

EXTRA_VOCAB = [
("portcullis","/pɔːrtˈkʌlɪs/","n.","城门铁闸","Winterfell gate"),("filly","/ˈfɪli/","n.","年轻母马","Dancer"),("circuit","/ˈsɜːrkɪt/","n.","一圈；巡回路线","yard training"),("lope","/loʊp/","v.","轻快大步奔跑","direwolves"),("broadhead","/ˈbrɔːdhed/","n.","宽刃箭头","Theon arrows"),("coif","/kɔɪf/","n.","锁子甲头罩","guards"),("undressed stone","/ʌnˈdrest stoʊn/","n.","未经精细修整的石料","houses"),("tendril","/ˈtendrəl/","n.","细长卷曲物","smoke"),("loom","/luːm/","v.","逼近；赫然出现","winter"),("cradle","/ˈkreɪdəl/","v.","稳稳托住","saddle"),("tremulous","/ˈtremjələs/","adj.","轻颤的","smile"),("squirm","/skwɜːrm/","v.","扭动","Theon’s crude talk"),("restless","/ˈrestləs/","adj.","焦躁不安的","Grey Wind"),("pummel","/ˈpʌməl/","n.","马鞍前后突起部分","sword-hand rest"),("saddle sore","/ˈsædəl sɔːr/","n.","骑乘磨伤","ride limit"),("musk","/mʌsk/","n.","动物麝香般气味","forest"),("ford","/fɔːrd/","n.","浅滩渡口","stream crossing"),("surcoat","/ˈsɜːrkoʊt/","n.","罩袍","rich clothing"),("windburnt","/ˈwɪndbɜːrnt/","adj.","被风吹伤的","Stiv face"),("lank","/læŋk/","adj.","平直稀疏的","hair"),("forfeit","/ˈfɔːrfɪt/","adj.","已丧失；必被处死的","deserter life"),("lordling","/ˈlɔːrdlɪŋ/","n.","小领主（轻蔑）","Bran"),("hostage","/ˈhɑːstɪdʒ/","n.","人质","Mance value"),("venison","/ˈvenɪsən/","n.","鹿肉","elk kill"),("overextend","/ˌoʊvərɪkˈstend/","v.","动作伸展过度失衡","Osha spear"),("hamstring","/ˈhæmstrɪŋ/","v.","咬断腿筋；使失去行动","Grey Wind"),("windpipe","/ˈwɪndpaɪp/","n.","气管","hostage threat"),("savage","/ˈsævɪdʒ/","v.","猛烈撕咬","direwolf"),("lever","/ˈlevər/","v.","用杠杆方式撑起","Osha rises"),("thrum","/θrʌm/","n.","弓弦低沉振响","Theon shot"),("abashed","/əˈbæʃt/","adj.","羞愧尴尬的","Quent"),("ofttimes","/ˈɔːfttaɪmz/","adv.","常常（古风）","Luwin"),("carrion","/ˈkæriən/","n./adj.","腐肉；食腐的","crows"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def extract_blocks():
    blocks = extract_range(363, 375, "BRAN", "CH37")
    # The grey man's sentence continues from p.369 to p.370 with capitalized “Only”.
    blocks[70]["text"] = str(blocks[70]["text"]) + " " + str(blocks[71]["text"])
    blocks[70]["end_page"] = blocks[71]["end_page"]
    del blocks[71]
    for order, block in enumerate(blocks, 1):
        block["order"] = order
        block["id"] = f"CH37-P{int(block['page']):03d}-{order:03d}"
    # Redact the explicit sexualized mutilation threat toward eight-year-old Bran.
    blocks[71]["text"] = (
        "[原文含针对八岁Bran的明确性化身体伤害威胁，此处不逐字复录。"
        "请参见源 PDF p.370 中对应段落。]"
    )
    return blocks

def main():
    blocks = extract_blocks()
    write_chapter(
        out=OUT, chapter=37, pov="BRAN", page_start=363, page_end=375,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Bran辅助骑行、Robb继承压力、亡命者风险、direwolf bond与战后判断。",
        vocab=VOCAB,
        guide="Bran借Tyrion设计的saddle、特训Dancer与straps第一次骑出Winterfell，gallop让他重新感到接近flying。自由感很快被King’s Landing噩耗打断：Jory、Wyl、Heward死亡，Eddard重伤；十五岁的Robb在Theon催促blood for blood时被迫用Lord voice考虑north honor。兄弟进wolfswood寻找direwolves，Robb短暂离开后Bran遭六名贫困亡命者包围，其中两人是Night’s Watch deserters，Osha则是wildling。Robb、Summer和Grey Wind迅速压倒对方，Stiv却以Bran做人质；Theon用高风险一箭救人。Robb随后不以成功结果掩盖射击风险，质问Theon与guards为何失职，并在Luwin建议下留下Osha审问，显示他正在从报复冲动学习lord式决策。",
        people=[
            ("Bran Stark","本章视角；首次独立骑出Winterfell，遭绑架并观察Robb、wolves与Theon救援"),
            ("Robb Stark","Bran十五岁brother与acting heir，面对家族噩耗、战斗和俘虏处置压力"),
            ("Theon Greyjoy","随行ward与archer，因追turkey掉队，后以一箭杀Stiv救Bran"),
            ("Maester Luwin","医疗与政治顾问，检查Bran、识别deserters并建议审问Osha"),
            ("Summer / Grey Wind","与Bran、Robb绑定的direwolves，在伏击中发挥决定性战力"),
            ("Osha","来自beyond the Wall的wildling woman，主张留Bran作hostage，后投降求生"),
            ("Stiv / Wallen","Night’s Watch deserters；Stiv挟持Bran，最终被Theon射杀"),
            ("Jory / Wyl / Heward","King’s Landing被Jaime men杀死的Stark household guards，噩耗推动Robb考虑动员"),
        ],
        terms=[
            ("winter town","Winterfell外随winter人口迁入而扩张的季节性聚落"),
            ("call the banners","lord要求vassal houses带兵集结的军事命令"),
            ("deserter","逃离Night’s Watch oath者，被捕依法处死，常因亡命而格外危险"),
            ("King-beyond-the-Wall","Mance Rayder在wildlings中的称号，不受Iron Throne或Night’s Watch统治"),
            ("direwolf bond","Summer与Grey Wind既响应whistle/voice，也分别优先保护对应Stark child"),
        ],
        synthesis="Chapter 37反复检验“独立”不是孤立。Bran能骑，是Dancer、saddle、straps、训练与陪护共同作用；当Robb和后队同时离开，他的自由立刻暴露为高风险。Robb也在经历同样问题：他想成为man grown和Lord，却需要Bran提醒Luwin counsel，需要wolves救场，也需要Luwin提供不杀Osha的制度理由。Theon则代表另一种独立英雄姿态——一箭成功、立即赞美dead enemy——但Robb正确指出，成功结果不能消除射击当时对Bran的巨大风险。成长因此不是证明自己不需要别人，而是学会让勇气、协作、信息和责任共同工作。",
        contrasts=[
            "**straps的保护／straps的束缚：** 它防止Bran坠马，也让Stiv能控制并割落他。",
            "**ride如flying／woods如closing：** Robb在旁时是自由，独处后同一环境变成牢笼。",
            "**banner幻想／Jory死亡：** war从少年冒险想象变成具体熟人尸体。",
            "**Stark threat／smart begging：** Bran把不求饶当honor，对手把它视为无效愚蠢。",
            "**Theon成功一箭／Robb事前风险：** outcome好不代表decision process稳健。",
            "**instant revenge／questioning Osha：** Robb从Theon提议喂wolves转向Luwin建议的信息获取。",
        ],
        questions=[
            "Osha所说white walkers和Mance为何使她远离north、接近Winterfell？",
            "Robb会在Eddard尚活但重伤时真正call banners吗？",
            "Bran对Lannisters的身体记忆何时会恢复成可叙述内容？",
            "Robb与Theon因这次高风险射击产生的裂痕会如何影响后续决策？",
        ],
        extraction_notes="PDF pp.363–375校勘后共136段；自动提取曾把pp.369–370间同一段以Only开头的续句误切，已合并。共7处跨页续段：pp.363–364、364–365、365–366、367–368、369–370、370–371与373–374。PDF p.369原图印作broad fiat face，疑似源文件排印错误，按原文保留。校勘后第72段含针对八岁Bran的明确性化身体伤害威胁，保留稳定定位与分析但不逐字复录。",
    )
    print(f"Wrote Chapter 37 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
