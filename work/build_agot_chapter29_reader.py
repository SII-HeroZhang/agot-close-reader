#!/usr/bin/env python3
"""Build Chapter 29 (SANSA) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter28_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"Sansa乘金色薄纱litter来到Hand’s tourney，被帐篷、铠甲、战马、旗帜与knights的盛景震撼。",2:"她觉得现场胜过歌谣，也意识到自己精心打扮后正被贵族们注视。",3:"Kingsguard、Jaime、Gregor、Yohn Royce、Jason Mallister与Thoros依次登场，历史战绩被包装成可观看的英雄谱。",4:"更多hedge knights、贵族子弟和Frey家族成员入场；Sansa与Jeyne相信他们都将名扬Seven Kingdoms。",5:"Jeyne先因Jalabhar Xho外貌害怕，又看见Beric便立刻想嫁给他。",6:"Sandor、Renly与Winterfell三人参赛；Jory装备朴素却表现不错，Alyn和Harwin较早落败。",7:"joust持续至黄昏，赛场被踩烂；Sansa以great lady应有的镇定要求自己不躲避坠马场面。",8:"Jaime轻松获胜，之后又艰难击败年长许多的Barristan。",9:"Gregor的长枪刺穿一名Vale年轻骑士的喉咙；阳光、蓝披风和逐一染红的月牙把死亡写得异常清晰。",10:"Jeyne崩溃离席，Sansa却着迷地观看；她把没有哭解释为泪已为Lady和Bran耗尽，并悲伤死者将无人歌唱。",11:"尸体被抬走，男孩铲土盖住血迹，比赛立刻继续。",12:"Renly被Sandor猛烈撞落但无大碍；他把断金鹿角赠给胜者，民众争抢后又由他恢复秩序。",13:"赛事继续，伤马、换马、平局与落败快速交替。",14:"最后只剩Sandor、Gregor、Jaime和Loras四名强者。",15:"十六岁的Loras身披花朵铠甲、骑白马并向观众少女赠白玫瑰，成为Sansa眼中美的化身。",16:"Loras击落Robar；Sansa完全忽略伤者，只注视胜者骑到自己面前。",17:"Loras破例送她红玫瑰并赞美她，Sansa因他的gallantry失语，久久抱着花。",18:"一名带笑却眼神不笑的中年男人认出她具有Tully相貌。",19:"Sansa自报姓名，却不认识佩mockingbird扣饰的高贵男子。",20:"Septa Mordane介绍此人是small council的Petyr Baelish。",21:"Petyr说Catelyn曾是自己的queen of beauty，触摸Sansa头发后突然离开。",22:"夜深后Robert把最后三场延至次晨，court转往河边参加丰盛feast。",23:"Sansa获高位并与Joffrey相邻；她重写Lady之死的责任，把怨恨从Joffrey移向Cersei和Arya。",24:"Joffrey的美貌让她无法恨他，她既盼关注又怕他再次残酷。",25:"Joffrey亲吻她的手，并借Loras赠花赞美她。",26:"Sansa谦逊回应，称Loras是真正的knight并问他能否获胜。",27:"Joffrey说Sandor或Jaime会打败Loras，未来自己会打败所有人；他给Sansa和Septa倒酒。",28:"酒没有令Sansa陶醉，音乐、杂耍、Moon Boy与梦想成真的glamour才让她忘我。",29:"Joffrey整夜礼貌健谈，使Sansa沉迷到忽略Septa。",30:"一道道精致食物上桌；Joffrey亲自教她吃snails、开烤鱼和切肉，受伤右臂仍未抱怨。",31:"甜点继续上桌，Sansa吃撑仍想再吃lemon cake，忽然听见Robert吼叫。",32:"Robert整晚越来越喧闹，但Sansa此前听不清内容。",33:"醉酒Robert公开向Cersei宣称自己是king，执意次日参赛。",34:"众人旁观而不敢干预；Cersei面无血色，沉默离席。",35:"Jaime试图制止却被Robert推倒并羞辱；Robert夸口拿起warhammer便无人能敌。",36:"Jaime起身，以僵硬语气顺从回应。",37:"Renly微笑上前，用添酒转移Robert注意。",38:"Joffrey神情恍惚地问Sansa是否需要escort回城。",39:"Septa已醉倒，Sansa只得接受保护。",40:"Joffrey呼叫Dog。",41:"换上红衣的Sandor像从夜色中突然成形。",42:"Joffrey命Sandor护送未婚妻，自己不告别便离开。",43:"Sandor嘲笑Sansa原以为Joffrey会亲送，并说自己可能次日要杀Gregor。",44:"Sansa想叫醒Septa却失败；空桌与散席标志美丽梦境结束。",45:"Sandor举火把带路；Sansa虽恐惧他的脸，仍用礼仪称赞Ser Sandor骑得gallantly。",46:"Sandor拒绝空洞恭维和Ser称号，鄙视knights与誓言，并反问她是否看见Gregor。",47:"Sansa颤抖着答看见，并迟疑寻找合适赞词。",48:"Sandor讽刺替她补上gallant。",49:"Sansa意识到嘲弄，改说无人能抵挡Gregor；这句话既安全也真实。",50:"Sandor称她是被训练重复漂亮话的talking bird。",51:"Sansa说他刻薄且令人害怕，要求离开。",52:"Sandor断言Gregor故意利用年轻骑士未扣好的gorget杀人，又强迫Sansa直视自己的烧伤脸。",53:"Sandor铁钳般捏住她下巴，以醉酒而愤怒的眼神逼她看。",54:"叙述先描写Sandor尚完整的右半脸。",55:"随后展示左半脸被烧毁的耳、皮肤与裸露骨头，视觉反差破坏“只看美”的习惯。",56:"Sansa哭后Sandor放手熄灯，讲述六七岁时Gregor因木制knight玩具把他的脸按进炭火，父亲与三名成人才制止。",57:"父亲谎称床铺失火；四年后Gregor仍被正式涂油册封为knight，制度荣誉未惩罚私人暴行。",58:"Sandor沉默喘息；Sansa对他的悲伤取代了恐惧。",59:"她开始为Sandor而害怕，触碰其肩并说Gregor不是真正的knight。",60:"Sandor大笑后认同这句话，以little bird称她。",61:"余程Sandor沉默护送她穿城回Red Keep，一直送到bedchamber外。",62:"Sansa温顺地向他道谢并称my lord。",63:"Sandor抓住她，警告不能把今晚的话告诉Joffrey、Arya或Eddard。",64:"Sansa承诺保密。",65:"Sandor仍不满足，以死亡威胁强化秘密。",
}
SUMMARIES = [S[i] for i in range(1, 66)]

KEY_NOTES = {
1:"黄色薄纱把whole world变成gold，明确提示读者：本章的盛景先经过Sansa的审美滤镜，而非中性镜头。",
2:"better than the songs是她的最高评价，也为后文现实暴力反过来审判songs埋下结构性对照。",
3:"人物名单把war record、纹章和服饰压缩成spectacle；真实杀戮在tourney里被重新包装成荣耀背景。",
4:"尚无功绩的名字也被Sansa预先写进未来歌谣，说明她把可见的贵族身份等同于必然的英雄性。",
6:"Jory的plain armor被嘲作beggar，却不妨碍实际表现；外观与能力第一次出现轻微裂缝。",
7:"Sansa的composure既是勇气，也是社会训练：她观看危险，是因为great lady应该如此。",
9:"火光从钢甲消失、白月牙逐枚变红，把死亡从突然刺击延长为无法移开的视觉过程。",
10:"她不为陌生人哭，却为其不会进入歌曲而悲伤；同情仍需通过自己熟悉的song价值体系表达。",
11:"一铲土让娱乐继续，制度对死亡的回应是清理可见痕迹，而不是暂停追问。",
12:"gold antler从身份装饰变成群众争抢物，Renly靠亲自介入恢复秩序，显示popularity也可转为治理能力。",
15:"Loras精心控制armor、horse、flowers和巡场动作；gallantry既是真实礼仪，也是一场高度设计的public performance。",
16:"Robar呻吟不动与Sansa完全没看见并置，展示美丽焦点如何主动遮蔽受伤者。",
17:"红玫瑰让Sansa相信自己被从所有maidens中选中；颜色差异制造个体化亲密感。",
18:"Petyr的嘴笑而眼睛不笑延续他言行与内心可能分离的描写，Sansa只感到不适，尚不知道原因。",
21:"他用Catelyn旧日称号建立亲近，又未经邀请触摸Sansa头发；怀旧、投射与越界在同一动作里出现。",
23:"Sansa把Joffrey从责任链中剔除，是为维持婚约幻想而进行的心理重写；文本没有改变此前事实。",
24:"too beautiful to hate把审美直接变成道德免责机制，这正是本章要逐步拆解的认知模式。",
27:"my dog再次把Sandor物化为Joffrey工具；倒酒给Septa则让不合礼仪的行为获得监护人许可。",
28:"drunk on magic说明真正使她失去判断的不是wine，而是梦想被court表演逐项兑现。",
30:"Joffrey的体贴动作真实发生，但一夜courtesy不能自动抹去Trident事件；Sansa却愿意让当前表演覆盖过去。",
33:"feast的音乐与礼仪被Robert一句吼声切断，私人婚姻冲突也因王权身份变成全场政治表演。",
34:"Cersei的mask与沉默说明她不在公开场合回击，不表示冲突消失；旁观者的静止显示king难被约束。",
35:"Robert用旧战士身份羞辱Jaime，夸耀warhammer；过去的战功成为他否认当前身体与职责限制的依据。",
37:"Renly不直接争辩，而用fresh goblet顺着Robert欲望转移他，属于宫廷式危机处置。",
38:"Joffrey的queer look显示父母公开冲突已影响他，但Sansa无法进入其视角，只能观察疏离。",
43:"Sandor把兄弟生死战当笑话，酒意背后已有深仇线索；Sansa尚不了解其来源。",
44:"beautiful dream ended用散席完成结构转折：前半章的golden spectacle正式进入无灯的黑暗道路。",
45:"Sansa的courtesy既限制她，也保护她：害怕时仍能用共同礼仪启动对话，尽管称Ser恰好触怒Sandor。",
46:"Sandor拒绝knighthood不是谦逊，而是认为誓言与称号无法保证行为；Gregor正是他的反证。",
49:"no one could withstand him回避道德赞美，只描述力量事实，是Sansa第一次在礼貌模板内寻找不撒谎的措辞。",
50:"little bird意象指出她的语言来自训练与复述；这不是说她没有思想，而是思想常被现成songs词汇包裹。",
52:"Sandor对故意杀人的判断基于Gregor经验与gorget细节，具有可信动机但仍是其指控，并非正式裁决。",
55:"分两侧描写强迫读者像Sansa一样先看normal、再看ruin，无法再用courtesy把伤疤从视野中抹掉。",
56:"争夺的玩具恰是wooden knight：理想化knight形象成为导致伤害的导火索，象征极具反讽。",
57:"anointed与ointments音近并列：一边是治疗烧伤的药膏，一边是授予荣誉的圣油，制度却把施暴者册封。",
58:"黑暗让Sandor不再是可怕脸孔，而成为呼吸与创伤叙述；Sansa的同情因此能够出现。",
59:"no true knight仍来自songs伦理，却首次被用来批判现实称号，而非赞美外观，显示她的框架开始具备判断力。",
60:"Sandor的大笑既可能嘲讽她仍执着true knight概念，也包含苦涩认同；文本没有把情绪简化。",
61:"尽管口头粗暴且醉酒，Sandor实际完整履行护送任务；行为、称号与礼貌不再整齐对应。",
65:"结尾威胁阻止把脆弱经历公开化，也重新建立力量差；同情没有消除Sandor对Sansa的恐吓。",
}

STAGES = [
(1,14,"金色滤镜下的tourney汇集著名knights；Jory的朴素表现、年轻骑士之死和迅速清场开始撕开spectacle。"),
(15,30,"Loras以花与礼仪实现Sansa的歌谣幻想，Petyr短暂越界；feast上Joffrey又以完美courtesy重新获得她的信任。"),
(31,44,"Robert醉酒公开羞辱Cersei和Jaime，feast失序；Joffrey把护送交给Sandor，美丽梦境随散席结束。"),
(45,60,"黑暗归途中Sandor拒绝Ser称号，揭露Gregor可能故意杀人及童年烧伤真相；Sansa由恐惧转向同情。"),
(61,65,"Sandor实际把Sansa安全送回房门，却以死亡威胁要求保密，使保护、坦白、脆弱与暴力并存。"),
]

BACKGROUNDS = {
1:"**tourney：** 赛事在King’s Landing城外河边举行，包括joust与次日melee；观众从court到common folk均可参加。",
3:"**参赛者：** Kingsguard、great lords、hedge knights、freeriders和squires同场竞技，但装备、声望与资源差异巨大。",
6:"**Winterfell队伍：** Jory、Alyn、Harwin代表Eddard household参赛；他们不是本届最华丽或最著名的选手。",
9:"**joust风险：** 骑手高速相向、长枪对撞，即使以竞技规则进行也可能致死；gorget负责保护颈喉。",
15:"**Loras Tyrell：** Mace Tyrell幼子，十六岁，称Knight of Flowers；本章突出其竞技能力和公共形象。",
18:"**Petyr Baelish：** small council成员、Catelyn童年旧识，以mockingbird为个人纹章；此前曾向Catelyn提供dagger说法。",
22:"**aurochs：** 体型巨大的野牛，六头整烤体现royal feast的资源规模。",
23:"**Lady事件：** Nymeria咬伤Joffrey后逃走，Cersei要求处死Sansa的direwolf Lady；Eddard亲自执行。Sansa本段重新分配责任不改变事件经过。",
33:"**次日参赛争执：** Robert声称要参加melee；其国王身份、体型与酒醉使这一决定同时涉及个人危险和政治风险。",
41:"**Sandor Clegane：** Joffrey sworn shield，绰号the Hound；不是受封knight，却长期从事武力护卫。",
52:"**事实／指控：** 年轻knight确因长枪穿喉死亡，gorget未系妥；Sandor断言Gregor故意瞄准弱点，现场文本未提供独立裁定。",
56:"**兄弟年龄：** Sandor称自己当时约六七岁，Gregor大五岁且已异常高大强壮；故事来自Sandor本人。",
57:"**knighting：** septons以seven oils涂抹候选人、宣誓后由有资格者以剑触肩册封。Gregor由Rhaegar册封，但称号并未证明其道德。",
}

EXTRA_VOCAB = [
("litter","/ˈlɪtər/","n.","轿；肩舆","Sansa’s transport"),("pavilion","/pəˈvɪljən/","n.","大型帐篷；亭阁","tourney camp"),("caparisoned","/kəˈpærɪsənd/","adj.","披挂华丽马衣的","chargers"),("freshfallen","/ˌfreʃˈfɔːlən/","adj.","刚落下的","snow simile"),("ward against","/wɔːrd əˈɡenst/","phr.v.","防护；抵御","magic runes"),("filigreed","/ˈfɪlɪɡriːd/","adj.","饰有金银丝细工的","armor"),("acquit oneself","/əˈkwɪt wʌnˈself/","phr.v.","表现得……","Jory’s performance"),("unhorse","/ʌnˈhɔːrs/","v.","把骑手击落马下","joust result"),("tilt","/tɪlt/","n./v.","马上比武；参加比武","tourney"),("gorget","/ˈɡɔːrdʒɪt/","n.","护喉甲","fatal weakness"),("tine","/taɪn/","n.","叉尖；鹿角分枝","broken antler"),("forfeit","/ˈfɔːrfɪt/","adj./n.","被判失去资格；罚失","illegal horse strike"),("dais","/ˈdeɪɪs/","n.","高台","royal seating"),("demur","/dɪˈmɜːr/","v.","谦让地表示异议","modest reply"),("flagon","/ˈflæɡən/","n.","大酒壶","summerwine"),("giddy","/ˈɡɪdi/","adj.","兴奋眩晕的","glamour"),("motley","/ˈmɑːtli/","n./adj.","弄臣杂色服装","Moon Boy"),("jape","/dʒeɪp/","n.","玩笑；嘲弄","court humor"),("sweetbread","/ˈswiːtbred/","n.","动物胰腺或胸腺做的菜","feast course"),("reel","/riːl/","v.","踉跄摇晃","drunken Robert"),("guffaw","/ɡəˈfɔː/","v./n.","哄然大笑","Robert’s laugh"),("brusquely","/ˈbrʌskli/","adv.","粗率生硬地","Joffrey’s order"),("rasp","/ræsp/","v.","用粗哑声说","Sandor"),("gaunt","/ɡɔːnt/","adj.","瘦削憔悴的","face"),("fissure","/ˈfɪʃər/","n.","裂缝","scar tissue"),("sear","/sɪr/","v.","烧灼","burned flesh"),("brazier","/ˈbreɪziər/","n.","火盆","childhood attack"),("anoint","/əˈnɔɪnt/","v.","以油涂抹并祝圣","knighting ritual"),("postern","/ˈpoʊstərn/","n.","城堡侧门；后门","Red Keep entry"),("brooding","/ˈbruːdɪŋ/","adj.","阴郁沉思的","Sandor’s eyes"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def extract_blocks():
    blocks = extract_range(273, 282, "SANSA", "CH29")
    # PDF page break splits “Freys of the Crossing” inside one paragraph.
    blocks[3]["text"] = str(blocks[3]["text"]) + " " + str(blocks[4]["text"])
    blocks[3]["end_page"] = blocks[4]["end_page"]
    del blocks[4]
    for order, block in enumerate(blocks, 1):
        block["order"] = order
        block["id"] = f"CH29-P{int(block['page']):03d}-{order:03d}"
    return blocks

def main():
    blocks = extract_blocks()
    write_chapter(
        out=OUT, chapter=29, pov="SANSA", page_start=273, page_end=282,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Sansa的审美滤镜、tourney礼仪、court表演与Sandor对knighthood的质疑。",
        vocab=VOCAB,
        guide="Sansa第一次亲见Hand’s tourney，黄色薄纱、闪亮铠甲、名门骑士与Loras的红玫瑰使现实仿佛胜过歌谣。然而一名年轻骑士死在她面前，血迹被土盖住后比赛照常继续。夜宴上Joffrey用完美礼仪重新赢得她的信任，Robert醉酒失控又让盛景破裂。回城路上，Sandor拒绝Ser称号，指控Gregor故意在赛场杀人，并讲出自己童年被兄长按进炭火、而Gregor后来仍获册封的经历。Sansa第一次用“true knight”概念批判拥有正式称号的人，但Sandor的护送、坦白与最后的死亡威胁仍然并存，现实没有变成另一则简单歌谣。",
        people=[
            ("Sansa Stark","本章视角；从tourney陶醉进入对knighthood与外表的第一次实质动摇"),
            ("Sandor Clegane","Joffrey护卫，拒绝knight称号；讲述被Gregor烧伤的童年经历"),
            ("Gregor Clegane","tourney强者；杀死年轻knight，并被Sandor指控故意利用护甲弱点"),
            ("Loras Tyrell","十六岁的Knight of Flowers，以竞技胜利、花甲与赠玫瑰俘获观众"),
            ("Joffrey Baratheon","feast上对Sansa极尽courtesy，随后让Sandor代为护送"),
            ("Robert Baratheon","醉酒后公开宣布参加melee，羞辱Cersei与Jaime"),
            ("Petyr Baelish","认出Sansa的Tully相貌，以Catelyn旧日记忆接近并触摸她头发"),
            ("Septa Mordane / Jeyne Poole","Sansa同伴；Jeyne因死亡崩溃，Septa在feast醉倒"),
        ],
        terms=[
            ("joust / lists","骑士持长枪沿赛道相向冲刺的竞技；lists也指比赛场地"),
            ("gorget","保护颈部与喉部的甲片；未固定妥当会形成致命缺口"),
            ("Knight of Flowers","Loras称号，结合花饰铠甲、玫瑰马衣与公开赠花形象"),
            ("true knight","Sansa原本把美貌礼仪与骑士德性合一；本章开始用于区分称号和行为"),
            ("seven oils","Faith of the Seven册封knight时使用的祝圣油，仪式不能保证受封者道德"),
        ],
        synthesis="Chapter 29先让Sansa的世界成为gold，再逐层撤去光线。她通过songs认识knights，因此容易把漂亮armor、gallantry和道德善良视为同一件事；Loras和Joffrey都熟练满足这种期待。年轻knight之死却没有song，只有盖血的土。Sandor进一步提出最尖锐的反例：Gregor拥有Ser称号、由Rhaegar亲自册封，却曾残害幼弟，也可能故意杀死装备不足的对手；Sandor没有称号且粗暴恐吓，却确实护送Sansa安全回房。小说没有要求Sansa立刻抛弃true knight理想，而是让她第一次把理想变成衡量现实的标准——“He was no true knight”不再是赞美外表，而是对制度失灵的判断。",
        contrasts=[
            "**golden silk／night darkness：** 前半章由金色滤镜组织，后半章在熄灭火把后听见创伤。",
            "**songs／无名死者：** 英雄被反复歌唱，年轻knight却会随血迹一同被覆盖。",
            "**beautiful armor／实际行为：** Loras的形象与技艺高度统一，Gregor的正式荣耀却遮不住暴行。",
            "**Joffrey courtesy／过往 cruelty：** 一晚礼貌被Sansa用来重写Lady事件责任。",
            "**Ser Gregor／非Ser Sandor：** 有称号者可能残酷，无称号者既能保护也能威胁。",
            "**害怕Sandor／为Sandor害怕：** 同一介词变化标志Sansa从自我防卫转向同情。",
        ],
        questions=[
            "Sandor关于Gregor故意杀死年轻knight的判断能否得到其他证据？",
            "Sansa会如何保存或使用Sandor要求她保守的秘密？",
            "Joffrey一夜的courtesy能否持续，还是只在特定场合出现？",
            "Robert坚持参加melee会怎样影响次日赛事与court关系？",
        ],
        extraction_notes="PDF pp.273–282校勘后共65段；自动提取曾把pp.273–274间同一段中的“Freys of the Crossing”误切为两段，已合并。共6处跨页续段：pp.273–274、274–275、275–276、276–277、280–281与281–282。",
    )
    print(f"Wrote Chapter 29 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
