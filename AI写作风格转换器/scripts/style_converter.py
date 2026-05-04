#!/usr/bin/env python3
"""
AI写作风格转换器
去除AI生成痕迹，转换为自然人类写作风格
"""

import re

# AI常用词汇替换表
AI_WORD_REPLACEMENTS = {
    "赋能": "帮助",
    "打通": "连接",
    "构建": "建立",
    "迭代": "更新",
    "沉淀": "积累",
    "聚焦": "专注",
    "协同": "合作",
    "整合": "合并",
    "驱动": "推动",
    "赋能": "助力",
    "生态": "系统",
    "闭环": "完整",
    "维度": "方面",
    "赛道": "领域",
    "玩法": "方式",
    "打法": "方法",
    "盘子": "规模",
    "壁垒": "门槛",
    "破局": "突破",
    "拉齐": "对齐",
}

# 需要简化的句式模式
AI_PATTERNS = {
    r"首先、其次、最后": "然后",
    r"第一、第二、第三": "首先、其次、最后",
    r"综上所述": "总之",
    r"由此可见": "所以",
    r"从某种意义上来说": "其实",
    r"不得不承认": "确实",
    r"客观来说": "说实话",
    r"值得注意的是": "要注意",
    r"换句话说": "也就是说",
    r"可以说": "其实",
}

def convert_to_human_style(text: str) -> dict:
    """将AI风格文本转换为人类写作风格"""
    
    result = text
    
    # 1. 替换AI常用词汇
    for ai_word, human_word in AI_WORD_REPLACEMENTS.items():
        result = result.replace(ai_word, human_word)
    
    # 2. 简化句式
    for pattern, replacement in AI_PATTERNS.items():
        result = result.replace(pattern, replacement)
    
    # 3. 去除过多的"首先、其次、最后"
    if result.count("首先") > 2:
        result = re.sub(r"首先(，|，)", "第一，", result)
        result = re.sub(r"其次(，|，)", "第二，", result)
        result = re.sub(r"最后(，|，)", "第三，", result)
    
    # 4. 增加口语化表达
    result = result.replace("。", "。")
    result = re.sub(r"(\w)！", r"\1呀！", result)
    
    # 5. 去除过度完美的表达
    result = re.sub(r"的、的、的", "的", result)
    result = re.sub(r"，是的", "，没错", result)
    
    # 6. 添加一些自然的不完美
    result = re.sub(r"非常(\w)", r"特别\1", result)
    result = re.sub(r"十分(\w)", r"挺\1", result)
    result = re.sub(r"极其(\w)", r"超\1", result)
    
    changes = []
    for ai, human in AI_WORD_REPLACEMENTS.items():
        if ai in text and ai not in result:
            changes.append(f"'{ai}' → '{human}'")
    
    return {
        "original": text,
        "converted": result,
        "changes": changes
    }

if __name__ == "__main__":
    # 测试
    test_text = "首先，我们需要赋能业务发展，打通各个环节，构建完整的生态体系。其次，要迭代产品，沉淀经验。最后，综上所述，可以看到其维度是非常广阔的。"
    
    result = convert_to_human_style(test_text)
    print("原文:")
    print(result['original'])
    print("\n转换后:")
    print(result['converted'])
    print("\n修改:", result['changes'])
