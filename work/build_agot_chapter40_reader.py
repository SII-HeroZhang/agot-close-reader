#!/usr/bin/env python3
"""Build Chapter 40 (CATELYN) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter39_reader import VOCAB as BASE_VOCAB

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"/"AGOT_逐章精读"

S={
1:"日出把Vale从黑转为彩色，Catelyn在阳台感受Alyssa’s Tears的水雾。",
2:"Alyssa失去全家却生前无泪，死后瀑布永不停息；Catelyn想到自己死后会流多少泪。",
3:"Rodrik报告Jaime在Casterly Rock集结军队，Edmure派Vance与Piper守Golden Tooth并誓以Lannister血守土。",
4:"Catelyn认为美丽日出反衬将临恶日，追问真正的Riverrun lord Hoster。",
5:"信中未提Hoster；Rodrik伤后白须已长回，恢复得像从前。",
6:"Catelyn由Edmure掌防推断father病重，并不满无人及时叫醒她。",
7:"Rodrik说Lysa认为应让她睡觉。",8:"Catelyn坚持自己本应被叫醒。",
9:"Rodrik转述Lysa想等combat后再谈。",
10:"Catelyn认为Tyrion操纵了Lysa，决定决斗后离开Eyrie，经Gulltown乘船回Winterfell。",
11:"晕船的Rodrik脸色发绿，仍同意再坐船。",
12:"梳妆时Catelyn想在决斗前劝阻Lysa，并回顾sister从羞怯女孩变成情绪反复的成人。",
13:"她曾主张私下听Tyrion confess，Lysa却坚持在半个Vale前公开展示，酿成如今局面。",
14:"前往Lysa住处途中，Catelyn再次强调Tyrion是自己的prisoner。",
15:"Brynden怒气冲冲出来，讽刺劝Lysa只会伤到自己的手。",
16:"Catelyn提起来自Edmure的Riverrun信。",
17:"Brynden早已从Colemon得知；Lysa拒给一兵回援，他辞去Knight of the Gate并决定当晚返乡。",
18:"Catelyn阻止Brynden独走危险high road，邀他与自己同行并承诺给Riverrun一千人。",
19:"Brynden考虑后同意绕远但更安全的路线，去下方等待。",
20:"Catelyn与Rodrik交换眼神，伴着Robert尖细笑声入内。",
21:"Eyrie石地无法让weirwood扎根，未完成的godswood变成花园，也成为把三条性命交给gods的决斗场。",
22:"盛装的Lysa在露台被求婚者与Vale nobles环绕，但Catelyn认为他们都无望真正共享统治。",
23:"Robert坐高台看木偶互砍，宾客饮酒吃果，把生死决斗办成fool’s festival。",
24:"Lysa当日偏爱Hunter与Corbray；Catelyn分别看到年老家族负担与鲁莽、贫困及相关宫廷传言。",
25:"Lysa看到Catelyn便亲热拥吻，称天气好、gods微笑并劝她喝酒。",
26:"Catelyn拒绝wine，要求谈话。",27:"Lysa承诺after，已经转身回避。",
28:"Catelyn提高声音要求现在谈，指出活Tyrion有价值，死者无用，且Bronn可能获胜。",
29:"Lord Hunter以Ser Vardis勇猛保证能迅速击败sellsword。",
30:"Catelyn根据high road实战经验怀疑，记得Bronn像panther、剑如手臂延伸。",
31:"Ser Morton以性别偏见贬低Catelyn，并断言knight独斗必胜、雇佣兵都是cowards。",
32:"Catelyn礼貌反问杀Tyrion能得到什么，Jaime不会因有trial就原谅处刑。",
33:"Ser Lyn建议斩首，把Tyrion的head当作警告。",
34:"Lysa以Robert想看他fly结束讨论，并把责任归给要求trial by combat的Tyrion。",
35:"Hunter强调Lysa出于honor无法拒绝Tyrion。",
36:"Catelyn无视众人，直接重申Tyrion归自己拘押。",
37:"Lysa坚信Tyrion毒杀Jon、使Robert失父，决意让他偿命后离开。",
38:"Rodrik私下问Catelyn是否真相信Tyrion杀Jon，因为他强烈否认。",
39:"Catelyn只确信某个Lannister谋杀Jon，却不知道具体是谁，并怀疑Lysa因Tyrion在手而改变归罪对象。",
40:"Rodrik用作案风格推测poison可能适合Tyrion或Cersei、却不像偏爱明刀的Jaime，并追问是否确定用毒。",
41:"Catelyn以自然死亡伪装推测poison，又看到Robert为木偶被切开狂喜，认为他必须离开Mother管教才能学会统治。",
42:"Colemon说Jon也曾同意送Robert去Dragonstone fostering，却因自己失言而慌张。",
43:"Catelyn纠正她听说的是Jon死后送Casterly Rock、且未经Lysa同意的计划。",
44:"Colemon激烈否认，正要说是Jon本人安排时被bell打断。",
45:"钟声令众人到栏杆旁，guards带Tyrion入花园，septon把他带到Alyssa石像前。",
46:"Robert称Tyrion为bad little man，要求亲手让他fly。",47:"Lysa哄他说稍后。",
48:"Ser Lyn概括为先trial、后execution。",49:"Ser Vardis与Bronn从花园两端出现。",
50:"Ser Vardis全身重plate、mail、rondels、金属裙与gorget，falcon helm只留狭窄视线。",
51:"Bronn轻装得近似赤裸，却更高、reach更长且年轻约十五岁。",
52:"两名champion在Alyssa像前跪下，septon以crystal散出rainbows，祈求gods按Tyrion有罪与否赐死或自由。",
53:"仪式后Tyrion对Bronn低语；Bronn起身大笑，显示心态轻松。",
54:"Robert在高椅上烦躁追问何时开打。",
55:"Vardis装备巨盾；Bronn拒绝同类盾牌，其日常精磨的剑刃危险锐利。",
56:"Vardis接过Jon Arryn华丽旧剑；Lysa认为让Jon之剑复仇很合适。",
57:"Catelyn觉得Vardis用自己的剑可能更顺手，却已厌倦无效争论而沉默。",
58:"Robert命令他们开打。",59:"Vardis向Robert举剑，为Eyrie与Vale致敬。",
60:"Bronn只对远处Tyrion作简短salute。",61:"Lysa提醒Robert由他下令。",
62:"Robert抓紧椅子发抖，尖叫Fight。",
63:"两人以试探交剑；Bronn不断后退绕圈，避开盾面并移向Vardis无保护侧，迫使重装knight转身追赶。",
64:"Hunter把不站定硬拼叫作craven，其他人附和。",
65:"Rodrik看懂Bronn策略：让Vardis被armor与shield重量耗尽。",
66:"Catelyn意识到这不是tourney而是一步错误即死的dance，触发另一场duel回忆。",
67:"回忆中Brandon为公平卸下部分armor；Catelyn拒给Petyr favor，把Tully手帕给未婚夫并求他饶Petyr。",
68:"Brandon迅速重伤拒绝yield的Petyr，最后一击几乎致命；Petyr倒下时望着Catelyn叫Cat。",
69:"此后直到King’s Landing重逢，Catelyn再未见Petyr。",
70:"Petyr两周后才可离开；Hoster禁止Catelyn探望，Lysa与maester护理他，最后送回Fingers养伤。",
71:"钢铁声把Catelyn拉回现实；Vardis猛烈追击却打不中，Bronn已在肩甲留下缺口。",
72:"Bronn借Alyssa石像闪开，Vardis只在雕像大腿上击出火花。",
73:"Robert抱怨他们没有好好打。",74:"Lysa安慰说Bronn不可能一直跑。",
75:"露台lords饮酒说笑，Tyrion却全神贯注观察champions。",
76:"Bronn突然强攻无盾侧，破坏helmet wing、盾牌和腹甲。",
77:"Vardis猛劈被挡，因狭窄visor看不清Bronn并撞上石像。",
78:"Hunter提醒太迟；Bronn击碎Vardis持剑肘甲，随后首次站定与受伤knight连续对砍。",
79:"Rodrik严肃指出Vardis已经受伤。",
80:"Catelyn看到血、呼吸急促、parry变慢以及armor多处深痕，Bronn则像越来越强。",
81:"连Vale nobles都看出败势，Lysa仍命Vardis赶快finish满足Robert。",
82:"Vardis忠于命令发动最后冲锋，盾击几乎放倒Bronn，再双手举剑准备致命一击。",
83:"Bronn后撤，Jon的美剑撞石折断；他推倒Alyssa像把Vardis压在下面。",
84:"Bronn踢开破rondel，从腋下弱点刺穿肋骨杀死Vardis。",
85:"Eyrie一片寂静；Bronn取下helmet，吐出被盾击断的tooth。",
86:"Robert问Mother是否结束。",87:"Catelyn心想事情其实才刚开始。",
88:"Lysa冷淡悲伤地承认结束，声音像已死guard captain。",
89:"Robert仍问能否让Tyrion fly。",90:"Tyrion起身说自己要乘turnip hoist下山。",
91:"Lysa想指责他presume。",92:"Tyrion引用House Arryn格言As High as Honor，要求兑现裁决。",
93:"Robert因不能处刑而尖叫发抖，指责Lysa违背承诺。",
94:"Lysa公开宣告gods判Tyrion无罪，只得释放、归还财物并给马与supplies，却指定危险high road路线。",
95:"Lysa因这条近似死刑的路线暗自满意；Tyrion明知危险仍以mocking bow接受。",
}
SUMMARIES=[S[i] for i in range(1,96)]

KEY_NOTES={
1:"rose and gold的日出极美，却在下一段与无尽眼泪、第三段与战争动员相接；景色不是安慰，而是反差框。",
2:"Alyssa’s Tears永远触不到埋葬亲人的土地，象征哀悼有巨大外观却不能完成实际抵达；Catelyn把传说投射到自身损失。",
3:"water land with Lannister blood把瀑布水意象转成战争血液，Edmure的誓言既激昂也预示升级。",
4:"Catelyn区分acting son与legal lord，立即从军令背后读出Hoster健康异常。",
7:"让她sleep表面是照顾，实际继续由Lysa决定Catelyn何时可获得影响家族生死的信息。",
10:"played her like pipes准确识别Tyrion把Lysa的公开欲、确信与honor规则组合成逃生程序。",
11:"一句轻喜剧回扣来Eyrie的海程，也显示Rodrik把身体不适置于duty之后。",
12:"形容词长串来自Catelyn此刻的愤怒观察；它揭示关系破裂，不应当成临床诊断。",
13:"private questioning本可保留调查弹性；public confession使Lysa一旦被嘲弄就更难后退。",
15:"bruise your hand把‘打醒’的惯用语实体化，Brynden认为问题不是力度不足，而是Lysa拒绝接收reason。",
17:"Brynden摘除office而保留Tully identity：当Vale命令与birth family危机冲突，他选择后者。",
18:"Catelyn承诺thousand men，但这些兵从何而来尚未落实；这是政治意向而非已完成调兵。",
21:"无法生根的godswood让宗教裁决落在人工花园；环境悄悄质疑‘gods亲自决定’的确定性。",
23:"木偶决斗、cream、berries和wine把真实死亡包装成儿童娱乐与贵族社交。",
24:"叙述列出的是Catelyn对政治婚配风险的判断；关于Ser Lyn私生活的内容明确只是whispered rumor。",
25:"the gods are smiling是Lysa对仪式结果的预设，讽刺在于结果随后违背她期待。",
28:"Catelyn从moral guilt转向strategic value劝说，因为她知道Lysa更可能听懂利益后果。",
30:"她不被title迷惑，而以high road存活率、footwork和weapon integration评估fighter。",
31:"Ser Morton用women understand little取消Catelyn实战观察，再用knight身份替代具体能力比较。",
32:"courtesy that made her mouth ache说明礼貌已成为压制愤怒的身体劳动。",
34:"Lysa说Tyrion only himself to blame，省略了自己先用sky cell和预设审判逼他诉诸combat。",
37:"Lysa把怀疑压缩成确定句，并从失夫、失父的真实痛苦直接跳到Tyrion必须是凶手。",
39:"Catelyn第一次明确承认无法指出具体凶手；可达性偏差使眼前Tyrion承受原信指向Cersei的罪名。",
40:"Rodrik依赖gender与personality stereotypes推凶并不可靠，但他追问‘是否真确定poison’有效暴露证据空缺。",
41:"木偶流出red sawdust把Robert的娱乐与即将真实流血重叠；Catelyn对fostering判断由此更急迫。",
42:"Colemon的酒后失言提供与Catelyn此前版本冲突的新信息；他未说完前不能确认全部含义。",
44:"句子停在Jon who—并被bell截断，是有意的信息中断；战斗 spectacle压过可能改变调查方向的证词。",
45:"weeping Alyssa从哀悼意象变成宗教审判中心，之后还会成为战术障碍与武器。",
48:"trial first, then execution公开承认众人把trial当礼仪前奏而非可能改变结论的裁决。",
50:"盔甲细节不是装饰清单：每项保护也增加重量、限制视野与关节活动，构成后续战术因果。",
51:"almost naked来自相对重装的视觉错觉；Bronn以reach、年龄、速度和体力交换防护。",
52:"rainbows落在Tyrion脸上制造神圣美感，但祷词的二元判决将复杂证据交给单次武力结果。",
53:"Tyrion低语内容暂不公开；Bronn笑可能是信心、策略或私人反应，不能确定。",
55:"拒盾不是轻视，而是保持双手剑速度与移动性；honed every day显示表面粗陋背后的职业纪律。",
56:"Jon的剑承载纪念意义，却不是Vardis熟悉的工具；Lysa优先symbolic fitness而非combat fitness。",
57:"Catelyn判断正确却沉默，显示反复被无视后产生的learned futility，也让悲剧继续。",
62:"Robert的身体trembling把兴奋与病弱混合；他拥有下令权，却不理解命令的死亡含义。",
63:"整段用circle、give way、away from shield等空间动词，让读者看到Bronn在移动中设计未来疲劳与角度。",
64:"观众把符合规则的有效策略叫cowardice，因为他们期待knightly spectacle而非生存效率。",
65:"Rodrik一句话把退让重新定义为主动资源消耗，显示expert reading与crowd reading的差异。",
66:"dance回扣Tyrion上一章roll the dice：法律把真相变成一步失误即可决定的身体游戏。",
67:"Brandon主动减甲形成honor对称；但Catelyn token明确表明婚约选择，Petyr仍以决斗拒绝社会现实。",
68:"Petyr多次拒yield使勇气与自毁难以区分；Catelyn的记忆聚焦血与最后呼名，解释重逢为何复杂。",
70:"Lysa曾护理Petyr的新信息给姐妹与Littlefinger关系增加历史层次，但本段不说明她当时感情。",
71:"回忆与现实都由steel sound连接；不同之处是Bronn不会像年轻Petyr那样停在正面承受。",
72:"Alyssa像第一次直接介入战斗：Ser Vardis的攻击浪费在象征Arryn哀悼的marble上。",
75:"饮酒观众把它当持续节目，Tyrion的凝视则提醒每一步都决定他本人是否活着。",
76:"Bronn从消耗阶段转入破坏阶段，每一击针对无盾侧、视野和装备完整性。",
77:"visor保护脸却缩窄感知，armor系统的安全收益在快速侧移战中转为信息劣势。",
78:"Bronn此时stand ground不是突然勇敢，而是等到Vardis关节受损后才选择对攻。",
80:"Bronn仿佛变强实为Vardis持续变弱；相对体能变化被Catelyn写成视觉逆转。",
81:"Lysa的finish him命令以Robert boredom替代战术判断，迫使忠诚的Vardis违背身体与局势信息。",
82:"Vardis最后冲锋几乎成功，避免把失败写成无能；他败在累积装备、伤势、命令与选择共同作用。",
83:"美丽纪念剑因击中纪念雕像而折断，Lysa为Jon配置的两件象征物共同压倒其champion。",
84:"Bronn利用arm-breastplate weak spot终结，呼应第50段rondel本用于保护的具体位置。",
85:"broken tooth证明轻装胜利也付出代价；沉默取代此前笑声，spectators终于面对真实死亡。",
87:"Catelyn的only now beginning把一场结束的duel重新放回更大的Stark–Lannister战争。",
92:"Tyrion把House words变成contract：若Arryn拒绝gods verdict，就公开否认自身以Honor立族的身份。",
94:"Lysa口头承认innocent，却在route安排中寻找程序外死亡；正式服从与实质规避同时发生。",
95:"mocking bow承认双方都看懂high road威胁；Tyrion仍以礼节讽刺拒绝给Lysa看到恐惧。",
}

STAGES=[
(1,19,"Catelyn由Vale日出听到Casterly Rock集兵、Hoster病况不明；Lysa拒援Riverrun，Brynden辞职并决定随Catelyn绕行。"),
(20,44,"Eyrie把trial办成节庆；Catelyn劝阻失败，却在与Rodrik、Colemon交谈中发现Jon之死和Robert fostering叙事存在空缺。"),
(45,62,"Tyrion与champions入场；Ser Vardis重装并持Jon纪念剑，Bronn轻装拒盾，Robert以儿童兴奋下令开战。"),
(63,70,"Bronn先以移动耗体力；战斗让Catelyn回忆Brandon与Petyr旧决斗，以及Lysa曾护理重伤Petyr。"),
(71,85,"Bronn逐步破坏Vardis装备与关节，利用Alyssa像压倒并杀死他；象征、装备与错误命令共同决定战果。"),
(86,95,"Lysa不得不承认gods判Tyrion无罪并释放，却指定致命high road；Tyrion看穿后仍以mocking courtesy接受。"),
]

BACKGROUNDS={
1:"**Alyssa’s Tears：** Giant’s Lance上的巨大瀑布；传说Alyssa Arryn死后须流泪直到水落到亲人埋葬的Vale土地，但水永远在途中化雾。",
3:"**Golden Tooth：** Westerlands通往riverlands的重要山口；Vance、Piper受Edmure命令防守Lannister可能东进。",
5:"**Hoster Tully：** Lord of Riverrun、Catelyn与Edmure之父；信中缺席使Catelyn推断病情严重。",
10:"**离开路线：** Eyrie可下至Vale，再往Gulltown乘船回north；high road穿Mountains of the Moon，沿途有clansmen。",
17:"**Knight of the Gate：** Bloody Gate的军事守将；Brynden辞去此职，拒绝让Vale中立阻止自己援助Tully homeland。",
21:"**godswood：** old gods信仰中心通常应有weirwood heart tree；Eyrie岩基使树无法扎根，只留下人工花园。",
24:"**证据边界：** 关于Ser Lyn对women无兴趣只是court whisper；本章没有确认其真实性，也不构成道德评价。",
37:"**指控变化：** Lysa写给Catelyn的信曾指向Cersei；如今她公开断言Tyrion亲手poison Jon，文本未提供新证据解释转变。",
40:"**poison推断：** Rodrik与Catelyn都在依据刻板作案风格猜测；截至此段，他们甚至没有确认Jon确系中毒。",
42:"**fostering矛盾：** Catelyn此前听说Lysa在Jon死后拟送Robert去Casterly Rock；Colemon则称Jon生前计划送Dragonstone。",
50:"**armor结构：** rondel护腋前接缝，gorget护喉，lobstered plates兼顾关节活动；重量与视野是相应代价。",
52:"**trial by combat：** 仪式宣称gods以champion胜负裁定被告有罪与否；这是该社会认可的法律规则，不是现代意义的事实证据。",
56:"**Jon’s sword：** Lysa曾为Jon在King’s Landing订制此剑；纪念价值高，但Vardis未必熟悉平衡与手感。",
67:"**旧决斗：** 少年Petyr因爱Catelyn挑战其betrothed Brandon Stark；Brandon应Catelyn请求饶其性命。",
70:"**Fingers：** Vale东北狭长半岛群，Petyr出身地；Hoster在他康复后将其送回家。",
84:"**战术终点：** Bronn从被破坏rondel后的腋下刺入，这是plate armor必须保留活动度的接缝。",
92:"**House Arryn words：** As High as Honor；Tyrion用家族格言要求Lysa尊重刚由其主持的gods verdict。",
94:"**释放条件：** Lysa归还horses、supplies、goods、weapons并护送至Bloody Gate；出Gate后仍须自行通过high road。",
}

EXTRA_VOCAB=[
("balustrade","/ˌbæləˈstreɪd/","n.","栏杆；栏杆柱列","Eyrie balcony"),("indigo","/ˈɪndɪɡoʊ/","n./adj.","靛蓝色","dawn colors"),("torrent","/ˈtɔːrənt/","n.","急流；洪流","waterfall"),("mass a host","/mæs ə hoʊst/","v.","集结大军","Casterly Rock"),("bristly","/ˈbrɪsli/","adj.","硬毛丛生的","Rodrik whiskers"),("mummer’s farce","/ˈmʌmərz fɑːrs/","n.","演员式闹剧","trial"),("inconstant","/ɪnˈkɑːnstənt/","adj.","反复无常的","Lysa"),("concession","/kənˈseʃən/","n.","让步；勉强采用之物","ornament"),("evenfall","/ˈiːvənfɔːl/","n.","黄昏（古风）","departure"),("brusque","/brʌsk/","adj.","简短生硬的","agreement"),("statuary","/ˈstætʃueri/","n.","雕像群","garden"),("sapphire","/ˈsæfaɪər/","n.","蓝宝石","Lysa necklace"),("moonstone","/ˈmuːnstoʊn/","n.","月长石","Lysa necklace"),("motley","/ˈmɑːtli/","n./adj.","丑角杂色服","puppeteer"),("espie","/ɪˈspaɪ/","v.","看见；发现（古风）","Catelyn"),("doughty","/ˈdaʊti/","adj.","勇猛顽强的（古风）","Ser Vardis"),("sellsword","/ˈselsɔːrd/","n.","雇佣剑士","Bronn"),("care a fig","/ker ə fɪɡ/","phr.","丝毫在乎","Jaime"),("ponderously","/ˈpɑːndərəsli/","adv.","沉重而煞有介事地","Lord Hunter"),("fostering","/ˈfɔːstərɪŋ/","n.","送往他家抚养与受训","Robert"),("a-fray","/əˈfreɪ/","adj.","紧张散乱的（古风）","nerves"),("rondel","/rɑːnˈdel/","n.","圆形护甲片","armpit joint"),("juncture","/ˈdʒʌŋktʃər/","n.","连接处","arm and breast"),("gorget","/ˈɡɔːrdʒɪt/","n.","护喉甲","plate armor"),("coif","/kɔɪf/","n.","锁子甲头罩","Bronn"),("faceted","/ˈfæsətɪd/","adj.","有切面的","crystal sphere"),("fidget","/ˈfɪdʒɪt/","v.","坐立不安","Robert"),("plaintively","/ˈpleɪntɪvli/","adv.","哀求抱怨地","Robert"),("tracery","/ˈtreɪsəri/","n.","精细装饰纹样","sword engraving"),("cursory","/ˈkɜːrsəri/","adj.","草率简短的","salute"),("craven","/ˈkreɪvən/","adj./n.","怯懦的；懦夫（古风）","crowd accusation"),("bailey","/ˈbeɪli/","n.","城堡外院","Riverrun duel"),("betrothed","/bɪˈtroʊðd/","n./adj.","未婚夫；订婚的","Brandon"),("handscarf","/ˈhændskɑːrf/","n.","作为信物的手帕","Catelyn token"),("litter","/ˈlɪtər/","n.","轿；担架式车舆","Petyr travel"),("lithely","/ˈlaɪðli/","adv.","轻盈灵活地","Bronn"),("plinth","/plɪnθ/","n.","雕像底座","Alyssa"),("parry","/ˈpæri/","n./v.","格挡","slowing defense"),("labored","/ˈleɪbərd/","adj.","吃力的","breathing"),("reel","/riːl/","v.","踉跄后退","Vardis"),("lurch","/lɜːrtʃ/","v.","突然踉跄冲动","last attack"),("totter","/ˈtɑːtər/","v.","摇晃欲倒","statue"),("turnip hoist","/ˈtɜːrnɪp hɔɪst/","n.","运萝卜的升降吊篮","Eyrie descent"),("presume","/prɪˈzuːm/","v.","擅自认为；放肆","Lysa objection"),
]
VOCAB=BASE_VOCAB+EXTRA_VOCAB

def extract_blocks():
    blocks=extract_range(396,406,"CATELYN","CH40")
    # p.400 ends “it was Lord”; p.401 continues with the proper name “Jon who—”.
    blocks[43]["text"]=str(blocks[43]["text"])+" "+str(blocks[44]["text"])
    blocks[43]["end_page"]=blocks[44]["end_page"]
    del blocks[44]
    # The visual page closes Lord Hunter's shouted quotation here; text extraction
    # returns the closing glyph as an opening curly quote.
    blocks[63]["text"]=str(blocks[63]["text"]).replace('coward! “ Other','coward!” Other')
    for order,block in enumerate(blocks,1):
        block["order"]=order
        block["id"]=f"CH40-P{int(block['page']):03d}-{order:03d}"
    return blocks

def main():
    blocks=extract_blocks()
    write_chapter(
        out=OUT,chapter=40,pov="CATELYN",page_start=396,page_end=406,
        blocks=blocks,summaries=SUMMARIES,key_notes=KEY_NOTES,stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Vale政治、trial by combat程序、Bronn与Vardis战术差异及Catelyn证据判断。",
        vocab=VOCAB,
        guide="Catelyn在Alyssa’s Tears水雾中听到战争逼近：Jaime据说集兵，Edmure守Golden Tooth，Hoster病况不明；Lysa却拒绝派Vale一兵援助Riverrun，促使Brynden辞去Knight of the Gate。与此同时，Lysa把Tyrion的trial by combat办成贵族节庆，众人预设Ser Vardis必胜。Catelyn是少数从high road实战、年龄、reach和装备代价判断Bronn危险的人。战斗通过移动耗竭、视野限制、关节破坏和地形利用逐步兑现这一判断，也唤起她对Brandon与Petyr旧决斗的记忆。Bronn杀死Vardis后，Lysa必须按自己主持的仪式承认Tyrion无罪，却把他赶上致命high road；形式上的honor与实质上的规避成为本章最后的尖锐矛盾。",
        people=[
            ("Catelyn Stark","本章视角；质疑Lysa审判、评估Bronn战术，并重新审视Jon之死证据与旧日Petyr决斗"),
            ("Lysa Arryn","Lady of the Eyrie；拒援Riverrun、主持trial，并在结果不利后以high road间接施压"),
            ("Tyrion Lannister","被告；以trial by combat取得正式无罪与释放"),
            ("Bronn","Tyrion的sellsword champion，以轻装、移动、体能和地形击败Vardis"),
            ("Ser Vardis Egen","Lysa champion与guard captain，重装、持Jon旧剑，忠于命令直至战死"),
            ("Robert Arryn","child Lord of the Eyrie，把决斗与Moon Door处刑当作娱乐"),
            ("Brynden Tully","Catelyn uncle；因Lysa拒援Riverrun辞去Knight of the Gate"),
            ("Ser Rodrik Cassel","Catelyn护卫与战术解释者，追问Jon是否确由poison所杀"),
            ("Maester Colemon","无意透露Jon曾计划把Robert送Dragonstone fostering"),
            ("Petyr Baelish / Brandon Stark","Catelyn回忆中的旧决斗双方；Petyr因爱她挑战其未婚夫"),
        ],
        terms=[
            ("Alyssa’s Tears","Giant’s Lance瀑布及Arryn哀悼传说，也指花园中的weeping woman石像"),
            ("Golden Tooth","Westerlands与riverlands之间的重要山口"),
            ("Knight of the Gate","Bloody Gate军事守将，原由Brynden担任"),
            ("trial by combat","通过champion单斗让gods裁定被告有罪或无罪的法律仪式"),
            ("As High as Honor","House Arryn格言，被Tyrion用来要求Lysa兑现裁决"),
        ],
        synthesis="Chapter 40反复追问‘看见’与‘知道’的差别。Vale nobles看见knight、华丽盔甲和美剑，就以为胜负已定；Catelyn与Rodrik看见重量、reach、年龄和移动策略，得出相反判断。Lysa看见Tyrion在手，就把原先指向Cersei的怀疑凝固到他身上；Rodrik一句‘Was it poison?’则揭露他们连死因都未证实。trial by combat最终让Bronn的战术能力被制度解释成gods宣告Tyrion无罪。这一结果在当地法律上有效，却不能逻辑证明谁杀Jon。Lysa随后遵守释放字面、破坏安全实质；Tyrion引用As High as Honor，正是把她最看重的身份表演变成最低限度的约束。",
        contrasts=[
            "**Alyssa无尽泪水／Lysa缺乏反思：** 家族哀悼传说宏大，现实统治者却把死亡变成节庆。",
            "**weirwood不能扎根／gods裁决：** 缺少heart tree的人工花园仍被宣称为神意现场。",
            "**knight身份／sellsword能力：** title与装备制造预期，训练、年龄、reach和策略决定实战。",
            "**beautiful sword／ugly blade：** 纪念与装饰价值输给熟悉、锋利和使用方式。",
            "**旧Petyr硬撑／Bronn主动退让：** 拒绝后退看似勇敢却近乎自毁，后退可成为胜利策略。",
            "**正式释放／high road死刑：** Lysa服从程序文字，同时试图让环境完成被禁止的处刑。",
        ],
        questions=[
            "Colemon未说完的‘it was Lord Jon who—’具体会如何改变Robert fostering与Jon死因调查？",
            "Lysa为何从信中怀疑Cersei转为确信Tyrion亲自poison Jon？",
            "Brynden与Catelyn能否真正调集一千人及时援助Riverrun？",
            "Tyrion与Bronn如何通过clansmen控制的high road安全离开Vale？",
            "Catelyn回忆Petyr旧决斗后，会如何重新评估他当前的证词与动机？",
        ],
        extraction_notes="PDF pp.396–406校勘后共95段。自动提取曾把p.400末尾it was Lord与p.401开头Jon who—误切为两段，已人工合并；p.403 Lord Hunter喊话末尾的右引号被文本层映射成左引号，已依页面图像修正。校勘后共7处跨页续段：pp.397–398、398–399、400–401、401–402、402–403、403–404与404–405。段落顺序、引号、专名和决斗动作链均已复核。",
    )
    print(f"Wrote Chapter 40 with {len(blocks)} paragraphs")

if __name__=="__main__":
    main()
