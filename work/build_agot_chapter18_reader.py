#!/usr/bin/env python3
"""Build Chapter 18 (CATELYN) close-reading Markdown."""

from pathlib import Path

from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter17_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"Captain Moreo告诉Catelyn，一小时内即可抵达King’s Landing。",
2:"Catelyn强作笑容，答应给每名oarman一枚silver stag。",
3:"Moreo以客套话说替贵妇服务已是船员的全部报酬。",
4:"Catelyn看穿客套，指出船员仍会收钱。",
5:"Moreo承认后，叙述交代这位Tyroshi船长的经历和六十桨双桅快船Storm Dancer。",
6:"Catelyn回想自己坚持雇快船是正确决定；逆风下若无船桨，他们仍会滞留Fingers附近。",
7:"她以受伤手指的持续疼痛提醒自己使命，并认为永久损伤是换取Bran生命的小代价。",
8:"Ser Rodrik上甲板，Moreo以绿色分叉胡须和热情问候迎接他。",
9:"严重晕船的Ser Rodrik用“已有两天不想死”自嘲病情好转。",
10:"他确实消瘦却恢复许多；此前在Dragonstone外的风暴中差点落海。",
11:"Catelyn告诉他航程即将结束。",
12:"Ser Rodrik苦笑“这么快”，并因反复呕吐不得不剃掉标志性白色络腮胡。",
13:"Moreo识趣离开，让二人谈正事。",
14:"快船像dragonfly掠水，Ser Rodrik为自己未能英勇保护Catelyn而自责。",
15:"Catelyn只在意安全抵达；她反复触摸匕首确认它仍在，并准备找king’s master-at-arms鉴定。",
16:"Ser Rodrik认为Ser Aron Santagar虚荣但诚实，也警告二人一上岸便可能被宫廷熟人认出。",
17:"Catelyn想到Petyr Baelish，并回忆Littlefinger绰号来自其矮小身材和家族在Fingers的小领地。",
18:"Ser Rodrik试图委婉提起Petyr过去对Catelyn的感情。",
19:"Catelyn直说二人自幼一起长大；Petyr曾为她挑战Brandon，败后被送走，后来写来的信也被她烧掉。",
20:"Ser Rodrik提醒她Littlefinger如今是small council成员。",
21:"Catelyn承认Petyr聪明、必会出头，却区分clever与wise，并忧虑岁月如何改变了他。",
22:"瞭望手报城，Storm Dancer忙碌起来，King’s Landing出现在三座山丘上。",
23:"Catelyn回顾Aegon三百年前从Dragonstone登陆，并在最高山丘修建最初堡垒。",
24:"她观察拥挤城市、Great Sept of Baelor、废弃Dragonpit及连接两丘的Street of the Sisters。",
25:"港口挤满各地船只；王后华丽驳船、Ibben捕鲸船与金色战舰并列。",
26:"Red Keep高踞Aegon’s hill；Maegor完工后杀死所有工匠，以独占堡垒秘密。",
27:"Targaryen黑龙旗已被Baratheon金色crowned stag取代。",
28:"来自Summer Isles的swan ship驶离，Storm Dancer继续靠岸。",
29:"Ser Rodrik建议Catelyn不进城堡，由自己秘密找Ser Aron。",
30:"Catelyn指出他同样会有风险。",
31:"Ser Rodrik认为剃掉胡须后连自己都认不出，足以充当伪装。",
32:"Moreo熟练指挥六十桨倒划、收桨、靠港，又询问是否把行李送进城堡。",
33:"Catelyn说不去城堡，请他推荐河边干净舒适的inn。",
34:"Moreo先谈余款和答应给船员的六十枚silver stags。",
35:"Catelyn强调额外银币属于oarsmen。",
36:"Moreo建议自己代管，声称船员会在King’s Landing赌博或寻欢花光。",
37:"Ser Rodrik说钱也可能有更坏用法，并引用Winter is coming。",
38:"Catelyn坚持成年人有权决定如何花自己挣来的钱。",
39:"Moreo表面顺从。",
40:"Catelyn亲自付钱并住进Eel Alley旅店；老板多疑但房间合用，最重要的是不问姓名。",
41:"Ser Rodrik伪装携武器出门，嘱她远离common room并承诺天黑前带Ser Aron回来。",
42:"疲惫的Catelyn看他消失在人群后，很快在草垫床上睡着。",
43:"猛烈敲门声把她惊醒。",
44:"夕阳已红，门外以king名义命她开门。",
45:"Catelyn披斗篷并先拿起床边匕首才开门。",
46:"闯入者穿City Watch的黑甲金斗篷；句子在本PDF跨页断开。",
47:"gold cloaks说奉命护送她去castle，无需用匕首。",
48:"Catelyn追问命令来自谁。",
49:"灰蜡mockingbird印章让她认出Petyr，并担忧Ser Rodrik出事。",
50:"队长并不知道她身份，只知道Littlefinger要求安全带人。",
51:"Catelyn冷静要求他们在门外等她更衣。",
52:"她艰难包扎、穿衣并推理消息如何泄露；Ser Rodrik忠诚，Lannisters先到也解释不通。",
53:"她怀疑Moreo出卖行踪，并讽刺希望他卖了好价钱。",
54:"gold cloaks护送她穿夜城，从postern进入封闭的Red Keep再登塔。",
55:"Petyr独自在灯边写字，以旧称“Cat”迎接她。",
56:"Catelyn质问为何用这种方式带她来。",
57:"Petyr遣走守卫，确认她未受虐待并注意到手上绷带。",
58:"Catelyn拒答伤情，冷冷批评他像召唤serving wench般无礼。",
59:"Petyr摆出童年犯错后惯用的悔意表情；Catelyn观察他仍矮小敏捷、眼含笑意并佩银色mockingbird。",
60:"她再次追问他如何知道自己在城中。",
61:"Petyr说Varys无所不知且即将加入，自己只想先与她独处片刻。",
62:"Catelyn无视亲昵称呼，确认发现她的是King’s Spider。",
63:"Petyr说Varys对绰号敏感，拥有遍布全城的little birds，且是他先把消息告诉自己。",
64:"Catelyn问Varys为何选择Petyr。",
65:"Petyr列举自己master of coin和councillor身份，并称自己与Lysa友好，因此是合理选择。",
66:"Catelyn试探Varys是否知道她此行秘密。",
67:"Petyr说Varys什么都知道，唯独不知道她为何来，并直接反问。",
68:"Catelyn以妻子思念丈夫、母亲思念女儿作掩饰。",
69:"Petyr识破，借Tully家语说明自己了解她的责任模式。",
70:"Catelyn僵硬念出Family, Duty, Honor，承认他确实熟悉自己。",
71:"Petyr说这些责任本应让她留在Winterfell，故突然来访必有急事；敲门声随后打断。",
72:"Varys以香粉、丝绸和柔软触感登场，握住Catelyn的手并热情提出提供药膏。",
73:"Catelyn抽回手，说Maester Luwin已处理伤口。",
74:"Varys为Bran遭遇表示悲伤。",
75:"Catelyn礼貌同意，却在心中认为他的lord只是council礼称，真正统治的是情报蛛网。",
76:"Varys强调自己敬重Eddard，且二人都爱Robert。",
77:"Catelyn被迫附和。",
78:"Littlefinger讥讽Robert只在Varys听得到的地方最受爱戴。",
79:"Varys又提出从Free Cities找神奇医者治疗Bran。",
80:"Catelyn拒绝谈Bran，不让这两个不可信男人看见悲伤，转问Varys为何带她来。",
81:"Varys承认安排护送，随后毫无铺垫地要求看那把匕首。",
82:"Catelyn震惊他知道秘密，立即怀疑Ser Rodrik遭到伤害。",
83:"Littlefinger坦言完全不知匕首和Ser Rodrik之事。",
84:"Varys准确叙述Ser Rodrik拜访Ser Aron、返回旅店并等候Catelyn的全过程，保证他无恙。",
85:"Catelyn追问Varys如何可能知道这些细节。",
86:"Varys只以little birds解释情报工作，并确认匕首就在她身上。",
87:"Catelyn把匕首扔到桌上，挑战little birds说出主人。",
88:"Varys夸张地试刀锋，拇指见血后尖叫丢刀。",
89:"Catelyn干巴巴提醒它很锋利。",
90:"Littlefinger指出Valyrian steel极利，熟练抛接并说寻主人根本不需Ser Aron。",
91:"Catelyn问若直接找他，他会给什么答案。",
92:"Littlefinger说King’s Landing只有这一把，随后把刀掷入门板并宣称它曾属于自己。",
93:"Catelyn困惑，因为Petyr不可能亲自出现在Winterfell。",
94:"Petyr说自己在Joffrey命名日tourney押Jaime，却因Loras获胜输掉匕首，赢家保留赌注。",
95:"Catelyn因旧伤记忆而恐惧，逼问赢家是谁。",
96:"Littlefinger指认Tyrion Lannister，Varys则观察Catelyn听到答案后的表情。",
}
SUMMARIES=[S[i] for i in range(1,46)] + [
    "闯入者穿City Watch的黑甲金斗篷；队长说奉命护送她去castle，无需使用匕首。"
] + [S[i] for i in range(48,97)]

KEY_NOTES={
2:"forced herself to smile表明礼貌是意志行为；Catelyn已经接近目标，却没有放松。",
4:"一句短答拆穿船长的华丽客套，使她保持实际判断。",
7:"pain既是身体后果也是她主动使用的记忆工具；scourge带有鞭打和惩戒色彩。",
9:"Ser Rodrik用夸张死亡愿望消解晕船羞耻，显出他恢复了自嘲能力。",
12:"白胡须曾是身份标志，呕吐迫使他剃掉后反而成为潜入伪装。",
15:"她反复触摸匕首类似检查伤口：物证、创伤与使命被绑在同一物件上。",
17:"Littlefinger同时来自地理、身材与童年权力关系；绰号把成年councillor固定在少年形象里。",
19:"Catelyn称Petyr像兄弟，而他为婚约决斗；双方对亲密关系的定义从少年时代就不一致。",
21:"clever不等于wise是Catelyn对Petyr的核心保留：聪明描述能力，智慧还包含判断与克制。",
23:"城市历史从少数渔民和木土堡垒开始，Aegon的登陆把自然山丘转成王权中心。",
24:"长列举让King’s Landing同时显得繁荣、拥挤、神圣、商业化和腐败，拒绝单一城市印象。",
26:"Red Keep的秘密建立在工匠被集体灭口上；宏伟建筑的权威外观遮住其暴力生产史。",
27:"建筑仍属于Targaryen时代，旗帜却已更换；政权更迭被压缩成城垛上的颜色和sigil。",
31:"失去胡须既削弱Ser Rodrik自我认同又提供保护，弱点被转化为行动资源。",
34:"Moreo把船员报酬说成自己可代管的款项，前文客套下的avarice此刻变得具体。",
38:"Catelyn以choice维护劳动者对工资的支配权，没有因预判他们可能挥霍便剥夺决定权。",
40:"老板咬金币和不问姓名同样体现交易逻辑：她只验证钱，不追问身份。",
44:"king名义使私人房门外的敲击带上国家强制力；Catelyn尚不知道真正发令者。",
49:"mockingbird seal在说明文字前完成身份识别，纹章在宫廷世界中等同签名。",
52:"这一段展示Catelyn快速排除假设，但她的推理仍受有限信息约束。",
53:"怀疑Moreo合理却尚无证据；后文必须区分她的即时猜测与Varys实际解释。",
55:"Petyr只说Cat，瞬间越过Lady Stark的正式身份，试图恢复旧日亲密位置。",
59:"contrite被明确称为gift，说明悔意表情可能是高效社交表演，而非可靠内心证据。",
63:"little birds把情报来源写得轻巧无害；与Spider绰号合起来则构成覆盖城市的捕捉网络。",
65:"Petyr用官职和人脉解释“为什么是我”，却没有证明Varys没有其他动机。",
68:"Catelyn给出社会上完全合理的女性理由，Petyr却因了解她的Family／Duty逻辑识破。",
71:"Petyr把Tully words当推理工具：真正的谎言不是内容不可能，而是行为不符合Catelyn一贯价值排序。",
72:"Varys的外貌、香气、触感和华服被密集描写，使他的存在几乎侵入所有感官。",
75:"Catelyn在口头礼称与内心降格之间维持礼仪防线，不让不信任直接暴露。",
78:"Littlefinger的笑话表明对Robert的公开忠诚需要根据谁在听而调整。",
80:"不谈Bran是信息自卫；在情报专家面前，情绪本身也可能成为可利用的数据。",
81:"Varys从寒暄突然跳到dagger，展示他不仅知道Catelyn位置，还知道秘密任务核心。",
84:"精确时间线既安抚Catelyn也向她展示监视能力；信息本身带有威慑。",
88:"Varys的尖叫可能是真实失手，也可能是表演；文本只确认刀锋割伤，不能确认意图。",
90:"Littlefinger熟练操刀与Varys的夸张谨慎构成表演风格对照，也强化他对物件的熟悉感。",
92:"“It’s mine”是经过投刀表演后才给出的戏剧性答案，但只说明过去所有权，并未说明刺杀命令。",
94:"Petyr给出一条可追踪的所有权链：自己输给tourney赢家；这仍是他的证词，尚未独立核实。",
96:"答案落在Lannister家族，正好符合Catelyn既有怀疑；Varys不看刀而看她的脸，说明反应也是情报。",
}

STAGES=[
(1,21,"Catelyn抵达前回顾航程、伤手、匕首任务与Petyr少年往事；安全计划建立在秘密入城和有限信任上。"),
(22,40,"King’s Landing以征服史、城市混杂和Red Keep暴力历史展开；Catelyn拒绝进castle并秘密住进Eel Alley。"),
(41,59,"Ser Rodrik外出后，City Watch凭mockingbird印章接走Catelyn；她与成年Petyr重逢，旧亲密和新权力同时出现。"),
(60,80,"Petyr解释Varys的little birds；二人用熟悉、礼貌、家语和客套不断试探Catelyn来意与情绪。"),
(81,96,"Varys直接点破dagger任务并展示完整监视时间线；Petyr声称匕首在tourney中输给Tyrion，使调查突然指向Lannister。"),
]

BACKGROUNDS={
5:"**航海：** Storm Dancer是Tyroshi六十桨trading galley；逆风时桨力使它比纯帆船更可靠。",
17:"**身份：** Petyr Baelish是Catelyn父亲昔日ward，现为Lord Baelish、绰号Littlefinger；其家族领地在Fingers。",
19:"**家族史：** Catelyn原与Eddard兄长Brandon订婚；Brandon死后，Eddard依婚盟娶她。Petyr少年决斗是当前已知旧事。",
23:"**城市史：** Aegon the Conqueror约三百年前从Dragonstone登陆并建立堡垒，King’s Landing由此发展。",
24:"**地标：** Great Sept位于Visenya’s hill；废弃Dragonpit位于Rhaenys’s hill；两者由Street of the Sisters连接。",
26:"**堡垒史：** Red Keep由Aegon下令、Maegor完成；工匠被杀是Catelyn所知历史叙述。",
27:"**纹章：** crowned stag代表House Baratheon，three-headed dragon代表House Targaryen。",
49:"**纹章：** 灰蜡上的mockingbird是Petyr的个人标志，所以Catelyn无需文字即可认出召集者。",
63:"**职务：** Varys是master of whisperers；little birds是他对informants的称呼，其具体人员与方法尚未说明。",
65:"**small council：** 当前留城的主要成员包括Petyr与Pycelle；Selmy、Renly北上，Stannis在Dragonstone。",
70:"**家语：** Family, Duty, Honor是House Tully的words，也是Petyr判断Catelyn行为是否反常的依据。",
75:"**称号：** Varys因council席位被礼称Lord，但没有已知封地；Catelyn内心因此否认其实质领主身份。",
84:"**文本事实：** Varys说Ser Rodrik安全，已见Ser Aron并在旅店等候；这一信息目前来自Varys，Catelyn尚未亲自验证。",
90:"**材料：** dagger刀身为Valyrian steel，兼具稀有、轻利和持刃性；这使它更容易被识别。",
94:"**证词链：** Petyr声称自己在Joffrey name-day tourney押Jaime失败，匕首由赢家保留；尚无第二来源核对。",
96:"**事实／指控：** Littlefinger说tourney赢家是Tyrion Lannister。这是重要线索，不等于已经证明Tyrion策划刺杀。",
}

EXTRA_VOCAB=[
("oarsman","/ˈɔːrzmən/","n.","桨手","galley crew"),("ply","/plaɪ/","v.","定期往返；经营航线","ply the narrow sea"),
("avarice","/ˈævərɪs/","n.","贪财；贪婪","Tyroshi stereotype"),("sloop","/sluːp/","n.","单桅帆船","fishing vessel"),
("scourge","/skɜːrdʒ/","n.","鞭子；折磨或警醒","pain as reminder"),("dexterous","/ˈdekstərəs/","adj.","手指灵巧的","lasting injury"),
("wry","/raɪ/","adj.","挖苦而无奈的","wry smile"),("befouled","/bɪˈfaʊld/","adj.","被严重弄脏的","seasick whiskers"),
("nonplussed","/ˌnɑːnˈplʌst/","adj.","困惑不知所措的","missing whiskers"),("valiant","/ˈvæliənt/","adj.","英勇的","protector"),
("redoubt","/rɪˈdaʊt/","n.","小型防御堡垒","Aegon's first fort"),("crookback","/ˈkrʊkbæk/","adj.","弯曲如驼背的","city streets"),
("barbican","/ˈbɑːrbɪkən/","n.","城堡外堡或门楼","Red Keep"),("battlement","/ˈbætəlmənt/","n.","城垛","banners above"),
("furled","/fɜːrld/","adj.","卷拢的","sails"),("postern","/ˈpoʊstərn/","n.","城堡小侧门","secret entrance"),
("contrite","/kənˈtraɪt/","adj.","悔恨的；显得抱歉的","Petyr's expression"),("solicitude","/səˈlɪsɪtuːd/","n.","关切；殷勤","Varys's manner"),
("bespeak","/bɪˈspiːk/","v.","表明；显示","bespeaks urgency"),("salve","/sæv/","n.","药膏","for injured hands"),
("admonition","/ˌædməˈnɪʃən/","n.","告诫；责备","sullen look"),("heft","/heft/","v.","掂量重量","test the dagger"),
("quiver","/ˈkwɪvər/","v.","颤动","blade in door"),("trifle","/ˈtraɪfəl/","n.","少量；一点","a trifle poorer"),
]
VOCAB=BASE_VOCAB+EXTRA_VOCAB

def merge_page_break(blocks):
    """Merge the real paragraph split after 'of the' across PDF pp.161–162."""
    left, right = blocks[45], blocks[46]
    assert left["text"].endswith("of the") and right["text"].startswith("City Watch")
    left["text"] = left["text"] + " " + right["text"]
    left["end_page"] = right["end_page"]
    del blocks[46]
    for order, block in enumerate(blocks, start=1):
        block["order"] = order
        block["id"] = f"CH18-P{int(block['page']):03d}-{order:03d}"
    return blocks

def shifted(mapping):
    """Shift commentary keys after the merged raw blocks 46/47."""
    return {(key - 1 if key >= 48 else key): value for key, value in mapping.items()}

def main():
    blocks=merge_page_break(extract_range(157,166,"CATELYN","CH18"))
    write_chapter(
        out=OUT,chapter=18,pov="CATELYN",page_start=157,page_end=166,
        blocks=blocks,summaries=SUMMARIES,key_notes=shifted(KEY_NOTES),
        stages=[(a - (1 if a >= 48 else 0), b - (1 if b >= 47 else 0), note) for a, b, note in STAGES],
        backgrounds=shifted(BACKGROUNDS),
        default_background="本段没有新增必须补充的世界观事实；重点在秘密行动、城市权力、旧日关系或信息不对称。角色当下的怀疑与证词不自动视为已证实事实。",
        vocab=VOCAB,
        guide="Catelyn与Ser Rodrik乘Storm Dancer抵达King’s Landing，计划秘密寻找Ser Aron鉴定匕首。她没有进入Red Keep，而是住进Eel Alley；然而Varys的情报网迅速发现她，并让Littlefinger借City Watch把她带入castle。Catelyn与童年旧识Petyr重逢，又第一次正面面对master of whisperers Varys。二人不仅知道她的位置，还知道匕首任务。Petyr最终声称匕首曾属于自己，后来在tourney赌局中输给Tyrion Lannister。这个答案是调查线索和个人证词，而非已经完成核实的定罪。",
        people=[
            ("Catelyn Stark","本章视角人物；秘密携匕首抵达King’s Landing调查Bran遇刺"),
            ("Ser Rodrik Cassel","同行保护者；剃去白胡须后秘密寻找Ser Aron Santagar"),
            ("Petyr Baelish / Littlefinger","Catelyn童年旧识、master of coin；声称匕首曾属于自己"),
            ("Varys","master of whisperers，以little birds掌握Catelyn行动和匕首秘密"),
            ("Captain Moreo Turnitis","Tyroshi船长，把二人快速送达King’s Landing"),
            ("Ser Aron Santagar","king’s master-at-arms，Ser Rodrik希望请他鉴定匕首"),
            ("Tyrion Lannister","Petyr声称在tourney中赢得匕首的人；当前只是被指认"),
        ],
        terms=[
            ("Storm Dancer","Moreo的六十桨双桅Tyroshi trading galley"),("King’s Landing","王国首都，分布于Blackwater Rush旁三座主要山丘"),
            ("Red Keep","Aegon下令、Maegor完成的王室堡垒"),("City Watch / gold cloaks","首都守卫，穿黑甲和金色斗篷"),
            ("little birds","Varys对遍布城市的informants的称呼"),("Valyrian steel dagger","刺杀Bran所用的稀有匕首，本章调查核心"),
        ],
        synthesis="Chapter 18把调查写成一场关于信息所有权的较量。Catelyn拥有匕首和受伤记忆，却不了解首都；Varys没有拿着物证，却掌握她的住处、同行者、访问路线和秘密目的；Petyr则拥有旧日亲密与对宫廷赌局的解释权。Catelyn一路不断作出合理推断——怀疑Moreo、排除Lannisters先到——但本章反复提醒读者：合理并不等于证实。结尾Tyrion之名极具冲击，因为它吻合她对Lannister的怀疑，也正因此更需要独立核验。",
        contrasts=[
            "**物证／情报：** Catelyn掌握dagger，Varys却掌握物证持有者的完整行动。","**clever／wise：** Catelyn承认Petyr聪明，却保留他是否有智慧和判断力的问题。",
            "**旧日Petyr／当下Littlefinger：** 熟悉的Cat称呼和悔意表情，与master of coin及City Watch调度权并存。","**公开城堡／秘密通道：** Catelyn试图避开Red Keep，最终仍由postern被带入其权力中心。",
            "**礼貌／威慑：** Varys不断说sweet lady、关心Bran，却用精确监视细节证明无人真正隐身。","**线索／定罪：** Petyr给出所有权故事和Tyrion姓名，但尚未提供独立证据证明刺杀命令。",
        ],
        questions=["Petyr关于tourney和dagger归属的说法能否被Ser Aron或其他人证实？","Varys为什么先把Catelyn的消息交给Petyr？","Varys的little birds如何得知匕首秘密？","Catelyn会怎样把Tyrion这一线索告诉Eddard？"],
        extraction_notes="PDF pp.157–166经页面边界复核共95段；除自动识别的pp.158–159、159–160、162–163与165–166外，显式合并p.161末尾‘of the’与p.162开头‘City Watch’，共5个跨页段落",
    )
    print(f"Wrote Chapter 18 with {len(blocks)} paragraphs")

if __name__=="__main__": main()
