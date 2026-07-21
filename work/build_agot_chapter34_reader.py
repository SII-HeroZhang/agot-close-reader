#!/usr/bin/env python3
"""Build Chapter 34 (CATELYN) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter33_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"Ser Donnel说Catelyn若预先通知，Vale会派escort，因为high road已不适合小队安全通行。",2:"Catelyn说自己已付出惨痛代价，列出六名死者；Arryn moon-and-falcon banner让准备最后一战的队伍终于放心。",3:"Donnel说Jon死后clans更大胆，Lysa却禁止出兵和参加tourney，把所有swords留在Vale防御不明威胁。",4:"Catelyn知道Lysa怕的是Lannisters，又看到Tyrion已从绑手俘虏变成持axe、dirk、穿mail且与Bronn亲近的人，开始怀疑自己是否错了。",5:"她压下疑虑，优先请求为高烧重伤的Ser Rodrik召Maester Colemon。",6:"Donnel迟疑说Lysa命Colemon始终留在Eyrie照看Robert，只能由gate septon处理伤口。",7:"Catelyn更信maester，却被山体中Bloody Gate的双塔、桥梁与防御线吸引；佩Riverrun黑鱼徽章的守门knight前来盘问。",8:"Donnel报出自己、Catelyn与同行者身份。",9:"Knight of the Gate掀visor，认出并亲昵称她little Cat。",10:"Catelyn也认出uncle，熟悉嗓音把她带回二十年前。",11:"Brynden说自己的home就在身后Vale。",12:"Catelyn说uncle的home在自己心中，请他摘helm相见。",13:"Brynden摘helm，虽衰老却笑眼未变，并问Lysa是否知道她来。",14:"Catelyn说无暇预告，自己正在storm之前赶路。",15:"Donnel礼仪性询问是否准入Vale。",16:"Brynden以Robert Arryn名义允许进入并要求遵守peace。",17:"Catelyn穿过曾挡住多支军队的Bloody Gate，眼前突然展开明亮丰饶的Vale。",18:"叙述铺陈山谷农田、河湖与护山，并把Giant’s Lance和Alyssa’s Tears置于最高背景。",19:"Brynden指向Alyssa’s Tears旁偶尔闪白光的Eyrie。",20:"Catelyn想起Eddard称其七塔如刺入天空的白daggers，询问路程。",21:"Brynden说黄昏可到山脚，但攀登还需一天。",22:"Ser Rodrik说自己今天无法再走，疲惫得随时可能坠马。",23:"Catelyn感谢其超额尽责，安排他和其余人休养，自己让Brynden护送并必须带Tyrion上山。",24:"Donnel答应款待；crossroads inn原队伍只剩Ser Rodrik、Bronn、Ser Willis和Marillion。",25:"发热憔悴的Marillion坚持要看故事结局，请求去Eyrie。",26:"Catelyn想到他自愿同行却奇迹般活下来，因而勉强同意。",27:"Bronn直接宣布自己也去。",28:"Catelyn承认Bronn战力救过众人，却不信其kindness或loyalty，也担心他与Tyrion关系；因已准Marillion，只能同意。",29:"Ser Rodrik与Ser Willis留下疗伤，队伍换mounts，并由Donnel先放ravens通知Eyrie和Gates of the Moon。",30:"下降一段且远离旁人后，Brynden才问Catelyn所谓storm。",31:"Catelyn说自己早非child，却完整讲述Lysa letter、Bran坠落、dagger、Littlefinger与Tyrion偶遇。",32:"Brynden沉默倾听；叙述回顾他与Hoster长期冲突以及black fish个人徽章来历。",33:"兄弟冲突直到Catelyn与Lysa婚礼仍未结束；Brynden转投Eyrie后，Hoster不再提他。",34:"但Catelyn三兄妹乃至Petyr童年都把Brynden当作愿意倾听、分享喜悲的成年人。",35:"听完后Brynden首先说必须警告Hoster，因为Riverrun正处Lannister进军路径。",36:"Catelyn同意，并准备让Colemon发出north防御等多封ravens，继而询问Vale情绪。",37:"Brynden说Vale因Jon之死和Jaime取代传统Arryn Warden职位而愤怒，公开虽不说murder但疑云浓厚，另有Robert问题。",38:"Catelyn追问Robert怎么了。",39:"Brynden说六岁Robert病弱爱哭，领主们争论由Nestor摄政或Lysa再婚；suitors已像battlefield crows聚集。",40:"Catelyn认为年轻widow加Vale领地必然吸引求婚者，问Lysa是否再嫁。",41:"Brynden说Lysa口头愿嫁合适者，却已拒绝Nestor和许多匹配，强调这次自己选择。",42:"Catelyn提醒最反抗arranged marriage的Brynden不应责怪她。",43:"Brynden说自己不怪，却怀疑Lysa只享受courtship，实际想亲自统治至Robert成年。",44:"Catelyn说woman可与man同样明智统治。",45:"Brynden同意right woman可以，却警告Lysa不是Catelyn，可能不会像期待般帮忙。",46:"Catelyn不明白。",47:"Brynden说King’s Landing多年已改变Lysa，政治婚姻也缺少passion。",48:"Catelyn说自己的婚姻起点也一样。",49:"Brynden指出结局不同：Lysa经历stillbirths、miscarriages和Jon death，只剩Robert作为生命中心，因怕Lannisters才逃回Vale；Catelyn却把lion带到门口。",50:"Catelyn强调Tyrion是在chains中带来，同时小心通过右侧crevasse。",51:"Brynden指出Tyrion实际持axe、dirk且Bronn如hungry shadow跟随，反问chains在哪里。",52:"Catelyn不安却坚持他仍非自愿、仍是prisoner，且Lysa letter本就指控Lannisters。",53:"Brynden用疲惫笑容说希望她正确，语气却明显不信。",54:"下到丰饶谷底后队伍加速，Arryn与Blackfish双旗让农商与小领主主动让路。",55:"入夜抵达Giant’s Lance山脚castle，drawbridge和portcullis已关闭。",56:"Brynden介绍Gates of the Moon是Nestor seat，并叫Catelyn抬头。",57:"Catelyn看到mountain上三座waycastles火光逐级升高，最顶处Eyrie白光引发vertigo。",58:"Marillion敬畏低语Eyrie。",59:"Tyrion说Arryns显然不爱来客，若夜里攀山宁愿当场被杀。",60:"Brynden说当夜住下、次晨攀登。",61:"Tyrion问如何上去，自己不会骑goat。",62:"Brynden答mules。",63:"Catelyn说山上有石阶，Eddard曾讲少年经历。",64:"Brynden解释Stone、Snow、Sky三座waycastles，mules只到Sky。",65:"Tyrion怀疑地问其后如何。",66:"Brynden说最后徒步或坐chains吊basket，调侃让Tyrion和bread、beer、apples一起上。",67:"Tyrion笑说若自己是pumpkin就好，但Lannister pride不容像turnips被运，决定步行。",68:"Catelyn被其轻松语气激怒，把pride改称arrogance、avarice和power lust。",69:"Tyrion把三项罪分别归Jaime、Tywin、Cersei，自称无辜lamb并问是否要bleat。",70:"drawbridge开启；Nestor带knights迎接，身材魁梧却鞠躬笨拙。",71:"Catelyn正式请求屋顶hospitality。",72:"Nestor答应，却说Lysa命Catelyn立刻上Eyrie，其他人次晨再上。",73:"Brynden直骂night ascent是broken neck邀请。",74:"十七八岁的Mya保证mules认路，自己已夜攀百次，并以父亲像goat的玩笑表现自信。",75:"Catelyn因她cocky而笑，询问名字。",76:"女孩自称Mya Stone。",77:"Stone姓令Catelyn想起Jon，产生愤怒与guilt；叙述解释各地baseborn children的地域姓氏。",78:"Nestor填补沉默，保证Mya聪明可靠。",79:"Catelyn把安全交给Mya，又命Nestor严守Tyrion。",80:"Tyrion要求先给自己wine、capon甚至girl，Bronn大笑。",81:"Nestor无视玩笑，命把Tyrion关tower cell并给meat、mead。",82:"Catelyn告别众人，随Mya骑mules进入漆黑山阶；Mya提醒害怕者别把mule勒太紧。",83:"Catelyn以Tully和Stark身份说自己不易害怕，并问为何不用torch。",84:"Mya说torch会致盲，清夜moon和stars足够；mule也无需催促便自动跟随。",85:"Catelyn问她反复提到的Mychel是谁。",86:"Mya说Mychel Redfort是自己的love，等他成为knight便结婚。",87:"她的幸福梦想像Sansa；Catelyn却知道Redfort家族不会让嫡出儿子娶bastard，最多只是秘密关系。",88:"第一段攀登比预想容易，密林、稳健mules和Mya night-eyes让Catelyn几乎睡着。",89:"抵达Stone后换mules、吃热肉；饥饿使Catelyn不再在意汁水弄脏cloak。",90:"Stone至Snow更陡更破，Mya多次清石；海拔、强风和下方缩小的火光显出高度。",91:"Snow虽小却控制上方石阶，可用rocks和arrows层层阻敌；Mya拒绝休息继续攀登。",92:"再次换mules，Mya介绍Whitey稳健但会踢不喜欢的人。",93:"Mya说古时snow line远低于如今，自己从未见过，summer已构成她全部记忆。",94:"Catelyn感叹她年轻，几乎说出Winter is coming，并觉得自己终于越来越像Stark。",95:"Snow以上风像活物，Catelyn学会向上不向下看；到窄saddle时Mya让两人下马牵行。",96:"面对两侧深渊，Catelyn第一步便被恐惧定住，不能前进也无法后退。",97:"Mya隔着gulf问她是否无恙。",98:"Catelyn吞下pride，承认自己做不到。",99:"Mya坚定说她可以，并提醒路其实很宽。",100:"Catelyn不敢看，闭眼调稳破碎呼吸。",101:"Mya说会回来接她，叫她别动。",102:"Mya握臂逐步口令引导，Catelyn闭眼颤抖地一步步过桥，Whitey平静跟随。",103:"到达Sky后，简陋石墙在Catelyn眼中胜过Valyria奇观，因为它意味着窄路结束。",104:"黎明时进入Sky；Mya介绍洞内设施、最后chimney般stone ladder，以及仍需一小时。",105:"Catelyn看到Eyrie只高六百英尺，选择Tully common sense，要求和turnips一起坐basket。",106:"日出后抵达Eyrie，Vardis与Colemon迎接，并说Lysa命令她到达即唤醒自己。",107:"Catelyn带刺地希望Lysa睡得好，暗含自己彻夜攀爬的不满。",108:"Eyrie虽小且能容五百人，七座白塔和空荡回声却让Catelyn觉得异常荒凉。",109:"Lysa披bed robes热情拥抱，反复感叹五年未见。",110:"Catelyn观察五年使妹妹显老、发胖、苍白、眼神游移，只剩auburn hair保留旧美。",111:"Catelyn撒谎说她气色好，只是疲倦。",112:"Lysa让maid、Colemon、Vardis退下，仍牵着姐姐手。",113:"门一关Lysa立刻放手变脸，怒斥Catelyn未经许可把Tyrion和Lannister争端带来。",114:"Catelyn难以置信，指出最初正是Lysa letter称Lannisters谋杀Jon。",115:"Lysa说信只是让Catelyn远离危险，自己从未想开战，追问她究竟做了什么。",116:"六岁Robert抱doll在门口，被争吵惊来；叙述写明他病弱并有shaking sickness。",117:"Lysa责怪地看姐姐，却向son介绍Aunt Catelyn。",118:"Robert模糊说似乎记得，尽管上次相见尚不足一岁。",119:"Lysa整理其衣发，坚称他美丽强壮，并把Jon临终the seed is strong解释为赞扬son。",120:"Catelyn说若Lannister威胁真实更应迅速行动。",121:"Lysa以Robert temperament delicate为由不许当面谈。",122:"Catelyn提醒Robert是Vale lord，战争将至时不能只求delicacy。",123:"Lysa喝止并安抚发抖的son，让六岁Robert继续breastfeed。",124:"Catelyn震惊，将他与三岁Rickon比较，并首次理解Vale lords不安及Robert想把孩子送去foster的理由。",125:"Lysa反复说这里安全，Catelyn不确定是说给谁听。",126:"Catelyn怒说无人安全，躲藏不会让Lannisters遗忘。",127:"Lysa捂住son耳朵，认为军队无法越mountains、Bloody Gate与impregnable Eyrie。",128:"Catelyn想打醒她，记起Brynden警告，并说没有castle不可攻破。",129:"Lysa仍坚持Eyrie例外，只问该如何处理Tyrion。",130:"Robert离开母亲乳房，问Tyrion是否bad man。",131:"Lysa称他非常坏，并保证不会让其伤害baby。",132:"Robert兴奋要求make him fly。",133:"Lysa抚摸son头发，低声说也许正会如此。",
}
SUMMARIES = [S[i] for i in range(1, 134)]

KEY_NOTES = {
2:"six brave men与names fading并置，Catelyn的麻木不是不在乎，而是疲劳、创伤和持续任务压缩了哀悼能力。",
3:"Lysa把所有swords留在Vale看似谨慎，却同时减少high road治安与盟友参与；封闭防御会把风险推到边缘。",
4:"Tyrion装备、cloak、Bronn关系逐项列出，让“prisoner”从法律标签变成越来越难维持的实际描述。",
5:"Resolute地push doubts away说明她不是解决疑问，而是主动延迟；六名死者反而制造继续相信原决定的sunk cost压力。",
7:"Bloody Gate把mountain geography转成fortification；黑鱼徽章又在Arryn边界突然召回Tully family。",
10:"smoky voice触发二十年记忆，声音比衰老脸孔更先恢复uncle身份，形成感官认亲。",
12:"home at my back/home in my heart用同一词完成地理与亲情双关，也承认Brynden已把Vale当现实归属。",
17:"穿Gate前是狭窄阴影和古战场，穿后是绿色光照；防线像舞台门帘般揭开被保护的丰饶核心。",
18:"Giant’s Lance让mountains也抬头，以尺度递增为Eyrie攀登建立近乎超现实高度。",
22:"Ser Rodrik直到安全边界内才承认极限，忠诚若无休息也会变成死亡；Catelyn此时终于允许停下。",
25:"Marillion仍把经历理解为tale结构，“看结局”的欲望压过伤病与此前恐惧。",
28:"Bronn不ask而announce，显示他已不把Catelyn当唯一决定者；她的礼仪一致性反而限制自己阻止他。",
31:"完整讲述耗时比想象长，说明事件链在她心中虽像单一阴谋，实际由多次推断、偶遇和他人消息连接。",
32:"black fish源自对Hoster insult的机智改写：Brynden把被排斥身份主动转化成可选择的personal emblem。",
35:"Brynden第一个军事判断指向Riverrun，而非安全Vale或遥远Winterfell，体现地图位置对政治风险的决定性。",
37:"True Warden title无法改变Jaime实际任命；称号可表达抗议，却不能让others fooled，呼应Tyrion prisoner标签。",
39:"suitors like crows把婚姻市场写成对widow、child和territory脆弱性的围食。",
43:"Brynden区分courtship sport与marriage intention，Lysa可能利用求婚者竞争稳固自身regency。",
45:"right woman含蓄但尖锐：他不否定女性统治，却明确怀疑Lysa判断，避免把个人批评泛化为性别论。",
49:"生育损失与Jon death解释Lysa恐惧和过度保护，但解释不等于所有决定正确；Brynden要求Catelyn先理解她的模型。",
50:"Catelyn说chains时正沿深渊小心前行，物理危险与她对控制Tyrion的脆弱信念并置。",
51:"Brynden只描述可见事实，不争论法律定义；axe、dirk、Bronn使Catelyn不得不面对实际power。",
53:"I hope you are right表面支持、语调否定；Brynden不替她下结论，却提前警示Lysa不会按信中逻辑行动。",
57:"三点火光和最终白闪把vertical journey可视化；Eyrie的安全来自难以接近，也意味着消息、援助和现实都被层层过滤。",
67:"Tyrion用pumpkin/turnips把可能羞辱改写成笑话，又以family pride拒绝basket，维持被押者尊严。",
69:"他承认family flaws却把罪分配给others，是机智的责任切割，不能因此证明自己innocent。",
72:"Lysa要求immediate night climb却让自己安睡到Catelyn到达，命令把风险和疲劳单向转嫁给visitor。",
74:"Mya的goat笑话轻描父亲身份；她的专业信心来自重复经验，不是贵族title。",
77:"Catelyn说nothing against this girl却立即迁怒，展示她对Jon的guilt如何投射到无关baseborn child。",
80:"Tyrion用banter测试新captors和环境；Bronn公开笑声继续显示二人关系已超出普通guard/prisoner。",
84:"torches just blind you与Arya地下章节直接呼应：自带强光会破坏暗适应，熟悉环境者更信弱光与身体经验。",
87:"Catelyn以marriage politics推断Mychel梦想不可能，可能现实而准确，却也复制她对Sansa future的成人悲观视角。",
91:"Stone、Snow、Sky构成defense in depth：每失一层，上一层仍从高处控制唯一通路。",
93:"Mya一生几乎全在summer，以个人记忆否定不了历史snow line；季节尺度超过单个人生经验。",
94:"Perhaps becoming a Stark把house words从丈夫家口号变成她内化的时间意识与警告冲动。",
96:"自称不易害怕后真正freeze，使勇气脱离身份宣言；高处恐惧不因Tully/Stark name自动消失。",
98:"吞下pride、向baseborn girl求助，是Catelyn本章重要自我修正；承认不能做才让专业者能救她。",
102:"Mya不用空泛鼓励，而把任务拆成foot by foot，给予触觉支撑并允许闭眼，是有效危机引导。",
105:"Catelyn最终选择basket，证明common sense可以战胜刚才的pride争论；turnips笑话也接回Tyrion。",
108:"Eyrie极强防御却echoing and empty；安全的architecture也形成社会孤立和心理空旷。",
109:"公开拥抱的sunlight式热情与关门后cloud式变脸形成表演/私心对照。",
113:"dropped hand瞬间取消sisterly intimacy；Lysa优先感受的是Catelyn把危险带入自己封闭安全区。",
115:"letter在Catelyn眼中是求援/指控，在Lysa眼中只是逃避警告；同一文本从未建立共同行动承诺。",
119:"Lysa把the seed is strong理解成Jon赞美Robert；结合Jon查lineages、bastards与外貌，这一解释至少存在疑问。",
123:"breastfeeding六岁child在叙事中服务于infantilization：Lysa以身体安抚替代让Robert面对lord责任。",
124:"Catelyn拿Rickon比较带有母亲偏见，却也说明Robert年龄与依赖程度不匹配Vale lords对ruler的期待。",
125:"safe here重复既是判断也像self-soothing mantra；不确定说给谁听显示mother与son共享同一恐惧回路。",
127:"impregnable只描述正面军事接近，不自动解决粮食、政治、内部决策或长期孤立；绝对安全是过度推论。",
132:"make him fly语义在此尚未解释，却因child兴奋与Lysa回应形成明显不祥感；不应提前指定执行方式。",
}

STAGES = [
(1,29,"Arryn escort救下仅存队伍；Bloody Gate内Catelyn重逢Brynden，留下Ser Rodrik疗伤，却带Tyrion、Bronn和Marillion继续。"),
(30,53,"Catelyn向Brynden复述全部证据；他警告Riverrun、Vale regency和Lysa恐惧，并用Tyrion武器与Bronn指出prisoner控制已变弱。"),
(54,81,"队伍抵Gates of the Moon；Lysa命Catelyn连夜独自上山，Mya Stone担任向导，Tyrion被关入tower cell。"),
(82,105,"Catelyn经Stone、Snow、Sky攀登，在高空窄路freeze后接受Mya引导，最终放下pride选择basket抵达Eyrie。"),
(106,133,"Lysa公开热情、私下怒斥姐姐把Lannister带来；她以Eyrie绝对安全和保护Robert拒绝战争现实，并考虑让Tyrion“fly”。"),
]

BACKGROUNDS = {
3:"**Vale防御政策：** Lysa在Jon死后召回或留住Vale swords，不许参加Hand’s tourney，也不准主动清剿clans。",
7:"**Bloody Gate：** high road进入Vale核心谷地的狭窄要塞，依山扼守，历史上多次阻断入侵。",
13:"**Brynden Tully：** Hoster弟弟、Catelyn uncle，personal sigil为black fish；现任Knight of the Gate并长期服务House Arryn。",
16:"**Robert Arryn：** Jon与Lysa六岁son，名义上是Lord of the Eyrie、Defender of the Vale与True Warden of the East。",
18:"**Giant’s Lance／Alyssa’s Tears：** Eyrie所在高峰及其瀑布；瀑水在落地前散成雾，远看如银线。",
32:"**Blackfish称号：** Hoster骂Brynden是家族black goat后，Brynden按Tully trout sigil自称black fish。",
35:"**Riverrun地理：** 位于riverlands西部、接近Lannister可能东进路线，比Winterfell与Eyrie更先承受战争。",
37:"**Warden争议：** Robert把Warden of the East授予Jaime；Vale仍称young Robert为True Warden以表达不承认。",
39:"**regency问题：** Nestor已代Jon管理Vale十四年；Robert未成年且病弱，实际统治权成为各lord关注焦点。",
49:"**Lysa经历：** Brynden称她有两次stillbirth、四次miscarriage，最终只有Robert存活；这些损失强化她的保护与恐惧。",
56:"**Gates of the Moon：** Giant’s Lance山脚castle，由High Steward Nestor管理，是攀登Eyrie的补给与住宿入口。",
64:"**三重waycastles：** Stone、Snow、Sky沿唯一山阶分层防守；Sky以上须徒步或用winch basket。",
77:"**baseborn surnames／Mya身世推断：** Vale用Stone、north用Snow、Reach地区用Flowers。Mya约十七八岁、在Vale长大；结合Eddard此前回忆Robert在Vale的长女，强烈暗示她就是该child，但本章未明说。",
91:"**defense in depth：** waycastles相互居高掩护，进攻者必须沿狭窄阶梯逐层突破。",
119:"**the seed is strong：** Jon临终反复说的话；Lysa解作称赞son，Eddard所见book、Gendry与bloodline调查使含义仍未解决。",
123:"**shaking sickness：** maesters对Robert间歇颤抖症状的称呼；本章未给现代诊断。",
}

EXTRA_VOCAB = [
("harry","/ˈhæri/","v.","反复袭扰","clansmen"),("fester","/ˈfestər/","v.","伤口化脓恶化","wounds"),("mordant","/ˈmɔːrdənt/","adj.","尖刻讽刺的","jest"),("root out","/ruːt aʊt/","phr.v.","彻底清剿；铲除","clan fastnesses"),("out of turn","/aʊt əv tɜːrn/","phr.","不合身份或时机地","frank speech"),("thick as thieves","/θɪk əz θiːvz/","idiom","关系非常亲密","Tyrion and Bronn"),("hauberk","/ˈhɔːbɜːrk/","n.","锁子甲长衫","taken armor"),("resolute","/ˈrezəluːt/","adj.","坚决的","push doubts away"),("defile","/dɪˈfaɪl/","n.","狭窄山口","Bloody Gate"),("abreast","/əˈbrest/","adv.","并排地","four riders"),("wrought","/rɔːt/","adj.","精工制成的","brooch"),("vista","/ˈvɪstə/","n.","远景；开阔景观","Vale reveal"),("bottomlands","/ˈbɑːtəmlændz/","n.","低地；河谷地","valley floor"),("ghost torrent","/ɡoʊst ˈtɔːrənt/","metaphor","幽灵般瀑流","Alyssa’s Tears"),("haggard","/ˈhæɡərd/","adj.","憔悴疲惫的","Marillion"),("scruff","/skrʌf/","n.","稀疏杂乱胡须","new beard"),("standard-bearer","/ˈstændərd ˌberər/","n.","旗手","double banner"),("verdant","/ˈvɜːrdənt/","adj.","青翠繁茂的","woodlands"),("hamlet","/ˈhæmlət/","n.","小村庄","Vale"),("vertigo","/ˈvɜːrtɪɡoʊ/","n.","眩晕；恐高眩晕","looking up"),("winch","/wɪntʃ/","n.","绞盘","supply basket"),("chagrined","/ʃəˈɡrɪnd/","adj.","懊恼难堪的","Tywin imagined"),("capon","/ˈkeɪpɑːn/","n.","阉鸡；肥嫩食用鸡","prison meal"),("night-eyes","/naɪt aɪz/","n.","夜间视力","Mya"),("surefooted","/ˌʃʊrˈfʊtɪd/","adj.","脚步稳健的","mules"),("rimed","/raɪmd/","adj.","覆有白霜的","Sky stones"),("halloo","/həˈluː/","v.","高声呼叫","guards"),("precipitous","/prɪˈsɪpɪtəs/","adj.","陡峭近垂直的","drop"),("skirling","/ˈskɜːrlɪŋ/","n./adj.","尖厉呼啸的","wind"),("placidly","/ˈplæsɪdli/","adv.","平静温顺地","mule follows"),("honeycomb","/ˈhʌnikoʊm/","n.","蜂巢状结构","Eyrie below"),("petulant","/ˈpetʃələnt/","adj.","任性易怒的","mouth"),("take leave of one’s senses","/teɪk liːv əv/","idiom","失去理智","Lysa accusation"),("restive","/ˈrestɪv/","adj.","不安且难控制的","Vale lords"),("impregnable","/ɪmˈpreɡnəbəl/","adj.","坚不可摧的","Eyrie claim"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def main():
    blocks = extract_range(332, 347, "CATELYN", "CH34")
    write_chapter(
        out=OUT, chapter=34, pov="CATELYN", page_start=332, page_end=347,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Vale分层防御、Catelyn对俘虏控制的疑虑、Mya专业能力与Lysa安全逻辑。",
        vocab=VOCAB,
        guide="Arryn骑兵终于救下穿越high road的残队，Catelyn在Bloody Gate重逢uncle Brynden。她已开始怀疑Tyrion是否无辜，却因六名死者与既有决定压下疑虑。Brynden听完证据后首先警告Riverrun，并指出Tyrion持axe、dirk、由Bronn跟随，所谓chains只是法律称呼。Lysa命Catelyn连夜独自攀登Eyrie；向导Mya Stone凭经验带她经过Stone、Snow、Sky，Catelyn在窄桥恐惧瘫住后放下pride接受帮助，最后选择basket。抵达后Lysa公开热情、关门即怒斥姐姐把Lannister危险带来。她的letter原意只是警告逃避，并非共同开战；她把Eyrie当绝对安全，把六岁Robert持续当baby保护，也把Jon临终the seed is strong解释为赞美son。姐妹对风险、责任与行动的理解由此正面冲突。",
        people=[
            ("Catelyn Stark","本章视角；怀疑逮捕决定、跨越Vale防线并面对Lysa拒绝合作"),
            ("Brynden Tully","Catelyn uncle、Blackfish与Knight of the Gate，倾听后提供军事和家庭警告"),
            ("Lysa Arryn","Catelyn妹妹；因丧失与恐惧封闭Vale，拒绝被拖入公开Lannister冲突"),
            ("Robert Arryn","六岁Lord of the Eyrie，病弱且被Lysa高度婴儿化保护"),
            ("Mya Stone","年轻baseborn mountain guide，以专业经验带Catelyn夜攀Eyrie"),
            ("Tyrion Lannister","名义俘虏，却已持武器、穿mail并与Bronn形成明显关系"),
            ("Bronn","sellsword，救过队伍但不受Catelyn信任；自行决定随Tyrion上山"),
            ("Nestor Royce","High Steward与Gates of the Moon keeper，接待队伍并执行Lysa命令"),
        ],
        terms=[
            ("Bloody Gate","high road进入Vale的狭口要塞，以山体和交叉火力阻断军队"),
            ("Gates of the Moon","Giant’s Lance山脚补给castle，也是攀登Eyrie的起点"),
            ("Stone / Snow / Sky","沿唯一山阶设置的三座waycastles，构成纵深防御"),
            ("baseborn regional names","Stone、Snow、Flowers等按出生地域标识非婚生children"),
            ("the seed is strong","Jon临终话语；Lysa给出son-centered解释，但调查语境仍保留疑问"),
        ],
        synthesis="Chapter 34把Eyrie的“安全”写成一条越来越窄、越来越高的选择链。Bloody Gate、三座waycastles、winch和空荡白塔确实能阻挡军队，却也让Lysa相信自己可以不回应外部战争；地理优势被扩大为心理绝对性。Catelyn在山桥上承认恐惧、接受Mya引导，是一种真正的适应；Lysa却用impregnable反复封闭问题。两姐妹都因children行动：Catelyn冒险抓Tyrion以保护Bran，Lysa封锁Vale以保护Robert。正因为动机相似，她们对“保护意味着追击威胁还是远离威胁”的分歧才更尖锐。",
        contrasts=[
            "**Bloody Gate外荒路／Gate内丰饶谷地：** 军事狭口保护了富足，也让内部容易相信外界可被隔绝。",
            "**prisoner称号／可见武力：** Catelyn说chains，Brynden看见axe、dirk和Bronn。",
            "**Tully/Stark pride／承认恐惧：** Catelyn靠放下身份宣言、接受Mya帮助才过窄桥。",
            "**Mya无title的能力／贵族的脆弱判断：** baseborn guide实际掌握通往最高贵castle的道路。",
            "**公开拥抱／关门斥责：** Lysa的亲情表演与政治恐惧在门的两侧迅速切换。",
            "**安全堡垒／隔绝牢笼：** Eyrie越难抵达，Lysa越能避免外界，也越难被外界纠正。",
        ],
        questions=[
            "Lysa会依据什么程序处理Tyrion，是否愿意检验dagger证据？",
            "Catelyn能否说服Lysa向Riverrun、north或Eddard提供军事支持？",
            "Mya是否就是Eddard回忆中Robert在Vale的长女？",
            "the seed is strong真正指向Robert Arryn，还是Jon在lineages与bastards中发现的另一规律？",
        ],
        extraction_notes="PDF pp.332–347共133段；正确合并7处跨页续段：pp.334–335、336–337、340–341、341–342、344–345、345–346与346–347。逐页复核未发现额外分页误切。",
    )
    print(f"Wrote Chapter 34 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
