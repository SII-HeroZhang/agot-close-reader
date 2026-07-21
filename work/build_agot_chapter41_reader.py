#!/usr/bin/env python3
"""Build Chapter 41 (JON) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter40_reader import VOCAB as BASE_VOCAB

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"/"AGOT_逐章精读"

S={
1:"Ser Alliser一边辱骂全体学员，一边宣布为五名新人腾位，Jon等八人将交Lord Commander分配。",
2:"Pyp欢呼后，Alliser警告他们仍是summer boys，winter来时会轻易死亡。",
3:"众人嬉闹庆祝，Jon却注意Sam独站在枯树下，主动递酒。",
4:"Sam礼貌拒绝。",5:"Jon询问他是否还好。",
6:"Sam强装高兴，祝Jon未来像Benjen一样成为First Ranger。",
7:"Jon纠正Benjen仍‘是’First Ranger；伙伴们用酒和雪球打闹，欢乐淹没不安。",
8:"Jon挣脱嬉闹时，Sam已经悄然离开。",
9:"晚餐以Lord Commander桌上的丰盛食物庆祝八人结束训练，older brothers也向Jon致意。",
10:"Pyp边吃边问八人是否会继续在同一部门。",11:"Toad开玩笑说早看腻Pyp的耳朵。",
12:"Pyp反嘲Toad长相能吓退Mance Rayder，因此必适合ranger。",
13:"众人笑时Grenn认真表示希望当ranger。",
14:"Matthar说人人都想；叙述解释rangers是越Wall侦察和战斗的核心。",
15:"Halder选择builders，指出没有维护Wall就没有rangers的立足点。",
16:"builders包括mason、carpenter、miner、woodsman；昔日增高Wall，如今只能巡检裂缝融化并尽力维修。",
17:"Dareon预测Halder当builder、Jon当ranger，却在提Benjen过去时尴尬住口。",
18:"Jon坚持Benjen仍任First Ranger，因众人已放弃希望而失去胃口。",
19:"Toad问他是否不要blueberries。",20:"Jon让给Toad，谎称吃饱后离席。",
21:"Pyp追出来问发生了什么。",22:"Jon承认自己在担心Sam缺席。",
23:"Pyp也觉得Sam错过meal反常，猜测是否生病。",
24:"Jon判断Sam是怕八人宣誓后离开保护圈，独自面对Alliser、Rast及未知新学员。",
25:"Pyp安慰他们已经尽力。",26:"Jon认为尽力却没有解决问题。",
27:"Jon焦躁地带Ghost骑出Castle Black；direwolf让马不安，随后独自去hunt。",
28:"Jon没有目的，只沿溪流和田野骑到kingsroad。",
29:"kingsroad让他渴望Winterfell与整个遥远世界，因为宣誓后这些地方都可能永远看不到。",
30:"Jon意识到自己尚未swear，可自由骑回Winterfell与brothers团聚。",
31:"内心声音提醒那是half brothers、Catelyn不会欢迎他、未知mother也没有给他位置，并用羞耻猜测攻击自己。",
32:"Jon转身看月下横贯地平线的Wall。",33:"他掉转马头，返回自己称作home的Castle Black。",
34:"Ghost带着猎物血迹归来；Jon继续想Sam，到stables时已有计划。",
35:"Maester Aemon因年老blind由Clydas和Chett协助；兄弟们以两人外貌开玩笑。",
36:"Chett开门，Jon要求见Aemon。",37:"Chett说maester已睡，叫他明天再来。",
38:"Jon用boot卡门，坚持morning太迟。",39:"Chett责问他是否知道Aemon多老。",
40:"Jon反击Chett缺礼，向Aemon致歉并强调事情重要。",41:"Chett问若自己拒绝如何。",
42:"Jon说可以整夜卡在门口。",43:"Chett嫌恶但让他进library生火，以免Aemon受寒。",
44:"Aemon穿bed robe却仍戴maester chain，在fire旁坐好，Chett给他盖fur。",
45:"Jon为深夜打扰道歉。",
46:"Aemon说年老少眠，常与五十年前ghosts相伴，反而欢迎midnight mystery，邀请Jon说明来意。",
47:"Jon请求让Sam结束训练并成为Night’s Watch brother。",
48:"Chett说此事与Aemon无关。",
49:"Aemon说明recruit readiness归Alliser判断，温和追问Jon为何来找自己。",
50:"Jon指出Lord Commander听取Aemon意见，且Watch伤病者归他照管。",
51:"Aemon问Sam现在是否受伤或生病。",52:"Jon保证若不帮忙，Sam将会受伤。",
53:"Jon坦白Ghost威胁Rast等全部经过，说明他们离开后Sam会在训练中受重伤或死亡。",
54:"Chett以体形与fear辱骂Sam是pig和craven。",
55:"Aemon暂不反驳，反问Chett会如何处理这种boy。",
56:"Chett主张让Sam无限训练，认为Wall不容weak，Alliser要么把他变成man、要么让他死。",
57:"Jon直斥愚蠢，深呼吸组织思路，开始讲Luwin解释maester chain的往事。",
58:"Aemon触摸自己的metal links，示意继续。",
59:"Jon解释不同金属象征不同学问和不同社会成员；两枚links成不了chain，realm需要各种人。",
60:"Aemon微笑追问结论。",
61:"Jon类推Night’s Watch也需要rangers、stewards、builders；Sam无法被打成warrior，却可像tin一样另有用途。",
62:"身为steward的Chett愤怒，列出狩猎、耕种、养畜、木柴、烹饪、制衣和运输等维持Watch的艰苦工作。",
63:"Aemon先问Sam是否会hunting。",64:"Jon承认Sam讨厌hunting。",
65:"Aemon继续问他能否plow、驾wagon、sail或butcher cow。",66:"Jon回答都不会。",
67:"Chett嘲笑soft lordlings做体力活会起泡流血甚至砍伤自己。",
68:"Jon说自己知道一件Sam比任何人都做得好的事。",69:"Aemon提示他说下去。",
70:"Jon谨慎看Chett后提出Sam可协助Aemon：识字、算术、读过大量书、善待animals和ravens，应被使用而非无意义杀死。",
71:"Aemon沉思后称Luwin教得好，赞Jon心智与剑术同样敏捷。",
72:"Jon急切问这是否表示同意。",
73:"Aemon只承诺考虑，然后结束深夜会谈让Chett送客。",
}
SUMMARIES=[S[i] for i in range(1,74)]

KEY_NOTES={
1:"Alliser把晋升包装成‘为新人腾空间’，故意不给八人正面认可；最后单独说Bastard继续用身份伤口控制Jon的喜悦。",
2:"green and stinking of summer把缺乏冬季经验写成气味；‘毕业’不等于成熟，只是从训练风险进入真正风险。",
3:"庆祝圆圈与bare dead tree下的Sam形成空间对照；Jon的注意力第一次没有被自己的晋升完全占据。",
6:"Sam强笑却用was谈Benjen，既无意触痛Jon，也显示Castle Black多数人已把失踪当死亡。",
7:"Jon只纠正一个时态，语法成为拒绝哀悼的防线；随即喧闹遮住两人的难受。",
8:"极短句把群体快乐的代价显出：Jon获得新阶段时，Sam从画面中消失。",
9:"丰盛menu和fire位置是institutional welcome，和Alliser辱骂式告别形成Night’s Watch内部两套文化。",
12:"crow call the raven black是pot calling the kettle black的世界内变体，以同属黑鸟的反讽互相嘲笑。",
14:"boys想做ranger因其英雄叙事最显眼；叙述随后用builders与stewards纠正‘战斗才有价值’的单一尺度。",
16:"Once / now对比直接显示Watch衰退：过去能扩建巨墙，如今只能勉强巡检维护。",
17:"Dareon话尾中断表明Benjen可能死亡已成社交禁区，伙伴知道Jon仍不能承受。",
18:"未动blueberries把Benjen话题从抽象悲伤变成食欲消失的身体反应。",
20:"I could not eat another bite是保护性谎言；Jon不愿在欢乐桌上要求别人共同承担自己的忧虑。",
24:"他把自身离开Winterfell的记忆投射到Sam：理解不是凭空同情，而是知道被留下和失去保护关系是什么感觉。",
26:"一句话标志Jon从‘我们已经善良过’转向‘结果仍危险，所以必须换办法’。",
27:"无目的骑行把restlessness转成身体运动；Ghost自由hunt与Jon即将失去离开自由形成对照。",
29:"地名清单从near到far扩张世界，句末the world… and he was here突然收缩，呈现vow的机会成本。",
30:"他准确知道法律边界：words尚未说出口，因此选择仍真实存在；诱惑不是违反已立誓言。",
31:"内心声音把事实、预期与侮辱混在一起：Catelyn不欢迎有经验依据，mother必不名誉则只是Jon以沉默填空的自伤推测。",
32:"kingsroad代表多方向世界，Wall只有冷白横线；Jon的选择在两幅空间图像间完成。",
33:"home指代已悄然从Winterfell移向Castle Black；这不是说旧家不重要，而是他决定将归属建在选择之上。",
34:"Ghost’s muzzle文本层丢失apostrophe已依页面修复；血迹说明wolf完成hunt，Jon也从漫游转入目标行动。",
35:"Watch对Clydas、Chett外貌的笑话反映粗粝群体文化；外貌不等于能力，后文Chett也会展示具体steward知识。",
38:"boot卡门是轻度强制，却被Jon限制在坚持见面，不升级为暴力；他用时间成本迫Chett重新评估。",
40:"Jon以courtesy反击无礼，同时补上对真正受打扰者Aemon的道歉，显示他开始区分gatekeeper与decision-maker。",
43:"Chett嘴硬但实际认真照顾Aemon，避免把一个敌意人物写成纯粹无用。",
44:"bed robe与chain collar并置：身体休息，office identity不卸；chain在后文成为Jon论证核心。",
46:"ghosts与上一章Eddard旧梦遥相呼应；老年记忆在Aemon这里不是惊醒创伤，而是长期夜间陪伴。",
49:"Aemon不直接说无权，而让Jon说明为何找错权限链仍合理，像口试般迫他展示制度理解。",
50:"Jon提出两条路径：Aemon对Lord Commander有influence，且可把可预见伤害纳入medical responsibility。",
52:"He will be把future harm当作可预防事实；这也是推论，须由后续证据支撑。",
53:"坦白Ghost威胁Rast会损害Jon自己，却增强陈述可信度；他没有把保护Sam美化成完全守规矩。",
54:"Chett用pig/craven把身体、性格与价值绑在一起，为Aemon的反问提供待检验前提。",
55:"Aemon没有立刻道德训斥，而让Chett把排斥逻辑说完整，方便Jon回应制度后果。",
56:"make a man or kill him把训练失败归为gods will，掩盖Alliser和制度主动制造的可避免危险。",
57:"深呼吸是论证转折：Jon压下即时怒骂，调用Luwin教给他的类比来争取听众。",
59:"chain隐喻同时解释knowledge diversity与social diversity；不同metal不是等级由低到高，而是缺一不能成链。",
61:"不能把tin锤成iron反对单一男子气概模型；承认差异不等于判定tin低劣，而是寻找fit。",
62:"Chett的反驳有效纠正Jon：steward不是给不勇敢者的轻松安置，而是庞大且需要具体技能的劳动系统。",
65:"Aemon用连续实际任务测试漂亮类比，提醒‘多样性有价值’仍需证明person-role fit。",
67:"Chett的嘲笑夹带class resentment：lordling受过读写教育，却可能缺少Watch生存所需的日常劳动技能。",
68:"one thing把论证从抽象同情转成comparative advantage，正是Aemon等待的答案。",
70:"Jon不再只说Sam不能fight，而列出sums、literacy、books、ravens、animal affinity等positive capabilities。",
71:"deft as your blade把Jon渴望的warrior价值延伸到mind，证明他也不是只能被锤成单一metal。",
73:"think on it不是承诺成功；Aemon保留审议权，也让Jon学会制度说服常以延迟决定结束。",
}

STAGES=[
(1,8,"Alliser宣布Jon等八人结束训练，伙伴庆祝时Sam因被留下而独自离场。"),
(9,18,"庆功宴介绍rangers、builders分工与Watch衰退；Benjen话题令Jon失去胃口。"),
(19,34,"Jon识别Sam恐惧，骑到kingsroad边缘考虑放弃宣誓，却选择返回Castle Black并形成行动计划。"),
(35,53,"Jon深夜坚持见Aemon，请求Sam结束训练，以可预见伤害和Aemon制度影响力说明理由。"),
(54,73,"Chett主张弱者被淘汰；Jon用maester chain说明组织需要多种能力，经反驳后锁定Sam可协助Aemon的具体角色。"),
]

BACKGROUNDS={
1:"**训练结束：** Alliser只决定recruit何时可swear vow；随后Lord Commander将其分配给rangers、builders或stewards。",
7:"**Benjen状态：** Benjen与ranging party失踪，尚未找到尸体或确认死亡；Jon坚持使用现在时。",
14:"**rangers：** 越过Wall侦察、巡逻、追踪wildlings并作战，是Watch最显眼的军事分支。",
16:"**builders：** 维修Wall、castles、roads、tunnels并清理forest；人力衰退使其从扩建转为勉强保养。",
24:"**宣誓后分散：** brothers可能留Castle Black，也可能调Eastwatch或Shadow Tower；Sam若未通过仍受Alliser训练。",
30:"**vow边界：** recruit在正式说words前可自由离开；宣誓后擅离则成为deserter并可被处死。",
35:"**Aemon household：** blind且高龄的Maester Aemon由stewards Clydas、Chett协助医疗、文书与日常生活。",
44:"**maester chain：** 每种metal link代表一种学习领域；maester自行以study锻成chain，并终身佩戴作为service象征。",
49:"**权限：** Alliser负责判断训练完成，Jeor Mormont作Lord Commander拥有最终组织权；Aemon主要靠counsel影响。",
53:"**既往保护：** Jon曾组织学员避免重伤Sam，并让Ghost威胁Rast；这降低即时欺凌，却依赖Jon等人在场。",
59:"**metal meanings：** 文中明确gold对应accounts、silver对应healing、iron对应warcraft；其他metal含义未在本段逐一说明。",
62:"**stewards：** 不只是室内仆役，而负责food、animals、fuel、clothing、transport、ravens、records等整个后勤系统。",
70:"**role proposal：** Jon建议Sam利用贵族教育协助Aemon处理读写、算术、books和ravens，并非免除所有劳动。",
}

EXTRA_VOCAB=[
("manure","/məˈnʊr/","n.","粪肥","shovels"),("swine","/swaɪn/","n.","猪（集合或古风）","herding"),("whoop","/wuːp/","n.","欢呼喊声","Pyp"),("reptile","/ˈreptaɪl/","n./adj.","爬行动物；冷酷似蛇的","stare"),("green","/ɡriːn/","adj.","缺乏经验的","boys"),("hoot","/huːt/","v.","哄笑叫喊","celebration"),("surcoat","/ˈsɜːrkoʊt/","n.","罩袍","wine stains"),("rack of lamb","/ræk əv læm/","n.","整排羊肋肉","feast"),("garnish","/ˈɡɑːrnɪʃ/","v.","配菜装饰","mint"),("chickpea","/ˈtʃɪkpiː/","n.","鹰嘴豆","salad"),("gorge","/ɡɔːrdʒ/","v.","狼吞虎咽","feast"),("quarry","/ˈkwɔːri/","v.","开采石料或冰块","builders"),("sledge","/sledʒ/","n.","重型雪橇","ice blocks"),("restlessness","/ˈrestləsnəs/","n.","焦躁不安","Jon"),("skittish","/ˈskɪtɪʃ/","adj.","易受惊的","horses"),("trickle","/ˈtrɪkəl/","n./v.","细流；缓缓流","creek"),("pocked","/pɑːkt/","adj.","布满坑点的","road"),("adulteress","/əˈdʌltərəs/","n.","通奸女性（贬称）","Jon’s self-wounding guess"),("rookery","/ˈrʊkəri/","n.","渡鸦房","Aemon keep"),("wen","/wen/","n.","皮肤囊肿或肿块（旧称）","Chett"),("abed","/əˈbed/","adv./adj.","在床上（古风）","Aemon"),("on the morrow","/ɑːn ðə ˈmɑːroʊ/","phr.","明日（古风）","return later"),("wedge","/wedʒ/","v.","楔住；卡紧","boot in door"),("bed robe","/ˈbed roʊb/","n.","睡袍","Aemon"),("diversion","/daɪˈvɜːrʒən/","n.","消遣；转移注意之事","midnight visitor"),("plow","/plaʊ/","v.","犁田","steward task"),("churn","/tʃɜːrn/","v.","搅乳制黄油","butter"),("blister","/ˈblɪstər/","v./n.","起水泡；水泡","hands"),("deft","/deft/","adj.","灵巧熟练的","mind and blade"),("comparative advantage","/kəmˈpærətɪv ədˈvæntɪdʒ/","n.","相对优势","interpretive term"),
]
VOCAB=BASE_VOCAB+EXTRA_VOCAB

def extract_blocks():
    blocks=extract_range(407,414,"JON","CH41")
    # The page image contains the apostrophe; the selectable text layer drops it.
    blocks[33]["text"]=str(blocks[33]["text"]).replace("direwolf s muzzle","direwolf’s muzzle")
    return blocks

def main():
    blocks=extract_blocks()
    write_chapter(
        out=OUT,chapter=41,pov="JON",page_start=407,page_end=414,
        blocks=blocks,summaries=SUMMARIES,key_notes=KEY_NOTES,stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Jon归属选择、Sam处境、Night’s Watch分工与制度内说服。",
        vocab=VOCAB,
        guide="Ser Alliser以一贯辱骂宣布Jon等八人结束训练。众人把这当作成为真正black brothers的前夜，Sam却因继续被留下而独站枯树下、缺席庆功宴。Jon意识到宣誓和部门分配将拆散原有保护网络；他骑到kingsroad，认真看见自己仍可离开，却最终把Castle Black称为home并返回。深夜，他不直接再用Ghost威胁bullies，而是找Maester Aemon走制度路径：先说明可预见伤害，再用maester chain类比组织需要多种metal。Chett正确反驳steward工作并不轻松后，Jon进一步提出Sam在literacy、sums、books、ravens和animals方面的具体能力，使诉求从同情弱者升级为让Watch更有效地使用一个人。",
        people=[
            ("Jon Snow","本章视角；结束训练、面对vow前最后离开机会，并替Sam进行制度游说"),
            ("Samwell Tarly","仍留在训练中的Jon friend，无法战斗但识字、善算、熟悉books与animals"),
            ("Maester Aemon","blind高龄maester；倾听Jon请求并测试其role-fit论证"),
            ("Chett","协助Aemon的steward，敌视Jon与Sam，却提供steward劳动的现实反驳"),
            ("Ser Alliser Thorne","master-at-arms，决定recruits何时结束训练并持续以辱骂施压"),
            ("Pyp / Grenn / Halder / Dareon","同期学员；分别以玩笑、愿望和部门选择呈现毕业情绪"),
            ("Benjen Stark","失踪的First Ranger；Jon拒绝用过去时承认其死亡"),
            ("Ghost","Jon的direwolf，随他夜骑并独自hunt"),
        ],
        terms=[
            ("rangers","越Wall巡逻、侦察并战斗的军事分支"),
            ("builders","维护Wall、castles、roads、tunnels和周边forest的工程分支"),
            ("stewards","维持food、animals、fuel、clothing、transport、records、ravens与医疗协助的后勤分支"),
            ("say the words","正式宣读Night’s Watch vow；此后终身服役且不得擅离"),
            ("maester chain","由不同metal links组成、象征多门学问与终身service的颈链"),
        ],
        synthesis="Chapter 41把‘成为男人’从单一战斗能力拆开。Alliser与Chett最初都相信不能成为fighter的Sam要么被锤成iron、要么死亡；Jon一开始也只从保护朋友出发。真正使论证成熟的是两次修正：kingsroad让Jon承认自己的vow是选择而非宿命，因此他必须对留下后的组织负责；Chett则迫使他承认steward不是coward避难所。于是Jon不再只列Sam缺点，而找到具体正能力与具体岗位。Aemon没有立刻答应，但他的赞许说明Jon学到一种比剑更难的领导方式：看见被主流尺度判为无用的人，理解制度权限，接受反驳，再证明差异如何成为共同生存资源。",
        contrasts=[
            "**graduation circle／Sam枯树：** 同一制度进步让多数人庆祝，也让未被选中者更加孤立。",
            "**ranger荣耀／builder与steward维生：** 可见的战斗依赖不显眼的维修和后勤。",
            "**kingsroad世界／Wall地平线：** 一边是未见之地与离开自由，一边是Jon主动选择的新home。",
            "**Ghost hunt／Jon vow：** wolf可按本能自由往返，Jon正决定接受永久规则。",
            "**hammer tin into iron／use tin as tin：** 训练可以发展能力，却不能靠暴力消灭人的差异。",
            "**同情Sam／证明role fit：** 善意开启诉求，具体能力与组织需要才使方案可执行。",
        ],
        questions=[
            "Aemon会否说服Lord Commander绕过Alliser，让Sam结束训练？",
            "Jon等八人将分别被分到rangers、builders还是stewards？",
            "Benjen与失踪rangers究竟发生了什么？",
            "Jon宣誓后是否仍会把Castle Black稳定地视作home？",
            "Chett对Jon揭露其不识字会如何反应，是否影响Sam未来处境？",
        ],
        extraction_notes="PDF pp.407–414校勘后共73段；共3处跨页续段：pp.407–408、408–409与413–414。p.410第34段的direwolf’s在文本层丢失apostrophe，已依页面图像修复。p.407章首直接排作You are…而无开引号，且同页Halder/Haider拼法不一致，均属源页现状，按原文保留并注明。",
    )
    print(f"Wrote Chapter 41 with {len(blocks)} paragraphs")

if __name__=="__main__":
    main()
