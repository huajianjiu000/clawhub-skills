#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
短视频话题标签生成器 - 主脚本
根据视频主题智能生成话题标签
"""

import random
import re

# 标签数据库（从references加载）
HASHTAG_DB = {
    "美食": ["#美食探店", "#网红餐厅", "#本地美食", "#美食推荐", "#吃货必备", "#美食日记", "#美食分享", "#探店打卡", "#快手美食", "#抖音美食", "#下饭菜", "#家常菜", "#美食教程", "#舌尖上的美味", "#今日份美食"],
    "搞笑": ["#搞笑", "#搞笑视频", "#搞笑段子", "#沙雕日常", "#笑死我了", "#太逗了", "#爆笑来袭", "#沙雕队友", "#搞笑合集", "#每日笑点", "#快乐源泉", "#沙雕视频", "#解压", "#爆笑视频", "#欢乐一刻"],
    "萌宠": ["#萌宠", "#宠物", "#猫猫", "#狗狗", "#可爱", "#小动物", "#宠物日记", "#萌宠来袭", "#吸猫", "#撸狗", "#铲屎官", "#宠物有爱", "#萌宠日常", "#家有萌宠", "#宠物治愈"],
    "旅行": ["#旅行", "#旅行打卡", "#旅游攻略", "#小众旅行", "#周末去哪玩", "#旅行vlog", "#自驾游", "#旅行记录", "#风景", "#治愈系风景", "#旅行的意义", "#说走就走", "#热门景点", "#拍照技巧", "#旅拍"],
    "美妆": ["#美妆", "#化妆教程", "#日常妆容", "#新手化妆", "#彩妆", "#护肤", "#变美", "#化妆技巧", "#素人改造", "#美妆分享", "#口红试色", "#眼妆教程", "#底妆分享", "#护肤心得", "#美妆教程"],
    "穿搭": ["#穿搭", "#每日穿搭", "#ootd", "#时尚穿搭", "#穿搭分享", "#平价穿搭", "#学生党穿搭", "#通勤穿搭", "#显瘦穿搭", "#搭配技巧", "#韩系穿搭", "#男生穿搭", "#女生穿搭", "#穿搭灵感", "#衣橱必备"],
    "生活": ["#生活", "#记录生活", "#我的日常", "#vlog", "#生活记录", "#日常分享", "#生活碎片", "#生活方式", "#慢生活", "#享受生活", "#宅家日常", "#独居生活", "#生活小妙招", "#日常碎片", "#热爱生活"],
    "情感": ["#情感", "#情感语录", "#情感共鸣", "#治愈", "#文案", "#情感文案", "#扎心文案", "#深夜话题", "#人间清醒", "#情感树洞", "#走心文案", "#情感故事", "#两性关系", "#情感驿站", "#情感励志"],
    "职场": ["#职场", "#职场干货", "#打工人", "#工作使我快乐", "#升职加薪", "#职场技巧", "#简历优化", "#面试技巧", "#职场女性", "#工作日常", "#加油打工人", "#副业", "#自由职业", "#自我提升", "#职场进化论"],
    "教育": ["#教育", "#学习方法", "#自律", "#自我提升", "#读书", "#书单推荐", "#知识分享", "#考证", "#上岸", "#学习vlog", "#studyaccount", "#学霸养成", "#时间管理", "#专注力", "#成长"],
    "科技": ["#科技", "#ai", "#人工智能", "#数码", "#手机", "#黑科技", "#科技改变生活", "#数码测评", "#智能家居", "#科技前沿", "#数码好物", "#手机摄影", "#ai工具", "#科技数码", "#数码科技"],
}

# 通用热词
HOT_TAGS = ["#热门", "#推荐", "#上热门", "#dou上热门", "#发现", "#推荐", "#必看", "#建议收藏", "#种草", "#干货"]

# 分类关键词映射
CATEGORY_KEYWORDS = {
    "美食": ["美食", "吃", "餐厅", "做饭", "菜", "吃货", "烹饪", "烘焙", "甜品", "奶茶", "咖啡", "下午茶"],
    "搞笑": ["搞笑", "段子", "沙雕", "逗", "笑", "幽默", "整蛊", "恶搞", "欢乐", "快乐"],
    "萌宠": ["宠物", "猫", "狗", "萌", "可爱", "动物", "铲屎", "萌宠", "小动物"],
    "旅行": ["旅行", "旅游", "打卡", "风景", "景点", "自驾", "出行", "游记", "酒店"],
    "美妆": ["美妆", "化妆", "妆容", "护肤", "口红", "彩妆", "素颜", "美容", "变美"],
    "穿搭": ["穿搭", "衣服", "衣服", "服装", "裙子", "裤子", "搭配", "时尚", "OOTD"],
    "生活": ["生活", "日常", "记录", "日记", "分享", "日常", "居家", "宅家"],
    "情感": ["情感", "爱情", "友情", "心情", "治愈", "扎心", "文案", "语录", "心理"],
    "职场": ["职场", "工作", "面试", "简历", "升职", "#打工人", "同事", "领导", "上班"],
    "教育": ["学习", "读书", "考试", "考证", "知识", "自律", "成长", "教育", "课堂"],
    "科技": ["科技", "数码", "手机", "电脑", "AI", "人工智能", "科技", "测评", "黑科技"],
}

def detect_category(content: str) -> list:
    """根据内容检测类别"""
    categories = []
    content_lower = content.lower()
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in content_lower:
                if category not in categories:
                    categories.append(category)
                break
    
    if not categories:
        categories = ["生活"]  # 默认归类到生活
    
    return categories

def generate_hashtags(content: str, count: int = 10) -> dict:
    """生成话题标签"""
    categories = detect_category(content)
    
    result = {
        "main_tags": [],
        "long_tail_tags": [],
        "hot_tags": []
    }
    
    # 主推标签：从相关分类中选取
    main_pool = []
    for cat in categories:
        main_pool.extend(HASHTAG_DB.get(cat, []))
    main_pool = list(set(main_pool))  # 去重
    random.shuffle(main_pool)
    result["main_tags"] = main_pool[:min(5, len(main_pool))]
    
    # 长尾标签：从其他分类补充
    other_categories = [c for c in HASHTAG_DB.keys() if c not in categories]
    long_tail_pool = []
    for cat in other_categories[:5]:  # 取5个其他分类
        long_tail_pool.extend(HASHTAG_DB.get(cat, []))
    random.shuffle(long_tail_pool)
    result["long_tail_tags"] = long_tail_pool[:min(8, len(long_tail_pool))]
    
    # 蹭热点标签
    random.shuffle(HOT_TAGS)
    result["hot_tags"] = HOT_TAGS[:3]
    
    return result

def format_output(hashtags: dict, content: str) -> str:
    """格式化输出"""
    output = f"📊 **话题标签推荐**\n\n"
    output += f"📝 根据「{content}」推荐：\n\n"
    
    output += f"🔥 **主推标签**（高热度）\n"
    output += " ".join(hashtags["main_tags"]) + "\n\n"
    
    output += f"📌 **精准标签**（长尾流量）\n"
    output += " ".join(hashtags["long_tail_tags"]) + "\n\n"
    
    output += f"⭐ **蹭热点标签**（当前热门）\n"
    output += " ".join(hashtags["hot_tags"]) + "\n\n"
    
    output += f"💡 使用建议：选择5-8个标签效果最佳\n"
    output += f"📏 标签总长度：{' '.join(hashtags['main_tags'] + hashtags['long_tail_tags'][:3] + hashtags['hot_tags'])}"
    
    return output

def main(content: str):
    """主函数"""
    if not content:
        return "请输入视频主题或内容描述，我将为你推荐合适的标签~"
    
    hashtags = generate_hashtags(content)
    return format_output(hashtags, content)

if __name__ == "__main__":
    # 测试
    test_input = "搞笑段子合集"
    print(main(test_input))
