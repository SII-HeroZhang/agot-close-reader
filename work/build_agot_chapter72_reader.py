#!/usr/bin/env python3
"""Build Chapter 72 (DAENERYS) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter71_reader import VOCAB as BASE_VOCAB

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"outputs"/"AGOT_逐章精读"

SUMMARIES=[
"在red、dead、parched土地上，Daenerys的人用稀缺木材搭pyre，并以斧击杀stallion作为葬礼准备。",
"被绑的Mirri警告只有horse blood不足以施法，嘲讽Daenerys是无知child，并提出释放自己即可帮助。",
"Daenerys厌烦Mirri说话，命Jhogo以whip迫使她沉默。",
"众人把Drogo的tent、衣物、鞍具、成年whip、arakh与dragonbone bow置上pyre；Daenerys保留属于自己的bride gifts。",
"正午将近时Jorah把Daenerys拉到一旁，仍称她Princess。",
"Daenerys挑战这个称呼，追问Viserys是否曾是Jorah的king。",
"Jorah确认。",
"Daenerys宣布Viserys死后自己是House Targaryen最后血脉和继承人。",
"Jorah改口称Queen并跪下，献上sword与heart，恳求她放下Drogo、不要登pyre，愿带她去east自由生活；页面将Daenerys误排为Dacnerys。",
"Daenerys温柔而悲伤地说自己必须完成计划，Jorah并不理解。",
"Jorah以自己曾失去wife却继续活着为例，拒绝旁观Daenerys自焚。",
"Daenerys确认他只怕这个，并说自己并非那样的child。",
"Jorah追问她是否发誓不与Drogo同死。",
"Daenerys用Common Tongue发誓，并在内心把Seven Kingdoms视为自己的right。",
"pyre第三层按north-south、ice-fire方向铺设；不到百名Dothraki围拢，Daenerys想到Aegon起步人数却不再在意。",
"Daenerys释放slaves并邀请自愿留下者组成新khalasar，又把whip给Jhogo、命他成为ko并宣bloodrider oath。",
"Jhogo困惑地说传统不允许woman拥有bloodrider，接受会使自己蒙羞；源页引号方向异常。",
"Daenerys无视拒绝，以If I look back I am lost继续，把dragonbone bow给Aggo并要求同一oath。",
"Aggo低眼接受bow，却说只有man能lead khalasar或name ko。",
"Daenerys转向Rakharo，把gold-chased arakh给他并继续命名ko。",
"Rakharo只承诺护送她到Vaes Dothrak加入dosh khaleen，拒绝承认更广bloodrider义务。",
"Daenerys仿佛没听见拒绝，许诺未来给Jorah一柄dragon-forged Valyrian steel sword并索要oath。",
"Jorah跪下放剑，发誓serve、obey，并在必要时为她死。",
"Daenerys确认无论发生什么。",
"Jorah重复Whatever may come。",
"Daenerys警告会要求履誓，并任命Jorah为首位Queensguard。",
"Dothraki侧目低语，认为Daenerys发疯；她承认可能如此，但很快便会知道。",
"Daenerys以scalding bath清洁身体，热度缓解产后疼痛，也像进入仪式前的净化。",
"[内容省略：涉及未成年角色的露骨身体接触。段落位置保留。] handmaids完成香料与身体准备。",
"[内容省略：涉及未成年角色的性化身体描写。段落位置保留。] Daenerys独自为Drogo清洁并在气味记忆中请求原谅。",
"Daenerys给Drogo编发、挂回bells并穿上最爱的旧vest，自己也选择相似衣装。",
"日落时Jhogo和Aggo把Drogo抬上pyre，头朝Mother of Mountains。",
"Daenerys命人倒oil浸透pyre，再以不容置疑语气叫handmaids拿dragon eggs。",
"Jorah劝她别把eggs陪葬，卖掉即可买船和获得终身财富。",
"Daenerys说eggs不是为了出售才送给自己。",
"她亲自把black、green、cream-gold eggs放在Drogo身体周围，并最后亲吻。",
"Mirri看着她下pyre，沙哑断言她疯了。",
"Daenerys反问madness与wisdom距离多远，命Jorah把Mirri绑上pyre。",
"Jorah震惊并试图反对。",
"Daenerys以他刚立的obey oath强迫执行，并命Rakharo协助。",
"Mirri被拖上pyre固定；Daenerys亲手浇oil，并感谢她教会的lessons。",
"Mirri说Daenerys不会听见自己尖叫。",
"Daenerys说想要的不是screams而是life，引用only death can pay for life；Mirri的contempt转为可能的fear。",
"正文解释Dothraki khal funeral：horse同焚，使死者骑fiery steed进入night lands成为star。",
"Jhogo看见东方第一颗star其实是bloodred comet；Daenerys把它解释为dragon’s tail和最强sign。",
"Daenerys点燃pyre，oil、brush和wood迅速燃烧；Mirri歌声最终变成痛苦wail。",
"[内容省略：涉及未成年角色与死者的露骨性想象。段落位置保留。] Daenerys在火包围Drogo时短暂产生与他同归的冲动。",
"燃烧肉味与巨兽般pyre迫使Dothraki和Jorah后退，Daenerys却以blood of the dragon自我理解站住。",
"她靠近conflagration，认为早先brazier不足以验证truth；把火焰看成婚礼舞者，并说children会成长学习。",
"火焰在她眼中化为lions、serpents、wolves、birds、trees和Drogo的smoky stallion，Jorah呼喊已失去重要性。",
"[内容省略：涉及未成年角色的裸体与性化身体描写。段落位置保留。] Daenerys更靠近火，并看见Drogo幻象挥whip。",
"第一声stone crack后pyre坍塌，pale-gold curved shell碎片滚到脚边，旁观者惊叫。",
"Only death can pay for life作为独立refrain出现。",
"第二声crack伴随恐慌；Daenerys自称Stormborn、daughter/bride/mother of dragons，主动步入firestorm。",
"第三声crack被比作world breaking。",
"[内容省略：涉及未成年角色裸体。段落位置保留。] 火灭后Jorah在ashes中发现Daenerys无伤，周围是焚毁遗骸。",
"[内容省略：涉及未成年角色裸体哺乳场景。段落位置保留。] 三只新生dragons分别依附在Daenerys身上。",
"Jorah无言跪下，Jhogo、Aggo、Rakharo依次伏地宣称Blood of my blood。",
"handmaids及全体Dothraki随后归附；Daenerys从眼神中知道他们如今真正属于她。",
"Daenerys起身，三只dragons展开translucent wings并发声；数百年来dragon music首次使夜晚复苏。",
]

KEY_NOTES={1:"pyre从贫瘠地景中的零碎材料搭起，创造行为不是凭空发生，而以最后资源和一匹horse为代价。",2:"Mirri用child否定Daenerys的knowledge；本章后续反复以child/grow回答她，但不能因此自动正当化Mirri遭受的处置。",4:"Daenerys保留bride gifts，表明葬礼不是把自身也完全交给Drogo，而是在继承其军事符号。",9:"Jorah从Princess改Queen完成语言上的主权转移；Dacnerys为页面原有拼写异常。",11:"Jorah误读计划为suicide并非毫无根据，Daenerys刻意不解释真实意图，因为她自己也只能以行动验证。",14:"用Common Tongue宣誓把对Jorah的私人保证与Seven Kingdoms claim连接。",15:"north to south/from ice to fire把pyre空间化为全书两大地理意象，但当前只作仪式方向理解。",16:"先free再邀请留下，试图把slave ownership改造为consent-based allegiance；众人的沉默说明同意尚未立即形成。",17:"Jhogo的拒绝不是个人怯懦，而是Dothraki gender rule：woman不被承认为khal或bloodrider leader。",22:"对Jorah的未来Valyrian sword承诺仍无法立即兑现，却创造Queensguard制度雏形。",26:"Whatever may come很快被Mirri命令检验，oath的空白范围让Jorah必须执行自己反感之事。",27:"Perhaps she was保留Daenerys自身不确定性；叙事没有在奇迹发生前让她拥有全知把握。",28:"scalding heat与cleanliness既是产后身体照护，也预演她主动接近fire。",29:"敏感接触省略；叙事功能是将沐浴变成完整的身体仪式准备。",30:"敏感内容省略；关键是Daenerys通过Drogo气味和hair完成告别，并承认bloodmagic price过高。",33:"Bring my eggs的voice让handmaids奔跑，显示她在followers尚未宣誓前已开始行使command presence。",34:"Jorah按exchange value看eggs，Daenerys按gift purpose与潜在生命意义看，双方理性框架不同。",36:"三枚eggs围绕Drogo摆放成ritual arrangement；文本不提供可重复的bloodmagic procedure。",38:"madness/wisdom反问回应Mirri开章‘maegi means wise’，夺回谁有资格定义knowledge。",40:"Daenerys用刚索取的absolute oath压制Jorah良知，显示新权力从诞生起就包含coercion。",43:"她把Mirri life当作payment，是Daenerys对only death can pay for life的应用，不等于客观宇宙规则已被完整解释。",45:"comet是可见天象；称dragon’s tail和sign属于Daenerys的interpretation。",46:"Mirri燃烧写得漫长而痛苦，阻止读者把dragon birth只当无代价奇观。",47:"敏感想象省略；功能是Jorah对suicide的担忧一度可能成真，但Daenerys没有停在与Drogo合一。",48:"blood of the dragon从genealogy claim转为耐火行动信念；她此前brazier经历并不足以证明能在pyre无伤。",49:"This is a wedding把Drogo funeral、旧wedding和Daenerys与dragon/fire的新结合叠加。",50:"火焰动物可能来自热、烟与意识状态的视觉解释；Drogo stallion是Daenerys主观vision。",52:"第一crack与curved shell明确把egg孵化从象征推进为物理事件。",53:"独立句像ritual equation，但life/death对应关系仍由Daenerys理解组织。",54:"mother of dragons先作为Daenerys在极端时刻的自称，下一段后的结果才提供外部验证。",56:"敏感裸体省略；核心事实是Daenerys处于火场中心却unhurt，hair与clothes焚毁。",57:"敏感裸体哺乳省略；核心事实是三只活dragons已孵化并依附她。",58:"先前拒绝成为woman bloodriders的三人现在主动宣誓，奇迹改变了文化可接受性和power relation。",59:"‘hers as never Drogo’s’把khalasar基础从继承Drogo改成对Daenerys个人的charismatic allegiance。",60:"最终music不是比喻性希望而已：三只可观察生物共同发声，dragon extinction在当前场景被事实性逆转。"}

STAGES=[(1,15,"在贫瘠土地上搭建Drogo pyre；Daenerys以Viserys继承人身份要求Queen称号，Jorah怕她自焚。"),(16,27,"Daenerys释放slaves并试图任命三名Dothraki ko，遭gender tradition拒绝；Jorah却立誓成为首位Queensguard。"),(28,36,"她沐浴净身、为Drogo完成葬仪，并拒绝出售dragon eggs，将三枚eggs置于pyre。"),(37,45,"Daenerys以绝对oath迫使Jorah把Mirri绑上pyre，把其life视作bloodmagic price，并以red comet为sign。"),(46,55,"pyre燃烧、Mirri死亡、eggs三次裂开；Daenerys把火视作wedding并主动走入firestorm。"),(56,60,"火灭后Daenerys无伤、三只dragons孵化；Jorah、khas与剩余Dothraki全体归附。"),]

BACKGROUNDS={1:"**Dothraki pyre：** khal死后与horse及个人treasures露天火葬，使其在night lands继续骑行。",4:"**bride gifts：** whip、bow、arakh原由Drogo bloodriders赠给Daenerys，因此她主张属于自己而不随葬。",9:"**Targaryen succession claim：** Viserys死后，Daenerys把其dynastic claim和Jorah效忠一并继承。",15:"**Aegon comparison：** Daenerys想到Aegon conquest起步规模，以少数followers并不必然阻止王权自我想象。",16:"**manumission：** Daenerys口头解除collars并允许离开，尝试让留下变成自愿；真实可行性仍受荒地资源和依附关系限制。",17:"**bloodrider rule：** ko通常由male khal命名，分享保护、复仇和生死义务；woman khalasar在Dothraki传统中不被承认。",21:"**dosh khaleen destination：** Drogo widow按传统应赴Vaes Dothrak加入widowed khaleesi council，Rakharo只承诺护送至此。",26:"**Queensguard：** Daenerys仿照Kingsguard命名自己的royal guard；本章首位成员为Jorah。",34:"**egg value：** 作为petrified dragon eggs已极其昂贵，Jorah认为出售即可获得船与财富。",43:"**bloodmagic phrase：** Only death can pay for life来自Mirri前章说明；Daenerys现在反向用于Mirri。",45:"**red comet：** 东方低空可见的红色comet；‘dragon’s tail’是Daenerys赋予的象征名称。",46:"**execution and ritual：** Mirri未同意成为sacrifice，且Jorah最初反对；这是强制处决，不应只以奇迹结果消解伦理。",52:"**first hatching evidence：** curved pale-gold shell碎片与crack提供egg破裂的直接物理迹象。",56:"**fire outcome：** Daenerys衣发焚毁却身体无伤；这是角色们可共同观察的异常事件。",57:"**内容安全：** 原段含未成年角色裸体哺乳描写，不复录；保留三只dragons的颜色、位置关系与孵化事实。",60:"**dragon return：** 最后一段明确三只dragons展开翅膀并发声，结束数百年无活dragon的时代。"}

EXTRA_VOCAB=[("parched","/pɑːrtʃt/","adj.","极度干旱的","land"),("gnarled","/nɑːrld/","adj.","扭曲多节的","cottonwood"),("sheaf","/ʃiːf/","n.","一捆草或谷物","brown grass"),("hewn","/hjuːn/","adj.","砍削成的","logs"),("carcass","/ˈkɑːrkəs/","n.","动物尸体","horse"),("disquiet","/dɪsˈkwaɪət/","n.","不安","Mirri eyes"),("bray","/breɪ/","v./n.","驴叫；刺耳说话","maegi"),("harness","/ˈhɑːrnɪs/","n.","马具","Drogo treasures"),("zenith","/ˈziːnɪθ/","n.","天顶；最高点","sun"),("exile","/ˈeksaɪl/","n.","流亡生活","Jorah offer"),("weave","/wiːv/","v.","编织交错","branches"),("wary","/ˈweri/","adj.","警惕的","freed people"),("chase","/tʃeɪs/","v.","在金属上雕饰","gold hilt"),("flinch","/flɪntʃ/","v.","因疼痛退缩","hot bath"),("enfold","/ɪnˈfoʊld/","v.","包裹环抱","warmth"),("stake down","/steɪk daʊn/","v.","用桩固定","Mirri"),("ululate","/ˈjuːljəleɪt/","v.","发出高亢颤鸣","song"),("writhe","/raɪð/","v.","扭动翻腾","flames"),("tendril","/ˈtendrəl/","n.","卷曲细条","smoke"),("gout","/ɡaʊt/","n.","喷出的一股","fire"),("unfurl","/ʌnˈfɜːrl/","v.","展开","fire banners"),("conflagration","/ˌkɑːnfləˈɡreɪʃən/","n.","大火","pyre"),("brazier","/ˈbreɪʒər/","n.","火盆","heat test"),("rivulet","/ˈrɪvjələt/","n.","细流","sweat"),("limn","/lɪm/","v.","勾勒；以光描边","stallion"),("nimbus","/ˈnɪmbəs/","n.","光环","blue flame"),("smolder","/ˈsmoʊldər/","v.","闷燃","vest"),("cinder","/ˈsɪndər/","n.","余烬；煤渣","firefall"),("crisp","/krɪsp/","v.","烧焦卷曲","hair"),("sinuous","/ˈsɪnjuəs/","adj.","蜿蜒柔曲的","dragon neck"),("translucent","/trænzˈluːsənt/","adj.","半透明的","wings")]
VOCAB=BASE_VOCAB+EXTRA_VOCAB

def extract_blocks():
 b=extract_range(724,731,"DAENERYS","CH72")
 # Remove non-body HTML navigation text at the first and last PDF pages.
 b=b[1:-1]
 for i,x in enumerate(b,1): x["order"]=i; x["id"]=f"CH72-P{x['page']:03d}-{i:03d}"
 red={29:"[Content omitted: explicit bodily contact involving a minor. Paragraph position preserved.]",30:"[Content omitted: sexualized bodily description involving a minor. Paragraph position preserved.]",47:"[Content omitted: explicit sexualized fantasy involving a minor and a deceased person. Paragraph position preserved.]",51:"[Content omitted: nudity and sexualized bodily description involving a minor. Paragraph position preserved.]",56:"[Content omitted: nudity involving a minor. Paragraph position preserved.]",57:"[Content omitted: nude breastfeeding imagery involving a minor. Paragraph position preserved.]"}
 for n,s in red.items(): b[n-1]["text"]=s
 return b

def main():
 b=extract_blocks(); write_chapter(out=OUT,chapter=72,pov="DAENERYS",page_start=724,page_end=731,blocks=b,summaries=SUMMARIES,key_notes=KEY_NOTES,stages=STAGES,backgrounds=BACKGROUNDS,default_background="本段没有新增必须展开的设定；重点在Daenerys继承王权、挑战Dothraki gender tradition、Drogo funeral、Mirri sacrifice与dragon hatching。",vocab=VOCAB,
 guide="Daenerys在贫瘠红地上为Drogo搭建pyre。她纠正Jorah的Princess称呼，宣称自己是Viserys的heir与Queen；Jorah担心她殉葬，发誓效忠并成为首位Queensguard。Daenerys释放不足百人的slaves，邀请其自愿组成khalasar，并试图把Jhogo、Aggo、Rakharo命名为ko，却因Dothraki不承认woman khal而遭拒。她仍把Drogo、treasures和三枚dragon eggs安置在pyre，并以Jorah刚立的absolute oath迫使他把Mirri绑上火堆，把Mirri的life当作‘only death can pay for life’的代价。red comet升起后Daenerys点火；Mirri在火中死亡，eggs随三声巨响裂开。Daenerys主动走入firestorm。火灭后她衣发尽毁却身体无伤，三只dragons已经孵化。Jorah和原先拒绝的三名warriors立即跪地，余下Dothraki也全部归附；数百年来夜空第一次响起dragon music。",
 people=[("Daenerys Targaryen","本章视角；宣告Queen身份，创建Queensguard并在pyre中孵化三只dragons"),("Ser Jorah Mormont","担忧Daenerys自焚，绝对宣誓后被迫协助处置Mirri，最终跪服奇迹"),("Khal Drogo","被依Dothraki传统火葬，其遗物、horse与eggs构成pyre中心"),("Mirri Maz Duur","被Daenerys作为life price强制绑上pyre并烧死"),("Jhogo / Aggo / Rakharo","先因gender tradition拒绝bloodrider oath，dragon孵化后主动宣誓"),("Irri / Jhiqui / Doreah","协助Daenerys净身、葬礼准备，最后随众归附"),("three dragons","cream-gold、green-bronze、black-scarlet三只新生dragon")],
 terms=[("funeral pyre","Drogo、horse、treasures、Mirri与eggs共同置于其上的露天火葬堆"),("ko / bloodrider","传统上由male khal命名、以blood of my blood宣誓的核心warrior"),("Queensguard","Daenerys仿Kingsguard建立的个人royal guard"),("only death can pay for life","Mirri提出、Daenerys反向用于sacrifice的bloodmagic命题"),("mother of dragons","Daenerys步入火中时的自称，随后由三只hatchlings外部验证")],
 synthesis="Chapter 72把Daenerys的权力从继承、命令与象征推向可观察的超自然事实。她先以Viserys之死主张Queen身份，这是dynastic inheritance；再释放slaves、分配bride gifts、任命ko，这是institution building。但三名Dothraki接受礼物却拒绝oath，说明单方面命名不能立刻推翻gender tradition。只有Jorah承认她，而他的Whatever may come马上产生道德代价：Daenerys用absolute obedience迫使他参与Mirri的强制处决。奇迹因此并非纯洁诞生。pyre消耗最后资源、horse、Drogo遗体和Mirri生命，Mirri的痛苦被详细写出，不能因dragons出现而被抹去。Daenerys对bloodmagic的理解也不是完整说明书：她布置方向、eggs与life payment，却承认自己可能mad，直到shell裂开才有外部证据。三声crack逐级重写她的称号。daughter of dragons来自血统，bride of dragons来自她把火称作wedding，mother of dragons则在三只hatchlings出现后成为现实关系。最后的政治转变同样清楚：Jhogo等人先说woman不可以，后主动Blood of my blood；剩余Dothraki不再因Drogo或collars留下，而被Daenerys在火中无伤与dragon birth形成的charisma重新组织。全章的壮丽因此与coercion、death和uncertain knowledge始终并存。",
 contrasts=["**dead parched land／new dragon life：** 极端贫瘠背景中的创造。","**Princess／Queen：** 被动家族女性称谓转为主权宣告。","**free to leave／culturally unable to swear：** 法律式释放不等于传统立即改变。","**Dothraki ko refusal／Jorah oath：** 旧gender秩序与新Queensguard制度。","**eggs as wealth／eggs as purpose：** Jorah的市场价值与Daenerys的象征、生命价值。","**wisdom／madness：** Mirri和Daenerys争夺谁有资格解释bloodmagic。","**funeral／wedding：** 与Drogo告别同时成为Daenerys与fire/dragons的新结合。","**forced obedience／voluntary kneeling：** Jorah执行Mirri命令时受oath强迫，结尾众人因奇迹主动归附。"],
 questions=["三只newborn dragons需要何种食物与照护？","Daenerys的fire immunity是否有边界，还是仅与这次ritual有关？","red comet与dragon hatching之间是因果、预兆还是巧合？","新khalasar会如何处理Dothraki传统与woman leader的冲突？","Daenerys获得dragons后将选择Vaes Dothrak、eastward exile还是Seven Kingdoms？"],
 extraction_notes="PDF pp.724–731自动提取出62块；删除首尾两个HTML导航行后，正文共60段。4处跨页续段：pp.725–726、726–727、727–728、729–730。第29、30、47、51、56、57段涉及未成年Daenerys的露骨接触、性化身体描写、裸体或哺乳场景，使用稳定占位符并保留葬仪、心理、孵化与归附后果。p.725页面本身排作‘Dacnerys’，p.726页面引号排作‘Khaleesi, “’，均原样保留并注明。")
 print(f"Wrote Chapter 72 with {len(b)} paragraphs")
if __name__=="__main__": main()
