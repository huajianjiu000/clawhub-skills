#!/usr/bin/env python3
"""
短视频爆款标题生成器
自动分析平台特性，生成高点击率标题
"""

import random
import re

# 平台特性配置
PLATFORM_CONFIG = {
    "抖音": {
        "max_length": 30,
        "style": "短平快、悬念感、情绪共鸣",
        "elements": ["悬念", "数字", "对比", "情绪"],
        "emoji": True
    },
    "快手": {
        "max_length": 28,
        "style": "接地气、真实感、亲近感",
        "elements": ["真实", "对比", "情绪", "数字"],
        "emoji": True
    },
    "B站": {
        "max_length": 50,
        "style": "知识型、系列感、深度内容",
        "elements": ["知识", "数字", "系列", "专业"],
        "emoji": False
    },
    "小红书": {
        "max_length": 25,
        "style": "种草风、emoji、生活感",
        "elements": ["种草", "emoji", "生活", "真实"],
        "emoji": True
    },
    "视频号": {
        "max_length": 35,
        "style": "情感向、引发讨论、正能量",
        "elements": ["情感", "讨论", "共鸣", "正能量"],
        "emoji": True
    }
}

# 标题模板库
TITLE_TEMPLATES = {
    "悬念类": [
        "【揭秘】{topic}背后的真相，{ending}",
        "竟然还有人不知道{topic}？{result}",
        "{topic}的{secret}，看完{reaction}",
        "为什么你的{topic}总是失败？{answer}",
        "{topic}的{time}，{celebrity}都{action}了"
    ],
    "数字类": [
        "{number}个{topic}的{method}，第{order}个最关键",
        "只需{number}步，让你彻底掌握{topic}",
        "{number}年经验总结的{topic}技巧，建议收藏",
        "{number}%的人都不知道的{topic}，太可惜了",
        "学会这{number}个{topic}，{benefit}不是梦"
    ],
    "对比类": [
        "同样是{topic}，为什么别人{success}而你{failure}？",
        "前后对比太震撼！{topic}前后竟然差距这么大",
        "别人家的{topic} VS 你家的{topic}，扎心了",
        "{topic}前 vs {topic}后，判若两人",
        "月薪3000和30000的{topic}，差距在哪里？"
    ],
    "情绪类": [
        "看完这个{topic}，我哭了😭",
        "太真实了！这就是{topic}的{feeling}",
        "{topic}这件事，真的{emotion}到我了",
        "终于有人敢说真话了！{topic}的{truth}",
        "救命！{topic}这件事，被他说透了"
    ],
    "利益类": [
        "学会这个{topic}，{benefit}效率翻倍",
        "收藏这一篇，{topic}问题全搞定",
        "自媒体人必看的{topic}指南，建议收藏",
        "{benefit}！这个{topic}技巧太实用了",
        "手把手教你{topic}，看完少走3年弯路"
    ],
    "种草类": [
        "亲测有效！这个{topic}真的绝绝子",
        "救命神器！用了{topic}之后我{result}",
        "吹爆这个{topic}，用完直接离不开",
        "私藏已久的{topic}好物，忍不住分享",
        "{topic}天花板！这也太好用了吧"
    ]
}

# 敏感词列表（简化版，实际使用需要完整词库）
SENSITIVE_WORDS = ["最", "第一", "国家级", "顶级", "极品", "绝对", "完美"]


def generate_title(topic, platform="抖音", num_options=3):
    """生成爆款标题"""
    config = PLATFORM_CONFIG.get(platform, PLATFORM_CONFIG["抖音"])
    
    results = []
    used_templates = []
    
    # 选择标题类型组合
    title_types = random.sample(list(TITLE_TEMPLATES.keys()), min(3, len(TITLE_TEMPLATES)))
    
    for i, title_type in enumerate(title_types):
        templates = TITLE_TEMPLATES[title_type]
        template = random.choice(templates)
        
        # 填充模板
        filled_title = fill_template(template, topic, config)
        
        # 检查长度
        if len(filled_title) > config["max_length"]:
            filled_title = filled_title[:config["max_length"]-3] + "..."
        
        # 计算预估点击率
        click_score = calculate_click_score(filled_title, config)
        
        results.append({
            "title": filled_title,
            "type": title_type,
            "click_score": click_score,
            "elements": identify_elements(filled_title)
        })
    
    # 按点击率排序
    results.sort(key=lambda x: x["click_score"], reverse=True)
    
    return results[:num_options], config


def fill_template(template, topic, config):
    """填充标题模板"""
    replacements = {
        "{topic}": topic,
        "{ending}": random.choice(["看完恍然大悟", "后悔知道太晚了", "太实用了", "赶紧收藏"]),
        "{result}": random.choice(["涨知识了", "太牛了", "学到了", "太香了"]),
        "{secret}": random.choice(["秘密", "真相", "诀窍", "内幕"]),
        "{reaction}": random.choice(["彻底被圈粉", "惊呆了", "跪服", "太绝了"]),
        "{time}": random.choice(["昨天", "今天", "刚刚", "最近"),
        "{celebrity}": random.choice(["明星", "网红", "大咖", "博主"]),
        "{action}": random.choice(["在用", "在推", "在学", "在夸"]),
        "{answer}": random.choice(["答案出乎意料", "看完秒懂", "太简单了", "原来如此"]),
        "{number}": str(random.randint(3, 10)),
        "{order}": str(random.randint(1, 3)),
        "{method}": random.choice(["技巧", "方法", "秘诀", "攻略"]),
        "{benefit}": random.choice(["效率", "效果", "收益", "成绩"]),
        "{success}": random.choice(["轻松上手", "快速涨粉", "月入过万", "爆火出圈"]),
        "{failure}": random.choice(["总是失败", "越做越差", "没人看", "被限流"]),
        "{feeling}": random.choice(["无奈", "心酸", "崩溃", "崩溃"]),
        "{emotion}": random.choice(["感动", "震撼", "治愈", "戳心"]),
        "{truth}": random.choice(["内幕", "真相", "本质", "核心"]),
        "{name}": topic.split("的")[0] if "的" in topic else topic
    }
    
    result = template
    for key, value in replacements.items():
        result = result.replace(key, value)
    
    # 添加emoji
    if config["emoji"]:
        emoji = random.choice(["🔥", "💡", "✨", "👏", "🤔"])
        if emoji not in result:
            result = emoji + result
    
    return result


def calculate_click_score(title, config):
    """计算预估点击率"""
    score = 60  # 基础分
    
    # 数字加分
    if re.search(r'\d+', title):
        score += 15
    
    # 悬念加分
    if any(word in title for word in ["竟然", "原来", "为什么", "真相", "揭秘"]):
        score += 12
    
    # 情绪加分
    if any(word in title for word in ["太", "竟然", "竟然", "哭", "救命"]):
        score += 10
    
    # 长度适中加分
    if 15 <= len(title) <= config["max_length"]:
        score += 8
    
    # emoji加分（抖音类平台）
    if config["emoji"] and any(char in title for char in ["🔥", "💡", "✨", "👇", "🙌"]):
        score += 5
    
    return min(score, 100)


def identify_elements(title):
    """识别标题中的爆款要素"""
    elements = []
    
    if re.search(r'\d+', title):
        elements.append("数字")
    if any(word in title for word in ["竟然", "原来", "为什么", "真相", "揭秘", "？"]):
        elements.append("悬念")
    if any(word in title for word in ["太", "竟然", "哭", "救命", "绝绝子"]):
        elements.append("情绪")
    if "VS" in title or "vs" in title or any(word in title for word in ["对比", "差距"]):
        elements.append("对比")
    if any(word in title for word in ["收藏", "必看", "指南", "技巧"]):
        elements.append("利益")
    
    return elements if elements else ["普通"]


def check_sensitive_words(title):
    """检测敏感词"""
    found = []
    for word in SENSITIVE_WORDS:
        if word in title:
            found.append(word)
    return found


def format_output(titles, config):
    """格式化输出"""
    output = ["## 🎯 爆款标题推荐", f"### 平台：{config['style']}\n"]
    
    for i, item in enumerate(titles, 1):
        click_stars = "⭐" * (item["click_score"] // 20)
        
        output.append(f"{i}. **{item['title']}**")
        output.append(f"   - 要素：{' + '.join(item['elements'])}")
        output.append(f"   - 点击率预估：{click_stars}\n")
    
    return "\n".join(output)


if __name__ == "__main__":
    # 测试
    topic = "视频剪辑"
    titles, config = generate_title(topic, "抖音", 3)
    print(format_output(titles, config))
