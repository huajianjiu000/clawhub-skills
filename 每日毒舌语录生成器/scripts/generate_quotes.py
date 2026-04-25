#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日毒舌语录生成器 - 主脚本
生成毒舌语录、毒鸡汤、人间清醒等文案
"""

import random

# 语录数据库
QUOTES_DB = {
    "毒鸡汤": [
        "努力不一定会成功，但躺着真的很舒服。",
        "别假装努力，结果不会陪你演戏。",
        "你以为你拼尽全力，其实只是感动了自己。",
        "失败是成功之母，但成功的人不会失败这么多次。",
        "少壮不努力，老大怪水逆。",
        "不是读书没用，是你读的那点书没用。",
        "有人总说顺其自然，其实只是别无选择。",
        "人生就像打电话，不是你先挂就是他先挂。",
        "你那么努力，难怪还是这么穷。",
        "咸鱼翻身还是咸鱼。",
        "只要功夫深，铁杵磨成针，但有人把针磨成铁杵。",
        "有钱人真的快乐吗？不，有钱人的快乐你想象不到。",
        "万事开头难，中间难，结尾更难。",
        "上帝是公平的，给了你丑的外表，还会给你低的智商。",
        "你的智商余额已不足，请及时充值。",
        "别人比你优秀不可怕，可怕的是比你优秀的人比你更努力。",
        "有些事不是你努力了就有用，关键在于你努力的方向对不对。",
        "条条大路通罗马，而有人就出生在罗马。",
        "年轻时不努力，老了只能遗憾。",
        "有时候不逼自己一把，永远不知道自己有多优秀……然后失败。",
    ],
    "人间清醒": [
        "你之所以焦虑，是因为你追求的不是自己真正想要的。",
        "不要总想着改变别人，先学会改变自己。",
        "成年人最好的默契是不言而喻。",
        "圈子不同，不必强融。",
        "所有的内向，都是因为聊不来的人太多。",
        "别人对你的态度，取决于你的实力。",
        "没有实力的时候，你的要求就是矫情。",
        "你若盛开，蝴蝶自来；你若精彩，天自安排。",
        "不要高估你和任何人的关系。",
        "学会独处，是一个人最好的奢侈品。",
        "时间识人，落难识心。",
        "少说多做，是最快的捷径。",
        "人生没有白走的路，每一步都算数。",
        "越努力越幸运，这话是真的。",
        "你的善良要带点锋芒。",
        "不要为了合群，丢掉自己的个性。",
        "真正能让你走远的，从来都是自律和积极。",
        "世界上只有两种东西不能直视：太阳和人心。",
        "认清自己，比认清别人更重要。",
        "人生最可怕的不是失败，而是你本可以。",
    ],
    "毒舌怼人": [
        "你这么努力，难怪还是这么穷。",
        "你的脸皮真是比城墙还厚。",
        "你不是脑子进水，是脑子本来就没装什么。",
        "别人都有人做了，你只能做自己……的那个版本。",
        "你长得很有创意，活得却很有勇气。",
        "上帝给你关上一扇门，顺手把你的窗也关了。",
        "你就是传说中那种「明明可以靠脸吃饭，却偏要靠才华」的人——结果才华也没有。",
        "你这么能说，怎么不去卖保险。",
        "有些人出现在你的生命里，就是为了给你上一课然后离开。",
        "你说话能不能过过脑子，它招你惹你了。",
        "你的智商跟你的体重一样，需要控制了。",
        "别把自己看得太重，没有你地球一样转。",
        "你以为你是谁，地球离开你照样转。",
        "不是所有事情努力了就有用，但你不努力肯定没结果。",
        "有些人出现在你的生命里，就是为了告诉你：你看，他比你还惨。",
        "你这么能熬夜，阎王都佩服。",
        "不要试图叫醒一个装睡的人，你也叫不醒。",
        "你那不叫直爽，叫没教养。",
        "你的格局决定了你看到的世界。",
        "你若盛开，清风自来；你若枯萎，苍蝇满天。",
    ],
    "摆烂文学": [
        "努力不一定有结果，但不努力一定会很舒服。",
        "躺平是一种态度，不是一种逃避。",
        "我不是不努力，我只是选择另一种活法——活着。",
        "人生苦短，及时行乐。明天的事，明天再说。",
        "别卷了，我选择躺。",
        "当代青年精神状态：能躺着绝不坐着。",
        "摆烂一时爽，一直摆烂一直爽。",
        "我已经放弃挣扎了，挺好的。",
        "不要PUA我，我不想努力了。",
        "卷不动了，让我躺一会儿。",
        "目标定太高不好，万一实现了呢。",
        "我已经放弃挣扎了，挺好的。",
        "我不焦虑，我只是在思考人生。",
        "低欲望生活，高质量摆烂。",
        "与其内卷，不如躺平。",
        "人生没有标准答案，不卷也是一种选择。",
        "躺平是门技术活，卷不过就躺平吧。",
        "适度躺平，有益健康。",
        "躺平哲学：能坐着绝不站着，能躺着绝不坐着。",
        "放过自己，也是一种成长。",
    ],
    "职场毒舌": [
        "别把加班当努力，结果才重要。",
        "公司离开你照样转，别把自己想得太重要。",
        "工资不涨，头发先秃了。",
        "你的努力在老板眼里，只值一个「辛苦了」。",
        "不要为了工作牺牲健康，不值得。",
        "职场不相信眼泪，只相信KPI。",
        "会做的不如会说的，会说的不如会拍的。",
        "升职加薪的秘密：要么有人，要么有钱。",
        "工作是为了生活，不是为了等死。",
        "别把平台当能力，离开平台你什么都不是。",
        "年纪轻轻就躺平？不，我只是选择了性价比最高的生活方式。",
        "工资到手，还完花呗，还剩多少？",
        "打工人，打工魂，打工都是人下人。",
        "辞职不敢，躺平不能，这就是中年危机。",
        "加班到深夜，明天依然要早起，这就是生活。",
        "你的工资，够你看病吗？",
        "工作不是为了梦想，是为了生存。",
        "职场生存法则：要么忍，要么滚，要么装死。",
        "别跟我谈理想，我的理想是不上班。",
        "老板画的饼，看得见吃不着。",
    ],
}

# 分类emoji映射
CATEGORY_EMOJI = {
    "毒鸡汤": "💀",
    "人间清醒": "🧠",
    "毒舌怼人": "🔥",
    "摆烂文学": "🛋️",
    "职场毒舌": "💼",
}

def get_random_quotes(category: str = None, count: int = 5) -> dict:
    """获取随机语录"""
    categories = [category] if category and category in QUOTES_DB else list(QUOTES_DB.keys())
    
    result = {}
    for cat in categories:
        quotes = random.sample(QUOTES_DB[cat], min(count, len(QUOTES_DB[cat])))
        result[cat] = quotes
    
    # 随机金句
    all_quotes = []
    for quotes in QUOTES_DB.values():
        all_quotes.extend(quotes)
    daily_quote = random.choice(all_quotes)
    
    return {
        "categories": result,
        "daily_quote": daily_quote,
    }

def format_output(result: dict, category: str = None) -> str:
    """格式化输出"""
    output = "🔥 **每日毒舌语录**\n\n"
    
    emoji_map = CATEGORY_EMOJI
    
    if category and category in result["categories"]:
        # 单分类输出
        cat = category
        emoji = emoji_map.get(cat, "📝")
        output += f"{emoji} **【{cat}】**\n"
        for i, quote in enumerate(result["categories"][cat], 1):
            output += f"{i}. {quote}\n"
    else:
        # 全部分类输出
        for cat, quotes in result["categories"].items():
            emoji = emoji_map.get(cat, "📝")
            output += f"{emoji} **【{cat}】**\n"
            for i, quote in enumerate(quotes[:5], 1):
                output += f"{i}. {quote}\n"
            output += "\n"
    
    output += f"💡 **今日金句**：「{result['daily_quote']}」\n"
    output += f"\n✨ 关注我，每天获取扎心语录~"
    
    return output

def main(category: str = None, count: int = 5):
    """主函数"""
    if not category:
        result = get_random_quotes(None, count)
    elif category in QUOTES_DB:
        result = get_random_quotes(category, count)
    else:
        # 匹配关键词
        category_lower = category.lower()
        matched_cat = None
        
        keyword_map = {
            "毒鸡汤": ["毒鸡汤", "鸡汤", "扎心"],
            "人间清醒": ["人间清醒", "清醒", "通透"],
            "毒舌怼人": ["毒舌", "怼人", "怼"],
            "摆烂文学": ["摆烂", "躺平", "摸鱼"],
            "职场毒舌": ["职场", "工作", "打工"],
        }
        
        for cat, keywords in keyword_map.items():
            for keyword in keywords:
                if keyword in category_lower:
                    matched_cat = cat
                    break
            if matched_cat:
                break
        
        if matched_cat:
            result = get_random_quotes(matched_cat, count)
        else:
            result = get_random_quotes(None, count)
    
    return format_output(result, category)

if __name__ == "__main__":
    # 测试
    print(main("职场"))
