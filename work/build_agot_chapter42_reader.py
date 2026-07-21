#!/usr/bin/env python3
"""Build Chapter 42 (TYRION) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter41_reader import VOCAB as BASE_VOCAB

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"/"AGOT_逐章精读"

S={
1:"Tyrion与Bronn在high road旁aspen林歇脚；他捡deadwood并承认不熟悉生火。",
2:"Bronn认为fire会从远处招来clansmen，斥Tyrion在求死。",
3:"Tyrion继续弯腰拾柴，并反问Bronn如何活下去；两人清晨已被Corbray逐出Bloody Gate。",
4:"Bronn主张两人轻装夜行、白天躲藏、避路禁火，以速度和隐蔽穿越。",
5:"Tyrion讽刺计划看似漂亮，却预言Bronn会先死。",
6:"Bronn露出Vardis盾击留下的断牙，反问Tyrion是否真能活更久。",
7:"Tyrion指出夜骑山路易坠崖、马匹会累死，且clans无论如何都在观察，选择慢行。",
8:"Bronn由此判断两人已经是dead men。",
9:"Tyrion宁愿舒适地死，认为fire、热食与士气比隐蔽更重要，并嘲笑Lysa给的硬粮。",
10:"Bronn说自己能hunt，又试探若带走Tyrion的horse独逃会怎样。",
11:"Tyrion平静回答自己大概会死。",12:"Bronn问他是否不相信自己真会这样做。",
13:"Tyrion相信Bronn会为生存立刻背弃，并以他结束重伤Chiggen生命为证。",
14:"Bronn说Chiggen必死且呻吟会引敌，双方只是同行者，并明确自己替Tyrion战斗却不爱他。",
15:"Tyrion说自己要的是Bronn的blade，不是love。",
16:"Bronn称赞Tyrion像sellsword一样大胆，追问他如何知道自己会出战。",
17:"Tyrion说只是tossed dice；他从inn上Bronn帮助Catelyn判断其动机不是duty或honor，而是gold。",
18:"Bronn把flint扔给Tyrion。",
19:"Tyrion解释Starks只会小额酬谢且厌恶无honor的sellswords，自己才是Bronn更有利的买主；第一次打火失败。",
20:"Bronn警告Tyrion的bold tongue迟早被割。",
21:"Tyrion继续直称Bronn是scum，却说明他聪明地发现Catelyn不再需要自己、Tyrion仍需要且Lannisters有gold。",
22:"Bronn接手knife与flint，一次便点燃bark。",
23:"Tyrion称他粗鄙但有用、剑术近Jaime，承诺只要保自己活着便给gold、land或women。",
24:"Bronn一边吹旺火一边问若Tyrion死了如何。",
25:"Tyrion笑说那样Bronn会成为真心哀悼者，因为报酬也随之消失。",
26:"Bronn接受交易，声明sword归Tyrion使用，但不跪、不逢迎，也不做toady。",
27:"Tyrion承认Bronn会为更高利润背叛，并预先承诺匹配任何报价，随后要他找supper。",
28:"Bronn让Tyrion照顾horses，持dirk进林hunt。",
29:"一小时后马已照料、火已升起，young goat在烤；Tyrion只遗憾没有wine。",
30:"Bronn还想要woman与十二把swords；磨剑声给Tyrion奇异安心，他又悲观地安排watch。",
31:"Tyrion认为clansmen睡前就会出现。",32:"Bronn看出他另有plan。",
33:"Tyrion称其只是又一次hope与toss of dice。",34:"Bronn确认赌注是两人性命。",
35:"Tyrion说别无选择，享用烤肉并拿sky cell的boiled bean反衬当前满足。",
36:"Bronn指出Tyrion仍给了Mord一袋gold。",37:"Tyrion说Lannister always pays his debts。",
38:"回忆中Tyrion兑现书面承诺，把gold给惊讶的Mord，还邀请他日后到Casterly Rock取余款。",
39:"Bronn切肉，Tyrion用stale bread做trenchers；Bronn问抵达river后做什么。",
40:"Tyrion先想享乐，再去Casterly Rock或King’s Landing调查某把dagger。",
41:"Bronn确认Tyrion此前说实话，knife确实不是他的。",42:"Tyrion以反问玩笑回应自己是否像liar。",
43:"夜深后Tyrion以shadowskin与saddle躺下，抱怨clansmen迟迟不来。",
44:"Bronn说对方可能怀疑如此公开的营地是trap。",
45:"Tyrion开玩笑应唱歌把他们吓走，开始whistle。",
46:"Bronn说Tyrion发疯了，同时用dirk清指甲。",47:"Tyrion问他为何不爱music。",
48:"Bronn说想听音乐就该让singer当champion。",
49:"Tyrion想象Marillion用woodharp抵挡Vardis，继续吹曲并问Bronn是否认识。",
50:"Bronn说inns与whorehouses偶尔会听到。",
51:"Tyrion认出Myrish歌The Seasons of My Love，并开始讲十三岁时与Jaime救下一个约大一岁的孤女。",
52:"Jaime想追outlaws；Tyrion留下照顾受惊女孩，带她去inn进食。",
53:"本段写十三岁的Tyrion与约十四岁女孩发生露骨性关系及其情感反应；不复录细节。",
54:"Bronn对Tyrion会陷入爱情感到好笑。",55:"Tyrion自嘲荒谬，随后承认自己娶了她。",
56:"Bronn惊讶Casterly Rock的Lannister竟娶crofter’s daughter，追问如何办到。",
57:"Tyrion说靠谎言、silver和醉septon秘密成婚并同住fortnight；septon向Tywin告发后婚姻终结，回忆仍令他荒凉。",
58:"Bronn问Tywin是否只是把女孩送走。",
59:"本段涉及约十四岁女孩被安排进入商业性关系及Jaime向Tyrion提供的解释；不复录具体性内容。",
60:"本段描写Tywin命guards对约十四岁女孩实施集体性暴力，并强迫十三岁的Tyrion观看和参与；不复录细节。",
61:"长久沉默后Bronn说无论十三、三十还是三岁，自己都会杀死这样对待他的人。",
62:"Tyrion说Bronn或许终有机会，并用pay debts暗示对Tywin的怨恨，然后准备睡觉。",
63:"Tyrion梦见自己成为sky-cell gaoler，挥strap把father逼向abyss。",
64:"Bronn低声急促警告Tyrion。",
65:"Tyrion瞬间醒来，见Bronn持双刃戒备；他示意不动，主动邀请暗影中的人来分享fire与goat。",
66:"暗处声音宣称mountain和goat都属于他们。",67:"Tyrion顺势承认goat归属并问对方身份。",
68:"Gunthor son of Gurn持long knife现身，叫Tyrion死后告诉gods是谁送他去。",
69:"巨大的Shagga son of Dolf持club与axe现身，以武器相击逼近。",
70:"至少十名clansmen依次报name；Tyrion等他们结束才以Clan Lannister格式自报并愿赔goat。",
71:"首领Gunthor问Tyrion能给什么。",
72:"Tyrion提出silver，并精确把自己的hauberk、battle-axe分别匹配Conn与Shagga。",
73:"Conn指出Tyrion只是在用本就会被夺走的财物付款。",
74:"Gunthor同意，宣称所有物资已属于Stone Crows，只让Tyrion选择死法。",
75:"Tyrion以活到八十、wine与成人性享乐的粗俗愿望作答。",
76:"Shagga大笑，其他人不全买账；Gunthor命夺horses、杀Bronn、留Tyrion做低贱劳动和娱乐。",
77:"Bronn跳起，问谁先死。",
78:"Tyrion喝止战斗，提出若安全护送，Tywin会用gold奖赏Stone Crows。",
79:"Gunthor说lowland lord的gold与halfman promise一样无价值。",
80:"Tyrion转而用courage与羞耻激将，嘲Stone Crows躲石后怕Vale knights。",
81:"Shagga与Jaggot被激怒；Tyrion忍住spear威胁，又贬低他们偷来的weapons和steel。",
82:"Shagga以针对Tyrion生殖器的暴力威胁回应其嘲讽。",
83:"Gunthor制止Shagga，因族中饥饿且steel比gold有用，询问Tyrion能给多少武器。",
84:"Tyrion微笑承诺swords、lances、mail以及更大报酬：整个Vale of Arryn。",
}
SUMMARIES=[S[i] for i in range(1,85)]

KEY_NOTES={
1:"曾有Morrec生火的Tyrion如今亲自拾柴，身份落差被写成弯腰、back ache与不熟练的具体劳动。",
2:"Bronn把fire只视为visibility risk；Tyrion随后把它当诱饵、士气和谈判舞台，同一物件承担相反策略。",
4:"Bronn方案符合小队隐蔽常识，却低估夜间山路、马力与clan观察网；合理不等于适合全部约束。",
5:"forgive me if I do not linger to bury you以礼貌句式包装死亡预测，是Tyrion惯用的防御性幽默。",
7:"Tyrion不是证明慢行安全，而是指出隐蔽方案也有致命代价，并接受clans必然找到他们的前提。",
9:"die comfortable听似享乐主义，实则维持warmth、food与morale；在无力避敌时，他把目标从逃避接触改为准备接触。",
10:"Bronn公开试探abandonment既是威胁也是合同谈判：他要求Tyrion证明合作收益高于独逃。",
13:"Tyrion准确读出Bronn的生存伦理；提Chiggen也让‘会背叛’从抽象评价落到已发生行为。",
14:"Bronn把mercy killing、noise discipline与friendship否认压在一起；他的原则冷酷却可预测。",
15:"blade not love确立双方交易型关系，也区别于封建忠诚与私人友爱。",
17:"Tyrion重构inn行为的incentive：同一帮捕动作在knights是duty，在sellswords是预期reward。",
19:"Starks评价既含洞察也带Tyrion阶级偏见；他用lowborn scum刺激Bronn，同时证明Lannister市场更匹配。",
21:"第二次打火仍失败与言辞成功并置：他能点燃Bronn的利益，却点不燃bark，需要对方补足实际技能。",
22:"Bronn一击出spark把他们的互补关系具象化：Tyrion提供策略与资源，Bronn提供技术与暴力。",
25:"报酬绑定Tyrion存活，形成最简单的incentive alignment；Bronn的真心悲伤不是爱，而是未来收益消失。",
26:"Bronn出售service但拒绝identity surrender；不bend knee划出雇佣合同与vassalage边界。",
27:"match their price把未来背叛风险转成竞价问题，但并不能防止非金钱动机或Tyrion无力支付。",
30:"磨剑声让Tyrion安心，说明信任并非相信Bronn善良，而是相信他会维护仍有价值的investment。",
33:"dice motif从Eyrie courtroom延续到mountain：Tyrion能改善赔率，不能消除随机与对手选择。",
35:"boiled bean回扣sky cell饥饿；当前粗硬goat因比较基准变化成为幸福。",
37:"家族格言式句子把兑现Mord reward变成reputation mechanism：未来承诺可信，才能继续买到危险中的帮助。",
38:"付清gold也把曾虐待自己的Mord转成潜在future asset；Tyrion的报复常延后，交易可先于情绪。",
40:"dagger使本章生存线重新连接Bran刺杀谜团；Tyrion仍只有questions，没有答案。",
42:"Do I look a liar既是玩笑也是回避：Bronn需要根据共同经历而非Tyrion自我声明判断。",
43:"friends是反讽称呼；Tyrion故意把clansmen预设为可谈对象，先在语言中改变关系框架。",
44:"公开营火造成signal ambiguity：既可能是愚蠢，也可能是trap；Tyrion用对方谨慎为自己争取准备时间。",
49:"用woodharp挡剑的荒诞图像缓解等待恐惧，也把Marillion传播功能与Bronn实战功能再次区分。",
51:"stars bright and merciless as truth触发回忆；‘truth’既指Bronn刚问dagger，也预告Tyrion生命中被权威告知的另一种真相。",
53:"本段涉及未成年人露骨性内容，不逐字复录。分析重点是：Tyrion把初次亲密经验与被爱、勇气和song永久绑定。",
55:"I married her延迟到自嘲和whistling之后才说，短句揭开关系对十三岁Tyrion的认真程度。",
57:"fortnight的短暂家庭游戏与多年desolate形成时间反差；dying fire把爱情回忆转入毁灭段落。",
59:"本段含未成年商业性剥削信息，不复录细节。Tyrion当时被Jaime提供的解释重新定义整段相遇，信任损伤来自‘一切被安排’。",
60:"本段含针对未成年人的集体性暴力与强迫参与，不复录细节。行为责任在Tywin及执行者；支付、命令或对女孩身份的指称都不能构成consent。",
61:"Bronn第一次不用笑或交易回应，而以杀意承认伤害严重性；年龄并不减轻施害者责任。",
62:"pay debts从守信口号转为复仇暗语，同一句家族价值同时维系contracts与延续创伤。",
63:"梦把sky cell角色反转：Tyrion不再是被Mord逼向蓝色，而是拥有strap、身体变大并把Tywin逼向abyss。",
65:"醒来即邀请敌人共享fire说明营火本来就是接触策略；他先给food与hospitality框架，不等对方完成attack。",
66:"Our mountain, our goat否定lowland property rules；Tyrion要谈判必须先承认对方的territorial premise。",
68:"Gunthor以完整父系name和Stone Crows身份报出，证明clans并非无名bandits，而有自己的荣誉与组织语言。",
70:"Tyrion模仿Clan naming把House Lannister翻译成对方可识别的kin group，同时耐心让每人完成自我展示。",
72:"他不笼统许诺财富，而当场识别Conn、Shagga欲望与装备fit，试图把掠夺变成exchange。",
73:"Conn拆穿现有财物不构成让步，迫使Tyrion提出他们无法单纯夺取的future value。",
75:"粗俗死法回答拒绝接受Gunthor设定的即时恐惧，也用Shagga laughter打破一致敌意；这不是实际条件。",
78:"Tywin gold因不可验证、难送达而缺乏可信度；Tyrion下一步必须找到clans更急迫且可想象的价值。",
80:"当greed无效，Tyrion攻击group identity；这是高风险激将，目的在让他们证明勇气而继续听。",
81:"不flinch是表演成本：只有在spear近脸时仍贬低weapon，他的steel offer才显得不只是求饶话术。",
82:"Shagga以性化身体伤害威胁成人Tyrion；此处分析其恐吓升级，不美化或复述更多细节。",
83:"mothers hungry与steel fills mouths揭示实际约束：clan需要的不只是个人gold，而是能改变军事与生存结构的装备。",
84:"give you the Vale把交易从escort fee升级为政治联盟提案；具体如何兑现仍完全未知，是chapter cliffhanger。",
}

STAGES=[
(1,15,"Tyrion拒绝Bronn夜行隐蔽方案，以fire、food和可预见接触重设high road生存策略；两人坦白关系只基于利益。"),
(16,28,"Tyrion解释自己如何押中Bronn会做champion，并用持续报酬、匹配报价与不要求跪拜建立雇佣合同。"),
(29,50,"营火、goat与磨剑形成诱饵；Tyrion等待clansmen时谈Mord债务、dagger问题与一首Myrish旧歌。"),
(51,63,"歌曲触发Tyrion十三岁秘密婚姻及其被Tywin暴力摧毁的创伤回忆；睡梦中他反转sky-cell权力，攻击father。"),
(64,84,"Stone Crows包围营地；Tyrion依次用hospitality、clan language、物资、幽默、羞耻与steel需求把处刑转为联盟谈判。"),
]

BACKGROUNDS={
1:"**high road：** Bloody Gate至riverlands的山路，狭险且受mountain clans袭扰；Lysa让两人带物资离开却不提供全程保护。",
3:"**放逐：** Ser Lyn奉Lysa命把Tyrion、Bronn送出Bloody Gate并禁止返回Vale核心区域。",
13:"**Chiggen：** high road伏击中腹部中箭的sellsword；Bronn为停止呻吟和吸引攻击而结束其生命，并对Catelyn隐瞒。",
17:"**inn选择：** Bronn、Chiggen本无lord oath，却在Catelyn号召下协助拘捕Tyrion；Tyrion事后以expected reward解释。",
19:"**Stark service：** Tyrion认为Starks偏好courage、loyalty、honor，不会长期收纳Bronn型sellsword；这是他的判断，不是正式政策。",
26:"**雇佣关系：** Bronn提供sword service换取未来报酬，不宣誓fealty；双方都公开承认可因利益变化而终止。",
38:"**Mord debt：** Tyrion曾书面许诺gold换取向Lysa传递confession；获释后按约付清，并承诺未来余款。",
40:"**dagger mystery：** Catelyn认为Bran袭击所用dagger属于Tyrion；Tyrion否认并准备追查真正来源。",
51:"**年龄事实：** Tyrion自称当时十三岁，女孩scarcely a year older，约十四岁；因此相关露骨内容不复录。",
53:"**安全说明：** 本段涉及两名未成年人的露骨性描写；保留稳定编号、页码、非露骨段意和叙事作用。",
59:"**安全说明：** 本段涉及未成年商业性剥削叙事；不复录具体性内容，也不将付费或身份标签误当consent。",
60:"**安全说明：** 本段涉及对约十四岁女孩的集体性暴力及对十三岁Tyrion的强迫参与；保留事件性质与责任分析，不复录过程。",
63:"**dream continuity：** sky cell曾由Mord持strap把Tyrion逼近悬崖；梦把Mord位置、身体力量和target全部反转。",
68:"**Stone Crows：** Mountains of the Moon clan之一；使用父名、自有chief与集体领地观念，不服从Vale lords。",
70:"**Clan Lannister：** 正式称呼是House Lannister；Tyrion故意改用Clan以匹配Stone Crows的社会语言。",
83:"**clan需求：** Gunthor明确说族中mothers挨饿，steel比gold更能获得食物；武器装备因此是核心谈判资源。",
}

EXTRA_VOCAB=[
("copse","/kɑːps/","n.","小树林","aspens"),("aspen","/ˈæspən/","n.","白杨；山杨","shelter"),("splintered","/ˈsplɪntərd/","adj.","劈裂的","branch"),("undergrowth","/ˈʌndərɡroʊθ/","n.","林下灌木草丛","deadwood"),("hole up","/hoʊl ʌp/","v.","躲藏起来","day travel"),("crag","/kræɡ/","n.","峭壁；嶙峋岩峰","mountains"),("veritable","/ˈverɪtəbəl/","adj.","名副其实的；十足的","ironic feast"),("kindling","/ˈkɪndlɪŋ/","n.","引火物","bark strips"),("flint","/flɪnt/","n.","燧石","fire starting"),("smolder","/ˈsmoʊldər/","v.","闷烧","bark"),("toady","/ˈtoʊdi/","n.","谄媚跟班","Bronn refuses"),("haunch","/hɔːntʃ/","n.","动物后腿肉","goat"),("kid","/kɪd/","n.","小山羊；山羊肉","meal"),("oilstone","/ˈɔɪlstoʊn/","n.","油磨石","sword honing"),("rasp","/ræsp/","n.","刺耳摩擦声","steel on stone"),("stake","/steɪk/","n.","赌注","lives"),("precipice","/ˈpresəpɪs/","n.","悬崖；险境","sky cell"),("drawstring","/ˈdrɔːstrɪŋ/","n.","束口绳","purse"),("trencher","/ˈtrentʃər/","n.","用硬面包做的食盘","stale bread"),("halfmoon","/ˈhæfmuːn/","n.","半月","night sky"),("lure","/lʊr/","v.","诱入","trap"),("Myrish","/ˈmaɪrɪʃ/","adj.","来自Myr的","song"),("dog someone’s heels","/dɔːɡ ˈsʌmwʌnz hiːlz/","v.","紧追不舍","pursuers"),("crofter","/ˈkrɔːftər/","n.","小佃农","girl’s father"),("in a lather","/ɪn ə ˈlæðər/","phr.","激动焦急","Jaime"),("septon","/ˈseptən/","n.","Faith of the Seven男祭司","secret wedding"),("desolate","/ˈdesələt/","adj.","凄凉孤绝的","Tyrion feeling"),("barracks","/ˈbærəks/","n.","兵营","trauma setting"),("abyss","/əˈbɪs/","n.","深渊","dream"),("ember","/ˈembər/","n.","余烬","fire"),("brandish","/ˈbrændɪʃ/","v.","挥舞武器","clansmen"),("pitchfork","/ˈpɪtʃfɔːrk/","n.","干草叉","weapon"),("scythe","/saɪð/","n.","长柄镰刀","weapon"),("hauberk","/ˈhɔːbɜːrk/","n.","锁子甲上衣","Tyrion armor"),("fire-hardened","/ˈfaɪər ˌhɑːrdənd/","adj.","火烤硬化的","wooden spear"),("flinch","/flɪntʃ/","v.","畏缩闪避","spear threat"),("lance","/læns/","n.","骑枪","promised arms"),("incentive alignment","/ɪnˈsentɪv əˈlaɪnmənt/","n.","激励一致","interpretive term"),
]
VOCAB=BASE_VOCAB+EXTRA_VOCAB

def extract_blocks():
    blocks=extract_range(415,423,"TYRION","CH42")
    blocks[52]["text"]="[原文涉及十三岁的Tyrion与约十四岁女孩之间的露骨性描写，此处不逐字复录。请参见源 PDF p.420 对应段落。]"
    blocks[58]["text"]="[原文涉及约十四岁女孩被安排进入商业性关系及Jaime向Tyrion提供的解释，此处不复录具体性内容。请参见源 PDF p.420 对应段落。]"
    blocks[59]["text"]="[原文涉及Tywin命guards对约十四岁女孩实施集体性暴力，并强迫十三岁的Tyrion观看和参与；此处不逐字复录。请参见源 PDF pp.420–421 对应段落。]"
    return blocks

def main():
    blocks=extract_blocks()
    write_chapter(
        out=OUT,chapter=42,pov="TYRION",page_start=415,page_end=423,
        blocks=blocks,summaries=SUMMARIES,key_notes=KEY_NOTES,stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在high road风险、Bronn雇佣逻辑、Tyrion创伤记忆与Stone Crows谈判。",
        vocab=VOCAB,
        guide="离开Bloody Gate后，Bronn想靠夜行与隐蔽逃出Mountains of the Moon，Tyrion却判断clansmen必然会找到他们，于是故意升火、进食，把无法避免的接触转成一次谈判。两人先把彼此关系说透：Bronn不爱、不跪、会为利益背叛；Tyrion则用持续gold和匹配报价把自己的存活变成Bronn的收益。等待Stone Crows时，一首Myrish歌触发Tyrion十三岁秘密婚姻被Tywin以性暴力摧毁的创伤回忆；涉及未成年人的露骨段落使用安全占位，但保留责任、情感与梦境作用。clans出现后，Tyrion从分享fire、模仿clan称谓、赔goat一路谈到steel与Vale，用对方的territory、honor和hunger重写交易。",
        people=[
            ("Tyrion Lannister","本章视角；以雇佣激励稳住Bronn，讲出少年创伤，并与Stone Crows谈联盟"),
            ("Bronn","Tyrion的sellsword；公开否认忠诚感情，却接受存活绑定的长期报酬"),
            ("Tywin Lannister","Tyrion father；以权力与性暴力摧毁其少年婚姻，是创伤主要责任者"),
            ("Jaime Lannister","Tyrion brother；参与少年相遇事件并后来向Tyrion提供改变其理解的解释"),
            ("Tyrion’s first wife","约十四岁的crofter orphan；与十三岁Tyrion秘密结婚，后遭Tywin及guards暴力"),
            ("Mord","Eyrie gaoler；Tyrion获释时按承诺向他支付gold"),
            ("Gunthor son of Gurn","Stone Crows chief，优先考虑mothers hunger与steel实际价值"),
            ("Shagga son of Dolf","体型巨大的Stone Crow warrior，持club与wood-axe"),
            ("Conn / Torrek / Jaggot","参与包围Tyrion、Bronn的其他mountain clansmen"),
        ],
        terms=[
            ("high road","穿越Mountains of the Moon、连接Bloody Gate与riverlands的危险山路"),
            ("sellsword contract","以报酬换取武力服务，不包含封建宣誓或私人友爱"),
            ("A Lannister always pays his debts","Tyrion反复使用的家族信誉话语，既指兑现报酬也暗含报复"),
            ("Stone Crows","不服从Vale lords的mountain clan，以父名、clan与领地建立身份"),
            ("Clan Lannister","Tyrion为适应mountain clans语言而对House Lannister的策略性改称"),
        ],
        synthesis="Chapter 42展示Tyrion最强的能力不是预知，而是把坏选择改写成可谈的选择。他无法隐身穿山，便让fire同时供暖、鼓舞、诱敌；无法要求Bronn忠诚，便让两人利益绑定；无法消除少年创伤，便把pay debts保留为未来行动意志；无法用眼前财物买通Stone Crows，便先承认其领地规则，再发现hunger与steel才是有效货币。每一步仍是toss of dice，成功依赖对方选择。尤其重要的是，Tywin对未成年人的暴力不是Tyrion聪明话术能够抹平的‘lesson’，而是解释其为何既渴望交易可预测性、又把亲密关系与羞辱、付款、背叛纠缠在一起的创伤核心。",
        contrasts=[
            "**no fire隐蔽／open fire接触：** Bronn减少被发现概率，Tyrion为不可避免的相遇预设谈判场。",
            "**love与loyalty／blade与gold：** 双方拒绝浪漫化关系，以可计算利益合作。",
            "**Mord payment／Tywin payment：** 一处付款兑现承诺并创造信用，另一处付款被权力用于制造性暴力与羞辱。",
            "**song sweet and sad／stars merciless as truth：** 美好记忆的入口迅速转为被强加‘真相’的创伤。",
            "**prisoner梦／gaoler梦：** Tyrion在无意识中夺回身体力量与惩罚方向。",
            "**gold无用／steel fills mouths：** 价值不由财富名义决定，而由对方生存结构决定。",
        ],
        questions=[
            "Tyrion如何可能兑现把Vale of Arryn交给Stone Crows的巨大承诺？",
            "Stone Crows会接受escort或更深的军事联盟吗？",
            "Tyrion所说关于dagger的questions将指向谁？",
            "Bronn在何种价格或风险下会真正背叛Tyrion？",
            "Tyrion对Tywin的pay debts暗示会否转化为实际行动？",
        ],
        extraction_notes="PDF pp.415–423校勘后共84段；共5处跨页续段：pp.416–417、418–419、419–420、420–421与421–422，段落边界与顺序无需额外合并。第53、59、60段分别涉及未成年人露骨性内容、商业性剥削与集体性暴力，保留稳定编号和分析但以安全占位替代原文。",
    )
    print(f"Wrote Chapter 42 with {len(blocks)} paragraphs")

if __name__=="__main__":
    main()
