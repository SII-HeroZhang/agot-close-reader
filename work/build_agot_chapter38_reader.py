#!/usr/bin/env python3
"""Build Chapter 38 (TYRION) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter37_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"Mord拿着油豆问Tyrion是否要吃。",2:"Tyrion饥饿却不肯示弱，故意点出一整套丰盛餐食。",3:"Mord只重复说这是beans并递出盘子。",4:"Tyrion评估Mord粗暴、愚钝而可预测，仍因饥饿伸手。",5:"Mord把盘子移到他够不到的地方取乐。",6:"Tyrion忍痛站起，厌恶每餐都重复这种羞辱游戏。",7:"Mord退到sky cell边缘诱他靠近取食。",8:"Tyrion怕被推下去，宁愿宣称不饿也不冒险。",9:"Mord把beans扔下悬崖并大笑。",10:"Tyrion愤怒咒骂Mord染病而死。",11:"Mord踢伤他离开；Tyrion痛中仍威胁亲手杀他。",12:"Tyrion反省自己的大嘴，缩在薄毯下想念被Mord夺走的shadowskin cloak。",13:"sky cell没有外墙，风寒如爪；他宁愿要Casterly Rock最阴湿的地牢。",14:"Mord曾预言他被关若干天后会飞下去。",15:"Tyrion曾趴到边缘确认六百英尺落差，把自己比作被拔翼的蜂。",16:"倾斜地面令他不敢睡，解释sky cells为何使人发疯。",17:"墙上疑似血写的旧留言说blue正在召唤；Tyrion不愿知道前囚犯结局。",18:"他再次懊悔没有闭嘴。",19:"回忆中，六岁的Robert在Eyrie王座上问Tyrion是否坏人。",20:"Lysa当众回答是。",21:"Robert因Tyrion矮小而发笑。",22:"Lysa公开指控Tyrion杀死Jon Arryn。",23:"Tyrion以讥讽反问自己是否连这件事也做了。",24:"他明知沉默屈服才是最佳防御，却面对Vale全无友军。",25:"登山时被Bronn背负的羞耻加剧怒火，使他继续讽刺自己过分忙于杀人。",26:"他本应记得Lysa母子受不了针对自己的机智。",27:"Lysa警告他礼貌说话，并以Vale knights的忠诚压制他。",28:"Tyrion用Jaime会报复作为反威胁，出口即知愚蠢。",29:"Lysa以dwarf能否飞反击，叫他吞下下一句威胁。",30:"Tyrion坚持那不是threat而是promise。",31:"Robert惊恐发作，要求Mother保证无人能伤害他们。",32:"Lysa拥住Robert，宣称Eyrie不可攻破、Lannisters全是liars。",33:"Tyrion根据艰难山路承认Eyrie确实几乎无法强攻。",34:"他仍忍不住说这里只是inconvenient，不是impregnable。",35:"Robert要求看他fly，guards抓住Tyrion。",36:"Catelyn及时主张Tyrion是自己的prisoner，不准Lysa伤害。",37:"Lysa让guards放开，却任他们把Tyrion摔倒。",38:"Tyrion腿抽搐再次倒地，满堂哄笑。",39:"Lysa以休息为名命Ser Vardis把他送入sky cell。",40:"Tyrion被架走时羞怒地说会记住这一切。",41:"他确实记得，却暂时毫无用处。",42:"起初Tyrion相信关押只是羞辱，且Lannister身份和war风险能保命。",43:"现在他不再确定。",44:"饥饿、寒冷和Mord殴打正在削弱他，blue也可能开始召唤。",45:"他推演Tywin、Jaime、Cersei、Robert与Eddard可能采取的行动，却不知道外界是否知其位置。",46:"他认为Cersei若冷静应要求king亲审；Starks缺乏证据，公开trial对自己有利。",47:"但他判断Cersei受pride蒙蔽，Jaime更习惯用剑斩结而非解结。",48:"Tyrion思考是谁派footpad刺杀Bran，并把精巧的Jon Arryn之死与笨拙袭童案对比。",49:"他怀疑还有第三方在利用direwolf与lion冲突，把自己当catspaw。",50:"因此必须尽快逃出；既无力制服Mord也无绳可逃，只能靠嘴。",51:"Tyrion忍住斜坡恐惧，持续敲门召来Mord。",52:"Mord带着皮带怒气冲冲出现。",53:"Tyrion压住恐惧，直接问Mord想不想发财。",54:"Mord用皮带打他并命他闭嘴。",55:"Tyrion边挨打边重复Casterly Rock的gold诱惑。",56:"重击把他打到悬崖边，手指摸空后才意识到差点坠落。",57:"Mord用皮带响声继续恐吓。",58:"Tyrion赌Catelyn要他活着，以Lord Mord和土地女人马匹继续描画报酬。",59:"Mord质疑这里根本没有gold。",60:"Tyrion察觉他已在听，解释钱袋仍属自己，只需Mord送一条message。",61:"Mord第一次认真咀嚼message这个概念。",62:"Tyrion灵机一动，要Mord告诉Lysa自己愿意confess。",63:"Mord在greed与疑心间犹豫，怕被欺骗。",64:"Tyrion承诺把gold promise写下来。",65:"Mord把writing视作近乎magic，终于降低皮带。",66:"Tyrion夸大Jaime盔甲为纯金，进一步强化财富想象。",67:"Mord最终取来纸墨并送信。",68:"深夜Ser Vardis来sky cell唤醒Tyrion见Lysa。",69:"Tyrion故作不情愿，以恢复谈判姿态。",70:"Ser Vardis不理会他的意愿，命他自行起身否则被抬走。",71:"Tyrion顺势要求Mord归还shadowskin cloak御寒。",72:"Mord怀疑地看着他。",73:"Tyrion把被夺取的cloak委婉说成代为保管。",74:"Ser Vardis命Mord拿来cloak。",75:"Mord只得服从；Tyrion取回财物与温暖，并以含蓄话语警告自己会记住他。",76:"High Hall灯火通明，Lysa穿mourning black准备听confession，Robert不在场。",77:"Tyrion确认Vale主要家族被召集为观众，正中计划。",78:"Catelyn一行也在；Marillion有新harp，正适合把事件传播出去。",79:"Bronn在后方靠柱观望，手放剑柄；Tyrion开始计算可能性。",80:"Catelyn先问他是否要confess。",81:"Tyrion确认。",82:"Lysa炫耀sky cells总能击溃囚犯。",83:"Catelyn指出Tyrion看起来并未崩溃。",84:"Lysa命Tyrion开口。",85:"Tyrion以真实但无关的个人恶习作夸张自白，把审判变成喜剧并引发笑声。",86:"Lysa羞怒打断，质问他在做什么。",87:"Tyrion装作无辜地说自己正confessing。",88:"Catelyn明确列出刺杀Bran与谋杀Jon Arryn两项指控。",89:"Tyrion拒绝承认自己不知道的murders。",90:"Lysa认为受辱，命把他送回更危险的cell。",91:"Tyrion突然高声诉诸Vale honor、king’s justice和公开trial，并展示脸上伤痕。",92:"厅内议论；Tyrion知道其高贵身份使Lysa难以拒绝trial。",93:"Lysa接受审判，却以Moon Door作为死刑威胁。",94:"guards打开Moon Door，夜空与狂风进入hall。",95:"Lysa称这就是king’s justice，火炬在风中摇灭。",96:"Catelyn认为此举不明智。",97:"Lysa仍提出由Robert听审，再决定Tyrion从哪扇门离开。",98:"Tyrion看穿Robert作judge必受Lysa控制，也想起孩子想看他fly。",99:"他绕过人审，依法要求trial by combat让gods裁决。",100:"众人因Tyrion身体条件而哄笑，连风声都像嘲弄。",101:"Lysa措手不及，却承认他确有此权。",102:"一名green viper knight抢先请求为Lysa出战。",103:"Lord Hunter也以爱Jon Arryn为由请战。",104:"Ser Albar以家族侍奉Arryn为由请战。",105:"Ser Lyn Corbray把正义与最强剑手巧妙并置，自荐为champion。",106:"多人争相杀他，使Tyrion一度怀疑计划是否聪明。",107:"Lysa最终指定沉默的Ser Vardis为己方champion。",108:"Ser Vardis认为屠杀矮小跛足的Tyrion有辱justice，请她另选。",109:"Tyrion立即赞同。",110:"Lysa提醒是他自己要求trial by combat。",111:"Tyrion主张自己也有权选champion，点名Jaime。",112:"Lysa指出Jaime远在数百league之外。",113:"Tyrion建议送raven，并愿意等。",114:"Lysa命他次日就对战Ser Vardis。",115:"Tyrion转向Marillion，预演一首传播Lysa剥夺残疾囚犯champion权的ballad。",116:"Lysa受公共名誉压力，怒允他自行寻找champion。",117:"Tyrion说要找替自己杀人的人；全场沉默令他以为豪赌失败。",118:"Bronn最终从厅后宣布愿为Tyrion出战。",
}
SUMMARIES = [S[i] for i in range(1,119)]

KEY_NOTES = {
2:"精致菜单不是认真点餐，而是以语言保住身份感；身体被控制时，他先控制谈话的风格。",
7:"食物被放到edge外，把最基本需求变成服从与冒险测试；Mord的娱乐建立在身体差异上。",
8:"Tyrion拒绝靠近不是怯懦，而是正确识别对方可用一个shove制造‘escape’假象。",
12:"big mouth既是自我批评也是全章结构线索：同一张嘴先致祸，后成为唯一逃生工具。",
15:"bee in a stone honeycomb却无wings，把Eyrie建筑秩序写成专为坠落而设计的自然陷阱。",
16:"倾斜几乎不可见，却持续剥夺睡眠；sky cell通过环境而非正式刑讯击溃人。",
17:"the blue is calling把天空由自由象征改写为自杀诱惑，颜色本身获得主动声音。",
19:"looked down on同时是空间动作与Tyrion一生承受的社会姿态，双关把Robert的高座变成旧伤。",
24:"他清楚最佳策略却做不到，说明聪明不等于能在羞耻与愤怒中执行最佳判断。",
25:"Bronn背他本是帮助，Tyrion却因长期被羞辱而体验为身份受损，怒气遂误投向庭审。",
28:"Jaime的威名在远处不能立即保护他，反而给Lysa一个公开展示无惧Lannister的机会。",
31:"Robert的twitch显示威胁触发异常强烈的恐惧；Lysa的安慰同时继续灌输绝对安全与敌我叙事。",
34:"merely inconvenient是机智也是失控：逻辑上细微修正，政治上却再次刺伤主人自尊。",
36:"Catelyn以prisoner ownership阻止即时伤害，而不是在此宣布Tyrion无罪。",
38:"大厅笑声把身体疼痛变成公共娱乐，解释Tyrion为何更依赖讽刺反夺观众控制。",
41:"短句用冷幽默切回现实：记忆能保存债务，却不能自动转化为权力。",
45:"一连串问句展示他以政治模拟抵抗信息隔绝；每条推演都受‘无人知位置’这个关键不确定性限制。",
47:"untied a knot / slash it in two是Tyrion对Jaime决策风格的凝练比喻：即时行动可能破坏更大结构。",
48:"他首次把两案的作案风格作比较；clumsy与subtle不匹配，是怀疑共同凶手叙事的重要逻辑裂缝。",
49:"catspaw既指被利用的人，也回扣袭击Bran的凶器与执行者；Tyrion怀疑自己被安排成替罪对象。",
50:"mouth从缺陷改为resource，章法由自责转向主动设计。",
53:"Never show them fear不是无恐惧，而是在恐惧存在时选择Mord能理解的欲望入口。",
56:"他几乎因自己的谈判招来坠落；语言策略并不神奇，必须承受真实身体成本。",
58:"Lord Mord是有意夸张的身份诱饵：Tyrion把自己熟悉的等级欲望翻译给看守。",
60:"Mord半心半意挥带说明gold已改变暴力节奏；Tyrion用这个细节判断谈判窗口打开。",
62:"confess是完美message，因为它同时满足Lysa的确信、公开欲和道德优越感。",
65:"writing对Mord具有制度与魔法双重权威；Tyrion利用文化差异让口头承诺变得可信。",
69:"故作不愿见Lysa是在guards面前掩盖主动求见，防止对方意识到自己正按Tyrion计划行动。",
73:"for safekeeping用礼貌词包装盗取，让Ser Vardis能在不审理争议的情况下顺手纠正它。",
75:"取回cloak是小型胜利：他借更高层命令迫使Mord归还物品，也重新建立体面外观。",
77:"confession的真正对象不只是Lysa，而是整个Vale公共圈；程序能否被扭曲取决于是否有人见证。",
78:"Marillion把现场变成未来舆论场；Tyrion不需控制每个knight，只需让故事能离开Eyrie。",
79:"对Bronn的长注视是无声试探；文本暂不说明两人是否已有明确约定。",
82:"Lysa把sky cell效果归于gods可见，借宗教语言遮蔽饥饿、寒冷、斜坡与殴打这些人造压力。",
85:"Tyrion的内容大多真实，却不响应指控；他利用confession一词的宽泛含义揭露Lysa只想要承认而非调查。",
88:"Catelyn把表演重新锚定具体charges，这也第一次让公开观众听清案件范围。",
91:"Tyrion把私人受虐转译成king’s justice问题，并展示bruises作为视觉证据，迫使旁观贵族考虑自身制度名誉。",
93:"Lysa表面接受trial，立即以处刑装置预定结论；程序形式与裁决控制仍在同一人手中。",
94:"Moon Door把‘open court’字面化为致命开口；冷星与风让自然景观成为权力剧场。",
97:"one door or the other是精心包装的假选择：正常离开与坠落被描述成同一审判的两个出口。",
99:"trial by combat把裁决者从Robert移到gods/武力，并调用Lysa不能公开否认的贵族法律传统。",
100:"笑声准确指出Tyrion若亲战的身体劣势，却也使众人低估他可要求champion的下一步。",
101:"Lysa的uncertain表明她熟悉权利存在，却没预见Tyrion会把它用于改变审判结构。",
105:"Ser Lyn的话把神意与剑术悄然等同，揭示trial by combat如何把‘truth’交给战斗能力。",
106:"Tyrion并非全知布局者；当champions争抢时，他也真实感到策略可能失控。",
108:"Ser Vardis的拒绝不是支持Tyrion无罪，而是担心明显不对等的屠杀玷污knightly honor与justice之名。",
111:"Tyrion借Lysa已选champion这一先例主张对称权利；Jaime既是理想战力，也是拖延时间的工具。",
115:"他不直接争法条，而是把未来ballad写进当前现场，以声誉成本逼Lysa兑现公平外观。",
116:"Lysa说I deny you nothing，证明公开羞辱叙事已迫使她改口；观众和singer共同构成约束。",
117:"kill for me把浪漫的die for you改成雇佣逻辑，准确预示Tyrion寻找的不是忠臣而是利益一致者。",
118:"Bronn从rear发声回应此前Tyrion的目光；他选择的是高风险机会，而非公开宣誓私人爱戴。",
}

STAGES = [
(1,18,"Mord以食物和暴力折磨Tyrion；sky cell的风、斜坡与高度持续侵蚀身体和睡眠，他反复后悔自己的嘴。"),
(19,41,"回忆抵达Eyrie后的公开冲突：Tyrion因羞耻与怒气不断讥讽Lysa母子，终于被送入sky cell。"),
(42,50,"Tyrion推演外界反应并比较两桩案件的手法，怀疑有人利用Stark–Lannister冲突，决定靠谈话逃生。"),
(51,67,"他承受Mord殴打，以gold、writing和confession逐步让看守送信。"),
(68,84,"Tyrion被带回High Hall，取回cloak并确认Vale nobles、Marillion和Bronn都在场，为公开表演搭好舞台。"),
(85,99,"假confession激怒Lysa后，Tyrion诉诸公开justice取得trial，再以trial by combat避开Robert控制的裁决。"),
(100,118,"Vale knights争当Lysa champion；Tyrion借champion对称权和ballad声誉逼她让步，最终由Bronn应战。"),
]

BACKGROUNDS = {
4:"**turnkey：** 负责钥匙与牢门的看守；Mord掌握Tyrion的食物、衣物和出入，却仍受Lysa与Ser Vardis命令约束。",
13:"**sky cell：** Eyrie临悬崖的开放牢房，无外墙且地板向外倾斜，以寒风、失眠和坠落恐惧逼迫囚犯。",
15:"**Sky：** Eyrie下方的中继城堡，距sky cells约六百英尺；并非抽象天空名称。",
19:"**Robert Arryn：** Jon Arryn与Lysa的六岁儿子、Lord of the Eyrie；身体与情绪状态脆弱，由Lysa强力保护。",
22:"**两项指控：** Lysa指Tyrion谋杀Jon Arryn；Catelyn另认为他的dagger与袭击Bran有关。此时尚无公开审理证据。",
33:"**Eyrie防御：** 城堡位于高山顶，通路狭窄陡峭；进攻者须沿多重山门攀升，因此历史上从未被攻陷。",
45:"**可能反应：** Tywin、Jaime、Cersei、Robert和Eddard各有政治能力，但Tyrion不知道消息是否已传出Vale。",
48:"**文本事实／推断：** Tyrion承认不知道两案真相；他只从作案手法差异推断可能有别的操盘者。",
62:"**confession：** Tyrion承诺的是‘承认我的罪’，没有明确承诺承认Lysa指定的两项murder charge。",
77:"**Vale houses：** Royce、Corbray、Hunter、Waynwood等主要贵族在场，使这次会面具有公开政治见证性质。",
91:"**king’s justice：** Vale属于Seven Kingdoms，贵族囚犯可要求正式审理；Tyrion用王国共同规范挑战Lysa私人处置。",
93:"**Moon Door：** High Hall外墙上的门，门外直接是高空；Eyrie以此执行坠落死刑。",
99:"**trial by combat：** 被告要求由单斗让gods显示正当一方的审判方式；贵族法律承认此项权利。",
102:"**champion：** 当事人可由代理战士出战。Lysa先选择己方champion，也给Tyrion主张同等选择留下程序空间。",
107:"**Ser Vardis Egen：** Jon Arryn生前household guard captain，现为Lysa服务；经验丰富，但对明显不对等决斗感到羞耻。",
118:"**Bronn：** 陪Tyrion上山的freerider，无家臣誓言；截至本段，他只公开承诺在决斗中代表Tyrion。",
}

EXTRA_VOCAB = [
("turnkey","/ˈtɜːrnkiː/","n.","狱卒；掌钥匙的看守","Mord"),("glower","/ˈɡlaʊər/","v.","怒目而视","Mord"),("flagon","/ˈflæɡən/","n.","大酒壶；一壶","mulled wine"),("mulled wine","/mʌld waɪn/","n.","加香料温热葡萄酒","meal fantasy"),("stone","/stoʊn/","n.","英石，约6.35公斤","twenty stone"),("turnkey","/ˈtɜːrnkiː/","n.","狱卒","jailer"),("shamble","/ˈʃæmbəl/","v.","蹒跚拖步","Mord"),("pox-ridden","/ˈpɑːks ˌrɪdən/","adj.","染满痘病的；恶毒辱骂","curse"),("bloody flux","/ˌblʌdi ˈflʌks/","n.","血痢","curse"),("shadowskin","/ˈʃædoʊskɪn/","n.","影子山猫皮毛","cloak"),("talon","/ˈtælən/","n.","猛禽爪","wind simile"),("dank","/dæŋk/","adj.","阴湿的","dungeon"),("gird up","/ɡɜːrd ʌp/","v.","鼓起；做好准备","courage"),("crane","/kreɪn/","v.","伸长脖子","look down"),("rheumy","/ˈruːmi/","adj.","眼睛水汪浑浊的","Robert’s eyes"),("austere","/ɔːˈstɪr/","adj.","冷峻朴素的","High Hall"),("falter","/ˈfɔːltər/","v.","蹒跚；支撑不住","climb"),("impregnable","/ɪmˈpreɡnəbəl/","adj.","坚不可摧的","Eyrie"),("impugn","/ɪmˈpjuːn/","v.","质疑；攻击名誉","king’s honor"),("headstrong","/ˈhedstrɔːŋ/","adj.","任性冲动的","Jaime"),("footpad","/ˈfʊtpæd/","n.","拦路盗匪；受雇袭击者","Bran attacker"),("catspaw","/ˈkætspɔː/","n.","被人利用的工具或替罪羊","Tyrion’s suspicion"),("purchase","/ˈpɜːrtʃəs/","n.","支点；抓力","push himself up"),("desultory","/ˈdesəltɔːri/","adj.","漫不经心的","strap swing"),("illiterate","/ɪˈlɪtərət/","n.","文盲者","writing"),("reverence","/ˈrevərəns/","n.","敬畏","written word"),("gilded","/ˈɡɪldɪd/","adj.","镀金的","Jaime’s armor"),("retainer","/rɪˈteɪnər/","n.","家臣；侍从","Vale court"),("side-whiskers","/ˈsaɪd ˌwɪskərz/","n.","络腮胡侧鬓","Ser Albar"),("gouty","/ˈɡaʊti/","adj.","患痛风的","Lord Hunter"),("sconce","/skɑːns/","n.","墙上烛台","torches"),("jape","/dʒeɪp/","n.","玩笑；戏弄（古风）","mock confession"),("petulant","/ˈpetʃələnt/","adj.","任性恼怒的","Lysa smile"),("pennon","/ˈpenən/","n.","狭长三角旗","torch flames"),("skirl","/skɜːrl/","v.","发出尖锐盘旋声","wind"),("derision","/dɪˈrɪʒən/","n.","嘲笑","hall laughter"),("boon","/buːn/","n.","恩准；请求赐予之事","championing"),("clamor","/ˈklæmər/","v.","吵嚷争取","knights"),("peeved","/piːvd/","adj.","恼怒的","Lysa"),("colossal","/kəˈlɑːsəl/","adj.","巨大的","blunder"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def main():
    blocks = extract_range(376,387,"TYRION","CH38")
    write_chapter(
        out=OUT, chapter=38, pov="TYRION", page_start=376, page_end=387,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在sky cell的心理压力、Tyrion的语言策略、Vale公开司法与trial by combat。",
        vocab=VOCAB,
        guide="Tyrion被关进Eyrie的sky cell后，食物、睡眠、保暖和身体安全都掌握在Mord手中。最初让他入狱的讥讽仍不断从记忆中回来，但他逐渐把‘big mouth’从缺陷转成唯一工具：先用gold与writing说服Mord传递confession，再确保Vale nobles、Marillion与Bronn共同见证。所谓confession刻意承认真实却无关的恶习，迫使Lysa公开说出具体指控；当她仍想把否认者送回牢房时，Tyrion诉诸king’s justice取得trial，随后要求trial by combat绕开Robert受控的裁决。最后，他又借champion权利与未来ballad施加声誉压力，逼Lysa允许他找代理战士，Bronn在全场沉默后应战。",
        people=[
            ("Tyrion Lannister","本章视角；在sky cell中把语言、法律程序和公共舆论转成逃生资源"),
            ("Mord","Eyrie turnkey，以食物、皮带和悬崖折磨Tyrion，也被gold promise说动"),
            ("Lysa Arryn","Lady of the Eyrie，确信Tyrion有罪并控制Robert的审判环境"),
            ("Robert Arryn","六岁Lord of the Eyrie；Lysa拟让他作为judge裁决Tyrion"),
            ("Catelyn Stark","Tyrion的原始捕获者；阻止即时处刑并明确两项指控"),
            ("Ser Vardis Egen","前Hand household guard captain，Lysa指定的trial champion"),
            ("Bronn","freerider；旁观Tyrion布局，最终自愿担任其champion"),
            ("Marillion","singer；作为在场传播者，使Eyrie的做法可能成为跨地域故事"),
        ],
        terms=[
            ("sky cell","Eyrie临高空且向外倾斜的开放牢房，以寒冷、失眠与坠落恐惧施压"),
            ("Moon Door","High Hall直通高空的处刑门，象征Lysa控制下的‘king’s justice’"),
            ("trial by combat","以单斗请求gods裁定正当一方的法律程序"),
            ("champion","替当事人参加trial by combat的代理战士"),
            ("catspaw","被第三方利用来承担风险、转移嫌疑或引发冲突的人"),
        ],
        synthesis="本章不是简单展示Tyrion‘能说会道’，而是逐步拆解语言何时有效。面对Mord，讽刺只会招来殴打，必须换成对方能理解的gold、lordship与writing；面对Lysa，私人辩解无效，必须制造公开观众并调用她声称尊重的justice；面对完整的Vale court，法条本身仍可能被操控，于是Marillion能够传播的ballad成为额外约束。Tyrion每一步都承受真实失败风险，也数次误判或失控。最终Bronn出声，不是奇迹式忠诚，而是Tyrion成功创造了一个让利益型行动者愿意下注的公开机会。",
        contrasts=[
            "**blue sky／dungeon darkness：** 通常代表自由的天空，在sky cell里变成持续召唤死亡的空缺。",
            "**big mouth致祸／mouth救命：** 能力的价值取决于是否根据听众改变表达方式。",
            "**confession内容真实／程序目的误导：** Tyrion承认恶习，却拒绝让‘认罪’自动等于承认两桩murder。",
            "**private power／public witness：** Lysa能控制牢房与Robert，旁观贵族、singer和共同法律则提高滥权成本。",
            "**king’s justice／Moon Door：** 共同王法的语言被Lysa与预设处刑并置，暴露程序外壳。",
            "**die for you／kill for me：** Tyrion不要求忠诚牺牲，而寻找与自己短期利益一致的专业暴力。",
        ],
        questions=[
            "Tyrion关于第三方catspaw的怀疑是否正确，谁可能从Stark与Lannister冲突中获益？",
            "Bronn为何愿意接受明显危险的trial by combat，他期待什么回报？",
            "Ser Vardis虽反感不公平屠杀，是否会在决斗中完全服从Lysa？",
            "公开见证和Marillion的传播能力，究竟能在多大程度上约束Eyrie权力？",
        ],
        extraction_notes="PDF pp.376–387校勘后共118段；共8处跨页续段：pp.376–377、377–378、378–379、379–380、380–381、381–382、383–384与385–386。段落边界、引号、专名与顺序均已复核，无额外人工合并。PDF p.382源页本身印作Lysa Anyn，按原文保留。",
    )
    print(f"Wrote Chapter 38 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
