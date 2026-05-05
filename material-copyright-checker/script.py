#!/usr/bin/env python3
"""
短视频素材版权查询助手 - 示例脚本

使用方法：
python demo.py
"""

from typing import Dict, List, Tuple


# 免费可商用素材网站
FREE_RESOURCES = {
    "图片": [
        {"name": "Unsplash", "url": "https://unsplash.com", "license": "CC0"},
        {"name": "Pexels", "url": "https://pexels.com", "license": "CC0"},
        {"name": "Pixabay", "url": "https://pixabay.com", "license": "CC0"},
        {"name": "Foodiesfeed", "url": "https://foodiesfeed.com", "license": "CC0"},
    ],
    "音乐": [
        {"name": "爱给网", "url": "https://aigei.com", "license": "免费"},
        {"name": "淘声网", "url": "https://tosound.com", "license": "免费"},
        {"name": "Free Music Archive", "url": "https://freemusicarchive.org", "license": "CC0"},
    ],
    "视频": [
        {"name": "Pexels Video", "url": "https://pexels.com/videos", "license": "CC0"},
        {"name": "Coverr", "url": "https://coverr.co", "license": "CC0"},
        {"name": "Life of Vids", "url": "https://lifeofvids.com", "license": "CC0"},
    ]
}


# 常见版权判断
COPYRIGHT_RULES = {
    "图片": {
        "安全": ["自己拍摄", "自己制作", "CC0图库", "购买正版"],
        "危险": ["百度图片", "微博图片", "小红书", "抖音截图", "博主原创"]
    },
    "音乐": {
        "安全": ["平台音乐库", "CC0音乐", "原创音乐", "购买授权"],
        "危险": ["热门歌曲", "影视原声", "演唱会", "付费歌曲"]
    },
    "视频": {
        "安全": ["自己拍摄", "CC0视频", "正版素材库", "购买授权"],
        "危险": ["电影片段", "电视剧", "综艺节目", "搬运他人"]
    }
}


def judge_copyright(source: str, material_type: str = "图片") -> Dict:
    """判断素材版权情况"""
    result = {
        "safe": False,
        "risk_level": "未知",
        "reason": "",
        "suggestions": []
    }
    
    source_lower = source.lower()
    rules = COPYRIGHT_RULES.get(material_type, {})
    
    # 检查是否安全
    for safe_keyword in rules.get("安全", []):
        if safe_keyword.lower() in source_lower:
            result["safe"] = True
            result["risk_level"] = "✅ 低风险"
            result["reason"] = f"来源：{safe_keyword}"
            return result
    
    # 检查是否危险
    for danger_keyword in rules.get("危险", []):
        if danger_keyword.lower() in source_lower:
            result["safe"] = False
            result["risk_level"] = "❌ 高风险"
            result["reason"] = f"⚠️ {danger_keyword}通常有版权保护"
            result["suggestions"] = get_suggestions(material_type)
            return result
    
    # 默认情况
    result["risk_level"] = "⚠️ 中风险"
    result["reason"] = "无法确定版权情况"
    result["suggestions"] = get_suggestions(material_type)
    
    return result


def get_suggestions(material_type: str) -> List[str]:
    """获取替代建议"""
    suggestions = [
        "建议使用正版授权素材",
        f"推荐免费可商用{material_type}网站："
    ]
    
    for resource in FREE_RESOURCES.get(material_type, []):
        suggestions.append(f"• {resource['name']} ({resource['license']})")
    
    return suggestions


def generate_report(source: str, material_type: str = "图片") -> str:
    """生成版权查询报告"""
    result = judge_copyright(source, material_type)
    
    report = f"""
🔍 短视频素材版权查询报告
{"="*35}

📦 素材类型：{material_type}
📍 素材来源：{source}

{"="*35}

🎯 版权判断：{result['risk_level']}

📝 判断理由：
{result['reason']}

"""
    
    if result["suggestions"]:
        report += "💡 建议：\n"
        for suggestion in result["suggestions"]:
            report += f"{suggestion}\n"
    
    if not result["safe"]:
        report += f"""
---
⚠️ 风险提示：
• 未经授权使用可能构成侵权
• 可能面临删除内容、下架、赔偿等后果
• 建议使用正版授权或免费可商用素材
"""
    
    return report


if __name__ == "__main__":
    print("短视频素材版权查询助手")
    print("=" * 40)
    
    # 测试案例
    test_cases = [
        ("小红书博主发布的图片", "图片"),
        ("Pexels视频素材", "视频"),
        ("抖音热门歌曲", "音乐"),
        ("我自己拍摄的照片", "图片"),
        ("电影预告片片段", "视频"),
    ]
    
    for source, material_type in test_cases:
        print(generate_report(source, material_type))
        print()
