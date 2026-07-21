#!/usr/bin/env python3
"""Build Chapter 30 (EDDARD) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter29_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"Barristan说自己为无亲友陪伴的Ser Hugh守了最后一夜，只听说他在Vale有母亲。",2:"晨光中Ser Hugh像睡着；Eddard怀疑他是否因自己调查而被Lannister封臣杀死，却知道未必能确认。",3:"Barristan说明Hugh侍奉Jon四年，渴望knighthood，却尚未准备好。",4:"疲惫的Eddard说没人真正准备好。",5:"Barristan问是指成为knight吗。",6:"Eddard答是死亡，并让silent sisters把铠甲送给母亲，感叹war不该成为game。",7:"Barristan说铠甲值钱且可能尚未付清。",8:"Eddard说Hugh已经以生命付出昂贵代价，承诺处理smith欠款。",9:"Eddard与Barristan穿过苏醒的营地，各种盾徽像门牌一样标出帐篷主人。",10:"Barristan告诉他Robert仍准备参加当天melee。",11:"Eddard早已从Jory处得知，因此彻夜难眠。",12:"Barristan委婉暗示醉后豪言常在清晨被放弃。",13:"Eddard说Robert绝不会因清醒而退缩。",14:"Robert金色pavilion外陈列warhammer与crowned stag巨盾。",15:"Robert已醒且喝beer，两个年轻squires因旧铠甲太小而无法替他扣好。",16:"Robert辱骂squires无能，又向Eddard抱怨是Cersei安排的人。",17:"Eddard直说问题不是boys，而是Robert胖得穿不下旧甲。",18:"Robert先阴沉反问，随即大笑并承认Eddard总是正确。",19:"Robert骗squires去找不存在的breastplate stretcher。",20:"boys慌忙离开后，Robert再也忍不住笑。",21:"众人短暂同乐，Eddard却注意两名squires都具有Lannister外貌。",22:"Robert希望恶作剧能让他们整天被支使。",23:"Eddard确认两人是否Lannister。",24:"Robert说是Tywin兄弟的儿子，却连父亲是谁都记不清。",25:"Eddard担忧Robert日夜被Cersei亲族包围，并提起昨夜夫妻争执。",26:"Robert说Cersei试图禁止他参赛，又把想象中的Lyanna当作不会羞辱自己的对照。",27:"Eddard纠正Robert并不了解Lyanna内在的坚硬，她同样会反对他参加melee。",28:"Robert抱怨Eddard在north冻干了激情，拍胸证明自己仍有活力。",29:"Eddard提醒他如今是king。",30:"Robert认为王位不应剥夺饮酒、女人、骑马与打人的欲望。",31:"Barristan从公平性劝阻：没人敢在melee中攻击king。",32:"Robert惊讶地认为所有人都应尽力打他。",33:"Eddard顺势指出最后幸存者必然是Robert，因为没人敢冒犯他。",34:"Robert愤怒地问那些cowards是否会故意让他赢。",35:"Eddard与Barristan确认一定如此。",36:"Robert暴怒掷出breastplate并命二人离开。",37:"Barristan迅速退出；Robert却留下Eddard。",38:"Robert重新斟beer，命Eddard喝。",39:"Eddard说自己不渴。",40:"Robert以王命强迫。",41:"Eddard喝下浓黑烈beer。",42:"Robert诅咒Eddard与Jon把自己推上王位，反说二人更该当king。",43:"Eddard以继承权解释Robert更适合。",44:"Robert不许争辩，哀叹kinging使自己胖得穿不下铠甲。",45:"Eddard试图回应。",46:"Robert回顾夺位时最有生命力、即位后反而如死；他怨Jon促成Cersei婚姻，也承认Joffrey在Trident事件中撒谎。",47:"Eddard说自己全心爱children。",48:"Robert坦言曾想弃冠去Free Cities当sellsword，却因害怕Cersei操控Joffrey即位而不敢离开。",49:"Eddard说Joffrey还小，并以Robert少年时也wild安慰他。",50:"Robert说Joffrey的问题并非wild，随后自称已成长为good king，并因Eddard沉默而不悦。",51:"Eddard谨慎开口。",52:"Robert让他只需说自己胜过Aerys，又迅速转向早餐、tourney、Loras及其妹妹。",53:"早餐时Robert恢复少年般兴奋，回忆在Eyrie打橙子仗，Eddard也被感染。",54:"Eddard重新看见自己深爱的旧友，乐观设想证实Lannister罪行后Robert会支持自己、击败Tywin。",55:"这顿早餐让Eddard久违地轻松，直到赛事重新开始。",56:"Eddard陪Robert去赛场与Sansa会合，并把Cersei缺席理解为希望信号。",57:"Sansa沉迷比赛，几乎没注意父亲到来。",58:"Sandor穿朴素灰甲登场，只有hound helm稍作装饰。",59:"Jaime华丽入场时Littlefinger押他一百gold dragons。",60:"Renly接受赌局并看好Sandor。",61:"Littlefinger以dog不咬主人之手讽刺Sandor受Lannister供养。",62:"Sandor与Jaime戴下面甲、持枪就位。",63:"第一轮Jaime借移动化解Sandor长枪并正面击中他，Sansa紧张观看。",64:"Littlefinger提前问Renly如何花赢来的钱。",65:"第二轮Sandor跟随Jaime变位，两枪同碎，Jaime被撞落并滚进泥里。",66:"Sansa说自己早知Sandor会赢。",67:"Littlefinger请她预测下一场，免得Renly把自己赢光。",68:"Renly遗憾Tyrion不在，否则自己能赢更多。",69:"Jaime华丽lion helm摔歪卡住，只能盲目踉跄地被带去blacksmith，引发全场嘲笑。",70:"Gregor以近八英尺的巨躯登场，战马和长枪在他身下都显得很小。",71:"Eddard回顾传闻：Gregor十七岁参与King’s Landing陷落，可能杀害婴儿Aegon并强暴、杀死Elia。",72:"更多流言把Gregor与妻子、妹妹、父亲、仆人及Sandor烧伤联系起来；Sandor继承日离家后从未回去。",73:"Loras以镶sapphires的银甲和真正forget-me-nots披风登场，Sansa再次赞叹其美貌。",74:"Loras骑处于发情期的grey mare，Gregor stallion闻到气味失控；Sansa戴着红玫瑰请求父亲保护Loras。",75:"Eddard说tourney lances会碎裂、不应伤人，却想起Ser Hugh而难以说出口。",76:"Gregor粗暴踢打失控stallion，险些被掀下。",77:"比赛开始后Loras平稳瞄准，Gregor同时控制马、盾、枪，最终连人带马摔倒。",78:"Sandor大笑，Loras的枪甚至未断；sapphires闪耀使观众疯狂。",79:"Gregor暴怒起身，摔掉helm并向squire索要sword。",80:"他一剑几乎斩断自己的马颈，继而持血剑冲向Loras，全场由欢呼变尖叫。",81:"Gregor击开squire并把Loras打落，准备致命一击时Sandor出手阻止。",82:"兄弟用真剑激斗；Gregor三次砍向hound helm，Sandor却从不攻击其裸露脸部。",83:"Robert用战场般洪亮的命令与二十把剑制止冲突。",84:"Sandor跪下服从，Gregor最后停手弃剑离场；Robert允许他走。",85:"Sansa问Sandor是否已是champion。",86:"Eddard说理论上还应由Sandor与Loras决赛。",87:"Loras回场，感谢Sandor救命并主动让出胜利。",88:"Sandor再次否认自己是Ser，却接受冠军、奖金和民众首次给予的爱戴。",89:"Littlefinger认为Loras明知mare发情，故意利用Gregor偏爱暴躁stallion的习惯。",90:"Barristan认为这种trick没有honor。",91:"Renly指出少量honor换来两万gold。",92:"无名平民Anguy击败贵族赢得archery；Eddard招揽他，却被刚获酒、胜利与巨款的少年拒绝。",93:"近四十人参加三小时melee，Thoros靠flaming sword获胜；伤亡清单令Eddard庆幸Robert未参加。",94:"晚宴上Lannisters缺席、Robert高兴、姐妹和睦，使Eddard充满希望；Sansa询问Arya的dancing。",95:"Arya开心展示腿上大块淤青。",96:"Sansa以字面理解，怀疑她是很差的dancer。",97:"Sansa听Dance of the Dragons时，Eddard亲自检查Arya伤势。",98:"Arya单腿站立并复述Syrio：每次受伤都是让人进步的lesson。",99:"Eddard虽认可Syrio名声与风格，仍因蒙眼、翻转等训练担心Arya是否要继续。",100:"Arya说次日要抓cats。",101:"Eddard觉得请Braavosi也许是错误，提议改由Jory或Barristan教学。",102:"Arya拒绝，坚持要Syrio。",103:"Eddard认为普通master-at-arms足以教基础，却知道无法说服她，只要求小心。",104:"Arya庄重承诺，同时流畅换腿保持平衡。",105:"深夜送女儿入睡后，Eddard回Tower，注意Littlefinger房间仍亮灯而河边狂欢渐息。",106:"他研究dagger，按Littlefinger叙述把它与Tyrion、Bran遇刺相连，却仍不理解动机。",107:"他直觉Bran坠落、dagger与Jon之死相关，但Stannis、Lysa、Hugh和brothel线索都无法继续追问。",108:"Eddard确信Gendry是Robert之子，依据是典型Baratheon外貌及排除Renly、Stannis。",109:"他想到Robert还有其他baseborn children，并公开承认过Storm’s End的一名男孩。",110:"他回忆Robert少年时在Vale生的长女，以及Robert曾真心疼爱婴儿。",111:"他认为这些baseborn children依法权利很少，不能威胁Robert的trueborn children。",112:"无名访客在门外轻敲，打断他的思考。",113:"Eddard让Harwin放人进来。",114:"访客穿泥靴与粗布brown robe，以cowl和宽袖遮住外貌。",115:"Eddard问身份。",116:"对方只称friend，并要求单独谈话。",117:"好奇压过谨慎，Eddard让Harwin离开；访客关门后才掀开cowl。",118:"Eddard惊认是Varys。",119:"Varys礼貌落座并要一杯酒。",120:"Eddard倒酒，惊叹自己近距离也认不出这名汗味粗衣人。",121:"Varys说伪装正为防人发现私会，并提醒Cersei严密监视Eddard。",122:"Eddard询问他如何越过多层guards。",123:"Varys暗示Red Keep有秘密通道，随后直言Robert愚蠢且危在旦夕，Lannisters原计划在melee中杀他。",124:"Eddard震惊追问是谁。",125:"Varys拒绝直接说，暗示答案若还需解释便选错了盟友。",126:"Eddard猜Lannisters，却认为Cersei明明劝阻Robert参赛。",127:"Varys指出公开禁止恰是逼Robert参赛最可靠的方法。",128:"Eddard承认这符合Robert性格，但仍问谁敢攻击king。",129:"Varys描述如何在四十人混战中伪装意外，并设想Cersei事后赦免或灭口执行者。",130:"Eddard愤怒指责Varys知情却不作为。",131:"Varys说自己掌握whisperers而非warriors。",132:"Eddard说他本可更早来报。",133:"Varys反问Eddard若早知必会告诉Robert，而Robert会如何反应。",134:"Eddard承认Robert会为证明不怕而照样参赛。",135:"Varys承认自己也在观察Eddard如何处理，因为此前并不信任他。",136:"Eddard对自己不被信任感到惊讶。",137:"Varys把Red Keep众人分为忠于realm和只忠于自己两类，称Eddard今晨表现已证明所属。",138:"Eddard说Cersei真正该怕的是Varys。",139:"Varys说Robert鄙视spies与eunuchs，自己可轻易被舍弃；Eddard却是Robert不会听Cersei命令杀死的朋友，因此可能成为救星。",140:"Eddard被宫廷复杂压得想回Winterfell，仍试图列举Robert其他忠友。",141:"Varys区分憎恨Cersei与爱Robert，并逐一说Barristan爱honor、Pycelle爱office、Littlefinger只爱自己。",142:"Eddard提出Kingsguard。",143:"Varys称其为paper shield：Jaime破誓，Boros与Meryn属Cersei，其他人可疑，只有年老Barristan是真钢。",144:"Eddard坚持应把阴谋告诉Robert。",145:"Varys说没有能对抗queen、Kingslayer、council与Casterly Rock的可用证据，贸然指控只会送命。",146:"Eddard指出敌人若失败必会再次行动。",147:"Varys同意，并说Eddard已令他们焦虑；他提出共同预防，又要求下次council继续公开轻蔑自己。",148:"Varys将离开时，Eddard问Jon究竟如何死。",149:"Varys说一直等他问到此事。",150:"Eddard命他说明。",151:"Varys称毒药为tears of Lys，无色无痕；自己曾劝Jon用taster，却被以男子气概为由拒绝。",152:"Eddard追问下毒者。",153:"Varys不直接定名，只暗示Jon亲近且受恩的Ser Hugh在Lysa离城后留下发达，又恰在Eddard问话前死去。",154:"Eddard感到头痛如中毒，意识到Hugh可能是层层阴谋的一环，并问Jon调查了什么。",155:"Varys只答：他在asking questions。",
}
SUMMARIES = [S[i] for i in range(1, 156)]

KEY_NOTES = {
2:"Eddard把Hugh之死与调查联系，是时间与阵营上的合理怀疑，不是已证实因果；happenstance一词保留了不确定。",
6:"War should not be a game直接拆解tourney浪漫化：Hugh的母亲得到的是铠甲遗物，而不是荣耀叙事。",
8:"paid dearly把欠smith的钱与死亡代价叠在同一句中，Eddard用冷峻双关拒绝只按市场价值衡量铠甲。",
9:"盾徽清单与上一章Catelyn识别sigils呼应；heraldry既组织营地空间，也组织封建政治。",
12:"Barristan用谚语给Robert保留体面退路，说明劝谏king往往先需管理其自尊。",
17:"Eddard的直言只有凭少年友谊才可能奏效；其他courtier很难公开说king太胖。",
19:"breastplate stretcher是让新手去找不存在工具的经典恶作剧，短暂恢复Robert与旧友的轻松关系。",
21:"笑声中Eddard仍读取gold hair与green eyes，调查者视角已使日常人物也成为家族pattern材料。",
25:"Lannister squires未做错事；Eddard担忧的是结构性包围与patronage，而非两个boys个人有罪。",
27:"Robert爱的主要是Lyanna想象，Eddard记得的则是会反驳他的真实妹妹；beauty与iron构成关键纠正。",
31:"Barristan不用危险劝退Robert，而用比赛不公平伤其warrior pride，比直接命令更有效。",
33:"Eddard立刻接住这一论点，显示他了解Robert把被让胜看得比受伤更不可忍。",
36:"Robert投甲并发死亡威胁，却仍把Eddard留下，呈现王权暴躁与私人依赖同时存在。",
42:"you or Jon should have been king既是醉后坦白，也把Robert的统治失败归给推举者，回避自身选择。",
46:"Robert能准确判断Joffrey撒谎却未在事件现场制止Lady被杀，识别事实与承担责任并非一回事。",
48:"他不退位的理由不是热爱治理，而是害怕继承结果；最低限度的责任感与逃离欲望被绑在一起。",
50:"自称good king后要求Eddard附和，笑点建立在他需要明知不真诚的确认。",
54:"Eddard的未来图景高度线性：prove guilt→Robert listens→Lannisters fall；希望让他暂时低估court反应与证据难题。",
56:"Cersei缺席可能是夫妻决裂、抗议或策略；Eddard把它读成hope，显示早餐情绪正在影响判断。",
61:"hand that feeds them把Sandor的忠诚降为受雇犬性，也忽略他与Gregor之间独立的私人敌意。",
65:"Sandor在第二pass适应Jaime的seat shift，胜利来自观察与调整，而非单纯蛮力。",
69:"黄金形象变成盲目踉跄的囚笼；ornament既制造荣耀，也在摔落后制造喜剧和实际障碍。",
71:"这些是长期流传的严重指控，Eddard没有亲见；无剧透阅读必须区分reputation与已证明事实。",
72:"流言数量形成pattern，却仍可能混杂真相、恐惧与夸张；Sandor上一章的第一手故事只证实烧伤来源。",
74:"mare in heat使Loras华丽布置获得战术功能；是否有意要到Littlefinger稍后才明确提出。",
75:"Eddard说出的安全保证与眼前Hugh尸体冲突，raw in throat把父亲安慰孩子的困难身体化。",
77:"just there强调Loras瞄准精确；胜利既依赖skill，也依赖对Gregor坐骑弱点的安排。",
80:"horse从Gregor力量象征瞬间变成怒火受害者，群众反应由cheers到shrieks完成道德翻转。",
82:"Sandor不砍Gregor裸脸可能出于控制、规则残余、创伤或复杂兄弟心理；文本只展示选择，不确定动机。",
83:"Robert最有效的王者时刻来自battlefield voice而非行政能力；二十把剑也说明命令背后有集体武力。",
88:"Sandor拒绝Ser却获得真正救人行为带来的public love，直接延续上一章对称号与德性的拆分。",
89:"Littlefinger把危险trick当作聪明算计欣赏；这符合他重结果与可操纵弱点的观察方式。",
92:"commoner击败贵族是tourney暂时开放性的一面；巨奖也使Eddard的稳定职位在当下失去吸引力。",
93:"伤亡账单再次证明blunted不等于安全；Eddard的desperately pleased带有刚避过政治谋杀可能性的后怕。",
96:"dancing双关制造姐妹信息差：Sansa理解court舞蹈，Arya指water dancing剑术。",
99:"Syrio的训练培养多感官、平衡和机动，而Eddard用传统slash-and-parry标准判断，因此误认部分内容为nonsense。",
104:"Arya一边承诺小心一边平稳换腿，动作本身证明古怪训练已产生效果。",
106:"Eddard复述Littlefinger版本时把争议信息压成事实链；why仍无法回答，正是该链尚需验证的信号。",
108:"Gendry血缘结论基于可见家族特征和排除法，Eddard确信不等于法律证明，但比dagger传闻有直接观察支持。",
111:"Eddard假设baseborn children无法威胁trueborn继承，因此仍看不出Jon调查意义；他尚未找到lineages中的pattern。",
114:"Varys用粗布、泥、汗味改写其平常silk/lilac形象，证明身份很大程度由可控制的感官信号构成。",
123:"Varys说they hoped与doomed都是情报判断；他没有在此出示证人或物证，读者应保留证据等级。",
127:"Cersei的forbid可同时是真反对与反向刺激；Varys只提供后一解释，符合Robert性格但仍属动机推断。",
129:"Varys描述的是一套可否认性方案：chaos掩护行为、grief重写意图、royal pardon或execution清除责任。",
133:"Varys延迟报警的理由有现实性，也意味着他把Robert生命作为测试Eddard的风险筹码。",
137:"realm/self二分听来清楚，却由掌握秘密的Varys定义；他对Eddard的认可也可能具有招募功能。",
139:"songs for spiders呼应Sansa为无名knight难过：秘密劳动不产生公开荣耀，也更容易被权力牺牲。",
141:"三句平行结构把职位忠诚拆成个人核心欲望；尤其Littlefinger loves Littlefinger是高度凝练的风险评估。",
143:"paper shield意为名义防护一遇真剑即破；Varys用Jaime的破誓历史质疑整个制度可靠性。",
145:"Varys的核心不是阴谋不存在，而是truth without proof在政治上不足；Eddard的道德确信无法替代可呈示证据。",
147:"公开相互轻蔑成为秘密合作的cover；两人的关系从观察与试探进入有限联盟。",
151:"tears of Lys的无色无痕解释Pycelle为何可能诊断自然急病，但毒药名称与Varys陈述仍需独立证实。",
153:"Varys把Hugh的受恩、留下、发达和死亡串成暗示，却故意不明确说他下毒；讽刺语气引导Eddard自行得出结论。",
155:"asking questions与Jon的死、Hugh的死、Eddard当前危险形成镜像：调查行为本身正在触发对手反应。",
}

STAGES = [
(1,17,"Hugh遗体使tourney代价具体化；Eddard与Barristan转去阻止Robert参赛，发现旧铠甲已容不下如今的king。"),
(18,55,"Robert由玩笑转向王位困境，承认Joffrey撒谎与自己想逃离；童年早餐记忆又让Eddard恢复对旧友的希望。"),
(56,93,"joust决赛从Sandor击落Jaime发展到Gregor失控袭击Loras；Sandor救人夺冠，archery与melee随后完成。"),
(94,112,"姐妹短暂和睦，Arya展示Syrio训练；深夜Eddard重新整理dagger、Jon与Robert baseborn children，却仍无答案。"),
(113,147,"Varys伪装来访，声称Lannisters试图借melee谋杀Robert，并以缺乏证据、宫廷忠诚脆弱说明不能公开指控。"),
(148,155,"Eddard追问Jon之死；Varys提出tears of Lys与Ser Hugh暗示，最后把杀机归结为Jon持续asking questions。"),
]

BACKGROUNDS = {
1:"**Ser Hugh：** Jon Arryn former squire，刚由Robert册封；前一日被Gregor长枪刺穿喉部死亡。",
6:"**silent sisters：** Faith of the Seven中负责清洗、包裹和准备遗体下葬的女性宗教人员。",
14:"**Robert’s warhammer：** Robert在Rebellion时期的标志武器；此处与穿不下的旧armor并置，象征过去战士身份。",
21:"**Lancel及同伴：** Cersei的Lannister cousins，被安排为Robert squires；Eddard担忧宫廷职位被queen亲族占据。",
31:"**melee规则：** 多名参赛者混战直至最后一人站立；即便使用blunted weapons，混乱仍可造成重伤和死亡。",
46:"**政治婚姻：** Jon促成Robert与Cersei结合，以绑定Tywin并防备Viserys未来复辟；这是Robert对当年理由的回述。",
59:"**赌注：** Littlefinger与Renly公开押注joust结果，延续tourney作为贵族娱乐与高额赌博场域。",
71:"**历史指控：** Aegon与Elia在King’s Landing陷落时被杀；Gregor被传为凶手，但本章明确以some said/whispered呈现。",
74:"**战术条件：** Loras骑mare，Gregor骑stallion；stallion闻到发情mare气味后难以控制。Littlefinger随后推断这是预谋。",
83:"**battlefield voice：** Jon曾教Robert commander需能让声音压过战场；本段显示Robert仍保留这种能力。",
92:"**Anguy：** 来自Dornish Marches的commoner，赢得archery prize；本章只写他拒绝Hand’s guard邀请。",
97:"**Dance of the Dragons：** 此处是多首交织ballads的表演名称；不要与后文可能出现的历史解释混同。",
99:"**water dancing：** Syrio教授的Braavosi sword style，重平衡、速度、感官与身体控制，不等同court dancing。",
106:"**dagger证据链：** Littlefinger称自己曾在tourney wager中输给Tyrion；该所有权说法尚无独立核验。",
109:"**Robert children：** Gendry之外，Eddard已知Storm’s End男孩与Vale长女；baseborn身份通常缺少继承权。",
123:"**情报状态：** Varys声称Lannisters计划在melee中制造Robert意外死亡；本章没有给出执行者姓名或物证。",
143:"**Kingsguard：** 七名white cloaks宣誓保护king；Varys认为多数成员忠诚对象已偏离誓言，这属于其评估。",
151:"**tears of Lys：** Varys所称的罕见无色甜味毒药，据说不留痕迹；此前Pycelle把Jon死亡描述为突然高烧。",
153:"**Ser Hugh线索：** Hugh受Jon提携、Lysa离城后仍留王都并获knighthood；Varys暗示其与投毒有关，但未明确证明角色。",
}

EXTRA_VOCAB = [
("last vigil","/læst ˈvɪdʒəl/","n.","最后守灵","Barristan with Hugh"),("rough-hewn","/ˌrʌf ˈhjuːn/","adj.","轮廓粗犷的；粗凿的","features"),("happenstance","/ˈhæpənstæns/","n.","偶然事件","suspicious death"),("needless","/ˈniːdləs/","adj.","不必要的","tourney death"),("herald","/ˈherəld/","v.","标示；宣告","shields identify tents"),("wisps","/wɪsps/","n.","缕；丝","morning mist"),("buckle","/ˈbʌkəl/","v.","扣紧","armor"),("oaf","/oʊf/","n.","蠢笨的人","Robert’s insult"),("swineherd","/ˈswaɪnhɜːrd/","n.","猪倌","mocking squires"),("bravado","/brəˈvɑːdoʊ/","n.","逞强的豪言","drunken promise"),("curdle","/ˈkɜːrdəl/","v.","凝结；由愉快转坏","mirth"),("sulking","/ˈsʌlkɪŋ/","adj.","生闷气的","Robert’s description"),("seemly","/ˈsiːmli/","adj.","合乎身份礼仪的","king in melee"),("craven","/ˈkreɪvən/","n./adj.","懦夫；胆怯的","Robert’s insult"),("puissant","/ˈpjuːɪsənt/","adj.","强大的；有权势的","warrior"),("wax fond","/wæks fɑːnd/","phr.v.","越说越深情怀念","Robert’s memory"),("concession","/kənˈseʃən/","n.","让步；有限采用","ornament"),("couch a lance","/kaʊtʃ ə læns/","phr.v.","把长枪夹稳准备冲刺","joust"),("destrier","/ˈdestriər/","n.","骑士战马","Jaime’s horse"),("implacable","/ɪmˈplækəbəl/","adj.","无法平息的；冷酷不屈的","ferocity"),("disquiet","/dɪsˈkwaɪət/","n.","不安","Ned watches Gregor"),("unaccountably","/ˌʌnəˈkaʊntəbli/","adv.","无法解释地","disappearances"),("trumpet","/ˈtrʌmpɪt/","v.","像号角般鸣叫","stallion"),("disentangle","/ˌdɪsɪnˈtæŋɡəl/","v.","挣脱纠缠","Gregor rises"),("raucous","/ˈrɔːkəs/","adj.","沙哑喧闹的","laughter"),("forestall","/fɔːrˈstɔːl/","v.","预先阻止","another plot"),("unheralded","/ʌnˈherəldɪd/","adj.","无名的；未被宣扬的","Anguy"),("rudiments","/ˈruːdɪmənts/","n.","基础知识与动作","sword training"),("close","/kloʊs/","adj.","闷热不通风的","room"),("by-blow","/ˈbaɪbloʊ/","n.","非婚生子女（旧式）","Robert’s children"),("roughspun","/ˈrʌfspʌn/","n./adj.","粗纺布；粗布制的","Varys disguise"),("cowl","/kaʊl/","n.","兜帽","hidden face"),("cloying","/ˈklɔɪɪŋ/","adj.","甜腻得令人厌烦的","public voice"),("beside oneself","/bɪˈsaɪd wʌnˈself/","phr.","情绪失控的","performed grief"),("bide one’s time","/baɪd wʌnz taɪm/","phr.","等待时机","future attempt"),("in a twinkling","/ɪn ə ˈtwɪŋklɪŋ/","phr.","转瞬间","execution"),("paper shield","/ˈpeɪpər ʃiːld/","metaphor","徒有其名的保护","Kingsguard"),("taster","/ˈteɪstər/","n.","试毒者","Jon’s meals"),("untimely","/ʌnˈtaɪmli/","adj.","过早的；不合时宜的","Hugh’s death"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def extract_blocks():
    blocks = extract_range(283, 299, "EDDARD", "CH30")
    # Varys's sentence continues across pp.297–298; uppercase “Ser” defeats auto-merge.
    blocks[140]["text"] = str(blocks[140]["text"]) + " " + str(blocks[141]["text"])
    blocks[140]["end_page"] = blocks[141]["end_page"]
    del blocks[141]
    for order, block in enumerate(blocks, 1):
        block["order"] = order
        block["id"] = f"CH30-P{int(block['page']):03d}-{order:03d}"
    return blocks

def main():
    blocks = extract_blocks()
    write_chapter(
        out=OUT, chapter=30, pov="EDDARD", page_start=283, page_end=299,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Robert的warrior identity、tourney风险、Eddard的证据判断与Varys情报的可靠性。",
        vocab=VOCAB,
        guide="Ser Hugh死后，Eddard与Barristan借Robert最在意的公平和warrior pride，成功阻止他参加melee。Robert随后坦白自己厌恶统治、识破Joffrey在Trident撒谎，却因害怕Cersei操控继承而不敢退位；短暂的童年回忆又让Eddard相信旧友仍可挽救。joust中Sandor击落Jaime，Loras利用mare使Gregor坐骑失控；Gregor杀马并袭击Loras，Sandor出手救人后成为champion。深夜Varys伪装来访，声称Cersei公开禁止Robert参赛本是反向激将的谋杀方案，又说Jon死于tears of Lys，并以讽刺方式暗示Ser Hugh涉入。所有这些都推进调查，但Varys没有提供可公开验证的物证；情报、推断与事实仍必须分层。",
        people=[
            ("Eddard Stark","本章视角；阻止Robert参赛、观看tourney，并从Varys处取得Jon中毒情报"),
            ("Robert Baratheon","仍认同旧日warrior身份，厌恶kinging；因公平与自尊放弃melee"),
            ("Varys","伪装秘密来访，提出Robert谋杀阴谋、tears of Lys与Ser Hugh暗示"),
            ("Sandor Clegane","击落Jaime并从Gregor剑下救出Loras，拒绝Ser称号却成为champion"),
            ("Gregor Clegane","被Loras战术击落后杀死坐骑、袭击对手，与Sandor真剑相斗"),
            ("Loras Tyrell","以mare影响Gregor stallion并获胜，遇袭后把championship让给救命者"),
            ("Ser Hugh","Jon former squire；死亡后被Varys暗示可能与Jon中毒有关"),
            ("Sansa / Arya","Sansa沉浸tourney；Arya以Syrio训练展示另一种身体与荣誉教育"),
        ],
        terms=[
            ("melee","多人数混战，临时联盟会形成又瓦解；本届由Thoros获胜"),
            ("breastplate stretcher","不存在的工具，用于捉弄缺乏经验的squires"),
            ("mare in heat","发情母马；气味令Gregor stallion难以控制，成为Loras战术条件"),
            ("paper shield","Varys对多数Kingsguard只具名义保护作用的比喻"),
            ("tears of Lys","Varys称杀死Jon的罕见无色毒药，声称clear、sweet且不留痕迹"),
        ],
        synthesis="Chapter 30反复区分外在职位与实际能力。Robert是king，却只有用battlefield voice时最像有效统治者；他穿不下象征过去的armor，也无法从胜利夺来的王位中获得生命感。Sandor不是knight，却救下Loras并赢得群众；Gregor有正式Ser称号，却在失败后杀马袭人。Kingsguard名为shield，Varys却称其paper。调查层面同样如此：Littlefinger和Varys都能提供结构完整的故事，但故事的解释力不等于证据力。Eddard需要Robert这位私人朋友，也需要能在公开政治中承受质询的proof；本章让他在友情带来的乐观与Varys揭示的制度脆弱之间来回摆动。",
        contrasts=[
            "**war／game：** Eddard认为战争不该娱乐化，tourney却不断以真实伤亡模仿war。",
            "**旧armor／当前身体：** Robert仍认同年轻warrior，却已无法穿进那套物质象征。",
            "**king／fighter：** 王位要求克制，Robert渴望的却是可亲自击打的明确敌人。",
            "**Ser Gregor／非Ser Sandor：** 正式称号与真正保护行为再次分离。",
            "**golden spectacle／blood and mud：** Jaime、Loras的华丽外观不断被摔落、失控与真剑暴力打断。",
            "**truth／proof：** Varys声称知道阴谋与毒药，Eddard却仍缺少可呈给Robert的证据。",
        ],
        questions=[
            "Varys关于melee谋杀方案的消息来自谁，是否能独立验证？",
            "Ser Hugh在Jon中毒中究竟扮演了什么角色，他为何随后被knighted？",
            "Jon关于Robert baseborn children和lineages究竟在追查什么pattern？",
            "Eddard与Varys的秘密合作能否在公开council中保持不被察觉？",
        ],
        extraction_notes="PDF pp.283–299校勘后共155段；自动提取曾把pp.297–298间Varys同一段中的连续评价误切，已合并。共7处跨页续段：pp.283–284、285–286、289–290、291–292、293–294、295–296与297–298。PDF p.283页面原图本身在首段I stood前缺少起始引号，按原页面保留。",
    )
    print(f"Wrote Chapter 30 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
