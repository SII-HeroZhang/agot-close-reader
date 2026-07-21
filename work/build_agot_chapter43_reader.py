#!/usr/bin/env python3
"""Build Chapter 43 (EDDARD) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter42_reader import VOCAB as BASE_VOCAB

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"/"AGOT_逐章精读"

S={
1:"夕阳在throne room投下暗红条纹；dragon skull已换成hunting tapestries，Eddard却只看见blood red。",
2:"Eddard坐在尖锐不适的Iron Throne上，断腿持续剧痛，暗骂Aegon的傲慢和Robert外出狩猎。",
3:"Varys确认袭击者是否真非普通brigands；多数court随Robert hunt，Eddard被迫代坐throne。",
4:"除council外，petitioners、lords、smallfolk与guards都必须站立或跪下。",
5:"衣衫破烂、带血恐惧的villagers跪着，三名knights在后作引见者。",
6:"Raymun讥讽说他们当然是brigands——Lannister brigands。",
7:"Eddard感到全厅各阶层都不安地竭力倾听。",
8:"他不惊讶：Tyrion被捕后双方call banners，Golden Tooth已有armies；现在要考虑如何止血。",
9:"Karyl说这些是Sherrer仅存者，Wendish Town与Mummer’s Ford也几乎全灭。",
10:"Eddard命villagers起身，因为不信任人在跪姿中说出的证词。",
11:"众人艰难站起，一名血衣女孩仍呆跪并盯着Kingsguard Arys。",
12:"Raymun叫alehouse keeper Joss讲述Sherrer发生的事。",
13:"Joss误把Eddard称His Grace。",
14:"Eddard纠正king正在hunt，自报Hand身份，命其说明自己及raiders。",
15:"Joss在现在时与过去时间挣扎，讲alehouse被喝空、烧毁，自己险些被杀。",
16:"farmer说来者夜焚田屋、杀阻挡者，却不掠stock而故意杀cow弃尸，因此不像求财raiders。",
17:"bandaged smith讲袭击者骑马把apprentice当游戏追刺，最终由big one一枪杀死。",
18:"跪地女孩说mother也被杀，随后在未完成的句子中哭泣。",
19:"Raymun说Wendish folk躲进木holdfast后被火攻，逃出者连妇女婴儿都被arrow射杀。",
20:"Varys低声感叹残酷。",
21:"Joss说石制Sherrer未被烧出，big one因upriver有更多目标而转往Mummer’s Ford。",
22:"Eddard触到Iron Throne仍锋利的blades，回顾Balerion熔千剑、59日锻成的杀人chair传说。",
23:"他不理解自己为何坐上这里，却因众人求justice而压住怒火，追问Lannister身份的proof与旗帜。",
24:"Marq急躁回应Lannisters不至于蠢到公开挂lion banner。",
25:"Karyl冷静列出全员骑马、mail、steel lance、longsword与battle-axe，并叫一名survivor讲horses。",
26:"old stable worker凭经验确认全是warhorses，从未拉过plow。",
27:"Littlefinger提出也可能是装备精良、抢来warhorses的brigands。",
28:"Eddard询问人数。",
29:"三名witness同时给出至少百人、五十人、数百人的不同估计。",
30:"Eddard说老太太比自己知道的更接近真相，再问armor是否有device。",
31:"Joss说装备无标记，但leader巨大如ox、声音如石裂，无法认错。",
32:"Marq立即认定是Mountain Gregor Clegane。",
33:"厅内各阶层窃窃私语，因为Gregor是Tywin bannerman，指控将牵动王室姻亲。",
34:"Eddard意识到villagers害怕被迫在king面前指认其father-in-law，并怀疑knights是否给他们选择。",
35:"Pycelle说realm还有很多large men，不能仅凭体型确认Gregor。",
36:"Karyl反问是否真有谁像Mountain That Rides一样巨大。",
37:"Raymun说连Sandor在Gregor旁都像pup，坚称无需尸体上的seal也可认出。",
38:"Pycelle质疑有land与keep的anointed knight为何会去当brigand。",
39:"Marq骂Gregor是false knight、Tywin的mad dog。",
40:"Pycelle提醒Eddard，Tywin是queen father。",
41:"Eddard反讽感谢提醒，暗示Pycelle立场明显。",
42:"Eddard看见有人悄悄离厅报信，也发现Sansa与Mordane旁听，虽生气却知septa无法预料court内容。",
43:"Littlefinger追问三名knights领地受保护时他们为何缺席。",
44:"Karyl说自己与Marq守Golden Tooth pass，Edmure得报后才派小队救survivors进京。",
45:"Raymun因Edmure召集主力在Riverrun，返地时Clegane已越Red Fork逃向Lannister hills。",
46:"Littlefinger问若raiders再来怎么办。",
47:"Marq激动说会用敌血灌溉被烧fields。",
48:"Karyl说Edmure已向边境各village、holdfast派人，下次袭击不会容易。",
49:"Eddard判断这或正中Tywin计谋：诱年轻Edmure为保护每寸土地而分散Riverrun兵力。",
50:"Littlefinger问既已加强防御，他们究竟向throne求什么。",
51:"Raymun请求获准以steel回击Lannisters，为三地smallfolk求justice。",
52:"Marq说Edmure也想报复Gregor，但Hoster命他们先请king许可。",
53:"Eddard感谢Hoster谨慎，并推演Tywin让Gregor夜间无旗伪装brigands，以便反咬Tully先破king’s peace。",
54:"Pycelle主张若Gregor违vow劫掠强暴，应向其liege Tywin申诉，此事不属throne。",
55:"Eddard回答各地justice都以Robert名义施行，因此全部属于king。",
56:"Pycelle接受措辞却想拖到Robert回来决定。",
57:"Eddard说Robert命自己以king耳朵听、声音说，他将履职，同时派Robar向hunt队报告。",
58:"Robar Royce上前行礼。",
59:"Eddard因Robar father随king hunt，请他传达今日court所言所为。",
60:"Robar承诺立刻出发。",
61:"Marq追问是否获准向Gregor复仇。",
62:"Eddard纠正他们谈的是justice而非vengeance，拒绝烧Clegane田地杀其people，并向villagers承诺有限司法补偿。",
63:"全厅注视下，Eddard忍断腿剧痛站起，解释north传统要求判死者亲自行刑，但伤势迫使他派人。",
64:"十六岁的Loras主动请命代Eddard执行，保证不会失败。",
65:"Littlefinger嘲若Loras独去，Gregor会把他的head配plum送回，并不会接受justice。",
66:"Loras傲然说自己不怕Gregor。",
67:"Eddard点Beric、Thoros、Gladden、Lothar各集二十人，再加二十Stark guards，由Beric统领。",
68:"Beric鞠躬接受命令。",
69:"Eddard以Robert与Hand完整名义，命队伍持king’s flag赴westlands，褫夺Gregor全部身份财产并判死。",
70:"宣判回声消散后，Loras困惑地问自己怎么办。",
71:"Eddard见他几乎像Robb般年轻，肯定valor却说其求的是vengeance，命Beric天明立刻出发并闭庭。",
72:"Alyn、Porther扶Eddard下throne；Loras怒视后先行离开。",
73:"Varys收papers时称Eddard比自己大胆；Littlefinger、Pycelle已走。",
74:"Eddard因leg痛不耐烦，问何出此言。",
75:"Varys说自己会派Loras，因为与Lannisters为敌者应结交Tyrells。",
76:"Eddard只说Loras年轻，会长大并忘掉失望。",
77:"Varys又指出Ser Ilyn是King’s Justice，另派人执行可能被视为grave insult。",
78:"Eddard说无意冒犯，实则不信任mute executioner，且Paynes是Lannister bannermen，故选无Tywin fealty者。",
79:"Varys表面称赞谨慎，又提醒Ilyn在后厅不悦，并阴冷玩笑他热爱execution work。",
}
SUMMARIES=[S[i] for i in range(1,80)]

KEY_NOTES={
1:"dragon heads换成hunting tapestries标志王朝更替，但sunset仍把墙染成blood；换装饰不能消除权力暴力。",
2:"A king should never sit easy被椅子字面执行；Eddard伤腿让治理责任成为持续身体刑罚，也怨Robert把工作留给他。",
3:"white hart吸走king与half court，使日常hunt和边境屠杀在同一时间并置；Robert absence不是中性背景。",
4:"sit/stand/kneel把等级写成身体高度；下一段受害者位于最低处，Eddard首先会改变这一姿势。",
6:"Lannister brigands是矛盾组合：brigand应无主，Lannister却指向有组织权力，这正是案件核心。",
8:"tinderbox、blood flow、stanch wound把政治冲突写成火与身体创伤；Eddard目标是止血而非赢一方。",
10:"不信kneeling testimony体现他的司法直觉：恐惧与讨好会扭曲话语，要求站起是恢复最低限度主体性。",
11:"女孩仍不能站不等于抗命；blank stare显示命令无法立即解除创伤与身体冻结。",
14:"black/white/grey, shades of truth让衣服颜色变成认识论：案件不是单纯善恶二色，需要在灰中判定。",
15:"I keep / I kept的自我修正把财产毁灭变成语法时态断裂，Joss仍习惯活在失去之前。",
16:"不抢cow而杀弃证明目的不是economic banditry，而是terror、资源破坏与诱发军事反应。",
17:"袭击者把apprentice的死亡当game，laughter使军事行动呈现刻意残酷而非战斗附带伤亡。",
18:"ellipsis保留女孩无法说完的伤害；文本没有具体完成句子，精读不替她确定遭遇。",
20:"Varys的感叹可能是真怜悯、礼仪或表演；仅凭soft voice无法判定内心。",
22:"Iron Throne本是敌人surrendered swords，却继续切伤使用者；胜利武器被熔成统治风险。",
23:"Eddard明知可能是谁仍先问proof，区分私人确信与可公开作出王权决定的证据标准。",
24:"Marq的推理合理，却用blind stupid替代证据；Eddard需要把可否认策略转成可裁判事实链。",
25:"Karyl用装备系统证明规模化资源：统一mounted、mailed与steel武器比单个coat of arms更难由普通brigands获得。",
26:"old man的stable expertise让smallfolk不是只提供痛苦故事，也提供技术证据。",
27:"Littlefinger提出alternative hypothesis，虽可被反驳，却有助测试推论是否只剩一个解释。",
29:"人数冲突展示恐惧条件下eyewitness estimation不可靠；差异不等于整场袭击虚构。",
30:"goodwoman说army在组织性质上可能更对，即使数字夸张；Eddard区分quantity error与category insight。",
31:"plain armor显示袭击者主动去标识化；leader巨大身体反而成为无法卸下的signature。",
34:"villagers可能被knights带来承担政治指控风险；Eddard不仅审证词内容，也审证词产生条件。",
35:"Pycelle说large men很多是抽象可能，Karyl下一句用极端体型稀有性压缩这个替代解释。",
38:"anointed knight与brigand不相容只是规范逻辑，不是事实不可能；title不能证明行为。",
40:"Pycelle用queen kinship提醒政治后果，实质要求证据判断向power relation让步。",
41:"Eddard反讽揭露提醒并非中立信息，而是众人都知道的压力。",
42:"hares或rats二选一描写离席者：可能自保，也可能给Cersei送信；Eddard不能确定，文本也不确定。",
43:"Littlefinger的问题把受害者证词外扩到lord protection failure，避免骑士只以正义代表自居。",
49:"Tywin strategy是Eddard inference：袭击迫Edmure分兵守每点，主力便被bleed off；合理但尚无Tywin书面命令。",
51:"steel for steel把justice和symmetrical retaliation等同；Eddard后面会拆开这两个概念。",
52:"Hoster要求royal leave阻止Tully落入‘先开战’叙事，是法律程序也是战略防护。",
53:"fox as lion强调Tywin兼具隐蔽算计与公开力量；no banners制造plausible deniability并诱敌承担formal blame。",
54:"让Tywin审自己bannerman会把控诉交给潜在指挥者；Pycelle以feudal channel形式制造利益冲突。",
55:"一句话确立central sovereignty：liege justice不是独立私域，而是king authority的层级执行。",
57:"合并的跨页长句把delegation说清：Hand不是等待king的秘书，而在授权期间借king voice作决定，同时仍建立报告链。",
62:"Eddard拒绝报复Clegane smallfolk，因collective punishment会复制原罪；justice以具体行为者为target。",
63:"他无法亲自wield sword，却公开说明例外理由，尽量维持判决责任与执行责任的可追踪关系。",
64:"Loras说honor，动机却与Gregor tournament冲突相连；Eddard不只评能力，也评执行者为何想去。",
65:"Littlefinger的plum羞辱Loras外貌，却指出派单人去不服从的armed lord不是execution而是送死。",
67:"Eddard派约百人、多人领队及king flag，把私人duel替换为可见的state enforcement。",
69:"denounce、attaint、strip、sentence形成递进法律动词：先公开定性，再法律褫夺，最后判死。",
71:"valor不足以保证justice；Eddard拒绝让个人荣耀与复仇欲主导王权执行。",
75:"Varys指出被Eddard忽略的alliance payoff：让Loras去可把Tyrell私人荣誉绑定到反Lannister阵线。",
76:"Eddard以成长问题处理Loras失望，低估被拒绝的政治与情感后果，这与他擅长法律原则、较弱于court coalition相符。",
77:"Varys从未明说Eddard错，只列第二个失去的关系：King’s Justice Ser Ilyn的office honor。",
78:"选择无Lannister fealty执行者是sound conflict-of-interest control；代价是可能冒犯正式execution office。",
79:"does so love his work把Ilyn的execution热情说成职业爱好，Varys用轻柔幽默把潜在敌意留在Eddard心中。",
}

STAGES=[
(1,14,"Robert hunt期间Eddard带伤代坐Iron Throne；三名riverland knights带来Sherrer等地survivors公开陈情。"),
(15,34,"villagers描述非掠夺式焚杀、warhorses与巨大leader；证词数量不一，却逐步指向Gregor及有组织Lannister行动。"),
(35,53,"Pycelle质疑身份与管辖，Littlefinger追问防守缺席；Eddard识别无旗袭击意在诱Edmure分兵并承担破坏peace罪名。"),
(54,69,"Eddard拒绝把案件交Tywin或等Robert，区分justice与vengeance，组织Beric率王旗队伍并正式褫夺、判死Gregor。"),
(70,79,"Eddard拒绝Loras参与；Varys指出他同时放弃Tyrell结盟机会并可能冒犯Ser Ilyn，揭示正确程序仍有court成本。"),
]

BACKGROUNDS={
1:"**throne room变迁：** Targaryen dragon skull已从墙上移走，换成Robert喜爱的hunting tapestries；Iron Throne仍保留。",
2:"**Iron Throne：** 传说Aegon以战败者千把swords、借Balerion dragonfire熔铸，尖锐不适用于提醒king不得安逸。",
3:"**Hand代理权：** Robert离城hunt时命Eddard代坐Iron Throne、听petitions并以king authority裁断。",
8:"**边境动员：** Catelyn拘捕Tyrion后，Riverrun与Casterly Rock均call banners，Golden Tooth pass两侧集兵。",
9:"**受袭地点：** Sherrer、Wendish Town、Mummer’s Ford位于riverlands西部，靠近Lannister边境与Red Fork。",
18:"**证词边界：** 女孩只说mother被杀并在后一句中断；不能由本段确定她未说出的具体遭遇。",
25:"**组织证据：** 数十上百全员warhorse、mail与steel arms需要lord-scale资源，但仍非直接命令书。",
32:"**Gregor Clegane：** 巨型knight、Tywin bannerman，号Mountain That Rides；体型是witness识别核心。",
34:"**王室亲缘：** Tywin是Cersei father，也即Robert father-in-law；公开指控他可能意味着王室阵营分裂。",
38:"**anointed knight：** 经宗教仪式授knighthood并发保护弱者等誓言；身份规范不保证实际遵守。",
45:"**Edmure部署：** riverland lords被召集到Riverrun或Golden Tooth防线，边境本地因而出现防守空隙。",
49:"**文本事实／推断：** Edmure确实分派村镇防卫；‘这是Tywin目的’是Eddard战略推断，未有直接证据。",
53:"**plausible deniability：** 无banners、plain armor、夜袭让Tywin可否认控制；Tully若正式反击则可能被指先开战。",
54:"**feudal chain：** 通常bannerman受liege lord审判；但king是全realm最高justice source，Hand可越过有利益冲突的liege。",
63:"**north execution principle：** 判死者应亲自挥剑以承担责任；Eddard因broken leg公开委派执行。",
67:"**royal party：** Beric等四组各20人，加20 Stark guards，合计约100；携king flag表明国家执法而非Tully raid。",
69:"**attainder：** 以统治权宣告某人丧失法律身份、titles、lands、income和holdings，并可判处死刑。",
77:"**King’s Justice：** Ser Ilyn Payne是王室正式executioner；未用他可能被解释为绕过office。",
78:"**fealty conflict：** House Payne对House Lannister负封建义务，Eddard因此不让Ilyn执行针对Tywin bannerman的任务。",
}

EXTRA_VOCAB=[
("cavernous","/ˈkævərnəs/","adj.","洞穴般宽大空旷的","throne room"),("tapestry","/ˈtæpəstri/","n.","织锦壁毯","hunting scenes"),("jagged","/ˈdʒæɡɪd/","adj.","参差尖锐的","Iron Throne"),("grotesque","/ɡroʊˈtesk/","adj.","怪诞扭曲的","metal"),("needs","/niːdz/","adv.","必定；不得不（古风）","must needs sit"),("petitioner","/pəˈtɪʃənər/","n.","请愿者","court"),("tattered","/ˈtætərd/","adj.","破烂的","villagers"),("tinderbox","/ˈtɪndərbɑːks/","n.","火药桶般易爆局势","west"),("stanch","/stɔːntʃ/","v.","止住血流","political wound"),("holdfast","/ˈhoʊldfæst/","n.","小型堡寨","village refuge"),("alehouse","/ˈeɪlhaʊs/","n.","麦酒馆","Joss"),("’prentice","/ˈprentɪs/","n.","apprentice省略形式；学徒","smith’s boy"),("suckling","/ˈsʌklɪŋ/","adj.","尚在吃奶的","babes"),("barb","/bɑːrb/","n.","倒钩；尖刺","throne"),("swaggering","/ˈswæɡərɪŋ/","adj.","趾高气扬的","Marq"),("bantam","/ˈbæntəm/","n./adj.","矮小好斗者；小型鸡","rooster metaphor"),("hot-blooded","/ˌhɑːtˈblʌdɪd/","adj.","冲动易怒的","young knight"),("device","/dɪˈvaɪs/","n.","纹章图案","shield or helm"),("red-handed","/ˌred ˈhændɪd/","adj.","当场有罪的；血债确凿的","butcher"),("ponderously","/ˈpɑːndərəsli/","adv.","沉重缓慢地","Pycelle rises"),("anointed","/əˈnɔɪntɪd/","adj.","受涂油礼授职的","knight"),("adjudicate","/əˈdʒuːdɪkeɪt/","v.","裁决","boundary stones"),("goad","/ɡoʊd/","v.","刺激迫使","Edmure"),("gallant","/ˈɡælənt/","adj.","英勇热心的","more than wise"),("pillage","/ˈpɪlɪdʒ/","v.","劫掠","border"),("guise","/ɡaɪz/","n.","伪装身份","brigand"),("forsake","/fərˈseɪk/","v.","背弃","holy vows"),("defer","/dɪˈfɜːr/","v.","推迟","matter"),("stripling","/ˈstrɪplɪŋ/","n.","年轻小伙（旧称）","Loras"),("plum","/plʌm/","n.","李子；梅子","Littlefinger insult"),("haughty","/ˈhɔːti/","adj.","傲慢自负的","Loras"),("befit","/bɪˈfɪt/","v.","适合身份","rank"),("denounce","/dɪˈnaʊns/","v.","公开谴责；宣布有罪","Gregor"),("attaint","/əˈteɪnt/","v.","依法褫夺权利与财产","sentence"),("valor","/ˈvælər/","n.","勇武","Loras"),("sullen","/ˈsʌlən/","adj.","闷怒的","stare"),("construe","/kənˈstruː/","v.","解释为；理解为","insult"),("fealty","/ˈfiːəlti/","n.","封建效忠义务","Payne to Lannister"),("plausible deniability","/ˈplɔːzəbəl dɪˌnaɪəˈbɪləti/","n.","可合理否认性","interpretive term"),
]
VOCAB=BASE_VOCAB+EXTRA_VOCAB

def extract_blocks():
    blocks=extract_range(424,432,"EDDARD","CH43")
    # p.430 continues the still-open quotation from p.429 with capitalized “I”.
    blocks[56]["text"]=str(blocks[56]["text"])+" "+str(blocks[57]["text"])
    blocks[56]["end_page"]=blocks[57]["end_page"]
    del blocks[57]
    for order,block in enumerate(blocks,1):
        block["order"]=order
        block["id"]=f"CH43-P{int(block['page']):03d}-{order:03d}"
    return blocks

def main():
    blocks=extract_blocks()
    write_chapter(
        out=OUT,chapter=43,pov="EDDARD",page_start=424,page_end=432,
        blocks=blocks,summaries=SUMMARIES,key_notes=KEY_NOTES,stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在riverlands证词、proxy raid识别、king’s justice与court政治成本。",
        vocab=VOCAB,
        guide="Robert带大半court追猎white hart时，Eddard拖着断腿代坐Iron Throne。Sherrer、Wendish Town与Mummer’s Ford幸存者描述一支不掠财、专门焚杀的去标识化骑兵：全员warhorses、mail、steel weapons，leader巨大如Mountain。Eddard既不因愤怒跳过proof，也不让旗帜缺失成为免责；他把装备规模、行动目的、身体识别与Tywin战略收益连成间接证据链，并看出无旗夜袭意在诱Edmure分兵、反击，从而让Tully承担先破king’s peace的名义。最终他拒绝对Clegane smallfolk报复，正式褫夺Gregor并派Beric率王旗队伍执行。Varys随后提醒：程序与利益冲突控制虽稳健，Eddard却失去了拉拢Loras、Tyrell和安抚Ser Ilyn的court机会。",
        people=[
            ("Eddard Stark","本章视角；代Robert审理riverlands袭击并以Hand身份判决Gregor"),
            ("Gregor Clegane","号Mountain That Rides的巨型knight与Tywin bannerman，被证词指认为raid leader"),
            ("Tywin Lannister","Gregor liege；Eddard推断其借无旗袭击实施可否认的间接战争"),
            ("Joss / Sherrer survivors","提供破坏目的、leader体型、装备与warhorse等事实证词"),
            ("Karyl Vance / Marq Piper / Raymun Darry","护送survivors进京并请求王权批准回击的riverland knights"),
            ("Pycelle","Grand Maester，质疑Gregor identification并主张交Tywin自行审理"),
            ("Littlefinger","测试alternative explanations与riverland lords防守责任"),
            ("Varys","观察court反应，事后指出Tyrell alliance与Ser Ilyn office两项政治成本"),
            ("Loras Tyrell","十六岁Knight of Flowers，主动请求执行Gregor却因vengeance动机被拒"),
            ("Beric Dondarrion","获Eddard任命率royal party执行判决的young lord"),
        ],
        terms=[
            ("king’s peace","禁止lords自行发动私战、要求争端接受王权裁判的全realm秩序"),
            ("plausible deniability","通过无旗、plain armor与夜袭让上级可否认指挥关系"),
            ("attainder","褫夺rank、titles、lands、income、holdings等法律身份与财产权"),
            ("King’s Justice","王室execution office，由Ser Ilyn Payne担任"),
            ("white hart hunt","Robert与大半court正在kingswood追猎的稀有白鹿活动"),
        ],
        synthesis="Chapter 43把justice写成证据、权限、目标与执行者四层选择。证词人数互相矛盾，却在非掠夺式破坏、军用装备、warhorses和异常巨大leader上相互支撑；没有lion banner降低直接证明，却恰好符合proxy raid所需。Eddard继而确认Hand可代表king裁决，不把案件交给有利益冲突的Tywin，也不允许Tully用焚村报复焚村。最后，他选择无Lannister fealty的Beric等人，携king flag公开执法。这样的判决在原则上连贯，却并非政治上无成本：Loras被拒、Tyrell友谊未被利用、Ser Ilyn被绕过。Varys的尾声提醒读者，正义决定不仅回答‘谁有罪’，还会重新排列谁觉得被尊重、被需要或被树为敌人。",
        contrasts=[
            "**hunting tapestries／blood testimony：** 王室把墙装成娱乐景观，真实乡野正在被猎杀。",
            "**跪姿／站立证词：** Eddard先改变受害者身体位置，再要求他们说事实。",
            "**无banner／巨大身体signature：** 可移除纹章，却无法轻易隐藏Gregor体型。",
            "**人数不一致／组织性质一致：** eyewitness数量估计混乱，不抹除共同技术证据。",
            "**vengeance／justice：** 前者向敌方无辜者复制伤害，后者瞄准被认定的行为者并公开授权。",
            "**legal prudence／court opportunity：** 回避利益冲突保护判决，也可能损失alliances并制造office insult。",
        ],
        questions=[
            "Beric率领的royal party能否真正拘捕或处死Gregor？",
            "Robert得知Eddard褫夺Tywin bannerman后会支持还是撤销判决？",
            "Tywin是否确实亲自下令raid，还是Gregor自行行动？",
            "Loras与Ser Ilyn会如何回应被排除在执行任务之外？",
            "Edmure分散防守后，Golden Tooth与Riverrun主力是否会暴露更大弱点？",
        ],
        extraction_notes="PDF pp.424–432校勘后共79段。自动提取曾把p.429末尾to speak with his voice.与p.430开头I mean to do just that误切为两段，已合并。校勘后共6处跨页续段：pp.425–426、426–427、428–429、429–430、430–431与431–432。段落顺序、证词说话人、法律宣判与引号均已复核。",
    )
    print(f"Wrote Chapter 43 with {len(blocks)} paragraphs")

if __name__=="__main__":
    main()
