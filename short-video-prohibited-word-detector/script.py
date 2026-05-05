#!/usr/bin/env python3
"""
短视频违禁词检测助手 - 示例脚本

使用方法：
python demo.py

功能：
1. 违禁词检测
2. 风险评级
3. 替换建议
"""

import re
from typing import List, Dict, Tuple

# 违禁词库（简化版）
PROHIBITED_WORDS = {
    # 广告法违禁词
    "absolute": [
        "最", "第一", "顶级", "极品", "绝佳", "独一无二",
        "首发", "独家", "唯一", "冠军", "领先", "世界级", "国家级"
    ],
    # 医疗健康类
    "medical": [
        "特效药", "神药", "根治", "治愈率", "延年益寿", "返老还童",
        "壮阳", "丰乳", "缩阴", "处方药", "药到病除"
    ],
    # 金融投资类
    "financial": [
        "稳赚", "保本", "高收益", "收益率", "涨停板", "内部消息",
        "资金盘", "原始股", "月入", "日赚", "财务自由"
    ],
    # 低俗色情类
    "vulgar": [
        "艳照", "约炮", "一夜情", "裸聊", "色情"
    ],
    # 诱导外链类
    "external": [
        "加微信", "加QQ", "淘宝下单", "拼多多", "外站链接"
    ]
}

# 替代词映射
REPLACEMENTS = {
    "最": "很",
    "第一": "领先",
    "顶级": "优质",
    "特效": "有效",
    "保准": "有望",
    "保证": "承诺",
    "100%": "高达",
    "彻底": "有效",
    "月入": "额外收入",
    "日赚": "额外赚取"
}


def detect_prohibited_words(text: str) -> List[Dict]:
    """检测文本中的违禁词"""
    findings = []
    
    for category, words in PROHIBITED_WORDS.items():
        for word in words:
            if word in text:
                # 计算位置
                positions = [m.start() for m in re.finditer(word, text)]
                for pos in positions:
                    findings.append({
                        "word": word,
                        "category": category,
                        "position": pos,
                        "replacement": REPLACEMENTS.get(word, "***")
                    })
    
    return findings


def get_risk_level(findings: List[Dict]) -> str:
    """根据检测结果评估风险等级"""
    if not findings:
        return "✅ 低风险"
    
    categories = set(f["category"] for f in findings)
    
    if "financial" in categories or "vulgar" in categories:
        return "❌ 高风险"
    elif "medical" in categories or "absolute" in categories:
        return "⚠️ 中风险"
    else:
        return "⚠️ 低风险"


def generate_report(text: str) -> str:
    """生成违禁词检测报告"""
    findings = detect_prohibited_words(text)
    risk_level = get_risk_level(findings)
    
    report = f"""
🔍 违禁词检测报告
{'='*30}

📝 原始文案：
{text}

🔎 检测结果：
"""
    
    if not findings:
        report += "✅ 未发现违禁词"
    else:
        report += f"⚠️ 发现 {len(findings)} 处违禁词：\n\n"
        
        # 按类别分组
        categories = {}
        for f in findings:
            cat = f["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(f)
        
        for cat, items in categories.items():
            cat_names = {
                "absolute": "📢 广告法违禁词",
                "medical": "💊 医疗健康类",
                "financial": "💰 金融投资类",
                "vulgar": "🎭 低俗色情类",
                "external": "📵 诱导外链类"
            }
            report += f"\n{cat_names.get(cat, cat)}：\n"
            for item in items:
                report += f"  • 「{item['word']}」 → 建议改为「{item['replacement']}」\n"
    
    report += f"\n{'='*30}\n"
    report += f"风险评级：{risk_level}\n"
    
    if risk_level.startswith("❌"):
        report += "\n⚠️ 建议：避免使用此类文案，可能被平台限流或封号"
    elif risk_level.startswith("⚠️"):
        report += "\n⚠️ 建议：修改后发布，降低被限流风险"
    else:
        report += "\n✅ 可以正常发布"
    
    return report


if __name__ == "__main__":
    print("短视频违禁词检测助手")
    print("=" * 30)
    
    # 测试文案
    test_texts = [
        "这款面膜含有特效成分，使用后能快速美白，淡斑祛痘，让你拥有完美肌肤！",
        "加入我们，月入十万不是梦，轻松实现财务自由！",
        "今天天气真好，来分享下我的日常"
    ]
    
    for text in test_texts:
        print(generate_report(text))
        print()
