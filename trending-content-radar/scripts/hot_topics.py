#!/usr/bin/env python3
"""
热点选题雷达
多平台热点追踪与选题推荐
"""

import random
from datetime import datetime
from typing import List, Dict

# 领域配置
DOMAIN_CONFIG = {
    "美食": {
        "hot_words": ["网红美食", "隐藏菜单", "必点推荐", "避雷指南", "宝藏店铺"],
        "trending_topics": ["周末去哪吃", "宝藏小店", "懒人食谱", "减脂餐", "夜宵推荐"]
    },
    "美妆": {
        "hot_words": ["平替", "种草", "测评", "教程", "避雷"],
        "trending_topics": ["换季护肤", "早八妆容", "学生党必备", "通勤妆容", "成分党"]
    },
    "穿搭": {
        "hot_words": ["ootd", "搭配", "显瘦", "平价", "小个子"],
        "trending_topics": ["一周穿搭", "换季穿搭", "职场穿搭", "约会穿搭", "通勤穿搭"]
    },
    "数码": {
        "hot_words": ["测评", "对比", "横评", "选购指南", "避坑"],
        "trending_topics": ["新机发布", "数码好物", "平板推荐", "键盘推荐", "耳机测评"]
    },
    "游戏": {
        "hot_words": ["攻略", "教程", "上分", "测评", "联机"],
        "trending_topics": ["新游戏", "赛季指南", "冷门好游", "外设推荐", "手游推荐"]
    },
    "教育": {
        "hot_words": ["学习方法", "提分技巧", "考研", "考证", "经验分享"],
        "trending_topics": ["学习技巧", "备考攻略", "时间管理", "书单推荐", "技能提升"]
    },
    "生活": {
        "hot_words": ["好物推荐", "生活技巧", "家居", "收纳", "日常"],
        "trending_topics": ["租房改造", "收纳技巧", "家居好物", "租房好物", "极简生活"]
    },
    "情感": {
        "hot_words": ["两性", "婚姻", "恋爱", "原生家庭", "自我成长"],
        "trending_topics": ["情感故事", "两性关系", "自我提升", "人际交往", "心理分析"]
    }
}

# 平台热点词库（模拟数据）
PLATFORM_HOT_DATA = {
    "抖音": [
        {"topic": "大学生食堂隐藏美食", "heat": 95, "duration": "中期热点", "category": "美食"},
        {"topic": "MBTI人格穿搭指南", "heat": 92, "duration": "长期热点", "category": "穿搭"},
        {"topic": "AI工具使用教程", "heat": 88, "duration": "长期热点", "category": "数码"},
        {"topic": "00后职场生存法则", "heat": 85, "duration": "中期热点", "category": "情感"},
        {"topic": "周末低成本约会", "heat": 82, "duration": "中期热点", "category": "生活"}
    ],
    "快手": [
        {"topic": "农村真实生活记录", "heat": 90, "duration": "长期热点", "category": "生活"},
        {"topic": "手工diy教程", "heat": 87, "duration": "中期热点", "category": "生活"},
        {"topic": "宠物搞笑瞬间", "heat": 85, "duration": "长期热点", "category": "生活"},
        {"topic": "家乡特产推荐", "heat": 80, "duration": "中期热点", "category": "美食"},
        {"topic": "搞笑剧情段子", "heat": 78, "duration": "长期热点", "category": "娱乐"}
    ],
    "B站": [
        {"topic": "数码产品深度测评", "heat": 93, "duration": "长期热点", "category": "数码"},
        {"topic": "学习方法论分享", "heat": 91, "duration": "长期热点", "category": "教育"},
        {"topic": "新番动画安利", "heat": 88, "duration": "短期热点", "category": "娱乐"},
        {"topic": "职场技能提升", "heat": 86, "duration": "长期热点", "category": "教育"},
        {"topic": "游戏攻略详解", "heat": 84, "duration": "中期热点", "category": "游戏"}
    ],
    "小红书": [
        {"topic": "平价好物大合集", "heat": 94, "duration": "长期热点", "category": "生活"},
        {"topic": "春季穿搭种草", "heat": 92, "duration": "季节热点", "category": "穿搭"},
        {"topic": "护肤成分党入门", "heat": 89, "duration": "长期热点", "category": "美妆"},
        {"topic": "考研上岸经验贴", "heat": 87, "duration": "中期热点", "category": "教育"},
        {"topic": "租房改造日记", "heat": 85, "duration": "长期热点", "category": "生活"}
    ],
    "视频号": [
        {"topic": "正能量故事分享", "heat": 91, "duration": "长期热点", "category": "情感"},
        {"topic": "家乡风景展示", "heat": 88, "duration": "中期热点", "category": "生活"},
        {"topic": "家庭教育心得", "heat": 86, "duration": "长期热点", "category": "教育"},
        {"topic": "美食制作教程", "heat": 84, "duration": "长期热点", "category": "美食"},
        {"topic": "才艺展示合集", "heat": 82, "duration": "中期热点", "category": "娱乐"}
    ]
}

# 切入角度模板
ANGLE_TEMPLATES = {
    "教程向": [
        "手把手教你如何{}",
        "{}入门指南，看这一篇就够了",
        "{}保姆级教程，建议收藏",
        "学会这{}步，彻底掌握{}"
    ],
    "情感向": [
        "作为一个{}，我有话想说",
        "{}后的真实感受，太扎心了",
        "为什么越来越多人开始{}",
        "{}这件事，只有经历过才懂"
    ],
    "盘点向": [
        "{}Top10排行榜",
        "盘点那些{}的{}",
        "{}合集，看完涨知识",
        "{}大公开，你知道几个"
    ],
    "对比向": [
        "{}前 vs {}后，变化太大了",
        "同样是{}，差距怎么这么大",
        "{}和{}，到底哪个更好",
        "为什么别人{}而你却{}"
    ],
    "测评向": [
        "{}真实测评，结果出乎意料",
        "花费{}元测评{}，值不值",
        "{}天使用报告，真实感受",
        "{}深度测评，优缺点全说"
    ]
}

# 内容类型
CONTENT_TYPES = ["教程", "娱乐", "情感", "干货", "种草", "测评", "盘点", "剧情"]


def get_hot_topics(domain=None, platform=None, limit=5) -> List[Dict]:
    """获取热点列表"""
    all_topics = []
    
    # 聚合所有平台热点
    platforms = [platform] if platform else list(PLATFORM_HOT_DATA.keys())
    
    for p in platforms:
        if p in PLATFORM_HOT_DATA:
            for topic in PLATFORM_HOT_DATA[p]:
                # 按领域过滤
                if domain and topic["category"] != domain:
                    continue
                topic_copy = topic.copy()
                topic_copy["source"] = p
                all_topics.append(topic_copy)
    
    # 按热度排序
    all_topics.sort(key=lambda x: x["heat"], reverse=True)
    
    return all_topics[:limit]


def generate_topic_angles(topic: str, category: str) -> List[Dict]:
    """生成选题切入角度"""
    angles = []
    
    # 获取该领域的热词
    domain_hot = DOMAIN_CONFIG.get(category, {}).get("hot_words", [])
    hot_word = random.choice(domain_hot) if domain_hot else "技巧"
    
    for angle_type, templates in ANGLE_TEMPLATES.items():
        template = random.choice(templates)
        
        # 填充模板
        filled = template.format(
            random.choice(["这个", "你", "别人", ""]),
            random.choice([hot_word, topic[:4], "方法", "技巧"])
        )
        
        # 预估效果
        effect_score = random.randint(70, 98)
        stars = "⭐" * (effect_score // 20 + 1)
        
        angles.append({
            "type": angle_type,
            "title": filled,
            "effect_score": effect_score,
            "stars": stars
        })
    
    return angles


def generate_content_suggestion(topic: str, category: str) -> Dict:
    """生成内容建议"""
    # 最佳时长
    duration_options = {
        "教程": "3-5分钟",
        "娱乐": "15-60秒",
        "情感": "1-3分钟",
        "干货": "2-5分钟",
        "种草": "30-60秒",
        "测评": "2-5分钟",
        "盘点": "3-8分钟",
        "剧情": "1-3分钟"
    }
    
    # 最佳发布时间
    publish_times = {
        "抖音": "12:00-13:00, 18:00-20:00, 21:00-23:00",
        "快手": "6:00-8:00, 12:00-13:00, 18:00-20:00",
        "B站": "18:00-22:00",
        "小红书": "7:00-9:00, 12:00-13:00, 18:00-21:00",
        "视频号": "12:00-13:00, 20:00-22:00"
    }
    
    # 标题建议
    title_templates = [
        f"原来{topic}这么简单！",
        f"{topic}的真相，必须知道！",
        f"学会{topic}，{random.choice(['效率翻倍', '少走弯路', '省钱又省力'])}",
        f"关于{topic}，我有话要说",
        f"揭秘{random.choice(['行业内幕', '真实原因', '背后逻辑'])}：{topic}"
    ]
    
    return {
        "best_duration": duration_options.get(category, "1-3分钟"),
        "best_time": random.choice(list(publish_times.values())),
        "title_suggestions": random.sample(title_templates, 3)
    }


def calculate_topic_value(heat: int, difficulty: int) -> Dict:
    """计算选题价值"""
    # 变现潜力计算
    monetization = random.randint(40, 95)
    
    # 综合推荐度
    recommend_score = (heat * 0.5 + (100 - difficulty * 20) * 0.3 + monetization * 0.2)
    
    return {
        "heat": heat,
        "difficulty": "⭐" * difficulty + "⭐" * (5 - difficulty),
        "monetization": "⭐" * (monetization // 20 + 1),
        "recommend_score": recommend_score,
        "recommend_stars": "⭐" * (int(recommend_score) // 20 + 1)
    }


def format_report(topics: List[Dict], domain=None, platform=None) -> str:
    """格式化报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    output = [
        f"## 📡 热点选题雷达",
        f"### 今日热点 TOP{len(topics)} | {today}"
    ]
    
    if domain:
        output.append(f"**筛选领域**：{domain}")
    if platform:
        output.append(f"**来源平台**：{platform}")
    
    output.append("\n---\n")
    
    for i, topic in enumerate(topics, 1):
        angles = generate_topic_angles(topic["topic"], topic["category"])
        suggestion = generate_content_suggestion(topic["topic"], topic["category"])
        value = calculate_topic_value(topic["heat"], random.randint(1, 4))
        
        output.extend([
            f"### 🔥 TOP {i}: {topic['topic']}",
            f"**热度指数**：{topic['heat']}/100",
            f"**平台来源**：{topic['source']} · {topic['duration']}",
            f"**内容分类**：{topic['category']}",
            "",
            "#### 🎯 推荐选题角度"
        ])
        
        # 输出角度表格
        output.append("| 角度 | 内容方向 | 预估效果 |")
        output.append("|------|---------|---------|")
        for angle in angles[:3]:
            output.append(f"| {angle['type']} | {angle['title']} | {angle['stars']} |")
        
        output.extend([
            "",
            "#### 💡 创作建议"
        ])
        
        output.extend([
            f"- **最佳时长**：{suggestion['best_duration']}",
            f"- **切入角度**：从用户痛点或好奇心入手",
            f"- **标题方向**：" + " | ".join([f"`{t}`" for t in suggestion['title_suggestions']]),
            f"- **发布时间**：{suggestion['best_time']}",
            f"- **生命周期**：{topic['duration']}，建议{'立即' if '爆发' in topic['duration'] else '尽快'}创作",
            "",
            "---"
        ])
    
    # 汇总表格
    output.extend([
        "",
        "### 📊 选题价值总览",
        "",
        "| 排名 | 选题 | 热度 | 难度 | 变现 | 推荐度 |",
        "|------|------|------|------|------|--------|"
    ])
    
    for i, topic in enumerate(topics, 1):
        value = calculate_topic_value(topic["heat"], random.randint(1, 4))
        output.append(f"| {i} | {topic['topic'][:15]}... | {topic['heat']} | {value['difficulty']} | {value['monetization']} | {value['recommend_stars']} |")
    
    output.extend([
        "",
        "### ⚠️ 注意事项",
        "1. 热点选题需注意平台规则，避免违规",
        "2. 原创内容质量比蹭热点更重要",
        "3. 同一热点可做系列内容，持续输出",
        "4. 观察评论区反馈，挖掘新的选题方向"
    ])
    
    return "\n".join(output)


if __name__ == "__main__":
    # 测试
    topics = get_hot_topics(limit=5)
    print(format_report(topics))
