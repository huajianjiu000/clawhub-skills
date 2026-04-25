#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
朋友圈九宫格配图文案生成器 - 主脚本
根据场景和风格生成朋友圈配文
"""

import random

# 文案数据库
COPYWRITING_DB = {
    "文艺清新": {
        "下午茶": [
            "偷得浮生半日闲",
            "一杯茶，一本书，一个下午",
            "把节奏放慢，生活是件浪漫的事",
            "今日份的糖分来源☕",
            "生活需要仪式感",
            "用一杯咖啡的时间，治愈一周的疲惫",
            "阳光正好，微风不燥",
            "简单的日子，也闪闪发光",
        ],
        "旅行": [
            "风吹又日晒，自由又自在",
            "换个地方看人间烟火",
            "背包、相机、目的地，下一站未知",
            "山川湖海，天地与爱",
            "答案在路上，自由在风里",
            "被好风景收买，剩下的全是好心情",
            "旅行的意义，是找到回家的路",
            "走走停停，或南或北",
        ],
        "日常": [
            "人间烟火气，最抚凡人心",
            "日子平淡，好在我喜欢",
            "普通的日子，也泛着光",
            "生活原本沉闷，但跑起来就有风",
            "今日份的开心~",
            "把普通的日子过得浪漫一点",
            "认真生活的人，都会被生活善待",
            "小日子，小生活，小美好",
        ],
        "美食": [
            "四方食事，不过一碗人间烟火",
            "人间不值得，但美食值得",
            "生活不止诗和远方，还有眼前的美食",
            "好好吃饭，好好生活",
            "食物是记忆的载体，味蕾记得一切",
            "今日份美食记录📝",
            "唯有美食不可辜负",
            "吃喜欢的东西，过可爱的人生",
        ],
    },
    "搞笑幽默": {
        "日常": [
            "今天的不开心就到此为止吧",
            "人生苦短，再来一碗",
            "别问，问就是在躺平",
            "周一到周五，努力搬砖",
            "钱包，你还好吗",
            "周一：我可以 周二：我能行 周三：放过我",
            "日复一日的工作，需要美食来治愈",
            "我的日常：穷、忙、饿",
        ],
        "美食": [
            "工资到手，先去吃顿好的",
            "减肥第三天，失败了",
            "吃饱了才有力气减肥嘛",
            "我不是饿，只是嘴巴寂寞",
            "今日份的快乐也是美食给的",
            "人生苦短，先吃再说",
            "没有什么是一顿饭解决不了的",
            "唯美食与爱不可辜负",
        ],
        "自拍": [
            "今天也是美貌与才华并存的一天",
            "自拍三千，只取一张",
            "今天的妆容：精致穷",
            "原图直出，拒绝容貌焦虑",
            "今天的自己，又好看了几分",
            "不是自恋，是事实",
            "这该死的美貌，我爱了",
        ],
    },
    "情感治愈": {
        "友情": [
            "有些人，光是遇见就很幸运",
            "懂你奇奇怪怪，陪你可可爱爱",
            "愿岁岁年年，身边人不变",
            "朋友是疲惫生活的解药",
            "和喜欢的人做喜欢的事",
            "你是我永远可以打扰的人",
            "时间会筛选，留下来的都是真朋友",
            "朋友是另一个自己",
        ],
        "爱情": [
            "世界很大，幸福很小",
            "陪伴是最长情的告白",
            "愿所有美好都如约而至",
            "有你在的每天都是晴天",
            "你是例外，也是偏爱",
            "愿我如星君如月，夜夜流光相皎洁",
            "是你，让平凡的日子泛着光",
            "和喜欢的人在一起，做什么都好",
        ],
        "自我": [
            "和自己和解，和世界和平相处",
            "偶尔脆弱，偶尔坚强",
            "愿你历经千帆，归来仍是少年",
            "好好爱自己，是终身浪漫的开始",
            "允许自己偶尔摆烂",
            "生活是自己的，尽情打扮，尽情可爱",
            "做自己的太阳，无需借别人的光",
        ],
    },
    "商务专业": {
        "职场": [
            "保持热爱，奔赴山海",
            "努力的意义是看更大的世界",
            "每天进步一点点",
            "认真生活的人最闪闪发光",
            "挑战自我，成就无限可能",
            "工作是为了更好的生活",
            "越努力，越幸运",
            "每一个认真生活的人，都值得被尊重",
        ],
        "个人品牌": [
            "专业铸就品质，品质赢得信任",
            "用专业创造价值",
            "持续学习，不断成长",
            "只为更优秀的自己",
            "精益求精，追求卓越",
            "做时间的朋友，与坚持同行",
            "你的选择，决定你的高度",
            "深耕专业，创造价值",
        ],
    },
}

# 话题标签库
MOMENTS_TAGS = {
    "文艺清新": ["#文艺 #慢生活 #生活仪式感 #岁月静好 #小确幸 #今日份的温柔"],
    "搞笑幽默": ["#沙雕日常 #笑死我了 #今日份快乐 #沙雕网友 #欢乐一刻"],
    "情感治愈": ["#情感 #治愈 #温暖 #正能量 #人间值得 #情感共鸣"],
    "商务专业": ["#职场 #成长 #自我提升 #正能量 #加油打工人 #女性成长"],
}

# 场景关键词映射
SCENE_KEYWORDS = {
    "下午茶": ["下午茶", "咖啡", "奶茶", "甜品", "饮品", "茶"],
    "旅行": ["旅行", "旅游", "打卡", "景点", "出游", "假期"],
    "日常": ["日常", "记录", "生活", "今天", "周末"],
    "美食": ["美食", "吃饭", "餐厅", "吃", "厨房", "烹饪"],
    "自拍": ["自拍", "照片", "拍照", "美照", "look"],
}

def detect_scene(text: str) -> str:
    """检测场景"""
    text_lower = text.lower()
    for scene, keywords in SCENE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text_lower:
                return scene
    return "日常"

def detect_style(text: str) -> str:
    """检测风格"""
    text_lower = text.lower()
    
    if any(word in text_lower for word in ["文艺", "清新", "简约", "意境"]):
        return "文艺清新"
    elif any(word in text_lower for word in ["搞笑", "幽默", "沙雕", "逗"]):
        return "搞笑幽默"
    elif any(word in text_lower for word in ["情感", "治愈", "温暖", "友情", "爱情"]):
        return "情感治愈"
    elif any(word in text_lower for word in ["职场", "商务", "专业", "工作"]):
        return "商务专业"
    
    return "文艺清新"  # 默认风格

def generate_copywriting(scene: str = None, style: str = None, count: int = 9) -> dict:
    """生成配文"""
    scene = scene or "日常"
    style = style or "文艺清新"
    
    # 获取该风格的文案
    style_db = COPYWRITING_DB.get(style, COPYWRITING_DB["文艺清新"])
    scene_copies = style_db.get(scene, style_db.get("日常", []))
    
    # 生成9宫格配文
    selected = []
    pool = scene_copies.copy()
    for i in range(min(count, 9)):
        if pool:
            selected.append(pool.pop(random.randint(0, len(pool) - 1)))
        else:
            selected.append(f"图{i+1}的小故事")
    
    # 统一文案
    if scene_copies:
        unified = random.choice(scene_copies)
    else:
        unified = "今日份的美好~"
    
    # 话题标签
    tags = MOMENTS_TAGS.get(style, MOMENTS_TAGS["文艺清新"])
    
    return {
        "unified": unified,
        "nine_grid": selected,
        "tags": tags,
        "scene": scene,
        "style": style,
    }

def format_output(result: dict) -> str:
    """格式化输出"""
    output = f"🎨 **朋友圈九宫格配图文案**\n\n"
    output += f"📍 **场景**：{result['scene']}  |  🎭 **风格**：{result['style']}\n\n"
    
    output += f"📝 **统一文案**：\n「{result['unified']}」\n\n"
    
    output += f"📸 **分图配文**：\n"
    emoji_map = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
    for i, copy in enumerate(result['nine_grid']):
        output += f"{emoji_map[i]} {copy}\n"
    
    output += f"\n🏷️ **话题标签**：\n{' '.join(result['tags'])}\n\n"
    
    output += f"💡 **发圈小技巧**：配图色调统一更美观哦~\n"
    
    return output

def main(scene: str = None, style: str = None):
    """主函数"""
    if not scene and not style:
        # 默认生成
        result = generate_copywriting("日常", "文艺清新")
    else:
        detected_scene = detect_scene(scene) if scene else "日常"
        detected_style = detect_style(style) if style else "文艺清新"
        result = generate_copywriting(detected_scene, detected_style)
    
    return format_output(result)

if __name__ == "__main__":
    # 测试
    print(main("周末下午茶", "文艺清新"))
