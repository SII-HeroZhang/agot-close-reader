#!/usr/bin/env python3
"""Build Chapter 32 (ARYA) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter31_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"一只缺耳黑tomcat弓背向Arya嘶叫。",2:"Arya踮着赤脚、控制呼吸靠近，以Syrio教的quiet as a shadow和light as a feather调节动作。",3:"抓猫训练让她满手抓痕、双膝结痂；Syrio以敌人会造成更重伤害为由逼她继续。",4:"Red Keep各类猫都已被她抓过，唯独这只敢从Tywin手中抢quail的老黑猫仍是目标。",5:"tomcat带她绕遍城堡多处，直到她完全不知位置。",6:"她以为终于把猫堵在狭窄死路，再次默念训练口令逼近。",7:"tomcat突围时Arya准确封路并将其抓住，躲开抓脸前还吻了它一下。",8:"陌生声音把她误称为he并询问她在对猫做什么。",9:"Arya受惊放猫，认出Myrcella、Tommen、septa与两名Lannister guards。",10:"Myrcella把她当成ragged boy并取笑。",11:"Tommen附和说是又脏又臭的男孩。",12:"Arya意识到自己的训练装束和污迹成功掩盖性别身份，于是低头跪下避免被认出。",13:"septa追问这个boy为何进入不该来的区域。",14:"guard把这类穷孩子比作无法挡住的rats。",15:"septa逼问她属于谁、为何不回答。",16:"Arya怕一开口就被Myrcella和Tommen认出。",17:"septa命Godwyn抓她。",18:"恐慌扼住喉咙时，Arya默念calm as still water。",19:"她把Syrio的snake、silk、deer口令逐项化为闪避、旋转和冲刺，撞倒Tommen后逃出包围。",20:"Arya翻滚避追、钻arrow slit、穿走廊庭院与窗户，最终躲进漆黑cellar。",21:"她气喘且迷路，却相信速度使对方没认出自己。",22:"黑暗与滴水唤起她关于Red Keep无尽迷宫、血墙和找不到Eddard的噩梦。",23:"她蜷缩等待，打算数到一万再出去。",24:"眼睛适应后，她看见巨大空眼和长牙，以Syrio口令压住恐惧再睁眼。",25:"“怪物”仍在，但恐惧已经离开。",26:"Arya起身触摸巨大颌骨与黑色利齿，确认它们是真实骨头。",27:"她告诉自己只是skulls，却仍感到被凝视；衣服被fang勾破后，她跃过最大一具的牙床逃向门。",28:"她拉动iron ring，沉重木门发出仿佛全城可闻的巨响后开启。",29:"门外走廊比skull room更黑，Arya改用water dancer的全部感官摸索。",30:"她沿粗石墙滑步前进，以all halls lead somewhere和fear cuts deeper than swords维持镇定，直到感到冷风。",31:"下方脚步、声音和微光显出一口巨大的螺旋石井，有人正从地底上来。",32:"Arya俯视见两人一支torch，影子在井壁上像giants扭动。",33:"第一人说已找到一个bastard，其他目标很快也会被找到。",34:"带Free Cities口音的第二人问那人知道truth后会怎样。",35:"第一人说谋害其son的笨拙行动必令wolf与lion开战，无论他们是否愿意。",36:"第二人认为战争来得太早，自己一方尚未ready，要求delay。",37:"第一人说这等于让他停止时间，反问是否把自己当wizard。",38:"第二人笑说他不亚于wizard；两人即将到顶，Arya伏地屏息隐藏。",39:"torchbearer矮壮、scarred、穿mail与steel cap，步伐无声，让Arya觉得似曾相识。",40:"forked yellow beard的肥胖男人提议既然一名Hand能死，第二名也可，并说对方以前已跳过这支dance。",41:"scarred man说现在不同、Eddard也不同；两人因torch眩光没有看见近在咫尺的Arya。",42:"forked beard要求更多时间，因为pregnant princess的khal要等son出生才行动。",43:"torchbearer触动机关，巨大红石板封住井口，使secret entrance恢复为完整墙面。",44:"scarred man列出失控变量：Stannis、Lysa、Tyrell计划、Littlefinger、Eddard的bastard与book，以及Catelyn拘捕Tyrion可能引发Lannister、Tully连锁战争。",45:"forked beard称他不只是juggler而是真sorcerer，请他继续维持局势。",46:"torchbearer答会尽力，但需要gold和另外五十只birds。",47:"Arya等他们走远后悄悄跟踪。",48:"远处对话提到所需birds难找，必须年轻且识字，也许年长些更不易死。",49:"另一人坚持越年轻越安全，并说要温柔对待。",50:"残缺声音提到如果他们能keep their tongues。",51:"又只听见the risk等碎片。",52:"声音消失后Arya仍追随远处torch，沿更深楼梯进入从砌石变成土木支撑的tunnel。",53:"她在黑暗泥水中继续前进，以想象Nymeria和Syrio陪伴，入夜才终于出地面。",54:"出口是河边sewer；Arya脱下臭衣跳河清洗，路过riders也忽略月下瘦小女孩。",55:"她以Aegon’s Hill上的Red Keep定位返回，却因gate关闭、外表像beggar而被postern guards拒绝。",56:"guard说厨房剩饭已无，不准夜间乞讨。",57:"Arya说自己不是beggar而住在城堡。",58:"guard威胁打耳光驱赶。",59:"Arya要求见father。",60:"年轻guard用粗俗愿望嘲讽她的要求同样不可能实现。",61:"年长guard问她的father是否city ratcatcher。",62:"Arya答是Hand of the King。",63:"guards笑并挥拳时，Arya预判躲开，公开完整身份、以斩首威胁，再反用对方的clout问句命令开门。",64:"Harwin与Fat Tom把她送到Eddard solar；他正在读巨大lineages book，听完报告后遣退guards。",65:"Eddard说半数guards都在找她，Septa Mordane也因恐惧祈祷，并重申不得擅自出castle gates。",66:"Arya急促讲述tunnel、skulls和两名男子谋杀Eddard的对话，又误猜他们说的bastard是Jon。",67:"Eddard追问Jon与说话人。",68:"Arya努力复述forked beard、steel cap、juggling、wolf/lion、pregnant princess和wizard，却承认信息已混杂。",69:"Eddard严肃地以童话式白胡子尖帽反问wizard。",70:"Arya坚持那人外貌不像Old Nan故事，只是被同伴称wizard。",71:"Eddard警告若她编造空气般的故事会受罚。",72:"Arya坚持有secret wall，却省略撞倒Tommen，只说追猫翻窗后发现monsters。",73:"Eddard把monsters、wizards和adventure并列，并抓住juggling与mummery两个词。",74:"Arya想说明还有区别。",75:"Eddard误判两人是来tourney赚钱的mummers，可能受king邀请表演。",76:"Arya固执否认。",77:"Eddard转而责备她跟踪、翻窗与满身抓痕，准备找Syrio谈话。",78:"Desmond敲门打断，报告Night’s Watch black brother有紧急事情求见。",79:"Eddard说自己的门永远向Night’s Watch开放。",80:"Desmond带入肮脏佝偻的Yoren，Eddard仍礼貌询问姓名。",81:"Yoren自报身份，并把Arya误认成Eddard son。",82:"Arya纠正性别后连珠问Robb、Bran、Jon和Ghost，还想托信；她相信Jon会听懂地下故事。",83:"Eddard温和为女儿失礼道歉，并问是否Benjen派Yoren来。",84:"Yoren说自己为Mormont招募人手；因Benjen同为black brother才拼命抢先赶来。",85:"Eddard追问所谓others。",86:"Yoren说旅店sellswords与freeriders闻到blood/gold便四散传讯，其中有人去更近的Casterly Rock，Tywin应已知情。",87:"Eddard问是什么消息。",88:"Yoren看向Arya，要求私下说。",89:"Eddard让Desmond送Arya回房，答应次日继续谈。",90:"Arya担心是Jon或Benjen出事。",91:"Yoren说离Wall时Jon安好，Benjen情况不知，但紧急消息并非关于二人。",92:"Desmond牵她离开。",93:"Arya想偷听却知道Desmond难骗，转而问Eddard在King’s Landing有多少guards。",94:"Desmond答五十。",95:"Arya问他们是否绝不会让人杀Eddard。",96:"Desmond以日夜守卫保证Eddard安全。",97:"Arya指出Lannisters人数超过五十。",98:"Desmond用一个northerner抵十个southron swords安慰她。",99:"Arya追问若派wizard来杀怎么办。",100:"Desmond拔剑说wizard被砍头后与普通人死法相同。",
}
SUMMARIES = [S[i] for i in range(1, 101)]

KEY_NOTES = {
2:"Syrio口令不是漂亮比喻，而是把呼吸、重心、速度转成可调用的身体程序；本章会逐次验证。",
3:"训练刻意把scratch视为低成本反馈，严酷却有明确生存逻辑；Myrish fire的剧痛也显示学习代价。",
4:"black tom被gold cloak称real king，因它能冒犯Tywin而逍遥；这是一则小型权力反讽。",
5:"猫的路线像随机追逐，实际上把Arya带过Red Keep的公开、服务和军事空间，最终越出她熟悉地图。",
7:"她成功不是扑得更快，而是预判左右并cut off escape，说明训练已从反应升级为控制路线。",
12:"衣着使princess误认贵族女孩为穷boy，阶级与性别判断都依赖外观；Arya暂时把偏见变成掩护。",
18:"panic先使她失语，口诀随后恢复行动；勇气不是没有恐惧，而是重获对身体的指挥。",
19:"四句短口令分别对应lean、spin、sprint、slip，语言节奏模拟动作连续加速。",
22:"噩梦中Eddard声音越追越远，把lost castle与失去father重叠；稍后她听见谋杀Eddard的对话便格外刺痛。",
24:"她不靠否认skulls存在消除恐惧，而是改变自己对它们的反应；这与later怪物仍在、fear gone精确对应。",
27:"理性说dead skull不能伤她，身体却被真实fang勾衣；想象恐惧与物理危险在黑暗中并非完全可分。",
29:"失去视觉迫使她实践Eddard刚觉得古怪的多感官训练，证明Syrio blindfold课程不是nonsense。",
30:"fear cuts deeper than swords从Syrio教学变成地下导航原则；心理失控会比无光本身更快使她迷失。",
32:"单torch把普通人影放大为giants，提醒视觉信息会被环境扭曲，正如Arya随后对身份只能靠零碎线索。",
33:"one bastard在当前信息中很可能指Gendry，但说话人未命名；Jon是Arya之后基于家庭语境的误猜。",
35:"fools tried to kill his son强烈对应Bran遇刺；wolf/lion指Stark/Lannister冲突，是文本支持充分的推断。",
36:"两人并非简单希望和平，而是认为war时机不利；delay是战略节奏诉求，目的尚未完全公开。",
39:"scar、stout build、无声步伐、伪装与情报语言强烈指向Varys；段落仍通过Arya的familiar feeling保持未明说。",
40:"forked yellow beard、肥胖、满手宝石戒指与Free Cities口音对应此前Daenerys章节的Illyrio外貌；这是跨章节强推断。",
41:"torch使持灯者看不见暗处观察者，知识与盲区同源：他们掌握大局，却漏掉脚边child witness。",
42:"pregnant princess与khal、son组合指向Daenerys与Drogo；对话者期待khal未来行动，但未解释最终目的。",
43:"活动石门说明Red Keep秘密路线是实际工程结构，也解释Varys上一章如何绕过Eddard guards。",
44:"长名单把多个已知支线放进同一危机模型；speaker的焦虑来自变量太多，而非完全失去信息。",
46:"birds结合Varys既有little birds称呼，很可能指儿童情报员；数目、识字与gold显示网络需持续招募和供养。",
48:"对年轻、识字、存活率的讨论把抽象spy network重新变成脆弱儿童；具体招募方式仍未明说。",
50:"keep their tongues既可指保守秘密，也可能含更阴暗双关；残缺语句不足以确定，不能过度解释。",
54:"她从secret tunnel以sewer出城，城堡权力中心与废物流道物理相连；无人注意的身体也成为隐形优势。",
55:"castle内贵族身份不能穿过关闭gate自动生效；guards只按外表把她归为beggar。",
63:"Arya先用Syrio训练躲拳，再用Stark身份与Eddard权力反击，身体能力和制度身份共同开门。",
64:"biggest book正是Eddard调查的lineages book；Arya在同一房间复述bastard/book，却没有意识到对应关系。",
66:"她保留了if one Hand could die、book、bastard等关键内容，却把bastard指向Jon；儿童转述可同时准确和误解。",
68:"信息mixed up不是完全失真：外貌、象征、pregnancy、tempo争执都相当准确，问题在缺少政治词汇框架。",
69:"Eddard用stereotyped wizard测试故事，却因此偏离Arya真正听到的隐喻称呼。",
72:"她为了避免Tommen事件惩罚而删减路线说明，使本已难信的报告更像adventure；选择性诚实削弱可信度。",
75:"mummer’s farce和juggling在密谈中是比喻，Eddard却按字面归为演员；成人也会因先入框架误读语言。",
77:"关键报告尚未澄清就被行为管教替代；父亲合理担心安全，却错过了继续核对description的机会。",
78:"Yoren敲门不仅打断Syrio话题，也带来恰好能证实Catelyn/Tyrion危机的外部消息。",
82:"Arya对Jon的信任基于被理解的经验；连续发问既显失礼，也表现她在恐惧后寻找可靠家人。",
86:"blood与gold气味相同说明消息传播由暴力和获利共同驱动；Yoren抢先并不能阻止其他方向的riders。",
89:"Eddard承诺tomorrow，却即将被紧急政治事件占据；延后的儿童证词可能失去最佳核验时机。",
93:"Arya离场后仍继续做security arithmetic，说明地下对话没有因成人不信而从她心中消失。",
98:"one against ten是安慰性夸张，不是有效兵力评估；Arya立刻用wizard问题指出数量之外还有未知威胁。",
100:"Desmond把未知威胁重新化为可砍头身体，以士兵逻辑提供安慰；这并未回答秘密通道与内部接近问题。",
}

STAGES = [
(1,21,"抓猫训练把Syrio口诀转为身体技能；Arya躲过royal children与guards追捕，却在Red Keep陌生区域彻底迷路。"),
(22,43,"噩梦般黑暗中她克服dragon skulls与无光走廊，在secret well旁听见两名伪装男子讨论bastard、truth和过早战争。"),
(44,63,"密谈列出Stannis、Lysa、Tyrell、Littlefinger、Eddard与Tyrion连锁危机；Arya沿sewer出城，再凭身份与训练返回。"),
(64,78,"她向正在读lineages book的Eddard复述危险，却因儿童误解、删减细节和成人字面框架被当作mummer故事。"),
(79,100,"Yoren带来Catelyn拘捕Tyrion的紧急消息；Arya被送走后仍计算guards与Lannister人数，担忧Eddard安全。"),
]

BACKGROUNDS = {
4:"**black tom：** Red Keep著名老猫，曾从Tywin餐桌夺食；“real king”是gold cloak的幽默称呼，不是世界观身份。",
9:"**royal children：** Myrcella与Tommen是Cersei、Robert的年幼children，由septa和Lannister guards保护。",
26:"**dragon skulls：** Targaryen dragons遗骨存于Red Keep地下；最大头骨的具体名字本章未给。",
33:"**bastard线索：** Eddard已找到Robert baseborn son Gendry，并在查其他children；故one bastard很可能指Gendry。",
35:"**wolf/lion：** wolf通常指House Stark，lion指House Lannister；Bran遇刺与Tyrion被捕正推动两家冲突。",
39:"**身份推断：** torchbearer的体型、scarred disguise、无声动作、secret passages与birds语汇强烈对应Varys，但对话未直呼其名。",
40:"**身份推断：** forked yellow beard的肥胖男子与Daenerys此前见过的Illyrio外貌高度一致；仍属跨章识别。",
42:"**princess与khal：** 当前唯一已知pregnant princess/khal组合是Daenerys与Drogo；他们在Essos，尚未公开出兵。",
44:"**当前变量：** Stannis在Dragonstone、Lysa在Eyrie；Renly曾问Margaery是否像Lyanna；Catelyn已拘捕Tyrion。",
46:"**little birds：** Varys对情报来源的称呼；本段暗示其中有年轻、识字的儿童，但细节不完整。",
64:"**lineages book：** Malleon的great houses世系史，Jon读过、Eddard正在查；对话者也说Eddard has the book。",
78:"**black brother：** Yoren是Night’s Watch recruiter，刚从crossroads inn急赶King’s Landing。",
86:"**消息内容：** Yoren显然要私报Catelyn拘捕Tyrion；他确认传讯者也分别奔向Casterly Rock等地。",
}

EXTRA_VOCAB = [
("tom","/tɑːm/","n.","公猫","one-eared cat"),("pad","/pæd/","v.","轻声走动","bare feet"),("mouser","/ˈmaʊzər/","n.","善捕鼠的猫","castle cats"),("midden","/ˈmɪdən/","n.","垃圾堆；粪堆","prowling cats"),("bailey","/ˈbeɪli/","n.","城堡内院","route"),("serpentine","/ˈsɜːrpəntaɪn/","adj.","蜿蜒的","steps"),("mortified","/ˈmɔːrtɪfaɪd/","adj.","羞愧难堪的","Septa reaction"),("mute","/mjuːt/","adj./n.","不能说话的；哑者","septa’s question"),("careen","/kəˈriːn/","v.","失控冲去","guard"),("wriggle","/ˈrɪɡəl/","v.","扭动钻过","arrow slit"),("rushes","/ˈrʌʃɪz/","n.","铺地灯芯草","floor covering"),("hunker down","/ˈhʌŋkər daʊn/","phr.v.","蹲伏下来","hide in cellar"),("cavernous","/ˈkævərnəs/","adj.","洞穴般巨大空旷的","skull room"),("loom","/luːm/","v.","阴森逼近；赫然出现","skull"),("pit","/pɪt/","n.","深坑；深渊","dark hall"),("draft","/dræft/","n.","穿堂冷风","find an opening"),("shaft","/ʃæft/","n.","竖井","secret stairs"),("bowels","/ˈbaʊəlz/","n.","内部深处","earth"),("writhe","/raɪð/","v.","扭动翻滚","shadows / smoke"),("fortnight","/ˈfɔːrtnaɪt/","n.","两周","search timeline"),("mummer’s farce","/ˈmʌmərz fɑːrs/","n.","演员演的闹剧；拙劣表演","failed assassination"),("bestir oneself","/bɪˈstɜːr/","phr.v.","开始采取行动","khal"),("tractable","/ˈtræktəbəl/","adj.","温顺易控制的","political bride"),("meddling","/ˈmedəlɪŋ/","n./adj.","插手干预","Littlefinger"),("juggler","/ˈdʒʌɡlər/","n.","杂耍者；同时操控多事者","political metaphor"),("portcullis","/pɔːrtˈkʌlɪs/","n.","铁闸门","castle gate"),("postern","/ˈpoʊstərn/","n.","侧门；后门","night entrance"),("clout","/klaʊt/","n.","重击；耳光","guard threat"),("crabbed","/ˈkræbɪd/","adj.","潦草难辨的","script"),("thread of air","/θred əv er/","metaphor","凭空编出的故事","Eddard’s warning"),("stooped","/stuːpt/","adj.","弯腰驼背的","Yoren"),("unkempt","/ˌʌnˈkempt/","adj.","不修边幅的","beard"),("single-minded","/ˌsɪŋɡəl ˈmaɪndɪd/","adj.","专注而不易转移的","Desmond"),("southron","/ˈsʌðrən/","adj.","南方的（古风/方言）","swords"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def main():
    blocks = extract_range(313, 323, "ARYA", "CH32")
    write_chapter(
        out=OUT, chapter=32, pov="ARYA", page_start=313, page_end=323,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Syrio训练的实际应用、Red Keep隐藏空间、秘密对话证据等级与Arya转述的信息损失。",
        vocab=VOCAB,
        guide="Arya追逐Red Keep最难抓的black tom，Syrio教的呼吸、平衡、速度与多感官训练让她躲开guards，却也把她带入收藏dragon skulls的地下空间。她在secret well旁听见两名男子讨论Gendry、Bran遇刺、Stark–Lannister冲突、Daenerys怀孕、Varys的birds和Eddard可能成为第二个死去的Hand。外貌与语汇强烈暗示两人为伪装的Varys与Illyrio，但文本没有直呼姓名。Arya回报时保留了许多关键句，却误把bastard猜成Jon，又因省略撞倒Tommen而使路线更像幻想；Eddard把juggling和mummery按字面理解为演员。Yoren随即带来Catelyn拘捕Tyrion的真实紧急消息，间接印证密谈所忧虑的战争升级。",
        people=[
            ("Arya Stark","本章视角；完成追猫训练、发现secret passage并努力报告密谈"),
            ("Syrio Forel","虽未亲自出现，其口诀与训练持续指导Arya身体、感官和恐惧管理"),
            ("Eddard Stark","正读lineages book，却误把Arya听到的政治比喻理解为mummer表演"),
            ("Yoren","从crossroads inn抢先来报Tyrion被捕及消息已向Casterly Rock传播"),
            ("scarred torchbearer","外貌、步态、secret routes与birds强烈暗示Varys；文本未明说"),
            ("forked-beard man","Free Cities口音、体型、黄胡须与宝石戒指强烈暗示Illyrio；文本未明说"),
            ("Myrcella / Tommen","把训练装束下的Arya误认成ragged boy"),
            ("Desmond","护送Arya并以士兵式确定性安慰她关于Eddard安全的担忧"),
        ],
        terms=[
            ("dragon skulls","Targaryen dragons遗骨，存放在Red Keep地下黑暗房间"),
            ("secret well","以螺旋石阶连通地下、可由滑动石板封闭的隐藏通道"),
            ("mummer’s farce","密谈者对Bran刺杀失败的比喻；Eddard误按字面理解为演员闹剧"),
            ("little birds","Varys情报人员的称呼，本章暗示需年轻且识字"),
            ("lineages book","Jon与Eddard调查great-house血统所读巨册，密谈者知道它在Eddard手中"),
        ],
        synthesis="Chapter 32讨论“看到”和“理解”不是同一件事。Arya在全黑走廊看不见，却因Syrio训练反而能前进；两名密谈者有torch和庞大情报网，却没看见脚边的孩子。Arya听得相当准确，但缺少bastard、khal、mummer等政治语汇的对应框架；Eddard拥有成人知识，却被monsters、wizard和省略情节诱导进错误解释。小说没有把孩子写成纯粹可靠的先知，也没有把成人写成纯粹愚蠢：传递链中的每个人都选择、压缩并套用既有模型。真正危险的是报告被打断后没有继续逐项核验。",
        contrasts=[
            "**贵族女孩／ragged boy：** 同一身体因衣着、污迹和姿态被完全不同地分类。",
            "**有光的密谈者／无光的偷听者：** 掌握torch的人反而被自身光线弄盲。",
            "**monster仍在／fear消失：** 勇气改变的是Arya行动能力，不是环境事实。",
            "**准确词句／错误解释：** Arya记住book与bastard，却猜成Jon；Eddard听见mummery，却猜成actors。",
            "**secret plot／公开消息：** 地下人担心Tyrion被捕，Yoren随后从道路网络带来同一事件。",
            "**五十guards／隐藏通道：** 数量能防公开袭击，未必能防内部秘密接近。",
        ],
        questions=[
            "Eddard之后会不会重新询问Arya并核对forked beard、steel cap与secret wall？",
            "密谈者为何既想延迟war，又认为Eddard接近truth必须处理？",
            "年轻识字的birds究竟如何被招募和使用？",
            "Yoren带来的Tyrion被捕消息会如何改变Eddard当前调查和安全部署？",
        ],
        extraction_notes="PDF pp.313–323共100段；正确合并4处跨页续段：pp.315–316、316–317、317–318与321–322。逐页复核无额外误切。PDF p.321原页面在Syrio Forel句末印作hirn，疑为源文件排印/OCR字形错误；为不改写原文予以保留。",
    )
    print(f"Wrote Chapter 32 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
