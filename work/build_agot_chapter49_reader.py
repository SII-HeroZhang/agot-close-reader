#!/usr/bin/env python3
"""Build Chapter 49 (EDDARD) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter48_reader import VOCAB as BASE_VOCAB

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"/"AGOT_逐章精读"

S={
1:"黎明马蹄声惊醒Eddard；他看见Sandor与Lannister guards高调操练、刺穿草人头部。",
2:"Eddard怀疑演武是向自己示威，也不解Cersei为何在获得多次逃走机会后仍留在城中。",
3:"阴沉早餐中Sansa拒食，Arya却大吃并请求启航前再上一次Syrio的课。",
4:"Eddard同意短课，但要求Arya中午前洗好、换装、准备离开。",
5:"Arya重复期限表示明白。",
6:"Sansa拿Arya获准上课作比较，再次请求向Joffrey告别。",
7:"Mordane愿陪Sansa前往并保证不误船。",
8:"Eddard只说现在见Joffrey不明智，没有揭露危险原因。",
9:"Sansa含泪追问原因。",
10:"Mordane以父权和服从制止Sansa质疑。",
11:"Sansa喊不公平，撞倒椅子哭着跑出solar。",
12:"Eddard阻止Mordane追赶，打算等全家安全回Winterfell再解释。",
13:"一小时后Pycelle神情沉重地来报Robert已经死亡。",
14:"Eddard用love、laughter和righteous battle替代rest悼念朋友；他压下哭泣，立即召集council到更安全的Tower of the Hand。",
15:"Pycelle建议悲痛新鲜时把国事推迟到明日。",
16:"Eddard坚持必须立刻开会。",
17:"Pycelle服从召集，同时接受座椅和sweet beer休息。",
18:"Barristan最先到场，却请求回到他认定的young king身边。",
19:"Eddard要求Barristan留在council。",
20:"Littlefinger穿昨夜衣服、boots带尘而来，报告Eddard交给他的任务已经完成。",
21:"Varys沐浴整洁后无声入内，以little birds的悲歌宣告realm哀悼并催促开始。",
22:"Eddard说要等Renly到场。",
23:"Varys告知Renly已经离城。",
24:"Eddard震惊，因为他原本指望Renly支持。",
25:"Renly在黎明前带Loras与约五十retainers从postern gate南逃，可能去Storm’s End或Highgarden。",
26:"Eddard意识到Renly的百剑已不存在，只能出示Robert last letter并说明其seal与witness。",
27:"Barristan验证seal未破，宣读Eddard获任Protector并摄政至heir成年。",
28:"Eddard暗想真正heir Stannis早已成年，却因不信Pycelle、Varys且顾忌Barristan忠于Joffrey而暂不公开，计划先巩固regency、送走女儿并等Stannis带兵回来。",
29:"Eddard请求council确认其Protector身份，同时观察众人难以读取的表情动作。",
30:"Fat Tom进门报告royal steward坚持求见。",
31:"steward以‘king’命令small council立刻去throne room。",
32:"Eddard早料Cersei会迅速行动；他指出Robert已死但同意前往，并命Tomard组织escort。",
33:"Littlefinger扶伤腿的Eddard下楼；八名Stark men护送，城墙与gate上众多gold cloaks使他安心。",
34:"全甲Janos Slynt在throne room门前迎接，City Watch打开巨大oak doors。",
35:"royal steward用完整王号宣布Joffrey为king及Protector。",
36:"Eddard在Littlefinger支撑下走向Iron Throne，回想上次曾带剑逼Jaime离座，怀疑Joffrey是否也会轻易退下。",
37:"五名Kingsguard全甲列阵，Cersei与两个年幼children站在其后，queen以华丽silk、emerald和tiara展示地位。",
38:"Joffrey穿融合lion与stag象征的王服坐在尖刺间，Sandor全副武装守在阶梯下。",
39:"throne后有二十Lannister guards，但Littlefinger兑现表面承诺：City Watch沿墙列阵，人数五比一压过Lannisters。",
40:"长距离行走使Eddard伤腿剧痛，只能继续扶Littlefinger站立。",
41:"Joffrey命council筹备两周内coronation，并要求councillors当日宣誓效忠。",
42:"Eddard拿出Robert letter，请Varys交给Cersei。",
43:"Cersei嘲笑一张paper不能成为shield，当众把授权撕碎撒在地上。",
44:"Barristan因Robert words遭毁而震惊抗议。",
45:"Cersei说已有new king，反过来劝Eddard跪拜Joffrey，以辞去Hand、平安返北作为交换。",
46:"Eddard拒绝，公开宣称Joffrey无权继位，Stannis才是Robert true heir。",
47:"Joffrey涨红脸尖叫Eddard撒谎。",
48:"Myrcella不解地问母亲Joffrey难道不是king。",
49:"Cersei把Eddard的继承主张定为自证treason，并命Barristan逮捕他。",
50:"Barristan犹豫，Stark guards立刻拔剑围住他。",
51:"Cersei把拔剑称为从言语到行动的treason；Sandor、Kingsguard与Lannister guards同步迎战。",
52:"Joffrey从throne上命令杀死Eddard及其所有人。",
53:"Eddard命Janos以City Watch拘押Cersei和children，强调不得伤害，只需软禁看守。",
54:"Janos戴盔下令，百名gold cloaks平举长矛包围。",
55:"Eddard仍要求避免流血，劝Cersei让部下放下武器，但话未说完。",
56:"最近的gold cloak突然从背后刺穿Tomard，表明City Watch真正攻击的是Stark side。",
57:"Janos亲手割开Varly喉咙；Cayn短暂反抗后被Sandor斩手并致命劈开胸肩。",
58:"Stark men被杀时Littlefinger抽出Eddard自己的dagger抵住其喉下，带着歉意提醒自己早警告过不可相信他。",
}
SUMMARIES=[S[i] for i in range(1,59)]

KEY_NOTES={
1:"mock warriors的head被lance刺爆，是公开演练也是即将真实流血的视觉预演；brave show带有Eddard轻蔑判断。",
2:"Eddard把Cersei未逃解释为foolish，显示他仍假定自己的warning定义了她的最佳选择，没有充分考虑她会进攻。",
3:"Sansa不食与Arya wolfed down以食欲对照心理状态；evening ship仍让Eddard相信撤离计划尚可执行。",
8:"不说明paternity与政变风险是保护也是信息隔离；Sansa只感受到任意禁止，无法按真实危险行动。",
12:"when safely back in Winterfell把解释推迟到安全之后，但安全本身依赖她们先服从不理解的命令。",
14:"标题带来的公共角色压制私人哀悼；Eddard没有时间完成grief，Robert death立刻成为constitutional deadline。",
15:"Pycelle的明日建议表面合礼，实际会把整夜准备时间交给掌控royal household的一方；本段不证明他故意拖延。",
18:"Barristan说young king而非Joffrey，先以office和assumed succession定位忠诚。",
20:"dusty boots与昨夜服饰是Littlefinger一夜活动的物证；accomplished只证明他声称完成，尚不证明gold cloaks忠于谁。",
21:"Varys洗浴、粉面与轻步和房中疲惫者形成反差；grievous song把情报网络拟作公共哀悼。",
25:"postern gate、before dawn、in haste显示Renly有预先撤退计划；目的地是Varys推测，不是已确认路线。",
26:"so much for压缩Eddard对一项兵力支柱消失的反应；他感到不祥却因时间已无法补救。",
27:"letter只写the heir而非Joffrey，延续Eddard上一章的语义改写；Barristan确认的是seal真实性，不是heir身份。",
28:"Eddard开始play the game并主动deceit，但计划依赖三件未完成事件：regency获确认、女儿离城、Stannis带power抵达。",
29:"half-closed eyes、half-smile、fluttering fingers提供表情却不提供内心，强调council room的信息不对称。",
31:"steward仍称the king，说明Cersei阵营已把Joffrey继位当作完成事实，而非等待council确认。",
33:"Eddard因gold cloaks数量而reassured；读者知道这一安全感完全依赖Littlefinger的交易确实把command交给他。",
35:"完整royal style通过口头仪式制造合法性；其中Protector title也抢先占据Robert letter赋给Eddard的称号。",
36:"过去Jaime坐throne的记忆把两次政权转换叠合；上次Eddard有victorious army，这次只能跛行并倚靠broker。",
37:"Cersei的服饰不是战甲，却用royal color、jewels与position构成政治armor。",
38:"lion/stag各五十的cape用纹章宣称Lannister与Baratheon结合合法；Iron Throne barbs让少年身体置于危险权力象征中。",
39:"five to one建立Eddard的数量优势错觉；人数只有在command loyalty可靠时才等于力量。",
40:"他字面上靠Littlefinger支撑身体，也在政治上靠其购买的Watch，双重依赖在背叛前被明确可视化。",
41:"Joffrey先要求coronation与fealty，把自己作为king的结论置于任何succession审议之前。",
43:"paper/shield对照把legal authority的弱点具体化：没有执行者时，真实seal也可被手撕毁。",
44:"Barristan的shock证明他尊重Robert command，却尚未自动转化为替Eddard对抗new king。",
45:"Cersei给的选择复制Eddard此前给她的逃生机会，却把条件改为公开承认Joffrey和政治自我放逐。",
46:"Eddard只说no claim与Stannis heir，未在hall公开children paternity；这保留部分隐私，却无法避免双方变成互斥主权主张。",
48:"Myrcella的普通疑问让children并非权力设计者这一事实短暂显现。",
50:"Barristan一瞬hesitation是制度忠诚冲突：Robert last command、Joffrey apparent kingship、Cersei arrest order彼此不兼容。",
51:"treason的定义取决于谁已是合法sovereign；双方都把对方武力称为叛乱，并用兵器把法律争论变成事实。",
53:"Eddard仍下令no harm，保持对children的保护边界；但custody本身正是他此前拒绝Renly时不愿先做的事。",
54:"closed没有立即标明朝谁合围，延迟一个段落维持Eddard与读者对忠诚方向的悬念。",
56:"长句被破折号打断后立刻出现spear thrust，形式上让暴力切断Eddard的no bloodshed愿望。",
57:"Janos亲自动手证明倒戈是command decision而非单兵误会；Cayn的短暂英勇无法改变兵力结构。",
58:"Eddard曾坚持dagger象征sharp right and wrong，如今它被Littlefinger反用；apologetic smile把礼貌、亲密距离与致命背叛压在一起。",
}

STAGES=[
(1,12,"黎明演武与家庭早餐并置：Eddard准备送女儿离城，却仍无法向Sansa说明Joffrey危险。"),
(13,29,"Robert死讯到来，Eddard压下悲痛召集council；Renly已南逃，他试图凭sealed letter先建立regency。"),
(30,40,"Cersei抢先召council到throne room并把Joffrey摆上Iron Throne；Eddard因City Watch五倍人数产生安全感。"),
(41,51,"Joffrey要求fealty，Cersei撕毁Robert letter；Eddard公开Stannis继承权后，双方互指treason并拔剑。"),
(52,58,"Eddard命City Watch拘押queen且避免伤害，但Janos反向屠杀Stark guards，Littlefinger以Eddard dagger完成背叛。"),
]

BACKGROUNDS={
1:"**Lannister household guard：** crimson cloaks直属Lannister权力，不等同由city treasury与Janos指挥的gold cloaks。",
3:"**撤离计划：** Wind Witch原定当晚载Sansa、Arya及household离开King’s Landing，Tomard负责escort。",
13:"**Robert death：** boar造成的大范围感染伤已被Pycelle判断无可救治；Robert临终任Eddard摄政。",
18:"**Kingsguard duty：** Barristan须保护reigning monarch；争议恰在Joffrey是否已合法成为king。",
20:"**Littlefinger task：** Eddard请他用六千gold确保Janos、officers与City Watch支持自己。",
25:"**Renly forces：** Renly前夜曾提议集结约百剑控制royal children；被Eddard拒绝后，他带自己核心retinue离城。",
27:"**Robert will：** Eddard将Robert口述的my son Joffrey写成my heir，使文件未明确点名继承者。",
28:"**Stannis claim：** Eddard已确认Cersei children并非Robert所生，因此认定Robert elder surviving brother Stannis为legal heir。",
34:"**Janos Slynt：** City Watch commander；Eddard相信Littlefinger已通过gold买到他的支持。",
35:"**royal style：** 长串称号是monarch正式身份宣告；说出称号本身不解决血统争议，却能制造既成礼仪。",
39:"**force map：** hall中约二十Lannister guards，五名Kingsguard与Sandor；City Watch约百人，表面数量占优。",
43:"**seal与enforcement：** king seal可证明命令真实，但paper无法自己指挥guards；authority需要institutions承认并执行。",
49:"**treason dispute：** 若Joffrey是king，Eddard否认他即treason；若Stannis是heir，Cersei拥立Joffrey才是usurpation。",
56:"**当前可知：** City Watch并未执行Eddard custody order，而是按Janos command攻击Stark men；更早交易细节仍未知。",
}

EXTRA_VOCAB=[
("hoofbeat","/ˈhuːfbiːt/","n.","马蹄声","thunder of hoofbeats"),("hard-packed","/ˌhɑːrd ˈpækt/","adj.","夯实坚硬的","ground"),
("dummy","/ˈdʌmi/","n.","假人；靶人","straw warrior"),("overcast","/ˈoʊvərkæst/","adj.","阴云密布的","morning"),
("disconsolate","/dɪsˈkɑːnsələt/","adj.","悲伤且无法安慰的","Sansa"),("sullenly","/ˈsʌlənli/","adv.","闷闷不乐地","stare"),
("wolf down","/wʊlf daʊn/","v.","狼吞虎咽","food"),("solar","/ˈsoʊlər/","n.","城堡中的私人起居室","Hand’s rooms"),
("righteous","/ˈraɪtʃəs/","adj.","正义的；正当的","battle"),("convene","/kənˈviːn/","v.","召集；开会","council"),
("immaculate","/ɪˈmækjələt/","adj.","一尘不染的；完美整洁的","white armor"),("enameled","/ɪˈnæməld/","adj.","有珐琅涂层的","scales"),
("garbed","/ɡɑːrbd/","adj.","穿着……的","velvets"),("grievous","/ˈɡriːvəs/","adj.","令人悲痛的；严重的","song"),
("postern","/ˈpoʊstərn/","n.","城堡侧门；便门","postern gate"),("retainer","/rɪˈteɪnər/","n.","家臣；随从","armed following"),
("herein","/ˌhɪrˈɪn/","adv.","在本文件中","legal wording"),("keep one’s counsel","/kiːp wʌnz ˈkaʊnsəl/","phr.","暂不吐露自己的计划","political caution"),
("tread softly","/tred ˈsɔːftli/","phr.","谨慎行事","avoid alarm"),("flutter","/ˈflʌtər/","v.","快速颤动；飘落","fingers/paper"),
("steward","/ˈstuːərd/","n.","管事；礼仪官","royal steward"),("nonetheless","/ˌnʌnðəˈles/","adv.","尽管如此","go anyway"),
("ornate","/ɔːrˈneɪt/","adj.","华丽繁复的","armor"),("high-crested","/ˌhaɪ ˈkrestɪd/","adj.","有高耸盔饰的","helm"),
("banded","/ˈbændɪd/","adj.","以金属条加固的","doors"),("hail","/heɪl/","v.","向……致敬；欢呼拥戴","All hail"),
("Rhoynar","/ˈrɔɪnɑːr/","n.","Rhoyne移民后裔；王号中的民族","royal style"),("barb","/bɑːrb/","n.","倒钩尖刺","Iron Throne"),
("Myrish","/ˈmɪərɪʃ/","adj.","来自Myr的","lace"),("tiara","/tiˈerə/","n.","冠状头饰","queen"),
("haft","/hæft/","n.","刀枪的柄","spear haft"),("fortnight","/ˈfɔːrtnaɪt/","n.","两周","coronation deadline"),
("coronation","/ˌkɔːrəˈneɪʃən/","n.","加冕礼","king-making ritual"),("fealty","/ˈfiːəlti/","n.","臣属效忠","oath of fealty"),
("courtesy","/ˈkɜːrtəsi/","n.","礼尚往来；礼貌","return the courtesy"),("condemn","/kənˈdem/","v.","判定有罪；使陷入不利","condemn yourself"),
("seize","/siːz/","v.","逮捕；夺取","seize the traitor"),("rasp","/ræsp/","n.","刺耳摩擦声","metal on metal"),
("take into custody","/teɪk ˈɪntuː ˈkʌstədi/","phr.","拘押","queen and children"),("level","/ˈlevəl/","v.","把武器平举瞄准","spears"),
("bloodshed","/ˈblʌdʃed/","n.","流血冲突","avoid violence"),("nerveless","/ˈnɜːrvləs/","adj.","失去知觉或力量的","fingers"),
("flurry","/ˈflɜːri/","n.","一阵快速连续动作","blows"),("sheath","/ʃiːθ/","n.","刀鞘","dagger sheath"),
]
VOCAB=BASE_VOCAB+EXTRA_VOCAB

def extract_blocks():
    return extract_range(480,485,"EDDARD","CH49")

def main():
    blocks=extract_blocks()
    write_chapter(
        out=OUT,chapter=49,pov="EDDARD",page_start=480,page_end=485,
        blocks=blocks,summaries=SUMMARIES,key_notes=KEY_NOTES,stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Robert死后的继承争议、Eddard信息限制及各支武装的实际command。",
        vocab=VOCAB,
        guide="Robert死亡把Eddard的私下调查变成必须立即执行的succession crisis。他一面仍安排Arya、Sansa当晚离城，一面召council凭sealed will确立regency，却发现Renly已带核心人马南逃。Eddard决定暂不公开paternity细节，等女儿安全、Stannis率军抵达后再处理继承；这一计划需要时间，也需要Littlefinger承诺买下的City Watch。Cersei不给他时间：她先把Joffrey置于Iron Throne、要求fealty，并当众撕碎Robert letter。双方的法律主张最终由hall里的武装决定。Eddard看到gold cloaks五倍于Lannisters而安心，却忽略了数量不等于忠诚；Janos命他们屠杀Stark guards，Littlefinger则以Eddard自己的dagger抵住他。纸面合法性、军事执行力与中间人控制在这一场景中彻底分离。",
        people=[
            ("Eddard Stark","本章视角；试图凭Robert will摄政并拥立Stannis，最终遭City Watch与Littlefinger背叛"),
            ("Cersei Lannister","抢先拥立Joffrey、撕毁will，并把Eddard继承主张定为treason"),
            ("Joffrey Baratheon","坐上Iron Throne、要求coronation与fealty，并下令杀死Eddard一方"),
            ("Petyr Baelish","声称已完成收买City Watch，先支撑Eddard行走，最后持其dagger控制他"),
            ("Janos Slynt","City Watch commander；表面兵力优势的关键，实际下令攻击Stark guards"),
            ("Barristan Selmy","验证Robert seal，却在旧王遗命与new king命令间犹豫"),
            ("Renly Baratheon","黎明前带Loras与五十retainers离城，使Eddard失去预期支持"),
            ("Tomard","Eddard loyal guard，被gold cloak从背后刺杀"),
            ("Cayn","奋力反抗City Watch，随后被Sandor杀死"),
        ],
        terms=[
            ("Robert’s last letter","任Eddard为Protector与Regent至‘heir’成年、带真实seal的遗命"),
            ("Lord Protector","摄政期间保卫并治理realm的职位；Eddard与Joffrey王号同时争用此权威"),
            ("City Watch / gold cloaks","King’s Landing治安武装，人数优势由Janos Slynt统一指挥"),
            ("Iron Throne","Seven Kingdoms王权的座位，也是双方争夺合法性的舞台中心"),
            ("oath of fealty","臣属向君主宣誓忠诚；Joffrey用它迫council承认既成继位"),
        ],
        synthesis="Chapter 49把失败写成一连串彼此嵌套的错误安全感。Eddard认为Cersei未逃说明她愚蠢，却没有把留下视为她准备进攻；认为解释可以等女儿安全返家，却没有确保她们先离开；认为Robert seal能建立regency，却没有控制宣读后的执行机构；认为gold cloaks人数五倍即可压倒Lannisters，却把command loyalty完全外包给Littlefinger。Cersei的优势不是证明Joffrey血统，而是控制时间、地点、仪式和可动用的武力：council被召到Joffrey已坐稳的throne room，coronation与fealty被当作待办事项，will则被降为可撕的paper。Eddard仍坚持不伤害children、不流血，但当双方都以treason称呼对方时，他的克制只有忠诚武装才能执行。最后的dagger reversal总结全章：道德判断可以像刀刃一样清楚，谁握着刀柄却决定当下结果。",
        contrasts=[
            "**Robert seal／Cersei撕纸：** 可验证的legal authorization与缺乏enforcement的物理脆弱性。",
            "**five-to-one numbers／single commander：** 数量优势被Janos的command loyalty瞬间反转。",
            "**Littlefinger扶肩／dagger抵喉：** 身体支撑与政治依赖在同一亲密距离内转成控制。",
            "**mock dummy／Tomard、Cayn：** 清晨草人演武在午前变成真实杀戮。",
            "**no bloodshed／sentence interrupted：** Eddard的克制愿望被突刺和破折号同时截断。",
            "**old king’s Hand／boy king’s command：** Robert遗命与Joffrey现场命令争夺Barristan及全hall的服从。",
        ],
        questions=[
            "Littlefinger从何时起决定让City Watch倒向Cersei，六千gold交易实际如何执行？",
            "Renly为何在Robert死前离城，他准备去Storm’s End还是Highgarden？",
            "Barristan在Robert will被撕毁、双方拔剑后会如何定义自己的duty？",
            "Arya与Sansa是否仍能按中午准备、晚间登船的计划离开？",
            "Stannis是否已经收到Eddard密信并会带何种力量返回？",
        ],
        extraction_notes="PDF pp.480–485校勘后共58段，无误切或重复。共4处跨页续段：pp.481–482、482–483、483–484及484–485；段落边界、引号、Robert will措辞、兵力数字与最后dagger动作均已复核。",
    )
    print(f"Wrote Chapter 49 with {len(blocks)} paragraphs")

if __name__=="__main__":
    main()
