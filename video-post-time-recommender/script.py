#!/usr/bin/env python3
"""
视频发布时间推荐器 - 示例脚本

使用方法：
python demo.py
"""

from datetime import datetime, timedelta
from typing import Dict, List


# 各平台发布时间推荐
PLATFORM_SCHEDULES = {
    "抖音": {
        "泛娱乐": {
            "weekday": ["12:00-13:00", "18:00-21:00"],
            "weekend": ["14:00-16:00", "20:00-22:00"]
        },
        "知识干货": {
            "weekday": ["7:00-9:00", "12:00-13:00"],
            "weekend": ["10:00-12:00"]
        },
        "种草带货": {
            "weekday": ["12:00-13:00", "20:00-22:00"],
            "weekend": ["13:00-15:00", "19:00-21:00"]
        },
        "搞笑娱乐": {
            "weekday": ["18:00-22:00"],
            "weekend": ["15:00-18:00", "21:00-23:00"]
        }
    },
    "快手": {
        "泛娱乐": {
            "weekday": ["11:00-13:00", "18:00-20:00"],
            "weekend": ["12:00-14:00", "19:00-21:00"]
        },
        "带货直播": {
            "weekday": ["20:00-23:00"],
            "weekend": ["14:00-17:00", "20:00-23:00"]
        },
        "情感故事": {
            "weekday": ["21:00-23:00"],
            "weekend": ["20:00-22:00"]
        }
    },
    "视频号": {
        "泛娱乐": {
            "weekday": ["7:00-9:00", "12:00-13:00"],
            "weekend": ["10:00-12:00"]
        },
        "新闻资讯": {
            "weekday": ["7:00-8:00", "12:00-13:00"],
            "weekend": ["9:00-11:00"]
        },
        "朋友圈分享": {
            "weekday": ["12:00-13:00", "18:00-20:00"],
            "weekend": ["11:00-13:00", "19:00-21:00"]
        }
    },
    "B站": {
        "知识区": {
            "weekday": ["18:00-22:00"],
            "weekend": ["14:00-18:00"]
        },
        "游戏区": {
            "weekday": ["20:00-24:00"],
            "weekend": ["15:00-20:00"]
        },
        "美食区": {
            "weekday": ["17:00-20:00"],
            "weekend": ["11:00-13:00", "18:00-21:00"]
        }
    },
    "小红书": {
        "种草笔记": {
            "weekday": ["12:00-13:00", "19:00-21:00"],
            "weekend": ["10:00-12:00", "15:00-17:00"]
        },
        "干货分享": {
            "weekday": ["7:00-9:00", "12:00-13:00"],
            "weekend": ["9:00-11:00"]
        },
        "Vlog": {
            "weekday": ["18:00-21:00"],
            "weekend": ["14:00-17:00"]
        }
    }
}


def is_weekend(dt: datetime = None) -> bool:
    """判断是否为周末"""
    if dt is None:
        dt = datetime.now()
    return dt.weekday() >= 5  # 周六=5, 周日=6


def get_content_type_emoji(content_type: str) -> str:
    """获取内容类型emoji"""
    emojis = {
        "泛娱乐": "🎭",
        "知识干货": "📚",
        "种草带货": "🛍️",
        "搞笑娱乐": "😂",
        "带货直播": "📺",
        "情感故事": "💕",
        "新闻资讯": "📰",
        "朋友圈分享": "👥",
        "知识区": "🎓",
        "游戏区": "🎮",
        "美食区": "🍜",
        "种草笔记": "💄",
        "干货分享": "💡",
        "Vlog": "📹"
    }
    return emojis.get(content_type, "📱")


def generate_schedule(platform: str, content_type: str) -> str:
    """生成发布时间推荐"""
    if platform not in PLATFORM_SCHEDULES:
        return f"不支持的平台：{platform}"
    
    if content_type not in PLATFORM_SCHEDULES[platform]:
        available_types = list(PLATFORM_SCHEDULES[platform].keys())
        return f"该平台不支持的内容类型，可选：{', '.join(available_types)}"
    
    today_is_weekend = is_weekend()
    day_type = "weekend" if today_is_weekend else "weekday"
    time_slots = PLATFORM_SCHEDULES[platform][content_type][day_type]
    
    result = f"\n{get_content_type_emoji(content_type)} {platform} - {content_type}推荐：\n"
    result += "-" * 30 + "\n"
    
    for slot in time_slots:
        result += f"⏰ {slot}\n"
    
    return result


def get_recommendation(platform: str, content_type: str = None) -> str:
    """获取完整推荐"""
    report = f"""
📅 视频发布时间推荐报告
{"="*35}

📱 平台：{platform}
📝 内容类型：{content_type or '全部'}

"""
    
    if content_type:
        report += generate_schedule(platform, content_type)
    else:
        # 如果没有指定类型，显示所有类型
        for ct in PLATFORM_SCHEDULES.get(platform, {}):
            report += generate_schedule(platform, ct)
            report += "\n"
    
    # 添加当前时间建议
    now = datetime.now()
    report += f"""
---
💡 提示：
• 当前时间：{now.strftime('%Y-%m-%d %H:%M')} ({'周末' if is_weekend(now) else '工作日'})
• 以上为通用建议，具体以账号数据为准
• 新账号建议多测试不同时段
"""
    
    return report


if __name__ == "__main__":
    print("视频发布时间推荐器")
    print("=" * 40)
    
    # 示例查询
    print(get_recommendation("抖音", "美食探店"))
    print(get_recommendation("快手", "带货直播"))
    print(get_recommendation("小红书"))
