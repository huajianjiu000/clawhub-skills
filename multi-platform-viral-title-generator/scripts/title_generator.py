#!/usr/bin/env python3
"""
多平台爆款标题生成器
支持抖音、快手、视频号、B站、头条号五大平台
"""

import random
from typing import List, Dict, Optional

class TitleGenerator:
    """标题生成器核心类"""
    
    # 各平台标题特征配置
    PLATFORM_CONFIG = {
        "抖音": {
            "length_range": (15, 30),
            "style": "悬念感、情绪化、短平快",
            "elements": ["悬念", "数字", "情绪", "痛点", "好奇心"],
            "hashtag_prefix": "#",
            "emoji_usage": "可用"
        },
        "快手": {
            "length_range": (10, 25),
            "style": "接地气、烟火气、真实感",
            "elements": ["真实", "共鸣", "故事性", "情感", "生活化"],
            "hashtag_prefix": "$",
            "emoji_usage": "常用"
        },
        "视频号": {
            "length_range": (15, 30),
            "style": "价值感、情感连接、正能量",
            "elements": ["价值", "情感", "共鸣", "启发", "温暖"],
            "hashtag_prefix": "#",
            "emoji_usage": "少用"
        },
        "B站": {
            "length_range": (20, 50),
            "style": "系列感、知识性、有深度",
            "elements": ["系列", "深度", "解析", "测评", "教程"],
            "hashtag_prefix": "#",
            "emoji_usage": "可用"
        },
        "头条号": {
            "length_range": (15, 35),
            "style": "新闻感、资讯感、信息价值",
            "elements": ["新闻", "资讯", "曝光", "揭秘", "解读"],
            "hashtag_prefix": "#",
            "emoji_usage": "不用"
        }
    }
    
    # 爆款标题模板
    TITLE_TEMPLATES = {
        "悬念型": [
            "原来[主题]还能[动作]，后悔没早知道",
            "为什么[人群]都在[动作]这个[主题]",
            "看完这个[主题]，我[情绪反应]了",
            "[数字]个关于[主题]的秘密，第[数字]个最关键",
            "这[主题]的[特点]，99%的人都不知道",
        ],
        "数字型": [
            "[数字]个[主题]技巧，看完就会",
            "[数字]分钟学会[主题]，太简单了",
            "[数字]年[人群]总结的[主题]经验",
            "学会这[数字]点，[主题]轻松搞定",
            "[数字]天[主题]速成法，亲测有效",
        ],
        "情绪型": [
            "太[情绪]了！这个[主题]必须分享",
            "终于找到了！[主题]的正确方式",
            "哭了！[人群]必看的[主题]指南",
            "笑死了，[主题]还能这么玩",
            "太绝了！[主题]的正确打开方式",
        ],
        "痛点型": [
            "[人群]最怕的[主题]问题，终于解决了",
            "[人群]必看！[主题]避坑指南",
            "别再[错误动作]了！正确[主题]方式",
            "[主题]踩雷无数次，终于找到好方法",
            "[人群]注意！[主题]的[注意事项]",
        ],
        "价值型": [
            "[主题]核心逻辑，一篇讲透",
            "全网最全[主题]攻略，收藏备用",
            "[主题]入门到精通，看这一篇就够",
            "关于[主题]，这几点必须知道",
            "[主题]完整指南，建议收藏",
        ]
    }
    
    def __init__(self):
        self.platforms = list(self.PLATFORM_CONFIG.keys())
    
    def generate_titles(
        self,
        topic: str,
        platforms: Optional[List[str]] = None,
        count: int = 5,
        tone: str = "中性"
    ) -> Dict[str, List[Dict]]:
        """
        生成多平台标题
        
        Args:
            topic: 视频主题/关键词
            platforms: 指定平台列表，None表示全部
            count: 每个平台生成数量
            tone: 情绪基调
            
        Returns:
            包含各平台标题的字典
        """
        if platforms is None:
            platforms = self.platforms
            
        results = {}
        
        for platform in platforms:
            config = self.PLATFORM_CONFIG.get(platform, self.PLATFORM_CONFIG["抖音"])
            titles = self._generate_platform_titles(
                topic=topic,
                platform=platform,
                config=config,
                count=count,
                tone=tone
            )
            results[platform] = titles
            
        return results
    
    def _generate_platform_titles(
        self,
        topic: str,
        platform: str,
        config: Dict,
        count: int,
        tone: str
    ) -> List[Dict]:
        """为单个平台生成标题"""
        titles = []
        
        # 根据平台选择合适的模板类型
        template_pool = self._get_platform_templates(platform)
        
        for i in range(count):
            template = random.choice(template_pool)
            title = self._fill_template(template, topic, tone)
            hashtag = self._generate_hashtags(topic, platform)
            
            titles.append({
                "title": title,
                "hashtags": hashtag,
                "platform": platform,
                "length": len(title)
            })
            
        return titles
    
    def _get_platform_templates(self, platform: str) -> List[List[str]]:
        """根据平台选择模板"""
        if platform == "抖音":
            return [
                self.TITLE_TEMPLATES["悬念型"],
                self.TITLE_TEMPLATES["数字型"],
                self.TITLE_TEMPLATES["情绪型"]
            ]
        elif platform == "快手":
            return [
                self.TITLE_TEMPLATES["情绪型"],
                self.TITLE_TEMPLATES["痛点型"],
                self.TITLE_TEMPLATES["悬念型"]
            ]
        elif platform == "视频号":
            return [
                self.TITLE_TEMPLATES["价值型"],
                self.TITLE_TEMPLATES["情绪型"],
                self.TITLE_TEMPLATES["悬念型"]
            ]
        elif platform == "B站":
            return [
                self.TITLE_TEMPLATES["价值型"],
                self.TITLE_TEMPLATES["数字型"],
                self.TITLE_TEMPLATES["悬念型"]
            ]
        else:  # 头条号
            return [
                self.TITLE_TEMPLATES["价值型"],
                self.TITLE_TEMPLATES["数字型"],
                self.TITLE_TEMPLATES["情绪型"]
            ]
    
    def _fill_template(self, template: str, topic: str, tone: str) -> str:
        """填充模板"""
        replacements = {
            "[主题]": topic,
            "[动作]": random.choice(["做", "学", "用", "知道", "了解"]),
            "[人群]": random.choice(["新手", "上班族", "年轻人", "家长", "所有人"]),
            "[数字]": str(random.randint(3, 9)),
            "[情绪]": random.choice(["震惊", "感动", "惊喜", "后悔", "激动"]),
            "[情绪反应]": random.choice(["哭了", "笑了", "心动了", "后悔了", "感动了"]),
            "[特点]": random.choice(["真相", "内幕", "秘密", "技巧", "方法"]),
            "[错误动作]": random.choice(["瞎折腾", "乱花钱", "盲目跟风", "不听劝", "乱来"]),
            "[注意事项]": random.choice(["禁忌", "雷区", "坑", "陷阱", "红线"]),
        }
        
        result = template
        for key, value in replacements.items():
            result = result.replace(key, value)
            
        return result
    
    def _generate_hashtags(self, topic: str, platform: str) -> List[str]:
        """生成话题标签"""
        config = self.PLATFORM_CONFIG.get(platform, {})
        prefix = config.get("hashtag_prefix", "#")
        
        base_tags = [topic]
        generic_tags = []
        
        if platform == "抖音":
            generic_tags = ["热门", "推荐", "干货", "收藏", "学习"]
        elif platform == "快手":
            generic_tags = ["记录生活", "真实", "分享", "日常"]
        elif platform == "视频号":
            generic_tags = ["必看", "收藏", "推荐", "好物分享"]
        elif platform == "B站":
            generic_tags = ["知识分享", "教程", "干货", "必看"]
        else:
            generic_tags = ["资讯", "推荐", "热点", "关注"]
        
        all_tags = base_tags + generic_tags[:2]
        return [f"{prefix}{tag}" for tag in all_tags]


def main():
    """主函数示例"""
    generator = TitleGenerator()
    
    topic = input("请输入视频主题：").strip()
    if not topic:
        topic = "职场穿搭"
    
    print(f"\n正在为「{topic}」生成多平台爆款标题...\n")
    
    results = generator.generate_titles(
        topic=topic,
        count=3,
        tone="中性"
    )
    
    for platform, titles in results.items():
        print(f"\n## {platform}标题")
        for i, item in enumerate(titles, 1):
            print(f"{i}. {item['title']}")
            if item['hashtags']:
                print(f"   {', '.join(item['hashtags'])}")


if __name__ == "__main__":
    main()
