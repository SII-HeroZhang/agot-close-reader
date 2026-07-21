#!/usr/bin/env python3
"""Build Chapter 35 (EDDARD) close-reading Markdown."""
from pathlib import Path
from agot_extract import extract_range
from agot_reader_common import write_chapter
from build_agot_chapter34_reader import VOCAB as BASE_VOCAB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"

S = {
1:"Eddard在Chataya brothel common room找到Littlefinger；Heward、Jory等人正参与或旁观带脱衣惩罚的成人游戏。",2:"Eddard在楼梯下戴好gloves，宣布调查完毕、该离开。",3:"Heward慌忙收拾衣物，Jory让Wyl一起备马。",4:"Littlefinger从容告别并用Hand代表king延伸出粗俗性玩笑。",5:"Eddard打断，承认找brothel受其帮助，却拒绝mockery，并说明自己已不再是Hand。",6:"Littlefinger以prickly direwolf回敬。",7:"无星暖雨中众人去stable；Wyl也衣衫未整，被门边woman取笑。",8:"Jory确认返回castle，Eddard与Littlefinger等人上马。",9:"Littlefinger夸Chataya经营好，拿brothel比ships更稳健作投资和pirates双关。",10:"Eddard任其闲谈直至沉默；空街暖雨像blood、像old guilts不断冲刷他。",11:"他回忆Lyanna订婚时早已预见Robert不会忠于一张bed，并说love不能改变nature。",12:"brothel中的年轻mother可能尚未成年；她红发雀斑，哺乳女婴Barra并请求Eddard确认孩子像Robert。",13:"Eddard确认Barra黑发，并想起Robert在Vale的firstborn也有同样发色。",14:"年轻mother求他告诉Robert孩子美丽。",15:"Eddard答应；他把自己守诺视为curse，并想到对临终Lyanna的promises与代价。",16:"mother发誓Robert是唯一男子，愿在Chataya给的半年期限内等待，不求jewels只求他回来。",17:"Eddard空洞地想所谓good to you，并保证转告且让Barra生活无缺。",18:"她颤抖甜美的笑令他心碎；雨夜中Eddard想到Jon相貌与baseborn children，询问Littlefinger知道多少Robert bastards。",19:"Littlefinger先讽刺Robert的children比Eddard多。",20:"Eddard追问数量。",21:"Littlefinger说数量不重要，列Storm’s End已承认boy，又转述Cersei曾杀死Casterly Rock twins、卖掉mother的传闻。",22:"Eddard知道great lords常有丑闻，却担心如今的Robert是否会对Cersei恶行闭眼，继而问Jon为何调查baseborn children。",23:"Littlefinger说Jon作为Hand可能只是替Robert照顾他们。",24:"Eddard认为若只是供养，便不足以解释Jon被杀。",25:"Littlefinger嘲讽Robert有bastards人人皆知，不可能单凭发现此事招来灭口。",26:"Eddard无言，只想到自己认为不逛brothel的Rhaegar。",27:"雨更猛烈、黑水成河时，Jory警告，街道瞬间出现士兵。",28:"前后至少二十名带golden lion的Lannister men封路，Jory拔剑要求让道。",29:"对方leader嘲讽wolves pack太小。",30:"Littlefinger谨慎上前，仍以Eddard是Hand质问。",31:"Jaime骑blood bay从队列中出现，纠正Eddard曾是Hand，如今身份不明。",32:"Littlefinger称行动疯狂，要求放行并问Jaime意图。",33:"Eddard冷静说Jaime很清楚自己在做什么。",34:"Jaime描述Tyrion特征，直说在寻找brother。",35:"Eddard说自己记得Tyrion。",36:"Jaime说Tywin因Tyrion路上出事而愤怒，讽刺询问谁想伤害他。",37:"Eddard公开说Tyrion按自己命令被捕，以回答crimes。",38:"Littlefinger因局势升级而呻吟。",39:"Jaime拔剑，威胁像杀Aerys般杀Eddard，却希望他持剑死；同时叫Littlefinger快走免污衣。",40:"Littlefinger立刻离开，承诺带City Watch，Lannister队列特意放行后再合拢。",41:"Eddard方三人对二十人，旁观者不介入；他用Catelyn会杀Tyrion威胁，认为比冲锋更安全。",42:"Jaime判断Catelyn honor使她不会杀hostage，却不愿冒brother风险，因此收剑放Eddard，并命Tregar保证不伤他。",43:"Tregar服从。",44:"Jaime随即补充仍要惩戒Eddard，命令杀死他的men。",45:"Eddard尖叫拔剑，Jaime离开；Wyl、Heward、Jory与Eddard在雨中遭围杀，Eddard horse滑倒使他重伤。",46:"Eddard看见Jory被拖下马围杀，自己小腿bone穿出皮肉，随后失去意识。",47:"醒来后Eddard独处死者之间，拖着断腿穿泥；围观者开始出现却无人援助。",48:"Littlefinger最终带City Watch赶到，发现Eddard抱着Jory尸体。",49:"gold cloaks用litter送他返Red Keep；城墙被雨染成blood颜色，他反复昏迷。",50:"Pycelle给他milk of the poppy止痛并命人煮wine、取clean silk，Eddard再次失去知觉。",
}
SUMMARIES = [S[i] for i in range(1, 51)]

KEY_NOTES = {
1:"brothel日常轻浮与即将发生的street killing并置，角色以为调查已结束，真正危险却在门外。",
2:"pull on gloves像结束接触证据的仪式动作，也为雨夜离开与之后拔剑预备身体。",
4:"Littlefinger把Hand’s representative formula一路推到sexual substitution，故意测试Eddard刚辞职后的身份与耐性。",
5:"Eddard能同时acknowledge help与拒绝humiliation，显示感激不等于接受对方控制对话规则。",
9:"brothel/ship比较把人身服务完全转成资产收益语言，也延续Littlefinger擅长用经济逻辑消解道德不适。",
10:"warm as blood/relentless as old guilts把天气内化；雨不清洗他，反而使旧责任持续贴在脸上。",
11:"Lyanna准确区分love intensity与habit change；Eddard当年用betrothal前后界线安慰她，却低估nature连续性。",
12:"叙述刻意不确定mother年龄并写Eddard不敢问，提示权力与贫困下的性剥削；场景不是浪漫相遇。",
13:"Barra、Gendry与Vale firstborn均呈Robert black hair等特征，重复观察让bloodline pattern越来越稳定。",
15:"That was his curse说明守诺对Eddard既是identity也是持续负担；Lyanna promise仍未向读者完整说明。",
16:"mother把Robert短暂kindness解释为可持续love，并主动排除金钱动机；她的等待与Robert遗忘形成残酷信息差。",
18:"Jon脸孔由baseborn suffering触发，说明Eddard对Jon的guilt与promise密切相连，但具体原因仍不可确定。",
21:"Storm’s End boy有公开承认背景；Casterly Rock twins则由Littlefinger以whispers提供，不能提升为已证实Cersei命令。",
22:"Eddard开始承认Robert可能用not seeing逃避责任；不亲自下令也可能通过故意忽视容许伤害。",
25:"Littlefinger的反讽逻辑有效：Robert有bastards是公开常识，因此Jon被杀必与更具体的发现有关。",
26:"Rhaegar记忆并非证据，只是Eddard用对比重新评价Robert；somehow I thought not明确是个人印象。",
27:"Jory一声alarm把内省切断；street was full几乎无过渡，制造伏击已经完成部署的突然感。",
28:"前后封路显示不是偶遇争吵而是组织好的interception；人数优势也让公开街道变成受控空间。",
30:"Littlefinger仍称Hand可能是习惯、策略或给Eddard保护性身份；Jaime立即拆掉这层office shield。",
31:"was the Hand把早晨辞职消息已传到Jaime处，显示court information传播速度极快。",
33:"Eddard不接受madness解释，因为Jaime目的、兵力和路线都显示清醒算计；暴力可以蓄意而非失控。",
37:"Catelyn实际自主拘捕Tyrion；Eddard说at my command是在公开承担妻子行动的家族与政治责任，也可能保护她免被单独针对。",
39:"like Aerys把Jaime过去regicide作为威胁资本；他让Littlefinger离开说明控制对象和预定惩罚范围清晰。",
40:"Lannister line主动开合放行Littlefinger是文本事实；他随后确实带Watch返回，但这不足以证明事前参与伏击。",
41:"Eddard的hostage deterrence把Tyrion生命变成自身保护；他依赖Jaime相信Catelyn愿意报复。",
42:"Jaime判断Catelyn不会因honor杀hostage，却仍不肯risk，显示他把概率与stakes分开；brother affection限制杀Eddard。",
44:"no harm to Lord Stark与kill his men在相邻命令中构成冷酷字面规避：他保留Tyrion保险，却用属下生命实施惩罚。",
45:"Eddard从更surer tactic瞬间被迫进入混战，说明deterrence只保护了首要目标，没有覆盖companions。",
46:"rising and falling swords避免逐刀细写，却以重复运动表现Jory被人群吞没；断骨成为Eddard视野最后锚点。",
47:"windows中的观众延续tourney crowd motif，但这里没有规则或欢呼；城市居民对贵族暴力的安全选择是不介入。",
48:"Eddard抱Jory尸体把lord/retainer关系还原为私人丧失；援兵到达只证明晚到，无法逆转命令后果。",
49:"Red Keep pale pink转blood色把king’s seat视觉上纳入街头暴力，雨成为全章统一的罪责染料。",
}

STAGES = [
(1,10,"Eddard完成brothel问话，与Littlefinger、Jory及guards冒雨返城；Littlefinger以投资和性笑话保持语言挑衅。"),
(11,18,"回忆中Lyanna预见Robert本性；年轻mother展示Barra黑发并等待Robert，Eddard把守诺、Jon与baseborn suffering相连。"),
(19,26,"Littlefinger列公开bastard与未证实twins传闻，却指出仅发现Robert有children不足以解释Jon被杀。"),
(27,44,"Lannister men前后封街，Jaime追问Tyrion；Eddard承担拘捕责任，Jaime因hostage风险不杀他，却命杀其guards。"),
(45,50,"雨中围杀造成Wyl、Heward、Jory死亡与Eddard断腿；Littlefinger带City Watch晚到，Pycelle为Eddard止痛治疗。"),
]

BACKGROUNDS = {
1:"**Chataya’s brothel：** Jon与Stannis曾访问的地点；Eddard刚询问一名为Robert生下Barra的年轻mother。",
11:"**Lyanna betrothal：** Rickard曾把Lyanna许配Robert；Lyanna早知Robert在Vale已有child并怀疑其忠诚。",
13:"**bloodline observation：** Barra具有Robert黑发；Gendry与Vale firstborn也呈类似Baratheon外貌，Jon正调查这些children。",
15:"**Lyanna promises：** Eddard曾向dying Lyanna作出多项承诺；截至本段具体内容仍未公开。",
21:"**已知／传闻：** Storm’s End boy是Robert公开承认的baseborn son，由Renly household抚养；Casterly Rock twins遭Cersei杀害、mother被卖则只是Littlefinger转述的whispers，本章无独立证据。",
27:"**力量状态：** Eddard刚辞去Hand，随行主要是Jory、Wyl、Heward；Jaime带约二十名Lannister guards前后封路。",
31:"**office变化：** Jaime已知Eddard辞职，因此拒绝Littlefinger用Hand身份要求让路。",
37:"**拘捕事实：** Catelyn在crossroads inn自主下令抓Tyrion；Eddard此处公开归到自己command名下。",
39:"**Jaime与Aerys：** Jaime作为Kingsguard杀死Aerys，故以butcher you like Aerys威胁Eddard。",
42:"**hostage logic：** Jaime不杀Eddard，以免Catelyn报复Tyrion；他对Catelyn honor的信心仍不足以承受brother death风险。",
50:"**milk of the poppy：** 强效鸦片类止痛/镇静药；Pycelle随后准备处理Eddard开放性小腿骨折。",
}

EXTRA_VOCAB = [
("amiably","/ˈeɪmiəbli/","adv.","和蔼友好地","chatting"),("buxom","/ˈbʌksəm/","adj.","丰满健美的（旧式）","woman"),("forfeit","/ˈfɔːrfɪt/","n.","游戏输方惩罚；罚失物","parlor game"),("wench","/wentʃ/","n.","年轻女人（旧式、可能冒犯）","brothel worker"),("wry","/raɪ/","adj.","挖苦而克制的","smile"),("presume","/prɪˈzuːm/","v.","越界放肆；擅自假定","too much"),("prickly","/ˈprɪkli/","adj.","易怒难接近的","direwolf"),("pelt down","/pelt daʊn/","phr.v.","雨点猛烈落下","warm rain"),("prattle","/ˈprætəl/","v.","喋喋不休说琐事","Littlefinger"),("rivulet","/ˈrɪvjələt/","n.","细流","rainwater"),("acknowledge","/əkˈnɑːlɪdʒ/","v.","公开承认","baseborn son"),("affront","/əˈfrʌnt/","n.","公开侮辱；冒犯","Lannister pride"),("sodden","/ˈsɑːdən/","adj.","湿透的","cloak / shrug"),("blurt out","/blɜːrt aʊt/","phr.v.","脱口泄露","obvious fact"),("greaves","/ɡriːvz/","n.","护胫甲","soldiers"),("vexed","/vekst/","adj.","恼怒的；烦扰的","Tywin"),("perchance","/pərˈtʃæns/","adv.","或许（古风）","sarcastic question"),("butcher","/ˈbʊtʃər/","v.","残杀","threat"),("unchastened","/ʌnˈtʃeɪsənd/","adj.","未受惩戒的","Jaime’s punishment"),("phantom","/ˈfæntəm/","n.","幽影；难辨身影","red cloaks in rain"),("bridle","/ˈbraɪdəl/","n.","马笼头与缰具","seized horse"),("lurch","/lɜːrtʃ/","v.","突然摇晃起身","horse"),("rank","/ræŋk/","adj.","浓烈难闻的","blood scent"),("cradle","/ˈkreɪdəl/","v.","怀抱托住","Jory’s body"),("milk of the poppy","/mɪlk əv ðə ˈpɑːpi/","n.","罂粟乳止痛镇静药","treatment"),
]
VOCAB = BASE_VOCAB + EXTRA_VOCAB

def main():
    blocks = extract_range(348, 353, "EDDARD", "CH35")
    write_chapter(
        out=OUT, chapter=35, pov="EDDARD", page_start=348, page_end=353,
        blocks=blocks, summaries=SUMMARIES, key_notes=KEY_NOTES, stages=STAGES,
        backgrounds=BACKGROUNDS,
        default_background="本段没有新增必须补充的世界观事实；重点在Robert bloodline线索、Littlefinger信息可靠性、Jaime hostage calculation与街头伏击责任。",
        vocab=VOCAB,
        guide="Eddard在Chataya brothel确认Robert新生女儿Barra同样拥有黑发，并想到Vale firstborn、Gendry与Jon；Robert baseborn children的外貌pattern越来越稳定，但Jon为何因此被杀仍未知。Littlefinger列出Storm’s End已承认son和Casterly Rock twins传闻，后者没有独立证据；他也正确指出“Robert有bastards”本是公开常识，不能单独解释谋杀。返城雨夜，约二十名Lannister guards前后封街，Jaime为Tyrion问责。Eddard把Catelyn自主拘捕公开说成自己的command，承担家族政治责任。Jaime因担心Catelyn杀Tyrion而不杀Eddard，却用字面规避命令杀死Wyl、Heward和Jory。Littlefinger获准离开并最终带City Watch返回，这些是事实；文本没有证明他预先参与伏击。Eddard断腿，被送回Red Keep治疗。",
        people=[
            ("Eddard Stark","本章视角；确认Barra特征、承担Tyrion拘捕责任，并在伏击中重伤"),
            ("Jaime Lannister","为Tyrion带兵截路，因hostage风险保留Eddard性命，却下令杀其guards"),
            ("Petyr Baelish","提供brothel地点与bastard信息，获Jaime放行后带City Watch返回"),
            ("Jory Cassel","Eddard captain of guards，在Lannister围杀中冲锋并死亡"),
            ("Barra / young mother","Robert新生baseborn daughter及其年轻mother；母亲仍等待Robert回来"),
            ("Heward / Wyl","随行Stark guards，在Jaime惩戒命令后的战斗中死亡"),
            ("Chataya","brothel经营者，给Barra mother半年照料child并等待Robert"),
            ("Pycelle","为Eddard提供止痛并准备处理开放性骨折"),
        ],
        terms=[
            ("Baratheon look","Robert baseborn children反复出现的黑发及相关面部特征"),
            ("hostage deterrence","以Tyrion可能被报复为代价，阻止Jaime直接杀Eddard"),
            ("at my command","Eddard对Catelyn拘捕的公开责任声明，不是事件现场事实描述"),
            ("milk of the poppy","用于重伤止痛与镇静的强效药剂"),
            ("open fracture","Eddard小腿骨穿出皮肤的严重骨折，伴随剧痛、失血和感染风险"),
        ],
        synthesis="Chapter 35让“nature”和“责任”同时显形。Lyanna说love不能改变Robert nature；多年后Barra mother仍把短暂温柔当永久承诺，而Eddard替Robert承担兑现照顾的责任。街头另一端，Jaime也由brother love驱动，却把爱转成集体惩罚：不杀Eddard以保护Tyrion，杀guards以维护Lannister honor。Eddard的hostage threat在狭义上成功、在整体上失败。小说由此展示政治威慑常只保护被明确计价的目标，身边较弱者则被当作可替代成本。",
        contrasts=[
            "**Robert短暂温柔／mother长期等待：** 双方对同一关系的时间尺度完全不同。",
            "**black hair线索／未知谋杀动机：** 血缘pattern更清晰，Jon死亡因果仍缺关键一步。",
            "**Hand身份／former Hand：** Littlefinger用office要求让路，Jaime以辞职消息拆除保护。",
            "**不杀Eddard／杀其men：** Jaime在hostage约束内寻找仍能施加的惩罚。",
            "**公开街道／无人介入：** 可见性没有自动带来安全，围观者选择避开贵族武装冲突。",
            "**暖雨／blood色：** 雨从旧guilt意象变成真实死亡，并把Red Keep染入同一画面。",
        ],
        questions=[
            "Barra、Gendry与其他Robert children的共同外貌如何对应Jon阅读lineages book的发现？",
            "Littlefinger为何能比Jory更快找到brothel，又为何选择此时带Eddard前来？",
            "Robert会如何回应Jaime在首都公开杀死former Hand guards并重伤Eddard？",
            "Eddard受伤与Jory死亡会怎样影响原定立即带daughters离城的计划？",
        ],
        extraction_notes="PDF pp.348–353共50段；正确合并2处跨页续段：pp.348–349与351–352。逐页复核未发现额外分页误切。",
    )
    print(f"Wrote Chapter 35 with {len(blocks)} paragraphs")

if __name__ == "__main__":
    main()
