#!/usr/bin/env python3
"""Build Chapter 2 (CATELYN) close-reading Markdown."""

from __future__ import annotations

import json
from pathlib import Path

from agot_extract import PDF, extract_range
from build_agot_chapter1_reader import VOCAB as BASE_VOCAB
from build_agot_prologue_reader import english_names, term_present


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"


SUMMARIES = [
    "Catelyn从未喜欢过Winterfell的godswood，开篇直接建立她与北方信仰空间之间的疏离。",
    "她出生于南方Riverrun；故乡的godswood明亮、开放，像供人散步和休息的花园。",
    "Winterfell的godswood却古老、浓暗而原始，粗壮树木遮住天空，使她感到被监视和压迫。",
    "尽管不喜欢这里，Catelyn知道Ned每次亲手处决犯人后都会来到此处清洗剑并沉思。",
    "Catelyn信奉Faith of the Seven；她的命名与信仰仪式发生在Riverrun的sept中。",
    "Ned为她修建sept，但Stark血脉仍属于旧神与北方森林，婚姻并未消除两人的信仰差异。",
    "树林中心的古老weirwood俯临黑水池，白骨般树皮与血手般红叶构成不安的圣树形象。",
    "南方多数weirwood早已被砍毁，北方却仍保留；Catelyn觉得树上的面孔既陌生又具有神性。",
    "她在weirwood下找到Ned；Ice横在他膝上，他正用黑水清洗剑上的血。",
    "Ned以正式疏远的语气叫她，并首先询问孩子们在哪里。",
    "Catelyn说孩子们正在厨房为direwolf幼崽取名，并靠近Ned坐下。",
    "Ned询问三岁的Rickon是否害怕幼崽。",
    "Catelyn承认Rickon有一点害怕，强调他毕竟只有三岁。",
    "Ned认为Rickon必须学习面对恐惧，并说出House Stark的家族箴言：Winter is coming。",
    "Catelyn虽然同意，却一如既往地因这句家族箴言感到寒意；它不像别家箴言那样炫耀荣誉。",
    "Ned评价逃兵死得还算体面，一边用油革擦亮Ice。",
    "他很高兴Bran表现得好，认为Catelyn会为Bran骄傲。",
    "Catelyn回答自己一直为Bran骄傲，并观察Valyrian steel反复折叠锻造形成的波纹。",
    "Ned说这是当年第四名逃兵；此人近乎疯狂，恐惧深入到言语之外。",
    "Catelyn猜测这种变化是否由wildlings引起。",
    "Ned认为最可能是wildlings，并判断局势会恶化；Mance Rayder正在集结北方人，守夜人力量则不断衰弱。",
    "Catelyn听见Ned打算亲自越过长城处理此事，立即感到恐惧。",
    "Ned安慰她说Mance Rayder不值得他们害怕。",
    "Catelyn认为长城外还有更黑暗的事物，并不安地看向heart tree。",
    "Ned温和地把她的担忧归为Old Nan的故事，认为异鬼和children of the forest早已消失。",
    "Catelyn用当天发现direwolf反驳：此前人们同样认为活人不可能看见它。",
    "Ned带着无奈笑容结束争论，收剑起身，问她为何来到这里。",
    "Catelyn牵住丈夫的手，说明自己带来噩耗，并直接告诉他Jon Arryn已经去世。",
    "Ned遭受沉重打击；Jon Arryn曾在他年少时收养并教养他，如同第二位父亲。",
    "十五年前Jon Arryn又与Ned并肩对抗Mad King Aerys，并协助Robert Baratheon夺得Iron Throne。",
    "Ned难以接受消息，询问Jon Arryn的死讯是否确定。",
    "Catelyn确认信件有国王印章且由Robert亲笔书写；Jon Arryn病势迅速，来不及挽救。",
    "Ned在悲痛中仍先关心Jon Arryn的妻子Lysa和儿子Robert是否安好。",
    "Catelyn说母子已经返回Eyrie，并遗憾他们没有去Riverrun寻求家人陪伴。",
    "Ned指出Catelyn的叔叔Brynden正在Vale任Knight of the Gate，应能提供帮助。",
    "Catelyn承认Brynden会尽力，但仍担心姐姐Lysa失去丈夫后的处境。",
    "Ned建议Catelyn带孩子们去陪伴Lysa，用家庭的声音和欢乐缓解她的悲痛。",
    "Catelyn表示自己也想去，但信中还有另一消息：国王正前往Winterfell。",
    "Ned短暂无法理解，随后意识到Robert即将来访，悲色立刻转为惊喜。",
    "Catelyn无法分享他的喜悦；direwolf与鹿角的传言使她把国王来访视为可能的不祥事件。",
    "Ned决定通知在长城的弟弟Benjen，并让Maester Luwin派出最快的鸟送信。",
    "Catelyn估计王室队伍至少包括百名骑士、随从、自由骑手以及Cersei和孩子们，规模庞大。",
    "Ned认为Robert会顾及车队而慢行，这让Winterfell有更多时间准备。",
    "Catelyn补充，王后的兄弟们也在队伍中。",
    "Ned听后皱眉；他与Lannister家族关系冷淡，而Cersei及其兄弟在王廷拥有重要影响。",
    "Catelyn用一句话概括王室出行：国王到哪里，整个王国的权力与人员就跟到哪里。",
    "Ned期待见到王室孩子，却把最小的孩子记成仍在吃奶。",
    "Catelyn纠正Prince Tommen已经七岁，并提醒Ned谨慎说话，因为Lannister家族骄傲且容易记仇。",
    "Ned开始盘算宴会、歌手、狩猎、守卫和庞大队伍的食宿，亲密地抱怨老友带来的麻烦。",
]


KEY_NOTES = {
    1: "极短开篇把空间写成关系：godswood属于Ned和北方传统，却没有成为Catelyn的精神家园。",
    2: "南方树林像经过整理的花园，北方树林则保留原始状态；地景差异承载宗教与文化差异。",
    5: "Catelyn的信仰通过油、彩虹光和七面神呈现，明亮秩序与北方黑水、红叶形成对照。",
    7: "白骨、血手和注视的眼睛把圣树写得既神圣又令人不安，也贴合Catelyn的外来者感受。",
    9: "Ice再次出现，但视角从Bran的司法教育转为妻子观察丈夫事后承担的心理重量。",
    14: "`Winter is coming`既是家族箴言，也是教育原则：舒适不会永久存在，孩子必须提前学会面对困难。",
    15: "别家箴言强调荣耀，Stark箴言却是一句警告；这种克制定义了家族的自我想象。",
    18: "剑身波纹来自反复折叠锻造；Catelyn观察工艺，却明确不爱武器，保持她的独立视角。",
    19: "Ned说逃兵无法清楚表达恐惧，与Chapter 1中Jon从其眼睛判断恐惧相互补充。",
    21: "Ned把异常归入可理解的政治威胁：Mance集结、守夜人衰弱。这是理性解释，不是已证实结论。",
    25: "Ned像Chapter 1中的Bran一样把超自然担忧归于Old Nan；读者因看过序章而掌握更多信息。",
    26: "Catelyn用direwolf挑战“旧事物已经消失”的确定语气，是基于新证据的谨慎反驳。",
    28: "噩耗放在Ned清洗Ice之后出现，使死亡从公共司法转入私人情感。",
    29: "fosterage在贵族社会不仅是抚养安排，也能建立近似父子的持久政治与情感纽带。",
    30: "一段家族回忆迅速连接私人亲情、旧战争和当前王权，却不提前展开后文政治。",
    33: "Ned的第一反应从个人悲痛转向遗属安危，表现他把照料责任置于情绪表达之前。",
    38: "同一封信先带来死亡，再带来国王来访；私人哀伤与国家权力在家庭空间中汇合。",
    39: "Ned情绪骤变显示Robert对他不仅是国王，也是多年未见的亲密旧友。",
    40: "Catelyn把鹿角、direwolf和国王到访连成不祥预感；这是人物的解释，文本此时没有证明因果。",
    45: "三个Lannister各自占据王室核心位置，说明王后家族的影响不止来自婚姻。",
    46: "`the realm follows`把数百人的车队写成权力结构的移动：王室从不只是一个人。",
    48: "Catelyn管理语言风险，Ned则以老友情感看待来访；两人关注点分别偏向政治后果与私人重逢。",
    49: "Ned的抱怨带亲昵而非敌意；从哀痛到忙乱计划，结尾让家庭生活暂时重新流动。",
}


STAGES = [
    (1, 8, "本段通过Catelyn的感官和回忆对比南北信仰，使godswood同时成为宗教空间与婚姻差异的象征。"),
    (9, 18, "本段以夫妻间克制的对话延续处决余波，并把孩子教育、家族箴言和Ice连接起来。"),
    (19, 27, "本段围绕逃兵恐惧展开理性解释与旧故事之间的争论，形成读者知道更多的戏剧性反差。"),
    (28, 39, "本段借Jon Arryn死讯补足Ned的旧日亲情与政治经历，再把叙事转向Robert来访。"),
    (40, 49, "本段从Catelyn的不祥预感转向王室车队的现实规模，展现家庭、后勤和宫廷政治同时逼近Winterfell。"),
]


BACKGROUNDS = {
    2: "**文本事实：** Catelyn出身House Tully，故乡Riverrun位于南方Trident河流域；她是嫁入北方的外来者。",
    5: "**文本事实：** Faith of the Seven以七种面相理解神；sept是其礼拜场所。",
    6: "**文本事实：** House Stark遵循old gods传统；Ned为Catelyn修建sept，是对妻子信仰的实际尊重。",
    7: "**文本事实：** weirwood是旧神信仰的圣树，刻有面孔的古树称heart tree。",
    14: "**文本事实：** `Winter is coming`是House Stark的家族箴言。",
    21: "**文本事实：** Mance Rayder被称为King-beyond-the-Wall；守夜人负责长城防务，但人数正在减少。",
    25: "**文本事实：** children of the forest属于古老传说中的族群；Ned认为它们与异鬼一样早已消失。",
    29: "**文本事实：** Ned年轻时在Jon Arryn处foster，与Robert Baratheon一同受其教养。",
    30: "**文本事实：** 十五年前Ned、Robert与Jon Arryn反抗Aerys Targaryen；Robert随后成为国王。",
    34: "**文本事实：** Lysa是Catelyn的妹妹、Jon Arryn的妻子；Eyrie是House Arryn的家堡。",
    35: "**文本事实：** Brynden Tully是Catelyn的叔叔，目前在Vale担任Knight of the Gate。",
    41: "**文本事实：** Benjen Stark是Ned的弟弟，人在长城；maester常通过渡鸦传递远距离消息。",
    42: "**文本事实：** 王室出行包括骑士、retainers、freeriders、王后和王子女，不是私人拜访。",
    45: "**文本事实：** Cersei Lannister是王后；其兄弟Jaime属于Kingsguard，Tyrion也随王室同行。",
    48: "**文本事实：** Prince Tommen与Bran同为七岁；Catelyn担心Ned的随口玩笑冒犯Lannister家族。",
}


EXTRA_VOCAB = [
    ("godswood", "/ˈɡɒdzwʊd/", "n.", "神木林；城堡内的信仰树林", "本书旧神崇拜空间"),
    ("primal", "/ˈpraɪməl/", "adj.", "原始的；远古本能的", "强调未被人工驯化"),
    ("canopy", "/ˈkænəpi/", "n.", "树冠层；天篷", "树枝叶形成的顶部覆盖"),
    ("anoint", "/əˈnɔɪnt/", "v.", "涂圣油；举行傅油仪式", "宗教仪式用语"),
    ("sept", "/sept/", "n.", "七神圣堂", "Faith of the Seven的礼拜场所"),
    ("weirwood", "/ˈwɪərwʊd/", "n.", "鱼梁木；旧神圣树", "本书专名"),
    ("brood", "/bruːd/", "v.", "阴沉地笼罩；沉思", "此处把古树拟人化"),
    ("melancholy", "/ˈmelənkɒli/", "adj.", "忧郁的；哀伤的", "形容树脸神情"),
    ("sap", "/sæp/", "n.", "树液", "红色树液像血或眼泪"),
    ("swatch", "/swɒtʃ/", "n.", "一小块布料或材料", "此处为涂油皮革"),
    ("rueful", "/ˈruːfəl/", "adj.", "苦笑的；带懊恼的", "承认自己争不过对方"),
    ("grievous", "/ˈɡriːvəs/", "adj.", "令人悲痛的；严重的", "`grievous news`"),
    ("foster", "/ˈfɒstər/", "v.", "寄养并教养", "贵族子弟在另一家族成长"),
    ("comprehend", "/ˌkɒmprɪˈhend/", "v.", "理解；领会", "比understand更正式"),
    ("mercy", "/ˈmɜːrsi/", "n.", "宽慰；幸事；仁慈", "`some small mercy`指不幸中的一点安慰"),
    ("tidings", "/ˈtaɪdɪŋz/", "n.", "消息；音讯", "古风复数名词"),
    ("retainer", "/rɪˈteɪnər/", "n.", "贵族家臣；随从", "长期依附某家族服务"),
    ("wheelhouse", "/ˈwiːlhaʊs/", "n.", "大型有篷马车", "王室长途出行工具"),
    ("grimace", "/ˈɡrɪməs/", "v./n.", "皱脸；厌恶表情", "表现Ned对Lannister的不喜"),
    ("royal progress", "/ˈrɔɪəl ˈprəʊɡres/", "n.", "王室巡行", "君主带宫廷人员巡视领地"),
    ("guard your tongue", "/ɡɑːrd jər tʌŋ/", "idiom", "谨慎说话；管住嘴", "避免言语得罪人"),
]

VOCAB = BASE_VOCAB + EXTRA_VOCAB


def note(order):
    if order in KEY_NOTES: return KEY_NOTES[order]
    return next(text for start,end,text in STAGES if start <= order <= end)


def background(order):
    return BACKGROUNDS.get(order, "本段没有新增必须补充的世界观设定；重点在夫妻关系、信仰差异或消息推进。")


def vocab_for(text):
    seen=set(); out=[]
    for entry in VOCAB:
        if entry[0] not in seen and term_present(entry[0],text): out.append(entry); seen.add(entry[0])
    return out


def source_label(b):
    return f"PDF p.{b['page']}" if b['page']==b['end_page'] else f"PDF pp.{b['page']}–{b['end_page']}"


def build_markdown(blocks):
    pages={}
    for b in blocks: pages.setdefault(b['page'],[]).append(b['id'])
    lines=[
        "# *A Game of Thrones* Chapter 2 — CATELYN 逐段精读","",
        "> **阅读模式：** 无剧透｜人物姓名保留英文｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        "> **文本范围：** 原 PDF 第 25–29 页，共 49 个正文段落","",
        "## 本章导读","",
        "Catelyn在Winterfell的godswood找到处决归来的Ned。两人的谈话从孩子、家族箴言和逃兵的恐惧，转向Jon Arryn的死讯与King Robert即将到访。章节通过Catelyn的外来者视角，把北方信仰、夫妻亲密、旧日战争和王室政治放进同一场安静对话。","",
        "## 人物表","","| 人物 | 当前身份与关系 |","|---|---|",
        "| Catelyn Stark | 本章视角人物；出身House Tully，嫁给Ned |",
        "| Eddard “Ned” Stark | Lord of Winterfell；Catelyn的丈夫 |",
        "| Jon Arryn | Ned与Robert年少时的foster father，刚刚去世 |",
        "| Robert Baratheon | 国王；Ned的旧友，正前往Winterfell |",
        "| Lysa Arryn | Catelyn的妹妹、Jon Arryn的遗孀 |","",
        "## 专名与设定","","| 英文 | 中文解释 |","|---|---|",
        "| godswood | 神木林；城堡中的旧神信仰树林 |",
        "| weirwood / heart tree | 鱼梁木／心树；刻有人脸的旧神圣树 |",
        "| Faith of the Seven | 七神信仰；Catelyn成长环境中的宗教 |",
        "| Winter is coming | House Stark的家族箴言 |",
        "| Eyrie | 鹰巢城；House Arryn的家堡 |",
        "| Iron Throne | 铁王座；王权象征 |","",
        "## 段落目录","",
    ]
    for p,ids in pages.items(): lines.append(f"- [PDF 第 {p} 页：{ids[0]}–{ids[-1]}](#{ids[0].lower()})")
    lines += ["","---","","## 逐段精读",""]
    for b,summary in zip(blocks,SUMMARIES,strict=True):
        o=b['order']; bid=b['id']; original=b['text']
        lines += [f'<a id="{bid.lower()}"></a>',f"### {bid}","",f"**来源：** {source_label(b)}","","**英文原段**","",f"> {original}","","**难词与短语**",""]
        v=vocab_for(original)
        if v:
            lines += ["| 词语 | 音标 | 词性 | 此处含义 | 用法提示 |","|---|---|---|---|---|"]
            for t,ipa,pos,m,n in v: lines.append(f"| `{t}` | {ipa} | {pos} | {m} | {english_names(n)} |")
        else: lines.append("本段没有新增的四级以上重点词；重点留意语气和上下文。")
        lines += ["","**这一段说了什么**","",summary,"","**值得注意的地方**","",note(o),"","**背景与伏笔（无剧透）**","",background(o),"","[回到段落目录](#段落目录)","","---",""]
    lines += [
        "## 本章整体梳理","",
        "本章先以godswood呈现Catelyn在婚姻中的双重位置：她深爱Ned并管理Winterfell，却仍不是北方旧神传统的内部人。夫妻谈话随后把Chapter 1的处决重新解释为Ned必须承担的领主责任，也让逃兵的异常恐惧继续存在。Jon Arryn的死亡把私人记忆与国家政治带入Winterfell，而Robert的到访则意味着整个王室权力网络即将进入Stark家庭。","",
        "### 关键对照","",
        "- **南方花园／北方原始森林：** 对应Catelyn的出生文化与婚后环境。",
        "- **七神彩光／心树红眼：** 两套信仰以光线、颜色和空间呈现不同气质。",
        "- **Ned的理性／Catelyn的警觉：** Ned倾向用wildlings解释危险，Catelyn用direwolf提醒他旧传说未必已经死亡。",
        "- **私人悲痛／王室来访：** 同一封信把Jon Arryn之死和Robert到来并置，家庭无法与政治分开。","",
        "### 当前仍未解答的问题","",
        "1. 逃兵为何已经是本年第四人，他无法说明的恐惧来自哪里？",
        "2. Jon Arryn为何突然病逝？",
        "3. Robert为何亲自带着庞大王室队伍来到Winterfell？",
        "4. Catelyn对direwolf与鹿角的担忧是否只是巧合联想？","",
        "以上问题不使用后文章节答案。","","## 词汇总表","","| 词语 | 音标 | 词性 | 核心释义 |","|---|---|---|---|",
    ]
    all_text=' '.join(b['text'] for b in blocks); seen=set()
    for t,ipa,pos,m,_ in VOCAB:
        if t not in seen and term_present(t,all_text): lines.append(f"| `{t}` | {ipa} | {pos} | {m} |"); seen.add(t)
    lines += ["","## 使用说明","","- 人物姓名一律保留原始英文。","- 可使用如 `CH02-P027-025` 的段落编号继续提问。","- 背景讲解只采用截至当前段落可知的信息。",""]
    return '\n'.join(lines)


def build_map(blocks):
    records=[]
    for b,s in zip(blocks,SUMMARIES,strict=True):
        o=b['order']; records.append({"id":b['id'],"page":b['page'],"end_page":b['end_page'],"type":"paragraph","order":o,"original_text":b['text'],"translation":"","paragraph_explanation_zh":s,"reading_note_zh":note(o),"background_note_zh":background(o),"bbox":[0,0,0,0],"confidence":"high","refs":[],"insert_after":b['id']})
    all_text=' '.join(b['text'] for b in blocks); glossary=[]; seen=set()
    for t,_,_,m,n in VOCAB:
        if t not in seen and term_present(t,all_text): glossary.append({"term":t,"translation":m,"note":english_names(n)}); seen.add(t)
    return {"paper":{"title":"A Game of Thrones — Chapter 2 (CATELYN)","author":"George R. R. Martin","source_type":"pdf","language":"en","source_path":str(PDF),"pdf_page_range":[25,29],"reader_mode":"spoiler-free close reading; English personal names"},"blocks":records,"pages":[{"page":p,"block_ids":[b['id'] for b in blocks if b['page']<=p<=b['end_page']]} for p in range(25,30)],"figures":[],"glossary":glossary}


def main():
    blocks=extract_range(25,29,'CATELYN','CH02')
    if len(blocks)!=len(SUMMARIES): raise RuntimeError((len(blocks),len(SUMMARIES)))
    (OUT/'source_maps').mkdir(parents=True,exist_ok=True); (OUT/'notes').mkdir(parents=True,exist_ok=True)
    (OUT/'Chapter_02_CATELYN_精读.md').write_text(build_markdown(blocks),encoding='utf-8')
    (OUT/'source_maps'/'Chapter_02_source_map.json').write_text(json.dumps(build_map(blocks),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'notes'/'Chapter_02_notes.md').write_text('# Chapter 2 extraction notes\n\n- Source: selectable-text PDF pages 25–29.\n- 49 paragraph blocks after cross-page repair.\n- Personal names remain in original English.\n- Commentary is spoiler-free; no full translation requested.\n',encoding='utf-8')


if __name__=='__main__': main()
