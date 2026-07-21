#!/usr/bin/env python3
"""Build Chapter 31 (TYRION) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter30_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"黎明前Chiggen宰杀Tyrion死去的mare；Tyrion把这笔损失也记作Stark欠债，并担心血腥味引来shadowcats。",2:"Bronn说horse meat足够让众人不挨饿，并以瘦硬如shadow的外貌登场。",3:"Tyrion说自己尤其不愿吃自己的马。",4:"Bronn认为meat就是meat，并提到Dothraki偏爱horse meat。",5:"Tyrion反问自己哪里像Dothraki，并想到自己厌恶的Dothraki习俗。",6:"Chiggen割下生肉挑衅Tyrion是否想尝。",7:"Tyrion平静说这匹mare是Jaime送的name day礼物。",8:"Chiggen叫他若还能见Jaime就代为道谢，并用well bred拿马的血统开玩笑。",9:"Bronn补充用洋葱煎会更好吃。",10:"Tyrion沉默跛行回队，寒冷、疼痛与无尽赶路使他诅咒Catelyn和Starks。",11:"他回忆旅店中自己从点晚餐瞬间变成被武装人群包围的俘虏。",12:"Tyrion先压下Jyck拔剑的手，表面遵守旅店礼貌，再否认参与袭击Bran。",13:"Catelyn展示手上伤疤，称Tyrion的dagger曾用于割Bran喉咙。",14:"伤疤使抽象指控变成可见证据，陌生人迅速从旁观者变成要求杀他的群体。",15:"Tyrion压住声音颤抖，主动同意随Catelyn接受指控。",16:"他计算敌我人数、能力和Yoren中立誓言，判断武力突围必死。",17:"Yoren果然退开，Bronn替Ser Rodrik缴械；Tyrion从声音认出剃须后的Winterfell master-at-arms。",18:"Masha吐着sourleaf红沫，恳求Catelyn别在旅店杀人。",19:"Tyrion插话说哪里都别杀。",20:"Masha只求把high lord争端带走，避免血溅自己店里。",21:"Catelyn公开说押往Winterfell；Tyrion却统计出约五十人中只有十二人响应，尤其Frey队伍几乎未动。",22:"Tyrion赞同Winterfell路线，并以Tywin重赏消息为诱饵向freerider递出求援信号。",23:"Ser Rodrik宣布Tyrion随从同行，并要求所有目击者保密。",24:"Tyrion认为保密不可能：freerider、Yoren、Marillion、Freys都可把消息传向不同势力。",25:"Catelyn承诺House Stark感谢和报酬，立即招到更多押送者；Tyrion暗自决定日后以另一种方式“奖励”他们。",26:"雨中众人捆绑、蒙眼并带他出发；Tyrion仍相信追兵和riverlords会阻止自己抵达Winterfell。",27:"蒙眼骑行令他呼吸、听觉、平衡和身体都受折磨；Marillion却为写“splendid adventure”自愿同行。",28:"天明摘hood后，Tyrion从山路和雪峰认出这是通往Vale的high road，指责Catelyn欺骗。",29:"Catelyn承认自己故意反复高喊Winterfell，让潜在追兵走错方向。",30:"多日后Tyrion仍因被Catelyn全面outwit而愤怒，受挫的是赖以自豪的cunning。",31:"进入高地后押送者不再蒙眼捆手，因为荒野、shadowcats和mountain clans本身就是牢笼。",32:"Tyrion知道目的地是House Arryn领地，也不愿再次面对对Lannisters敌视的Lysa。",33:"队伍在溪边休整；俘虏、guards与Marillion各自疲惫或抱怨。",34:"率先响应Catelyn的Whent hedge knight Ser Willis要求休息。",35:"Ser Rodrik同意，并指出已损失第三匹马。",36:"Catelyn担心放慢会被Lannister追兵赶上，疲惫仍未削弱意志。",37:"Tyrion插话说在此被追上的可能性很小。",38:"Bracken man Kurleket侮辱他；Tyrion已记下所有押送者姓名，准备日后偿还待遇。",39:"Catelyn允许Tyrion发言。",40:"Tyrion分析追兵应被Winterfell假路线引向Neck，Tywin未必因爱他出兵；继续急行只会损马甚至让俘虏死去。",41:"Catelyn冷言说Tyrion死亡可能正是目的。",42:"Tyrion指出若真要杀他，旅店内就能做到，不必冒险押送。",43:"Catelyn说Starks不会在床上谋杀人。",44:"Tyrion说自己也不会，再次否认谋害Bran。",45:"Catelyn坚持assassin拿的是他的dagger。",46:"Tyrion指出用本人名贵武器装备普通刺客极其愚蠢，不符合隐藏罪行的基本逻辑。",47:"Catelyn短暂显出疑虑，却问Petyr为何要骗自己。",48:"Tyrion说撒谎是Littlefinger本性，并提醒Catelyn本应最了解他。",49:"Catelyn紧张追问这话含义。",50:"Tyrion揭露court流传的Littlefinger私密夸口。",51:"Catelyn愤怒否认。",52:"Marillion故作震惊地谴责Tyrion。",53:"Kurleket兴奋拔dirk，请求割下Tyrion舌头。",54:"Catelyn把Petyr少年感情定义为真实、纯洁的悲剧，并称Tyrion邪恶。",55:"Tyrion以粗暴措辞反驳，认为Littlefinger只爱自己且把Catelyn当作炫耀对象。",56:"Kurleket揪发压刀在Tyrion喉下，问是否放血。",57:"Tyrion喘息说杀死自己也会让truth消失。",58:"Catelyn再次命令让他继续。",59:"Kurleket不情愿地松手。",60:"Tyrion转向可核验细节，问Littlefinger究竟怎样描述dagger赌局。",61:"Catelyn复述：Tyrion在Joffrey name day tourney中赢得dagger。",62:"Tyrion确认Littlefinger所指正是Jaime被Loras击落的比赛。",63:"Catelyn承认，眉头皱起，说明逻辑核验开始产生影响。",64:"山脊watcher突然高喊riders。",65:"叫声来自Ser Rodrik派去侦察的Lharys。",66:"短暂僵住后Catelyn率先组织上马、藏马和看守俘虏。",67:"Tyrion抓住她要求给俘虏武器，因为每一把剑都需要。",68:"Catelyn知道mountain clans不分Stark或Lannister都会杀，甚至可能掳走她生育后代，却仍犹豫。",69:"逼近的蹄声使所有人立即行动。",70:"Lharys报告约二十至二十五名Milk Snakes或Moon Brothers，且对方显然布有hidden watchers。",71:"Ser Rodrik、Mohor与Ser Willis准备战斗，Marillion僵住，Morrec反而主动帮忙穿甲。",72:"Tyrion计算放武器可多出四名战斗者，足以决定生死。",73:"Catelyn要求他们承诺战后交还swords。",74:"Tyrion以Lannister honor歪斜微笑作出承诺。",75:"Catelyn最终下令武装三名俘虏；Jyck取剑、Morrec拿bow，Bronn给Tyrion一把双刃axe。",76:"Tyrion承认从未用过axe，武器在手中笨重陌生。",77:"Bronn让他想象劈木头，自己与前排骑手列阵。",78:"Tyrion说木头不会流血，无甲的他寻找岩石掩体。",79:"躲藏的Marillion尖叫说自己只是singer、不想参战。",80:"Tyrion讽刺他失去冒险兴趣并踢他让位，袭击者随即到达。",81:"clansmen没有旗鼓礼仪，只随箭声从晨光冲出，装备混杂而致命。",82:"各战士高喊领地名冲锋；Tyrion也短暂想喊Casterly Rock，却理智地继续蹲伏。",83:"正面战斗混乱展开，Bronn、Chiggen、Ser Rodrik和Jyck各自交战，领头clansman中箭倒下。",84:"一骑冲向藏身处；Tyrion用axe砍倒马，再杀死被压住的rider，Marillion也被压在尸马下。",85:"Marillion求救并说自己流血。",86:"Tyrion判断是horse blood，踩碎他伸出的手指，叫他装死。",87:"战斗化为碎片化感官；Tyrion贴边砍马腿、杀伤员、取helm，看到Jyck与Kurleket先后死亡。",88:"Catelyn被三人围住；Tyrion口头想弃她，却身体先行动，与她配合杀死两人并赶走第三人。",89:"战斗突然结束；Tyrion难以相信自己存活，也惊讶主观半日实际只过片刻。",90:"战后Bronn一边问是否初战，一边从Jyck尸体剥下优质boots。",91:"Tyrion承认是first battle，讽刺Tywin会自豪；战中未觉的腿痛此刻涌回。",92:"Bronn说初次见血后需要woman。",93:"Chiggen暂停搜尸，以表情附和。",94:"Tyrion看向照料Ser Rodrik的Catelyn开性玩笑，引发freeriders笑声，并认为关系已有突破。",95:"Tyrion洗去血迹后观察clansmen尸体，发现其人马瘦弱、武器廉价生锈，外在威势随死亡和loot消失。",96:"己方死三人：Kurleket、Mohor与Jyck；Tyrion认为Jyck裸骑冲锋至死仍是fool。",97:"Ser Willis催促立刻赶路，担心clansmen很快返回。",98:"Catelyn坚持安葬勇敢死者，不愿把他们留给crows和shadowcats。",99:"Ser Willis指出石地无法挖坟。",100:"Catelyn改提议堆stone cairns。",101:"Bronn拒绝为死者堆石，号召想活到夜晚的人立即同行。",102:"受伤疲惫的Ser Rodrik承认第二次袭击可能致命，支持离开。",103:"Catelyn愤怒却无选择，只能求gods原谅并下令出发。",104:"死者留下充足horses；Tyrion换上Jyck坐骑时Lharys要求收回dirk。",105:"Catelyn让他保留dirk并归还axe，以防再次遇袭。",106:"Tyrion上马道谢。",107:"Catelyn说不必谢，自己依旧完全不信任他。",108:"Tyrion比较蒙眼绑手的开局，认为持axe自由骑行已是游戏中的明确进步。",109:"队伍重新编组；Marillion断肋、断harp和四根手指，却捡到华丽shadowskin cloak并终于沉默。",110:"身后shadowcats争食尸体；Tyrion用craven/raven押韵回敬Marillion此前写imp歌。",111:"Catelyn紧抿嘴唇看他靠近。",112:"Tyrion续上被伏击打断的论证：Littlefinger故事有严重缺陷，因为自己从不押注反对家族。",
}
SUMMARIES = [S[i] for i in range(1, 113)]

KEY_NOTES = {
1:"horse从Jaime礼物变成生存肉源，私人情感、阶级价值与荒野实用性在同一carcass上冲突。",
8:"well bred把贵族评价人的血统语言转用于horse meat，Chiggen用粗俗双关削弱Tyrion身份优势。",
10:"dead mare was lucky并非真愿死亡，而是身体极限下的黑色幽默；Tyrion以讽刺维持心理控制。",
12:"他先制止Jyck再讲honor，说明求生判断先于自尊；courtesy在此是一种降温技术。",
14:"Catelyn伤疤具有强烈修辞效力，却只能证明dagger袭击真实，不能单独证明Tyrion所有权或命令。",
16:"Tyrion把每个人按战力与誓言分类，快速承认不利现实是其cunning的基础。",
21:"他同时赞Catelyn策略sweet又统计响应缺口，能在作为受害者时分析对手做对了什么。",
22:"Tywin reward是策略性谎言；它利用outsider对Lannister wealth与family solidarity的想象。",
24:"消息网络分析与Catelyn的道路误导形成对抗：无法封住所有嘴，就只能控制追兵如何解释消息。",
25:"well rewarded在Catelyn口中是赏赐，在Tyrion内心变成复仇，重复短语改变道德方向。",
28:"地景本身揭穿路线：Tyrion依据foothills、peaks和high road重建位置，空间识读胜过口头宣告。",
29:"Often and loudly表明Catelyn的谎言是刻意让大量证人传播的公开misdirection，而非只骗Tyrion。",
30:"outwitted比abduction更刺痛他，因为cunning是其对抗身体与社会偏见的核心自我价值。",
31:"解除绳索并非信任增加，而是自然环境接管监狱功能；自由程度与逃生能力不是同一件事。",
38:"A Lannister always paid his debts在此明确带有复仇含义，家族格言式声誉被个人化为记名账本。",
40:"Tyrion把“别杀俘虏”包装成mount logistics与任务目标，使用对方利益而非请求怜悯。",
42:"若死亡是目标，长途押送不合成本效益；这是从Catelyn行动反推真实目的的有效论证。",
46:"名贵personal dagger交给common footpad会直接回指主人，Tyrion提出的是作案逻辑反证，而非不在场证明。",
47:"why would Petyr lie把人物信任当证据；Tyrion接下来试图把问题转成Petyr是否一贯可靠。",
50:"他用court rumor攻击Catelyn与Petyr关系，信息可能相关，但表达方式也主动激化危险。",
54:"Catelyn维护的是童年Petyr形象与自身记忆；她承认tragic passion，却拒绝把它理解为当下操控。",
55:"Tyrion的粗暴内容使可能有价值的信誉警告更难被接受，真信息也会被说话方式削弱。",
57:"truth dies with me把自己从可杀的enemy改写为唯一信息载体，是喉下有刀时最有效的交换筹码。",
60:"他从人格争执切回精确赌局细节，证明可检验事实比互相辱骂更可能改变Catelyn判断。",
63:"皱眉不是相信Tyrion，只表明Littlefinger叙述首次遇到内部一致性检查。",
66:"Catelyn反应最快，说明领导力在突袭前首先表现为打破freeze并分配具体任务。",
68:"共同外敌暂时重排阵营：great houses仇恨对不承认其秩序的clans毫无意义。",
72:"Tyrion把释放俘虏重新定义为增加战力，不要求Catelyn信任，只要求她计算。",
74:"Lannister honor在旅店曾被Catelyn讽刺；此刻她仍只能把同一句当作战时contract，语境改变其功能。",
80:"Marillion把现实危险一直当song素材，直到危险要求他本人承担风险；splendid adventure在此彻底破产。",
81:"no heralds/no banners/no horns把伏击与tourney对照：同样骑马持武器，却没有能把暴力美化为spectacle的仪式。",
82:"想喊Casterly Rock是英雄叙事冲动，继续躲低才是Tyrion真实生存策略；自嘲让两者并存。",
84:"Bronn的splitting logs建议以血肉现实方式实现；Tyrion第一次杀人既笨拙又有效，没有歌谣般流畅。",
86:"踩Marillion手指既是旧怨报复，也残酷利用对方无力反抗；Tyrion帮助自己生存不等于行为都正当。",
87:"叙述由完整战术变成声音、气味和闪回片段，模拟缺乏全局视野的首次实战经验。",
88:"thought says abandon、body moves to rescue形成内心与行动反差；共同战斗建立的实际关系超出彼此信任。",
89:"主观时间被恐惧拉长，sun scarcely moved以自然尺度纠正体验，表现adrenaline效应。",
90:"Bronn在尸体旁问初战并立即loot boots，展示sellsword对死亡与财物的彻底实用主义。",
94:"There’s a start不是浪漫兴趣，而是Tyrion发现共同笑声可把Bronn、Chiggen从陌生押送者变成可经营关系。",
95:"shadowskin cloak被取走、greatsword显出锈蚀，使敌首的象征威势随胜负被剥离；贫困仍解释不了全部暴力。",
98:"Catelyn以honor坚持埋葬，Bronn以survival拒绝；两套伦理都面对mountain clans即将回返的现实。",
101:"breathing, for one把活命列为better thing，以尖刻句式迫使贵族仪式让位给时间压力。",
105:"归还武器不是赦免，而是承认Tyrion已成为有用战斗资源；权力关系从纯俘虏转成受控合作。",
108:"ahead in the game显示Tyrion以相对位置而非绝对自由衡量成功，这让他在不利局势中持续行动。",
109:"Marillion获得cloak却失去演奏手、harp和声音地位，冒险给他的“素材”同时摧毁其职业工具。",
112:"never bet against my family直接攻击Littlefinger故事的核心下注方向；它是可查证的习惯与赛事事实，但仍是Tyrion自述。",
}

STAGES = [
(1,10,"死去mare被宰作食物，Tyrion在寒冷疼痛中以讽刺记账；当前荒野困境由数日前的旅店逮捕引出。"),
(11,30,"回忆显示Tyrion因人数劣势主动投降，也看见Catelyn动员并不完整；她用Winterfell假消息把追兵引错方向。"),
(31,63,"high road环境替代绳索成为牢笼；休息争论中Tyrion攻击dagger作案逻辑与Littlefinger可信度，开始动摇叙述。"),
(64,89,"mountain clans突袭迫使双方武装合作；Tyrion首次用axe杀人，并在可以旁观时主动救下Catelyn。"),
(90,112,"战后loot、伤亡与埋葬争论突出survival伦理；Tyrion保留武器、改善位置，并继续指出Littlefinger赌局故事的破绽。"),
]

BACKGROUNDS = {
5:"**Dothraki：** Essos游牧战士文化，以horse为生活核心；Tyrion的描述带有强烈个人厌恶与外部视角。",
16:"**Night’s Watch中立：** black brothers宣誓不介入realm贵族争斗，因此Yoren不会为Tyrion或Catelyn拔剑。",
21:"**封臣响应：** 旅店约五十人中约十二人实际拔剑；公开承认lord关系不保证所有随从都参与拘捕。",
24:"**通信：** 骑手传讯与raven network会把逮捕消息送往Casterly Rock、King’s Landing或各riverlord。",
28:"**high road：** 从riverlands向东进入Vale山区的道路，目标不再是Winterfell，而很可能是Eyrie。",
31:"**mountain clans：** Vale高地独立武装群体，不服从Arryn法律；本章提到Milk Snakes与Moon Brothers等名称。",
32:"**Lysa Arryn：** Catelyn妹妹、Jon遗孀，掌控Eyrie；此前已指控Lannisters杀害丈夫。",
38:"**押送成员：** Ser Willis属House Whent；Kurleket、Lharys、Mohor属Bracken；Bronn与Chiggen为sellswords。",
45:"**dagger争议：** 刺客确持Valyrian steel dagger；其是否属于Tyrion只来自Littlefinger对旧赌局的说法。",
61:"**赌局版本：** Catelyn所知说法是Tyrion在Joffrey name day tourney、Jaime对Loras的比赛中赢得dagger。",
68:"**clan目标：** Tyrion判断clans不尊重great-house阵营，可能杀男俘女；这是基于其地区知识的风险评估。",
81:"**装备差异：** clansmen使用boiled leather、拼凑armor及农具改制武器，与tourney统一纹章和昂贵plate形成对照。",
96:"**本方伤亡：** Kurleket、Mohor和Jyck死亡；Ser Rodrik负伤，Marillion重伤，horses也有损失。",
112:"**逻辑而非证明：** 若Littlefinger版本要求Tyrion押Loras胜Jaime，就与Tyrion所称“从不押反对家族”冲突；可疑点仍需账目、见证者等核验。",
}

EXTRA_VOCAB = [
("chalk up","/tʃɔːk ʌp/","phr.v.","记上一笔；归因于","a debt"),("carcass","/ˈkɑːrkəs/","n.","动物尸体","dead mare"),("deftly","/ˈdeftli/","adv.","熟练利落地","butchering"),("feral","/ˈferəl/","adj.","野化的；凶野的","dogs"),("scant","/skænt/","adj.","很少的；不足的","appeal"),("queasy","/ˈkwiːzi/","adj.","恶心不安的","forced smile"),("slattern","/ˈslætərn/","n.","邋遢女人（侮辱语）","crowd voice"),("quaver","/ˈkweɪvər/","n./v.","声音颤抖","fear"),("succor","/ˈsʌkər/","n.","援助；救济","call for help"),("palpably","/ˈpælpəbli/","adv.","明显可感觉地","tension ebbs"),("bestir oneself","/bɪˈstɜːr/","phr.v.","开始行动；费心行动","Tywin pursuit"),("curry favor","/ˈkɜːri ˈfeɪvər/","phr.v.","讨好；巴结","river lord"),("chafe","/tʃeɪf/","v.","摩擦磨伤","rope"),("seep","/siːp/","v.","渗入；逐渐显现","dawn light"),("galling","/ˈɡɔːlɪŋ/","adj.","令人恼怒屈辱的","outwitted"),("fastness","/ˈfæstnəs/","n.","险固据点","mountain homes"),("stolid","/ˈstɑːlɪd/","adj.","沉着木讷的","Ser Willis"),("red smile","/red smaɪl/","metaphor","割喉形成的血口","threat"),("footpad","/ˈfʊtpæd/","n.","拦路贼；低级刺客","assassin"),("maidenhead","/ˈmeɪdənhed/","n.","处女身份（旧式委婉语）","court boast"),("dirk","/dɜːrk/","n.","长匕首","Kurleket"),("fervor","/ˈfɜːrvər/","n.","狂热；强烈激情","clan violence"),("tuft","/tʌft/","n.","一簇毛发","Lharys hair"),("quiver","/ˈkwɪvər/","n.","箭袋","Morrec"),("haft","/hæft/","n.","斧、刀等的柄","axe"),("maul","/mɔːl/","n.","重锤","clan weapon"),("brandish","/ˈbrændɪʃ/","v.","挥舞展示武器","battle cry"),("hew","/hjuː/","v.","砍劈","horse legs"),("vanquish","/ˈvæŋkwɪʃ/","v.","击败","enemy"),("blooded","/ˈblʌdɪd/","adj.","首次经历战斗见血的","first battle"),("scrawny","/ˈskrɔːni/","adj.","骨瘦如柴的","clan horses"),("notched","/nɑːtʃt/","adj.","有缺口的","cheap sword"),("cairn","/kern/","n.","石堆坟标","burial"),("craven","/ˈkreɪvən/","n./adj.","懦夫；怯懦的","rhyme with raven"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def main():
    blocks = extract_range(300, 312, "TYRION", "CH31")
    write_chapter(
        out=OUT, chapter=31, pov="TYRION", page_start=300, page_end=312,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在俘虏处境、路线欺骗、证据逻辑、mountain clans威胁与临时合作。",
        vocab=VOCAB,
        guide="Tyrion在high road上回忆自己如何因寡不敌众主动投降，又如何看出Catelyn在旅店只动员了少数人。她公开宣称返回Winterfell，实际借hood和夜路转向Eyrie，把消息传播者变成误导追兵的工具。休整时Tyrion指出：用自己的rare dagger雇普通assassin极不合理，且Littlefinger有撒谎动机；争论尚未结束，mountain clans突然袭击。共同生存迫使Catelyn给俘虏武器，Tyrion首次参战并主动救下她。战后双方仍不互信，但他保留dirk和axe，已从蒙眼绑手的囚犯变成受控战斗资源。结尾他给出Littlefinger赌局故事的核心破绽：自己从不押注反对Jaime或家族。",
        people=[
            ("Tyrion Lannister","本章视角；分析Catelyn策略、质疑dagger证据、首次参战并改善俘虏位置"),
            ("Catelyn Stark","以Winterfell假路线误导追兵，在clan伏击中暂时武装俘虏"),
            ("Ser Rodrik Cassel","押送队军事骨干，伏击中受伤，战后支持立即撤离"),
            ("Bronn / Chiggen","实用主义sellswords，作战强悍、战后loot，并优先选择生存"),
            ("Marillion","为歌曲素材自愿同行，遇袭后harp、肋骨与手指受损"),
            ("Jyck / Morrec","Tyrion随从；Jyck战死，Morrec以bow参战"),
            ("Kurleket / Lharys / Mohor","Bracken men；Kurleket与Mohor战死，Lharys负责侦察"),
            ("Ser Willis Wode","Whent hedge knight，支持Catelyn并多次提出休息或撤离建议"),
        ],
        terms=[
            ("high road","进入Vale山区并通往Eyrie的险路；地形使逃跑与追击都困难"),
            ("mountain clans","不服Arryn法律的高地武装群体，使用拼凑装备伏击旅人"),
            ("misdirection","Catelyn公开反复说Winterfell，实际向东，以真实传播制造错误追踪方向"),
            ("red smile","割喉威胁的黑色隐喻，显示押送者对Tyrion的敌意"),
            ("cairn","用石块覆盖或纪念尸体的石堆，在无法挖掘的山地替代坟墓"),
        ],
        synthesis="Chapter 31把聪明写成动态校正，而不是永远算对。Tyrion在旅店准确判断不能拔剑，却错误相信公开消息会让人救他；Catelyn更高一层地利用了这套传播网络。到了high road，Tyrion又从失败中重新计算：他以俘虏不能死说明休息的必要，以rare dagger不该回指主谋攻击指控，以四名额外战士换取武器。伏击让语言谈判变为共同流血；他救Catelyn不是因为已经原谅她，而是行动先于仇恨。战后Catelyn仍拒绝trust，却允许他持武器，说明合作可以建立在利益和已观察行为上，不必假装双方已和解。",
        contrasts=[
            "**公开Winterfell／实际Eyrie：** 可传播的真话形式被用于制造错误路线。",
            "**绑绳监狱／山地监狱：** 手被放开后，环境仍使Tyrion无法逃生。",
            "**great-house feud／共同外敌：** clans不承认封建阵营，迫使Stark与Lannister协战。",
            "**tourney heraldry／clan伏击：** 前者有旗鼓和规则，后者只以箭声开始。",
            "**想让Catelyn被抓／实际救她：** Tyrion的即时行动反驳其报复念头。",
            "**trust／utility：** Catelyn不信任Tyrion，却承认他的axe可能救命。",
        ],
        questions=[
            "Catelyn会如何核验Littlefinger关于dagger赌局的版本？",
            "Tyrion救下Catelyn并遵守战后约定，会不会改变押送队对他的判断？",
            "队伍能否在horses、guards和Ser Rodrik受伤的情况下抵达Eyrie？",
            "Bronn与Chiggen开始同Tyrion共享笑声，未来更看重谁提供的利益？",
        ],
        extraction_notes="PDF pp.300–312共112段；正确合并5处跨页续段：pp.300–301、303–304、308–309、309–310与310–311。逐页复核未发现额外分页误切。",
    )
    print(f"Wrote Chapter 31 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
