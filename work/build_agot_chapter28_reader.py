#!/usr/bin/env python3
"""Build Chapter 28 (CATELYN) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter27_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"Ser Rodrik催Catelyn遮住头，免得雨中受寒。",2:"Catelyn享受温暖的南方雨，回忆Riverrun童年与Lysa、Littlefinger一起玩泥巴。",3:"她对比北方冰冷坚硬、会毁坏庄稼的雨。",4:"浑身湿透的Ser Rodrik只想要火、热餐和干衣服。",5:"前方crossroads inn唤起Masha Heddle红牙与童年点心的记忆。",6:"Catelyn担心旅店会暴露身份，忽然听见后方骑兵。",7:"Mallister骑士涉水而来，Ser Rodrik提醒她遮脸；鹰纹使她认出Seagard人。",8:"Catelyn反而放下hood，看见Jason Mallister与儿子Patrek南下参加tourney。",9:"Jason是父亲的封臣却未认出她；她短暂羡慕他们能公开骑行、无须隐藏。",10:"Ser Rodrik惊讶竟无人认出他们。",11:"Catelyn判断满身泥水的旅人不会被当成liege lord之女，因此决定住店。",12:"他们抵达旅店；衰老的Masha只剩两间garret rooms，楼下又已客满。",13:"Masha叫他们脱掉泥靴，并用钟声规定晚餐时间，昔日亲切已不复见。",14:"晚餐钟响时，Catelyn隔着起泡玻璃望雨和道路，权衡下一步。",15:"她可以向西去Riverrun求助病中的父亲，却担心靠近Casterly Rock会引发战争。",16:"也可向东去Eyrie见Lysa，寻求答案与Arryn、Tully联盟。",17:"但通往Eyrie的山路险恶，而她只有一名年老骑士护卫。",18:"她最终决定继续北上回到儿子身边，并计划过Neck后公开身份、召集北方封臣。",19:"她在心中复盘riverlands的道路与河流位置。",20:"她盘点Blackwood、Bracken、Whent、Frey等家族的兵力与旧日立场，意识到任何召集都可能点燃战争。",21:"Ser Rodrik催她下楼吃饭。",22:"他提议假扮父女，使两人关系显得自然。",23:"Ser Rodrik习惯性称她my lady，暴露贵族礼仪难以彻底隐藏。",24:"Catelyn接受安排，并提醒他别称赞Masha的笑容。",25:"两人进入由壁炉和长桌组成的拥挤common room。",26:"crossroads把不同方向、不同阶层的旅人临时混在同一屋檐下。",27:"屋中武器众多；Bracken与Frey随从人数可观，但都太年轻，不认识Catelyn。",28:"他们坐近厨房，一名年轻singer主动搭话。",29:"singer连珠炮般打听消息；Catelyn只谨慎透露自己两周前离开King’s Landing。",30:"singer要去tourney赚钱，并说自己上次押Jaime获胜而输掉银钱。",31:"Ser Rodrik说诸神不赞成赌博。",32:"singer反驳说真正使他输钱的是Loras。",33:"Ser Rodrik问他是否吸取教训。",34:"他声称吸取了，这次将改押Loras。",35:"食物送到，Ser Rodrik专心进食。",36:"singer自称Marillion，并默认自己的名声理应人尽皆知。",37:"Catelyn坦言从未听过。",38:"Marillion弹出哀怨和弦，反问谁才是最好的singer。",39:"Ser Rodrik答Alia of Braavos。",40:"Marillion夸口胜过Alia，愿为银币献唱。",41:"Ser Rodrik说只愿把铜币扔井里，并认为音乐适合少女、不适合健康男孩。",42:"Marillion反唇相讥，改称要以歌赞美Catelyn。",43:"Catelyn以父亲Hoster爱歌为饵，试探Marillion是否真去过Riverrun。",44:"Marillion夸称去过百次、与Edmure情同手足，反而因夸张露出破绽。",45:"Catelyn知道Edmure厌恶singers，转问他是否到过Winterfell。",46:"Marillion以南方偏见描绘北方；此时门被推开。",47:"仆人高声宣布一位Lannister lord要房间和热水澡。",48:"Ser Rodrik脱口惊呼，Catelyn立刻抓住他的手臂制止。",49:"Masha带着难看的笑解释客房已满。",50:"Tyrion与Yoren及两名随从进门；Tyrion开玩笑说小房间、草堆也能接受。",51:"Masha惶恐重复没有房间。",52:"Tyrion抛出金币，以财富迅速改变资源分配。",53:"一名freerider立刻愿意让出房间。",54:"Tyrion赞许并付款，又吩咐准备饭食。",55:"Catelyn一度想亲手掐死他，却在想象中看见Bran窒息流血，暴露愤怒背后的母亲恐惧。",56:"Tyrion要双份食物、烤鸡和酒，并邀请Yoren同桌。",57:"Yoren答应。",58:"Marillion主动要唱Tywin胜利之歌讨好Tyrion。",59:"Tyrion拒绝，却在人群中认出Catelyn并当众叫出Lady Stark。",60:"Marillion震惊，Catelyn起身，Ser Rodrik低声咒骂；她懊恼Tyrion没有留在Wall。",61:"Masha也惊问她是否真是Lady Stark。",62:"Catelyn不再隐藏，公开身份并根据黑蝙蝠纹章询问一名Whent家臣。",63:"那人确认自己的归属。",64:"Catelyn让他承认Lady Whent与Hoster Tully的友谊，把私人识别转化为封臣关系。",65:"他再次确认。",66:"Ser Rodrik悄悄松剑出鞘，Tyrion仍困惑地观察。",67:"Catelyn再以红马纹章点名Bracken人，并询问Jonos是否忠于父亲。",68:"Bracken men虽迟疑，仍表示会尊重这份忠诚。",69:"Tyrion以玩笑询问她究竟想做什么。",70:"Catelyn转向人数最多的Frey队伍，问Walder近况。",71:"队长答Walder身体很好，九十岁仍准备结婚。",72:"Catelyn借众人公开承认的封臣义务，指控Tyrion参与谋杀七岁儿子的阴谋，并以Robert和各领主之名要求逮捕他、押回Winterfell接受king’s justice。",73:"十余把剑同时出鞘；Catelyn从刀剑声和Tyrion的表情判断自己的临场策略奏效。",
}
SUMMARIES = [S[i] for i in range(1, 74)]

KEY_NOTES = {
2:"温暖的雨触发童年记忆，使返乡路线不只是地图选择，也是Catelyn旧身份的回潮；Littlefinger已被嵌进她最早的家庭记忆。",
5:"Masha与旅店同时承担地标和记忆容器功能：路没有变，熟悉的人却已衰老、冷淡。",
7:"heraldry在本章不是装饰，而是即时身份数据库；Catelyn能凭鹰纹、黑蝙蝠、红马辨认政治网络。",
9:"未被封臣认出既证明伪装成功，也制造身份疏离：她羡慕的不是Jason本人，而是公开行动的自由。",
11:"Catelyn利用阶级想象隐藏身份：旁人不相信liege lord之女会如此狼狈，因此泥水反而成为伪装。",
15:"去Riverrun最符合亲情，却在军事地理上最危险；她把个人求助可能引发的军队动员纳入判断。",
16:"Eyrie提供答案和强大联盟，但“可能得到帮助”不等于“能安全抵达或说服Lysa”。",
17:"一名忠诚的old knight能提供信任，却不能消除山路、brigands和人数差距带来的实际风险。",
18:"北上决定重新把mother与Lady Stark身份合并：先回到sons身边，再以公开身份调动northmen。",
20:"长名单体现她的政治素养，也揭示riverlands忠诚并非整齐统一；旧战争记忆会影响新危机。",
22:"father/daughter disguise把真实年龄差转化为可信社会关系，是现场表演而非单纯换衣。",
23:"一句my lady说明身体习惯和礼仪记忆比服装更难伪装；长期等级关系会从称呼中泄漏。",
26:"crossroads inn是叙事缩影：南北东西路线、不同家族与消息在此碰撞，所以偶遇既偶然又由地理促成。",
27:"Catelyn没有把年轻随从当作无关背景，而是立即评估数量、纹章、年龄与是否会认出自己。",
29:"她给Marillion的答案真实但有限，展示安全谎言未必需要虚构，只需控制信息量。",
30:"tourney的名声沿道路传播；Jaime和Loras的竞技结果已经成为赌局、歌曲与公共谈资。",
34:"笑点在于Marillion把失败解释为押错人，而不是赌博本身；所谓lesson learned其实毫无改变。",
41:"Ser Rodrik对音乐的看法显示旧式武人把艺术性视为不够阳刚，Marillion则靠机锋反击年龄和身份。",
43:"Catelyn主动设置可核验细节，开始反向审问爱吹嘘的陌生人；她并非被动听众。",
44:"Marillion过度声称与Edmure亲密，恰好触碰Catelyn掌握的一手事实，因此自我揭穿。",
46:"他对north的描述由传闻和偏见组成；门在此打开，真正来自north路线的人立刻打断幻想。",
48:"Ser Rodrik的惊呼险些先暴露两人，Catelyn用身体动作而非语言制止，避免进一步吸引注意。",
50:"Tyrion把不利处境转成笑话，保持对场面的语言控制；Yoren出现也把Wall路线与旅店相接。",
52:"gold使住宿从“没有”变为“有人愿让”，展示市场权力能立刻重排私人选择。",
55:"她想象Tyrion窒息却看见Bran受害，说明报复冲动无法带来纯粹满足，只会重新触发创伤。",
58:"Marillion先赞Loras、随后又准备唱Tywin，显示游唱者的赞美可随潜在赞助者迅速改向。",
59:"Tyrion认出她的瞬间使伪装整体失效；他或许只是惊讶问候，却在公开空间造成不可逆的信息扩散。",
62:"Catelyn没有逃跑或否认，而是把个人身份转化为政治资本：先让纹章持有者公开承认所属关系。",
64:"她的问题设计只要求对方确认公认友谊，降低拒绝门槛，并让下一步求援看似履行既有义务。",
67:"从Whent转到Bracken形成重复验证：她逐一把屋中陌生武装者重新分类为父亲封臣的men。",
70:"Frey人数最多，因此最后点名既完成政治铺垫，也确保真正执行逮捕时有足够武力。",
72:"指控建立在Littlefinger对dagger归属的说法及Bran遇袭事实上；逮捕不等于证据成立。她成功调用feudal obligations，却也把秘密调查升级为公开冲突。",
73:"结尾以声音与表情确认权力逆转：Tyrion的gold刚支配旅店市场，Catelyn的name与oaths又支配持剑者。",
}

STAGES = [
(1,20,"南方暖雨唤起Riverrun童年；Catelyn在四方道路之间权衡亲情、安全、联盟与战争风险，最终决定继续北上。"),
(21,46,"她与Ser Rodrik以父女身份进入旅店，在纹章、人数和闲谈中评估环境；Marillion的吹嘘构成短暂喜剧。"),
(47,60,"Tyrion意外抵达，以gold解决住宿，却在拥挤common room中认出Catelyn，使伪装瞬间崩溃。"),
(61,73,"Catelyn转守为攻，依次借Whent、Bracken、Frey纹章确认封臣义务，公开指控并成功让众人拔剑拘捕Tyrion。"),
]

BACKGROUNDS = {
7:"**House Mallister：** Seagard的riverlord家族，以银鹰为纹章，效忠House Tully；Jason与Patrek正南下参加Hand’s tourney。",
15:"**Hoster Tully：** Catelyn的父亲、Lord of Riverrun；她已知他病重，但尚未亲见病情。Riverrun位于riverlands西部。",
16:"**Eyrie与Lysa：** Lysa是Catelyn妹妹、Jon Arryn遗孀，现居难攻的Eyrie；姐妹关系并不自动保证立刻合作。",
20:"**riverlords：** Blackwood、Bracken、Whent与Frey等均处Tully体系内，但各家历史、邻里冲突和Robert’s Rebellion立场不同，忠诚不能机械等同。",
27:"**旅店武装：** Bracken与Frey队伍是领主属下，不是专为Catelyn集结；她后来利用的是既有封臣关系。",
30:"**Hand’s tourney：** King’s Landing即将举行的盛会已吸引各地骑士、singers和赌徒，也造成道路人口流动。",
43:"**家庭关系：** Hoster是Catelyn与Edmure的父亲；Edmure留在riverlands，是House Tully继承人。",
50:"**北返队伍：** Tyrion刚从Wall南返，Yoren是Night’s Watch的wandering crow；另外两人为Tyrion随从。",
62:"**House Whent：** Harrenhal领主家族，纹章为黑蝙蝠；Catelyn借Lady Whent与Hoster的关系请求其men表态。",
67:"**House Bracken：** Stone Hedge的riverlord家族，以红色stallion为纹章，Lord Jonos效忠Riverrun。",
70:"**House Frey：** 控制Twins渡口的强大家族，名义上是Tully封臣；Walder Frey年老且子孙众多。",
72:"**事实／推断：** Bran确曾遭刺客袭击，Catelyn也被Littlefinger告知dagger曾属Tyrion；但本章未提供独立核验。公开拘捕是政治与法律行动，不是罪名已经证明。",
}

EXTRA_VOCAB = [
("plod","/plɑːd/","v.","沉重缓慢地走","horses through rain"),("ragged","/ˈræɡɪd/","adj.","参差破旧的；不整齐的","clouds / appearance"),("nurture","/ˈnɜːrtʃər/","v.","滋养；培育","warm rain"),("wistfully","/ˈwɪstfəli/","adv.","惆怅而向往地","remember childhood"),("sourleaf","/ˈsaʊərlif/","n.","酸叶；使牙齿染红的咀嚼叶","Masha’s red teeth"),("sodden","/ˈsɑːdən/","adj.","湿透的","cloak and clothes"),("liege lord","/liːdʒ lɔːrd/","n.","受效忠的领主","Tully authority"),("cursory","/ˈkɜːrsəri/","adj.","草率简略的","inspection"),("garret","/ˈɡærət/","n.","顶楼小阁间","inn rooms"),("confluence","/ˈkɑːnfluəns/","n.","河流汇合处；交汇","river geography"),("loath","/loʊθ/","adj.","不情愿的","avoid a choice"),("impregnable","/ɪmˈpreɡnəbəl/","adj.","坚不可摧的","Eyrie"),("chasm","/ˈkæzəm/","n.","深谷；裂隙","mountain road"),("brigand","/ˈbrɪɡənd/","n.","拦路强盗","travel danger"),("staunch","/stɔːntʃ/","adj.","坚定忠诚的","supporter"),("levies","/ˈleviz/","n.","征召兵","feudal forces"),("clangor","/ˈklæŋər/","n.","金属铿锵声","drawn swords"),("drafty","/ˈdræfti/","adj.","漏风的","inn room"),("keg","/keɡ/","n.","小桶","ale storage"),("skewer","/ˈskjuːər/","n./v.","烤肉扦；刺穿","roast food"),("sellsword","/ˈselsɔːrd/","n.","雇佣剑士","armed traveler"),("boon companion","/buːn kəmˈpænjən/","n.","亲密酒友；好友","Marillion’s boast"),("plaintive","/ˈpleɪntɪv/","adj.","哀怨的","musical chord"),("homage","/ˈhɑːmɪdʒ/","n.","效忠；敬意","feudal duty"),("steep","/stiːp/","v.","浸泡","horse feed / liquid"),("chagrin","/ʃəˈɡrɪn/","n.","懊恼；难堪","failed concealment"),("stoutly","/ˈstaʊtli/","adv.","坚定地","answer loyalty"),("scabbard","/ˈskæbərd/","n.","剑鞘","loosen a sword"),("seize","/siːz/","v.","抓捕；夺取","arrest Tyrion"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def main():
    blocks = extract_range(264, 272, "CATELYN", "CH28")
    write_chapter(
        out=OUT, chapter=28, pov="CATELYN", page_start=264, page_end=272,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在伪装、道路选择、纹章识别、旅店权力关系与Catelyn的临场判断。",
        vocab=VOCAB,
        guide="Catelyn与Ser Rodrik冒雨来到crossroads inn。温暖雨水唤起Riverrun童年，她却必须在向西求父亲、向东找Lysa和继续北返之间做政治选择。旅店里聚集了Whent、Bracken、Frey等riverlord随从，她最初只想以父女身份低调过夜；Tyrion意外抵达并当众认出她后，伪装再无可能。Catelyn于是凭纹章逐一确认屋中武装者与House Tully的封臣关系，把暴露的身份转化成公共权威，指控Tyrion参与谋害Bran并成功发动逮捕。但行动所依据的dagger归属仍是未经独立验证的说法，逮捕不等于证明有罪。",
        people=[
            ("Catelyn Stark","本章视角；权衡路线、隐藏身份，并在暴露后调用父亲的封臣网络"),
            ("Ser Rodrik Cassel","同行护卫，提议父女伪装；旧式礼仪数次险些泄露身份"),
            ("Tyrion Lannister","从Wall南返，在旅店认出Catelyn，随后遭公开指控与拘捕"),
            ("Masha Heddle","crossroads inn老板；Catelyn童年旧识，如今衰老且态度冷淡"),
            ("Marillion","年轻singer，爱夸口并将赞美投向潜在赞助者"),
            ("Jason Mallister","Hoster封臣、Seagard领主，携Patrek南下参加tourney"),
            ("Whent / Bracken / Frey men","旅店中的riverlord随从，被Catelyn借纹章与效忠关系动员"),
            ("Yoren","Night’s Watch recruiter，与Tyrion一同南返"),
        ],
        terms=[
            ("crossroads inn","riverlands交通节点，连接南北东西道路，也让各家人员与消息高概率相遇"),
            ("House Tully bannermen","名义上向Riverrun效忠的riverlords；各家历史与实际可靠性并不完全一致"),
            ("heraldry / sigils","识别家族与政治归属的视觉系统，本章成为Catelyn动员陌生武装者的工具"),
            ("feudal homage","封臣对领主体系承认的效忠义务；Catelyn以父亲Hoster的权威加以调用"),
            ("king’s justice","以Robert王权名义实施的司法处置；宣称此名义不等于事实已由审判确认"),
        ],
        synthesis="Chapter 28把crossroads同时写成地理路口、人生选择和政治碰撞点。Catelyn先在四条道路间计算风险，又在旅店中读取每一面sigil。Tyrion的一声Lady Stark摧毁匿名性，却也使她能够公开扮演Hoster之女：她没有直接命令陌生人，而是用一连串容易回答的忠诚问题，让Whent、Bracken、Frey men在众目睽睽下先承认关系，再要求行动。策略在现场极其成功，也极其危险，因为它把基于Littlefinger说法的秘密调查升级为Lannister与Tully/Stark阵营间的公开拘捕。形式上的权威、临场的武力与事实上的真相，在这里并不是同一件事。",
        contrasts=[
            "**南方暖雨／北方冷雨：** 同一自然现象分别关联童年滋养与严酷生存。",
            "**隐藏身份／公开身份：** 泥水和父女伪装先保护Catelyn，暴露后她又用Lady Stark身份夺回主动。",
            "**四方道路／单一决定：** crossroads提供多种可能，每条路却对应不同政治代价。",
            "**Marillion的空谈／Tyrion的识别：** 前者制造噪音，后者一句准确称呼改变全场。",
            "**gold／homage：** Tyrion用金币重排住宿，Catelyn用封臣义务重排刀剑。",
            "**成功逮捕／尚未证明：** 武装响应证实Catelyn的政治权力，不证实指控本身。",
        ],
        questions=[
            "被捕后的Tyrion会被押往哪条道路，Catelyn为何可能不按公开说法直返Winterfell？",
            "Whent、Bracken与Frey men的现场服从能否转化为长期支持？",
            "公开指控一名Lannister会如何改变原本秘密进行的调查？",
            "Littlefinger关于dagger所有权的说法是否准确，之后能否得到独立核验？",
        ],
        extraction_notes="PDF pp.264–272共73段；正确合并5处跨页段落：pp.264–265、266–267、267–268、269–270与271–272。",
    )
    print(f"Wrote Chapter 28 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
