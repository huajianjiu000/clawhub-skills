#!/usr/bin/env python3
"""
视频封面优化助手脚本
根据视频主题和平台自动生成封面优化方案
"""

import json
import random
from datetime import datetime

# 平台配置
PLATFORM_SPECS = {
    "douyin": {
        "size": "1080 × 1920",
        "ratio": "9:16",
        "max_size": "10MB",
        "title_length": "8-15字",
        "features": ["竖版为主", "高饱和度", "情绪化"]
    },
    "kuaishou": {
        "size": "1024 × 1024",
        "ratio": "1:1",
        "max_size": "10MB",
        "title_length": "10-18字",
        "features": ["方版常用", "接地气", "人脸占比高"]
    },
    "videonum": {
        "size": "1080 × 1080",
        "ratio": "1:1",
        "max_size": "5MB",
        "title_length": "12-20字",
        "features": ["朋友圈风格", "品牌感", "偏中年审美"]
    },
    "bilibili": {
        "size": "1920 × 1080",
        "ratio": "16:9",
        "max_size": "5MB",
        "title_length": "15-25字",
        "features": ["横版为主", "二次元风格", "支持动态封面"]
    },
    "xiaohongshu": {
        "size": "1080 × 1350",
        "ratio": "4:5",
        "max_size": "10MB",
        "title_length": "10-15字",
        "features": ["竖版为主", "精致感", "排版要求高"]
    }
}

# 配色方案
COLOR_SCHEMES = {
    "enthusiastic": {
        "name": "热情活力",
        "primary": "#FF4757",
        "secondary": "#FFA502",
        "text": "#FFFFFF",
        "suitable": "搞笑/美食/娱乐"
    },
    "tech": {
        "name": "科技感",
        "primary": "#2F3542",
        "secondary": "#57606F",
        "text": "#FFFFFF",
        "suitable": "数码/科技/测评"
    },
    "fresh": {
        "name": "清新自然",
        "primary": "#7BED9F",
        "secondary": "#70A1FF",
        "text": "#2C3A47",
        "suitable": "旅行/生活/美妆"
    },
    "premium": {
        "name": "高级质感",
        "primary": "#2C3A47",
        "secondary": "#FD7272",
        "text": "#FFFFFF",
        "suitable": "职场/知识/干货"
    },
    "contrast": {
        "name": "强对比",
        "primary": "#FBC531",
        "secondary": "#000000",
        "text": "#000000",
        "suitable": "搞笑/猎奇/反转"
    }
}

# 标题模板
TITLE_TEMPLATES = {
    "number": ["{}个技巧，让你的{}提升{}倍", "99%的人都不知道的{}个{}", "月薪{}和{}的差距在哪？"],
    "suspense": ["最后一步{}的人都会忽略...", "这个视频可能会改变你的{}", "看完这个视频，我{}了3天"],
    "painpoint": ["还在为{}烦恼？看完你就明白了", "为什么你做的{}总是不成功？", "{}的3个致命错误，你中了几个？"],
    "benefit": ["免费送你一份{}攻略，点击领取", "学会这招，{}问题轻松解决", "{}天学会{}，全套教程拿走"],
    "emotion": ["这就是我不想{}的理由", "成年人的崩溃，往往就在{}", "感谢曾经的看不起，如今让你{}不起"],
    "reverse": ["月薪{}的工作，我为什么抢着做？", "{}和{}的差距，颠覆你的认知", "{}毕业去{},家人骂我..."]
}

def analyze_topic(topic):
    """分析视频主题，返回相关标签"""
    keywords = {
        "美食": ["food", "cook", "eat"],
        "搞笑": ["funny", "laugh", "joke"],
        "知识": ["learn", "teach", "skill"],
        "科技": ["tech", "digital", "gadget"],
        "生活": ["life", "daily", "vlog"],
        "美妆": ["beauty", "makeup", "skin"],
        "旅行": ["travel", "trip", "tour"],
        "职场": ["work", "job", "career"]
    }
    
    topic_lower = topic.lower()
    tags = []
    for keyword, values in keywords.items():
        if any(v in topic_lower for v in values):
            tags.append(keyword)
    
    if not tags:
        tags = ["通用"]
    
    return tags

def generate_color_scheme(topic):
    """根据主题推荐配色方案"""
    tags = analyze_topic(topic)
    
    if "美食" in tags:
        return COLOR_SCHEMES["enthusiastic"]
    elif "科技" in tags:
        return COLOR_SCHEMES["tech"]
    elif "生活" in tags or "旅行" in tags:
        return COLOR_SCHEMES["fresh"]
    elif "职场" in tags or "知识" in tags:
        return COLOR_SCHEMES["premium"]
    elif "搞笑" in tags:
        return COLOR_SCHEMES["contrast"]
    else:
        return COLOR_SCHEMES["enthusiastic"]

def generate_title_suggestions(topic, platform):
    """生成标题建议"""
    suggestions = []
    
    # 数字型
    for template in TITLE_TEMPLATES["number"][:2]:
        title = template.format(3, topic, 3)
        suggestions.append({
            "type": "数字型",
            "title": title,
            "suitable": "知识/技巧/干货类内容"
        })
    
    # 悬念型
    for template in TITLE_TEMPLATES["suspense"][:2]:
        title = template.format("90%", topic)
        suggestions.append({
            "type": "悬念型",
            "title": title,
            "suitable": "揭秘/真相/隐藏内容"
        })
    
    # 痛点型
    for template in TITLE_TEMPLATES["painpoint"][:1]:
        title = template.format(topic)
        suggestions.append({
            "type": "痛点型",
            "title": title,
            "suitable": "问题解决/教程类内容"
        })
    
    # 反转型
    for template in TITLE_TEMPLATES["reverse"][:1]:
        title = template.format(3000, 30000)
        suggestions.append({
            "type": "反转型",
            "title": title,
            "suitable": "故事/反差/逆袭内容"
        })
    
    return suggestions

def generate_layout_suggestion(platform):
    """生成布局建议"""
    layouts = {
        "douyin": {
            "safe_area": "顶部0-350像素为安全区",
            "core_area": "中间区域为核心内容展示区",
            "bottom_area": "底部0-450像素可能被评论遮挡",
            "face_position": "人脸建议放在中上位置"
        },
        "kuaishou": {
            "face_ratio": "人脸占封面1/3以上效果更好",
            "center": "核心内容建议居中",
            "simple": "元素不宜过多"
        },
        "videonum": {
            "brand": "朋友圈展示，需要品牌感",
            "simple": "简洁大气，不要太夸张"
        },
        "bilibili": {
            "full": "横版封面充分利用横向空间",
            "ratio": "16:9比例在列表页显示更好"
        },
        "xiaohongshu": {
            "ratio": "4:5竖版，图片质量要求高",
            "layout": "排版精致感要强"
        }
    }
    
    return layouts.get(platform, layouts["douyin"])

def optimize_cover(topic, platform, audience=""):
    """生成封面优化方案"""
    tags = analyze_topic(topic)
    platform_info = PLATFORM_SPECS.get(platform, PLATFORM_SPECS["douyin"])
    color_scheme = generate_color_scheme(topic)
    title_suggestions = generate_title_suggestions(topic, platform)
    layout_suggestion = generate_layout_suggestion(platform)
    
    result = {
        "basic_info": {
            "topic": topic,
            "platform": platform,
            "audience": audience,
            "tags": tags,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "platform_specs": platform_info,
        "color_scheme": color_scheme,
        "title_suggestions": title_suggestions,
        "layout_suggestion": layout_suggestion,
        "tips": [
            "封面即内容，第一眼就要让用户看懂视频讲什么",
            "文字要简洁有力，控制在{}以内".format(platform_info["title_length"]),
            "使用{}配色，提升点击率".format(color_scheme["name"]),
            "核心内容放在安全区域内，避免被遮挡",
            "保持与账号整体风格一致"
        ]
    }
    
    return result

def main():
    """测试脚本"""
    result = optimize_cover(
        topic="美食探店",
        platform="douyin",
        audience="年轻人/美食爱好者"
    )
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
