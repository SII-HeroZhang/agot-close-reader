#!/usr/bin/env python3
"""Build Chapter 71 (CATELYN) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter70_reader import VOCAB as BASE_VOCAB

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"outputs"/"AGOT_逐章精读"

SUMMARIES=[
"Catelyn想起多年前抱infant Robb渡过Tumblestone北上，如今同一孩子穿plate and mail凯旋归来。",
"Robb与Grey Wind坐船头，Theon同行，Brynden、Greatjon和Karstark乘后船。",
"童年waterwheel声、Tully banners与欢呼本应振奋，Eddard之死却使Catelyn无法真正高兴。",
"船从锈蚀portcullis下进入Water Gate；Catelyn本能评估城防能否承受ram，战争思维已成为日常。",
"Edmure与救他出营的Tytos Blackwood在water stair迎接；二人armor都留下战斗痕迹。",
"仆役用hooks拉船，Grey Wind吓得一人跌入水；Theon把Catelyn抱上干燥台阶。",
"负伤憔悴的Edmure拥抱Catelyn，姐弟重逢没有笑容。",
"Edmure分享她的grief，并发誓让Lannisters付出代价。",
"Catelyn尖锐问vengeance能否带回Ned，压下哀痛要求先见Hoster。",
"Edmure说Hoster在solar等她。",
"steward说明Hoster卧床，并要求立即带Catelyn去见。",
"Edmure陪她穿过曾见Petyr与Brandon决斗的bailey；Catelyn恐惧地问病情。",
"Edmure坦白maesters认为Hoster时日无多且持续剧痛。",
"Catelyn对亲友、maesters和gods同时愤怒，责怪Edmure没有早通知。",
"Edmure说Hoster禁止走漏病危消息，怕Lannisters利用Riverrun领主虚弱。",
"Catelyn补完‘他们可能攻击’，内心又把危险追溯到自己抓Tyrion的决定。",
"姐弟沉默走上spiral stair。",
"三角solar像Riverrun地形本身；Hoster的床被移到能看两河的sunlit balcony。",
"曾高大魁梧的Hoster如今严重消瘦，头发胡须全白。",
"Hoster称她little cat，摸索女儿的手，说一直等她。",
"Edmure亲吻父亲额头，把父女单独留下。",
"Catelyn握着失去力量的手，再次问为何不送rider或raven。",
"Hoster说通信会被截；他用belly里的crabs形容持续疼痛，并说靠dreamwine和milk of the poppy睡眠，只怕死前见不到孩子。",
"Catelyn安慰自己已到，并带来Robb。",
"Hoster模糊记得Robb有自己的眼睛。",
"Catelyn确认Robb仍像外祖父，并告诉他Jaime被俘、Riverrun解围。",
"Hoster昨夜被抬上battlements观看夜袭，觉得Lannister喊声和siege tower燃烧很美，并急问是否Robb所为。",
"Catelyn骄傲确认是Robb与Brynden共同完成，Brynden也回来了。",
"Hoster惊讶Blackfish从Vale归来。",
"Catelyn确认。",
"Hoster满怀希望询问Lysa是否也来了。",
"Catelyn不忍却只能说Lysa没有来。",
"Hoster明显失落，说希望死前见她。",
"Catelyn解释Lysa和Robert留在Eyrie。",
"Hoster记起Jon Arryn已死，追问Lysa为何不同行。",
"Catelyn说Lysa害怕且只在Eyrie感觉安全，转而问是否见Robb与Brynden。",
"Hoster愿意见Cat的child，记忆仍停留在Robb出生时。",
"Catelyn再问是否见brother。",
"Hoster望向河流，首先问Blackfish是否终于结婚。",
"Catelyn伤感地说Brynden至今未婚，也不会结婚。",
"Hoster断续坚持自己身为lord有权命他娶Bethany Redwyne。",
"Catelyn提醒Bethany多年前已嫁Lord Rowan并有三个孩子。",
"Hoster仍把Brynden拒婚理解为侮辱女孩、Redwynes和自己，又列Bracken与Frey人选，反复问他是否娶过任何人。",
"Catelyn强调Brynden虽未婚，却远途作战救下他们并回来见兄长。",
"Hoster承认Brynden一直是warrior，要求以后来见，自己太累且‘病得不能争吵’。",
"Catelyn亲吻、抚平父亲头发后离开；Hoster在俯瞰河流的shade中睡着。",
"她回到water stair，Brynden立即询问Hoster状况。",
"Catelyn直说父亲正走向死亡。",
"Brynden痛苦明显，问兄长是否愿意见自己。",
"Catelyn说Hoster自称太病弱不能争吵。",
"Brynden笑称自己不信，预测Hoster到funeral pyre前仍会责备Redwyne婚事。",
"Catelyn也笑并问Robb在哪里。",
"Brynden说Robb与Theon去了hall。",
"Theon正向garrison夸张讲述Whispering Wood杀戮和Grey Wind造成的恐慌。",
"Catelyn打断，询问儿子位置。",
"Theon说Robb去了godswood。",
"Catelyn觉得这正是Ned会做的事，提醒自己Robb也属于父亲。",
"Robb在heart tree前与守old gods的Northern lords祈祷；Catelyn已说不清自己还信何种gods。",
"她等待祈祷结束，童年骑马、Edmure摔伤及与Lysa、Petyr玩耍的记忆涌回。",
"[内容省略：涉及未成年角色的性化回忆。段落位置保留。] 这一记忆表现Riverrun童年与当下丧亲战争的距离。",
"[内容省略：涉及未成年角色的性化推测。段落位置保留。] Catelyn看见Robb已接近成人，却仍为他失去普通青春而落泪。",
"Robb一见母亲便要求召开council，说明有事必须决定。",
"Catelyn先要求他去见病危的grandfather。",
"Robb表示同情，却说south传来Renly称王的紧急消息，必须先开会。",
"Catelyn震惊，因为她本以为Stannis会提出claim。",
"Galbart说众人原本也如此判断。",
"war council在Great Hall举行；Hoster缺席，riverlords因Riverrun胜利陆续回归，其中多家已承受领主死亡或领地毁坏。",
"Northern lords人数较少；Karstark因两个儿子战死、长子失联而形如梦游。",
"争论持续到深夜，各lord按权利发言、叫骂、交易、离席又返回，Catelyn始终倾听。",
"情报显示Bolton重组残军、Frey守Twins、Tywin去Harrenhal，而realm已有两位kings却无共同立场。",
"诸侯分别主张攻Harrenhal、袭Casterly Rock、守Riverrun断补给或投Renly；Blackwood与Bracken依旧相互反对。",
"Robb首次开口，否认Renly已经是合法king，展现与Eddard相似的倾听习惯。",
"Galbart提醒Joffrey处决了Eddard，不能继续效忠。",
"Robb区分Joffrey的evil与succession law：若他是Robert trueborn eldest则合法，死后也应由Tommen继承。",
"Marq Piper说Tommen同样是Lannister。",
"Robb仍追问为何应跳过Robert的兄长Stannis让弟弟Renly继承，并用自己与Bran次序类比。",
"Maege同意Stannis的claim更强。",
"Marq以Renly已经crowned且可能联合五六great houses论证实力，承诺击败所有Lannisters，反问Stannis除了right还有什么。",
"Robb固执回答：The right；Catelyn听见Eddard般的语气。",
"Edmure问是否因此宣布支持Stannis。",
"Robb承认不知道；gods未回答，而若Joffrey合法，他们反抗就会成为traitors。",
"Stevron建议等待两王相争后再选胜者，并提议拿Jaime与Tywin议和赎俘。",
"诸侯以craven、示弱和不能交还Kingslayer等呼喊淹没提议。",
"Catelyn提出为何不能peace。",
"Robb拔剑置于桌上，说Lannisters杀父，这把剑是自己唯一提供的和平。",
"众人欢呼后Catelyn以妻子和母亲身份反问谁更爱Ned；她说再多victories也不能复活死者，只会增加死亡。",
"Greatjon以她是woman为由否定其判断。",
"Karstark称women是gentle sex，而men需要vengeance。",
"Catelyn反击若交出Cersei便能见识她是否gentle；她承认不擅tactics，却理解战争目标的futility。",
"她说最初目标之一已完成、救Ned已不可能；希望用四名Lannisters换回女儿，让Robb回Winterfell生活、成婚、生子，自己回家哀悼。",
"Catelyn说完后hall完全安静，说明论证短暂触及众人。",
"Brynden说peace很甜，却必须有可持续条款，否则plowshare很快又得锻回sword。",
"Karstark问若只带儿子尸骨回Karhold，他们究竟为何而死。",
"Bracken说Gregor毁田杀民、Stone Hedge成废墟，不能让一切恢复原状再向责任方屈膝。",
"Blackwood罕见同意Bracken，并担心与Joffrey议和会在Renly胜出后成为traitors。",
"Marq宣布无论别人如何决定，自己永不称Lannister为king。",
"年幼Darry也激动响应。",
"争吵重新爆发，Catelyn绝望地看见peace时机消失；她把Robb真正的bride认作桌上的sword。",
"她正思念女儿，Greatjon突然起身。",
"Greatjon拒绝Renly、Stannis和Lannisters，主张North恢复dragon conquest前的自主，并称Robb为King in the North。",
"Greatjon跪下，把greatsword放在Robb脚边。",
"Karstark接受这种peace，拒绝Red Keep与Iron Throne，也跪下称王。",
"Maege称King of Winter；连从未受Winterfell统治的riverlords也起身宣誓，复活三百多年未闻的旧称号。",
"众人第一次齐喊King in the North。",
"呼喊继续扩大。",
"最终以全大写的集体宣告达到政治与情绪高潮。",
]

KEY_NOTES={1:"infant swaddling与plate/mail把Robb成长压缩成一次渡河；homecoming也是childhood终结。",3:"公共victory景观无法穿透私人grief，Catelyn的双重身份从开章即冲突。",4:"看到rust便想ram说明战争已重塑她的attention，不再能单纯以归乡者观看城堡。",9:"‘bring Ned back’在本章反复成为反复仇论证核心：情绪合理不等于手段能实现目标。",14:"rage同时指向死者、亲属和gods，是失去控制后的广泛归责，不是逐项理性判断。",16:"Catelyn把Lannister attack可能性归咎自己抓Tyrion，显示guilt；战争因果实际还包含多方选择。",20:"little cat使成年政治行动者暂时回到父亲眼中的child，强化代际循环。",23:"crabs是Hoster对腹痛的体验性比喻，文本不提供可确定的现代诊断。",27:"sweet cries显示Hoster把解除围城与敌军痛苦绑定；病危并未消除封建战争情绪。",31:"对Lysa的hope是Hoster此刻最强情感之一，她缺席使家庭分裂比军事团聚更突出。",39:"死亡临近时Hoster仍问marriage，说明lordship与家族婚配权深植其身份。",43:"记忆错位把早已成婚的Bethany停留在waiting，dreamwine、疼痛和衰弱共同影响意识。",51:"too sick to fight是兄弟之间长期婚配争执的委婉密码，Brynden以笑承受预期丧失。",54:"Theon把屠杀讲成英勇娱乐，与Catelyn的丧亲视角形成刺耳反差。",58:"守old gods者围绕Robb祈祷，悄然勾勒即将形成的North政治共同体。",60:"敏感童年回忆省略；功能是让熟悉godswood同时容纳纯真、尴尬与后来Petyr关系的复杂根源。",61:"敏感推测省略；Catelyn在Robb的warrior adulthood与尚未经历的普通青春之间落泪。",64:"Robb把council置于探病前，显示lord duty已开始压过family time，呼应Hoster一生。",67:"riverlords回归并非完整恢复：dead fathers、ruined seats和child heirs把战争损失带进议事厅。",69:"长串动词表现feudal council不是现代投票，而是身份、声量、交易与武力威望共同作用。",72:"Robb先听后说复制Eddard治理风格，形式上的克制提高发言重量。",74:"本段‘trueborn’是Robb当前认知；读者已知Eddard调查所得，因此其法律推理建立在信息缺口上。",78:"Marq对比的是power coalition与legal right；两种king标准从此公开冲突。",79:"The right仅两词，既显原则也暴露Robb尚无可实行方案。",82:"Stevron的wait-and-ransom有现实理性，也服务Frey避免承担风险的利益。",85:"sword on table把peace词义改写成submission through violence，随后Catelyn争取把它恢复为停止死亡。",86:"Catelyn不是否定Ned价值，而以自己更亲密的grief取得反对报复升级的发言资格。",89:"gentle sex被她用Cersei反例反击；核心仍是futility而非证明女性更暴力。",90:"连续I want把外交目标还原为具体living people和未被战争吞掉的future。",92:"plowshare意象说明peace必须解决安全困境；单方解除武装会使下一轮战争更危险。",98:"true bride=sword把Walder Frey婚约与war commitment相对照，预示政治成人身份吞噬私人生活。",100:"Greatjon不在两位Baratheon中选择，而改变问题：North为何仍需southron king。",103:"riverlords也宣誓最关键，因为他们此前不受Winterfell统治；这一刻是新联盟创造，不只是旧North传统恢复。",106:"三次重复逐渐放大为集体政治现实；情绪一致暂时覆盖前一刻的路线分裂。"}

STAGES=[(1,17,"Catelyn与披甲Robb渡河归Riverrun；胜利欢呼被Eddard之死、Hoster病危和她对战争起因的guilt压住。"),(18,52,"Catelyn探望临终Hoster；父亲在孩子团聚、Lysa缺席与Brynden拒婚旧怨之间断续回忆。"),(53,69,"Robb祈祷后召集war council；Riverrun童年记忆与诸侯战争损失一起进入Great Hall。"),(70,83,"诸侯争论攻守、Renly/Stannis succession和议和；Robb坚持right却无法确定合法道路。"),(84,98,"Catelyn以living family与战争原始目标争取peace，短暂说服众人，却被复仇、安全与合法性疑虑打断。"),(99,106,"Greatjon跳出南方王位选择，拥立Robb为King in the North，North与riverlords共同宣誓。")]

BACKGROUNDS={1:"**Tumblestone crossing：** Catelyn曾从Riverrun带infant Robb去Winterfell；同一路线反向返回构成成长环。",4:"**Water Gate：** Riverrun可由河道直接进入城内，portcullis锈蚀也说明长期防御维护问题。",12:"**Petyr–Brandon duel：** Petyr少年时为Catelyn挑战其婚约对象Brandon，在此bailey附近败北。",23:"**Hoster illness：** 严重消瘦、持续腹痛并用opiates缓解；当前文本不提供明确疾病名。",27:"**Riverrun relief：** Robb/Blackfish夜袭三营，城内Tytos Blackwood sortie解救Edmure并打破围城。",39:"**Brynden marriage dispute：** Hoster作为house lord曾安排婚配，Brynden长期拒绝，由此得Blackfish之名并离开Riverrun。",58:"**old gods group：** 祈祷者多来自North或Blackwood传统；Catelyn出身Tully，通常敬奉Faith of the Seven。",60:"**内容安全：** 原段涉及未成年人之间的性化童年回忆，不复录；保留其作为Riverrun memory和Petyr/Lysa关系背景的作用。",61:"**内容安全：** 原段涉及对未成年Robb亲密经历的性化推测，不复录；保留Catelyn对其被战争迫使早熟的哀伤。",67:"**riverlords return：** 解围后此前逃散或领地被毁的Trident lords重新集结，但伤亡与旧家仇仍在。",70:"**current map：** Bolton在causeway、Frey守Twins、Tywin向Harrenhal；Robb控制Riverrun但政治目标未定。",74:"**succession rule：** 按Robb掌握的信息，Robert的trueborn sons优先于brothers，brothers又按长幼排序。",78:"**great houses arithmetic：** Marq把Baratheon/Tyrell/Stark/Tully及可能的Arryn/Dorne视为联盟资源，属于政治预测。",82:"**ransom leverage：** Jaime与其他Lannister prisoners可交换Sansa、Arya或换取停战，但执行取决于双方条件。",92:"**plowshare：** 把武器锻成农具象征和平；Brynden强调若敌意结构未解，解除武装只是短暂。",100:"**pre-Conquest kingship：** Aegon征服前三百多年，North由Kings of Winter统治；Greatjon主张dragon dynasty消失后恢复独立。",103:"**new realm：** riverlords加入意味着拥立不只是North内部复古，而是跨Trident的新政治共同体。"}

EXTRA_VOCAB=[("swaddling clothes","/ˈswɑːdlɪŋ kloʊðz/","n.","婴儿襁褓","Robb contrast"),("stern","/stɜːrn/","n.","船尾","boat"),("rampart","/ˈræmpɑːrt/","n.","城墙顶部防御工事","banners"),("portcullis","/pɔːrtˈkʌlɪs/","n.","可升降铁闸门","Water Gate"),("winch","/wɪntʃ/","v.","用绞盘拉起","gate"),("barbed","/bɑːrbd/","adj.","有倒钩的","spikes"),("inlaid","/ˌɪnˈleɪd/","adj.","镶嵌装饰的","armor"),("jet","/dʒet/","n.","黑玉","inlay"),("lurch","/lɜːrtʃ/","v.","突然踉跄","guard"),("haggard","/ˈhæɡərd/","adj.","憔悴的","Edmure"),("grievous","/ˈɡriːvəs/","adj.","极严重痛苦的","pain"),("frail","/freɪl/","adj.","虚弱的","Hoster"),("portly","/ˈpɔːrtli/","adj.","肥胖壮实的","older Hoster"),("wispy","/ˈwɪspi/","adj.","细弱飘忽的","voice"),("tremulous","/ˈtremjələs/","adj.","颤抖的","smile"),("spasm","/ˈspæzəm/","n.","一阵痉挛","pain"),("regale","/rɪˈɡeɪl/","v.","以故事款待娱乐","garrison"),("canopy","/ˈkænəpi/","n.","树冠；华盖","leaves"),("bower","/ˈbaʊər/","n.","树荫小亭；幽静处","godswood"),("trestle table","/ˈtresəl ˈteɪbəl/","n.","支架长桌","council"),("fugitive","/ˈfjuːdʒətɪv/","adj.","逃亡中的","lords"),("glower","/ˈɡlaʊər/","v.","怒目而视","Bracken"),("bluster","/ˈblʌstər/","v.","咆哮虚张声势","council"),("gaunt","/ɡɔːnt/","adj.","憔悴消瘦的","Karstark"),("cajole","/kəˈdʒoʊl/","v.","哄劝","debate"),("athwart","/əˈθwɔːrt/","prep.","横跨；阻断","supply lines"),("levy","/ˈlevi/","n.","征召兵","fresh levies"),("laggardly","/ˈlæɡərdli/","adv.","迟缓地","Dorne prediction"),("bestir oneself","/bɪˈstɜːr/","v.","行动起来","Arryns"),("plowshare","/ˈplaʊʃer/","n.","犁铧","peace image"),("futility","/fjuːˈtɪləti/","n.","徒劳无效","war aim"),("rafter","/ˈræftər/","n.","屋顶椽梁","shout"),("bellyful","/ˈbelifʊl/","n.","受够；满腹厌烦","Lannisters"),("scabbard","/ˈskæbərd/","n.","剑鞘","kneeling")]
VOCAB=BASE_VOCAB+EXTRA_VOCAB

def extract_blocks():
 b=extract_range(713,723,"CATELYN","CH71")
 b[59]["text"]="[Content omitted: sexualized recollection involving minors. Paragraph position preserved.]"
 b[60]["text"]="[Content omitted: sexualized speculation involving a minor. Paragraph position preserved.]"
 return b

def main():
 b=extract_blocks(); write_chapter(out=OUT,chapter=71,pov="CATELYN",page_start=713,page_end=723,blocks=b,summaries=SUMMARIES,key_notes=KEY_NOTES,stages=STAGES,backgrounds=BACKGROUNDS,default_background="本段没有新增必须展开的设定；重点在Riverrun family history、复仇与peace目标、succession legitimacy及Robb的新政治身份。",vocab=VOCAB,
 guide="Catelyn与披甲的Robb沿Tumblestone回到Riverrun，童年景物和胜利欢呼却无法减轻Eddard之死。她得知Hoster已病危；父亲在剧痛与药物中盼到女儿和外孙，因Lysa缺席失望，又在临终前仍执着Brynden多年前拒婚的旧争。随后Robb在godswood祈祷，并因Renly称王召集war council。诸侯在攻Tywin、袭Casterly Rock、守补给线、支持Renly或等待之间争论。Robb坚持legal right，却因Joffrey是否lawful而陷入traitor悖论。Catelyn提出peace：Ned无法复活，战争原始目标已变化，应以Jaime等俘虏换回女儿，让living children回家。她短暂使全场安静，但Karstark的丧子、Bracken的毁地和Brynden的安全疑问使议和无法成立。Greatjon最终拒绝在Renly与Stannis间选择，主张恢复North独立，拥立Robb为King in the North；连riverlords也共同宣誓。",
 people=[("Catelyn Stark","本章视角；在父亲病危、丈夫死亡和儿子称王之间争取peace"),("Robb Stark","解围Riverrun后面对succession难题，最终被North与riverlords拥立"),("Hoster Tully","病危的Riverrun lord，在家庭团聚与Brynden旧怨间断续回忆"),("Edmure Tully","Catelyn弟弟；获救后暂代父亲主持Riverrun"),("Brynden Tully","帮助解围，与Hoster仍有拒婚旧争，并提出peace必须可持续"),("Greatjon Umber","跳出Baratheon succession争论，率先拥立Robb"),("Rickard Karstark","两子战死且长子失联，拒绝无成果议和并支持North独立"),("Maege Mormont","支持Stannis claim，后称Robb为King of Winter"),("Marq Piper","以Renly联盟实力支持其claim，代表power-over-right路线"),("Stevron Frey","主张等待并用Jaime议和，遭多数武人反对")],
 terms=[("right versus might","Stannis较强的继承法次序与Renly较强联盟资源之间的冲突"),("peace terms","停止战斗之外还须解决俘虏、安全、赔偿、效忠与复仇"),("King in the North","Aegon conquest前North王号，本章被用来主张脱离southron throne"),("King of Winter","North古老君主称号，强调Stark与冬境传统"),("true bride=sword","Catelyn看见war已成为Robb比Frey婚约更真实的伴侣")],
 synthesis="Chapter 71由两个代际镜像组成。开头Catelyn记得抱infant Robb离开Riverrun，如今他披甲归来；随后她在Hoster床前又变回little cat。Hoster即使临终仍以lord身份执着Brynden婚配，Robb则把council置于探病之前：家族角色不断被政治职责覆盖。Catelyn最清楚这种覆盖会夺走什么。她的peace论证不是简单怯战，而是重新检查战争目标：阻止riverlands受袭已经部分完成，救Ned已永远不可能，继续杀戮不能bring him back；Jaime等俘虏对救回女儿仍有实际价值。反方也非纯粹嗜血。Karstark需要让儿子死亡获得意义，Bracken不能接受毁地后恢复原状，Brynden担忧次日重新开战，Blackwood担忧选错king。因此议和失败源于复仇、security dilemma、赔偿和legitimacy同时未解。Greatjon的突破正是改写问题。他不再问Renly或Stannis谁更合法，而问North为何必须接受任何southron king。Robb的right困境由此变成self-rule主张。宣誓之所以产生新政治事实，不只因为Northern lords恢复旧称，更因为Blackwood、Bracken、Mallister等riverlords也共同kneel。对Catelyn而言，这一高潮却带有悲剧色彩：别人看见king，她看见儿子已与sword成婚。",
 contrasts=["**swaddling clothes／plate and mail：** 母亲记忆中的child与战争制造的young lord。","**victory cheers／heart that will not lift：** 公共凯旋无法抵消私人丧失。","**little cat／Lady Stark：** Catelyn在父亲面前和council中的身份切换。","**Hoster marriage command／Brynden return：** 家族obedience失败与实际忠诚成功。","**the right／five or six houses：** succession legitimacy与coalition power。","**sword peace／living peace：** Robb以暴力复仇定义peace，Catelyn以停止新增死亡定义。","**Frey daughter／true bride sword：** 形式婚约与Robb真实政治承诺。","**two southron kings／King in the North：** 在既定选项内选择转为重新设定政治边界。"],
 questions=["Robb称王后将如何处理Renly、Stannis与Joffrey三方关系？","King in the North是否包括riverlands，边界和治理如何界定？","Catelyn还能否用Jaime等俘虏换回Sansa与Arya？","Hoster能否在死前与Brynden真正和解？","Bolton与Tywin在Harrenhal方向的行动将如何影响新王国？"],
 extraction_notes="PDF pp.713–723校勘后共106段，无误切或重复。6处跨页续段：pp.713–714、714–715、716–717、719–720、720–721、722–723。p.713页面本身排作‘direwolf s head’（缺所有格符号），p.717页面本身排作‘inutterably’，均原样保留并注明。第60–61段涉及未成年角色性化回忆/推测，使用稳定占位符并保留叙事功能。")
 print(f"Wrote Chapter 71 with {len(b)} paragraphs")
if __name__=="__main__": main()
