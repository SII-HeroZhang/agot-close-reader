#!/usr/bin/env python3
"""Build Chapter 10 (JON) close-reading Markdown."""

from pathlib import Path

from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter9_reader import VOCAB as BASE_VOCAB


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "Jon缓慢爬上通往Bran病房的楼梯，不愿想这可能是永久的最后一次；Ghost静静随行，城外离行队伍已在雪中准备。",
    "Jon在门前因害怕停留，Ghost用鼻子碰他的手给予勇气，他才挺直身体进房。",
    "Catelyn近两周昼夜守在Bran床边，几乎不吃不睡；Jon一直不敢前来，正是因为她从未离开。",
    "离行在即，Jon已经没有继续等待Catelyn离开的时间。",
    "Jon留在门边不敢开口或靠近；开着的窗外传来狼嚎，Ghost也抬起头。",
    "Catelyn仿佛一时认不出Jon，随后用奇异平坦、没有感情的声音问他为何来此。",
    "Jon说自己是来看Bran、向他告别的。",
    "Catelyn容貌憔悴，像老了二十岁；她冷淡地说Jon已经告过别，可以走了。",
    "Jon的一部分只想逃离，却怕今后再也见不到Bran，因而紧张地走进房间并说“求你”。",
    "Catelyn眼中变冷，再次命令Jon离开，还说“我们”不要他在这里。",
    "过去这句话会让Jon逃跑甚至哭泣，如今却使他愤怒；他用即将成为Night’s Watch弟兄的身份鼓励自己面对Catelyn。",
    "Catelyn威胁要叫守卫把Jon赶走。",
    "Jon倔强地让她尽管叫人，并绕到床的另一边俯看Bran，使床成为他与Catelyn之间的屏障。",
    "Catelyn握着Bran像爪子一样的手；Jon几乎认不出这个消瘦、骨头突出、胸口受伤的弟弟。",
    "即使肋骨粉碎、身体衰弱，Bran的胸膛仍随着浅呼吸起伏。",
    "Jon流着泪向Bran承认自己之前害怕过来，求他不要死，因为所有人都在等他醒来。",
    "Catelyn没有出声制止，Jon把沉默当成默认；窗外那只Bran还来不及命名的direwolf再次嚎叫。",
    "Jon说自己必须走了，Benjen正等着带他去Wall，必须赶在大雪前出发；他想起Bran曾对南下旅程多么兴奋。",
    "Catelyn轻声说，她原本希望Bran留在Winterfell陪自己。",
    "Jon警惕地观察她，发现她虽在对自己说话，却像根本没看见他。",
    "Catelyn说Bran是她特别疼爱的孩子，她曾在sept中向七神反复祈祷，希望Eddard改变主意、把Bran留下。",
    "Jon不知如何回应，沉默后只能说Bran的意外不是她的错。",
    "Catelyn忽然用充满毒意的目光盯住Jon，说自己不需要一个bastard的宽恕。",
    "Jon低下眼睛，在Catelyn抱着Bran一只手时握住另一只，感受那像鸟骨般的细弱手指，向他告别。",
    "Jon走到门口时Catelyn突然叫他的名字；她从未这样称呼他，所以他停下回头。",
    "Jon回应她的呼唤，等待她继续。",
    "Catelyn告诉Jon，坠落的本该是他；随后她转回Bran身边，全身颤抖地哭泣，这是Jon第一次见她落泪。",
    "受到重创的Jon走下楼、前往院子的路显得异常漫长。",
    "户外正在装车、套马和整队，人声鼎沸；细雪落在所有人身上，两支队伍即将走向不同方向。",
    "Robb站在混乱中发号施令，Bran坠落和Catelyn崩溃似乎迫他迅速长大；Grey Wind伴在他身边。",
    "Robb告诉Jon，Benjen一小时前就想出发，正在到处找他。",
    "Jon说自己知道，但还需要一点时间；真正离开比他预想得更难。",
    "Robb说对自己也一样，随后询问Jon是否已经见过Bran。",
    "Jon点头，但情绪让他不敢开口。",
    "Robb坚信Bran不会死，并说自己就是知道。",
    "Jon用“Starks很难被杀死”表示赞同，但他的声音平坦疲惫，病房探视已耗尽力量。",
    "Robb察觉Jon不对劲，试探着提起自己的Mother。",
    "Jon迟疑地说Catelyn对他“非常和善”，用谎言保护Robb。",
    "Robb明显松了一口气，笑着说下次见到Jon时，他就会全身黑衣。",
    "Jon强迫自己回以笑容，自嘲黑色本就适合自己，又问他们要多久才能重逢。",
    "Robb承诺不会太久，用力拥抱Jon，并以姓氏Snow向他告别。",
    "Jon也抱紧Robb，用Stark回应，并托他照顾好Bran。",
    "Robb答应后，两人分开并尴尬对视；他最后再次提醒Jon去马厩找Benjen。",
    "Jon说自己还有最后一个人需要告别。",
    "Robb默契地说那么自己没有见过Jon，让他继续拖延；Jon先去armory取上早已准备的包裹。",
    "Arya在房中收拾一只比她还大的ironwood箱子，Nymeria把她指出的衣服衔进箱子帮忙。",
    "Arya发现Jon后马上起身抱紧他，带着哽咽说自己害怕他已经离开。",
    "Jon被她的处境逗乐，问她这次又做了什么。",
    "Arya松开Jon并做鬼脸，声称自己没做什么，又指着只装了三分之一、周围衣物散乱的箱子证明自己已经收好。",
    "Jon亲昵地反问，这就是她所谓的收拾方法吗。",
    "Arya辩解说衣服反正总会乱，所以根本不必在意怎样叠。",
    "Jon提醒她Septa Mordane会在意，而且也不会喜欢Nymeria帮忙；但这正好给他带来的秘密礼物提供了理由。",
    "Arya听到礼物后立刻眼睛发亮。",
    "Jon说可以把它叫作礼物，但要求Arya先关门。",
    "Arya警惕又兴奋地查看走廊，命Nymeria在门外放哨；Jon则开始解开包裹的破布。",
    "Arya的深色眼睛像Jon一样瞠大，用一句轻声惊叹认出礼物是一把剑。",
    "Jon展示柔软灰皮剑鞘和深蓝光泽的钢刃，郑重警告这不是玩具，锋利到可以刮脸。",
    "Arya指出女孩不刮脸，从字面上拆解Jon的比喻。",
    "Jon回以玩笑，说女孩也许该刮，还问她是否看过septa的腿。",
    "Arya被逗笑，随即注意到剑身非常细。",
    "Jon说剑和Arya一样纤细，这是他让Mikken特制的；Free Cities的bravos使用类似武器，它不靠重砍断首，而靠速度和突刺取胜。",
    "Arya自信地说自己可以很快。",
    "Jon提醒她必须每天练习，将剑放到她手中、教她握法，并询问重心感受。",
    "Arya尚不确定如何判断剑的balance，只说自己大概喜欢。",
    "Jon给出第一课：用尖的那一端刺他们。",
    "Arya用剑脊拍打Jon的手臂，说自己当然知道用哪端；Jon虽被打疼却笑得像个傻子，Arya随后又担心Septa Mordane会没收它。",
    "Jon说只要Septa Mordane不知道，她就无法拿走剑。",
    "Arya问自己可以找谁一起练习。",
    "Jon承诺她会在庞大的King’s Landing找到人；在此之前，她应观察练武场、锻炼速度和平衡，并学会无声移动。",
    "Arya已经猜到Jon接下来会说的保密对象，两人同时开口。",
    "他们一起拉长语调说：不要告诉Sansa。",
    "Jon再次弄乱Arya的头发，坦白自己会想念这个小妹妹。",
    "Arya突然快要哭出来，说她希望Jon也能与他们一起南下。",
    "Jon用“不同道路也可能通向同一城堡”安慰她，不再允许自己悲伤，还开玩笑说会在Wall上冻掉笑容。",
    "Arya跑来做最后的拥抱，Jon笑着警告她先放下剑；她略带害羞地放好后，连续亲吻他。",
    "Jon在门口回头时看见Arya已再次拿起剑试重心，便提醒她所有最好的剑都有名字。",
    "Arya以Eddard的大剑Ice为例，急切追问自己的剑是否也有名字。",
    "Jon不直接告诉她，而是让她猜“你最喜欢的东西”。",
    "Arya起初困惑，随即迅速明白，两人再次同时说出答案。",
    "剑被命名为Needle，把Arya曾经受挫的女红工具转化成适合她的细剑。",
    "Jon北行的漫长路上，Arya当时的笑声一直给他带来温暖。",
]


KEY_NOTES = {
    1: "外面队伍已经向前移动，Jon却在楼梯上缓慢上行；外部时钟与内心拖延形成冲突。",
    2: "Ghost不说话，仅用碰手给予Jon勇气；direwolf在这里是情绪支撑，也是Jon无言的同伴。",
    3: "Catelyn不离开Bran是母爱的极端表现，却也客观上使Jon一直无法告别；同一行为对两人产生相反意义。",
    4: "七个单词的独立段落终止了Jon的逃避：不是恐惧消失，而是时间用尽。",
    6: "Catelyn的声音`flat and emotionless`并非平静，而是长期失眠、饥饿和悲痛后的感情耗竭。",
    10: "Catelyn用`we`把Bran也纳入“不要Jon”的主体，但Bran昏迷无法表态；语法上的包含加深了排斥。",
    11: "Jon借Night’s Watch的未来身份给当下自己撑胆；他尚未宣誓，却已在心理上使用那身黑衣。",
    13: "Jon把床留在自己和Catelyn之间，这既是物理自我保护，也是两人只能通过Bran建立关系的空间图像。",
    14: "“这不是他记忆中的Bran”把告别的两层损失合在一起：Jon既要离开，又已经失去那个健康活泼的弟弟。",
    15: "`frail cage`把破碎肋骨写成关住生命的脆弱笼子，浅呼吸是这幅静止图中唯一动作。",
    16: "Jon先承认恐惧，再请求Bran活下来；泪水不再令他感到羞耻，因为告别比保持体面更重要。",
    17: "Jon将Catelyn的沉默解释为接受，这是他当下需要的解读，但文本并未说Catelyn真正同意。",
    19: "Catelyn的“我希望他留下”将Bran的意外与她过去的愿望危险地相连，为下文的内疚与攻击打开缺口。",
    20: "Catelyn在语法上与Jon对话，感知上却穿过他；这种解离状态表现她正沉入自责而不是寻求交流。",
    21: "七次向七张神脸祈祷用数字重复强调Catelyn的虔诚和绝望；愿望意外“实现”后，她反而把它理解成可怕的责任。",
    22: "Jon说“不是你的错”是一种直觉安慰，但他无法看到Catelyn这时并不想从他这里得到宽恕。",
    23: "`absolution`本是宗教性的赦免，Catelyn用它将Jon的安慰扭成一种傲慢的审判，再用`bastard`把他压回社会身份。",
    25: "Catelyn首次以名字称呼Jon，短暂制造她终于看见他个人的希望；正因如此，下一句伤害更强。",
    27: "`It should have been you`把母亲的内疚转移到Jon身上；文本同时呈现Catelyn的崩溃和Jon受到的真实伤害，并不要求读者只选一方理解。",
    28: "极短的过渡段把空间距离变成心理重量：楼梯并未变长，Jon却被那句话拖住。",
    30: "Robb的“长大”不来自平稳成熟，而来自家庭危机迫他填补父母暂时空出的管理位置。",
    36: "Jon的话表面是坚强祝愿，`flat and tired`却向读者暴露他无法相信自己的语气。",
    38: "“她很和善”是明显的善意谎言；Jon拒绝把Catelyn的伤害转移给同样已在承受压力的Robb。",
    41: "Robb用`Snow`、Jon用`Stark`告别，表面是以姓氏互相调侃，实际上也坦然承认两人在法律身份上的差异。",
    45: "Robb说“那我就没见过你”，用一个小小谎言给Jon时间；这与Jon刚才为保护Robb而撒谎形成双向体谅。",
    46: "Nymeria用嘴衔衣服的“帮忙”必然使衣物更乱，但这幅喜剧画面迅速把章节从病房的死寂转入兄妹亲密。",
    47: "Arya的第一反应不是看礼物，而是抱住Jon；她与Catelyn不同，首先把Jon当作将要失去的亲人。",
    52: "Septa Mordane是此场秘密交付中未出场却持续存在的权威；剑必须隐藏，说明礼物同时越过了性别规范。",
    55: "Nymeria从包装助手转为门外哨兵，使一场家庭告别暂时具有密室仪式感。",
    56: "`Dark eyes, like his`在Arya看见剑的瞬间强调两人的外貌相似和亲缘认同；这是Jon正要送给最像自己的妹妹的东西。",
    57: "`supple as sin`让剑鞘的柔软带上禁忌吸引力；礼物对Arya有价值，正因它不是被允许的女孩玩具。",
    61: "Jon不是把Arya塞进传统重剑范式，而是按她的身材和速度制作武器；这与缝纫课用统一标准判定她失败形成对照。",
    63: "Jon没有只送一件物品，还给出握法、每日练习和重心的第一层教学，使礼物指向长期能力而非短暂新鲜。",
    65: "`Stick them with the pointy end`故意把剑术压缩成傻瓜都懂的常识，符合兄妹通过互相逗笑缓解离别情绪的方式。",
    66: "Arya立刻用剑脊回击，表明她不愿只是被教导的小孩；Jon的疼痛与傻笑显示他享受她的反驳。",
    69: "这些建议将练剑从找个人对打扩展为观察、奔跑、平衡和无声移动，暗合Arya本已具备的好动与敏捷。",
    71: "两人同时说“不要告诉Sansa”，共同节奏显示这不是第一次形成秘密联盟；Sansa在此是礼仪世界的代表。",
    74: "`Different roads sometimes lead to the same castle`既是安慰Arya，也是Jon对自己的希望；用旅行地理表达关系不一定因分道而终结。",
    75: "“先放下剑”是一个轻快实用的细节，它防止告别陷入纯粹伤感，也再次强调剑已经成为Arya身体的新延伸。",
    76: "Arya在Jon离开前已重新拿起剑试重心，这是她接受礼物最直接的证据：她想的不是展示，而是使用。",
    80: "`Needle`是一次语义夺回：原本象征Arya失败和羞辱的针，如今成为她自己选择的细剑名。",
    81: "末句从当场告别跳到北行途中的回忆，用“笑声带来温暖”对抗寒冷地理和Jon离家的孤独。",
}


STAGES = [
    (1, 17, "本段以Jon对Catelyn的恐惧和对Bran的爱形成拉扯；他借未来Night’s Watch身份坚持完成告别。"),
    (18, 28, "本段让Catelyn的内疚从祈祷回忆转成对Jon的攻击；两人都受到真实痛苦，但权力与身份并不对等。"),
    (29, 45, "本段从病房转到离行院子；Jon与Robb互相用善意谎言保护对方，再用姓氏玩笑承认分别。"),
    (46, 66, "本段用Arya与Nymeria的混乱收拾缓和气氛；Jon送出按Arya本人特点定制的细剑，并给出第一层训练建议。"),
    (67, 81, "本段围绕保密、练习、重逢愿望与命名展开；Needle将Arya的旧羞辱转化为兄妹共有的温暖记忆。"),
]


BACKGROUNDS = {
    3: "**文本事实：** Catelyn已在Bran床边守了近两周，从未离开；Jon因她在场而一直不敢前来。",
    11: "**当前可知设定：** Jon将随Benjen前往Wall并加入Night’s Watch；他此时尚未宣誓，`Sworn Brother`是他对即将获得的身份的想象。",
    17: "**文本事实：** Bran在坠落前仍未给direwolf命名；它当时持续守在窗外嚎叫。",
    21: "**宗教背景：** Catelyn信奉Faith of the Seven；sept是七神礼拜场所，七张神脸表示同一神性的不同面向。",
    23: "**词义与身份：** `absolution`是宽恕或赦免；Catelyn又以`bastard`称Jon，强调他婚外生子的社会身份。",
    29: "**文本事实：** 南下王室队伍与北上Wall的Night’s Watch队伍将在同一日离开Winterfell。",
    30: "**文本事实：** Eddard忙于Bran和南下安排，Catelyn无法离开病房；Robb正暂时承担院内组织指挥。",
    41: "**姓氏背景：** Jon作为北境贵族的bastard使用Snow，Robb作为trueborn继承人使用Stark；此处两人把法律区分变成亲密告别。",
    52: "**文本事实：** Septa Mordane负责Arya和Sansa的女红与礼仪教育；一把细剑显然不符合她对贵族女孩的常规训练安排。",
    55: "**文本事实：** Arya命Nymeria守在走廊上警戒来人，说明两人知道送剑必须保密。",
    61: "**武器背景：** Mikken按Jon要求特制了这把细剑；Jon将它类比为Pentos、Myr等Free Cities的bravos使用的快速突刺剑。",
    76: "**命名习惯：** 世界中的名剑常有专名，例如Eddard的大剑Ice；Jon也为Arya的剑预先准备了名字。",
    80: "**当前文本回声：** Arya在前章因needlework笨拙而受辱；将细剑命名为Needle，是对这段已知经历的重新命名，不涉及后文。",
}


EXTRA_VOCAB = [
    ("nuzzle", "/ˈnʌzəl/", "v.", "用鼻子亲昵地蹭", "动物表达亲近"),
    ("auburn", "/ˈɔːbərn/", "adj.", "红棕色的", "常形容头发"),
    ("defiant", "/dɪˈfaɪənt/", "adj.", "反抗的；挑战的", "拒绝服从权威"),
    ("frail", "/freɪl/", "adj.", "虚弱的；易损坏的", "此处形容受伤胸廓"),
    ("absolution", "/ˌæbsəˈluːʃən/", "n.", "赦免；宣告无罪", "带宗教和道德审判色彩"),
    ("cradle", "/ˈkreɪdəl/", "v.", "轻抱；小心托住", "像抱婴儿般保护"),
    ("sob", "/sɑːb/", "n./v.", "啜泣；哽咽", "哭泣时身体抽动"),
    ("harness", "/ˈhɑːrnɪs/", "v.", "给马套上挽具", "车队出发准备"),
    ("intrude", "/ɪnˈtruːd/", "v.", "闯入；打扰", "未受邀请进入"),
    ("disentangle", "/ˌdɪsɪnˈtæŋɡəl/", "v.", "从缠绕中挣脱；解开", "此处指松开拥抱"),
    ("ironwood", "/ˈaɪərnwʊd/", "n.", "铁木；坚硬深色木材", "奇幻世界材料"),
    ("scabbard", "/ˈskæbərd/", "n.", "剑鞘", "收纳刀剑的外套"),
    ("supple", "/ˈsʌpəl/", "adj.", "柔软易弯曲的", "`supple as sin`文学比喻"),
    ("sheen", "/ʃiːn/", "n.", "柔和光泽", "金属表面反光"),
    ("bravo", "/ˈbrɑːvoʊ/", "n.", "决斗士；受雇剑客", "此处为Free Cities剑客，非喝彩词"),
    ("hack", "/hæk/", "v.", "重砍；乱砍", "与突刺型剑术对比"),
    ("balance", "/ˈbæləns/", "n.", "平衡；武器重心手感", "评判剑是否易于控制"),
    ("whap", "/wæp/", "n./v.", "啪地打一下", "拟声感强的口语"),
    ("pointy", "/ˈpɔɪnti/", "adj.", "尖的；带尖头的", "儿童化、口语化形容"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB


def main():
    blocks = extract_range(90, 95, "JON", "CH10")
    write_chapter(
        out=OUT, chapter=10, pov="JON", page_start=90, page_end=95,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观设定；重点在Jon的告别、bastard身份、兄妹亲情或Needle的象征转化。",
        vocab=VOCAB,
        guide="出发前，Jon必须完成两场艰难的告别。他先冒着被Catelyn驱赶的恐惧去看Bran，在病床前流泪承认自己的害怕，却在离开时承受了Catelyn最残忍的一句话。他随后对Robb隐瞒真相，再去向Arya道别，将一把按她身材定制的细剑送给她。一场告别强调Jon在家中的排斥，另一场则展示Arya对他无条件的亲近。",
        people=[
            ("Jon Snow", "本章视角人物；离开Winterfell前向Bran、Robb和Arya告别"),
            ("Catelyn Stark", "Bran的母亲，近两周不离病床，对Jon长期存有排斥"),
            ("Bran Stark", "仍在昏迷的Jon弟弟"),
            ("Robb Stark", "Jon的兄弟，在家庭危机中承担组织责任"),
            ("Arya Stark", "Jon最亲近的妹妹，收到他秘密赠送的细剑"),
            ("Ghost / Nymeria", "Jon与Arya的direwolves，分别提供勇气与门外警戒"),
        ],
        terms=[
            ("Sworn Brother", "完成誓言后的Night’s Watch成员"),
            ("Faith of the Seven", "Catelyn信奉的七神信仰"),
            ("bravos", "Pentos、Myr等Free Cities中使用细剑的决斗士或剑客"),
            ("Needle", "Jon送给Arya的特制细剑之名"),
        ],
        synthesis="Chapter 10的两半部分用强烈对照界定Jon在Stark家庭中的位置。在Bran病房，他必须用未来Night’s Watch身份才能抵抗Catelyn的排斥；她的悲痛真实，但“本该是你”对Jon造成的伤害也同样真实。在Arya房中，Jon不需要证明自己有资格出现；Arya先拥抱他，再接受他按她本人特点制作的礼物。Needle因而不只是武器，它把女红课中的失败命名为新的能力，也保存了两个家庭边缘者之间的共同理解。",
        contrasts=[
            "**Catelyn的“我们”／Arya的拥抱：** 一个把Jon排除在家人之外，一个害怕他已经离开。",
            "**Bran的病床／Arya的乱箱子：** 前者静止、寒冷且充满死亡恐惧，后者混乱、活泼并充满动作。",
            "**伤害的话／善意谎言：** Catelyn把痛苦转移给Jon，Jon却对Robb隐瞒这段伤害。",
            "**Snow／Stark：** 兄弟以不同姓氏玩笑，把身份差异暂时转化为亲密。",
            "**needlework／Needle：** 同一个“针”从判定Arya失败的工具变成适合她的剑。",
        ],
        questions=[
            "Catelyn清醒后会如何看待自己对Jon说的话？",
            "Bran的病情会如何发展？",
            "Arya能否在King’s Landing找到教她使用Needle的人？",
            "Jon与Arya所走的不同道路何时可能再次交汇？",
        ],
    )
    print(f"Wrote Chapter 10 with {len(blocks)} paragraphs")


if __name__ == "__main__":
    main()
