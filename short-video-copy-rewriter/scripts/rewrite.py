#!/usr/bin/env python3
"""
短视频文案改写助手 - 参考脚本
用于演示文案改写的核心逻辑
"""

def rewrite_text(text, mode='high_originality'):
    """
    文案改写核心函数
    
    参数:
        text: 原文案
        mode: 改写模式
            - high_originality: 高原创版本
            - light_rewrite: 轻度改写版本
            - colloquial: 口语化版本
            - reverse: 反义转述版本
    """
    
    # 模拟改写逻辑
    # 实际使用时需要调用NLP模型或API
    
    if mode == 'high_originality':
        # 高原创版本 - 完全重构
        result = f"[高原创改写] {text}"
    elif mode == 'light_rewrite':
        # 轻度改写 - 保持原风格
        result = f"[轻度改写] {text}"
    elif mode == 'colloquial':
        # 口语化版本
        result = f"[口语化] 你知道吗？{text}"
    elif mode == 'reverse':
        # 反义转述
        result = f"[反义转述] 话说回来...{text}"
    else:
        result = text
    
    return result


def evaluate_originality(text):
    """
    评估文案原创度
    
    返回: 原创度评分 (0-100)
    """
    # 模拟评分逻辑
    # 实际使用时需要对接查重API
    
    score = 85  # 默认分数
    return score


if __name__ == "__main__":
    # 测试用例
    test_text = "这个视频告诉你如何快速学会做饭"
    
    print("原文:", test_text)
    print("原创度评分:", evaluate_originality(test_text))
    print()
    
    for mode in ['high_originality', 'light_rewrite', 'colloquial', 'reverse']:
        result = rewrite_text(test_text, mode)
        print(f"[{mode}]:", result)
