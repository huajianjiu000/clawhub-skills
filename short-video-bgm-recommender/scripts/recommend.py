#!/usr/bin/env python3
"""
短视频BGM推荐助手 - 参考脚本
用于演示BGM推荐的核心逻辑
"""

def analyze_video_content(content_type, emotion, duration):
    """
    分析视频内容并生成推荐条件
    
    参数:
        content_type: 内容类型 (美食/旅行/搞笑/情感/知识等)
        emotion: 目标情绪 (欢快/悲伤/紧张/温馨等)
        duration: 视频时长 (秒)
    """
    
    # 生成推荐条件
    conditions = {
        'content_type': content_type,
        'emotion': emotion,
        'duration': duration,
        'bpm_range': get_bpm_by_emotion(emotion),
        'style': get_style_by_content(content_type)
    }
    
    return conditions


def get_bpm_by_emotion(emotion):
    """
    根据情绪获取适合的BPM范围
    """
    bpm_map = {
        '欢快': '120-140',
        '悲伤': '60-80',
        '紧张': '140-160',
        '温馨': '80-100',
        '热血': '160-180',
        '神秘': '70-90'
    }
    return bpm_map.get(emotion, '100-120')


def get_style_by_content(content_type):
    """
    根据内容类型获取适合的音乐风格
    """
    style_map = {
        '美食': '轻快、温馨',
        '旅行': '自由、清新',
        '搞笑': '欢快、俏皮',
        '情感': '抒情、感人',
        '知识': '轻快、专注'
    }
    return style_map.get(content_type, '通用')


def recommend_bgm(conditions):
    """
    根据条件推荐BGM
    
    参数:
        conditions: 推荐条件字典
    
    返回:
        BGM推荐列表
    """
    
    # 模拟BGM数据库
    mock_bgm_db = [
        {
            'name': '阳光正好',
            'artist': '沐晴',
            'style': '轻快',
            'emotion': '欢快',
            'duration': 180,
            'bpm': 128,
            'copyright': '免费可商用',
            'hot': 9800
        },
        {
            'name': '城市夜景',
            'artist': '都市',
            'style': '抒情',
            'emotion': '温馨',
            'duration': 240,
            'bpm': 85,
            'copyright': '需授权',
            'hot': 9200
        },
        {
            'name': '搞怪时刻',
            'artist': '趣味',
            'style': '俏皮',
            'emotion': '欢快',
            'duration': 120,
            'bpm': 135,
            'copyright': '免费可商用',
            'hot': 8500
        }
    ]
    
    # 根据条件过滤和排序
    recommendations = mock_bgm_db
    
    return recommendations


if __name__ == "__main__":
    # 测试用例
    conditions = analyze_video_content('搞笑', '欢快', 60)
    print("推荐条件:", conditions)
    
    print("\n推荐BGM:")
    for i, bgm in enumerate(recommend_bgm(conditions), 1):
        print(f"{i}. {bgm['name']} - {bgm['artist']}")
        print(f"   风格: {bgm['style']}, 情绪: {bgm['emotion']}")
        print(f"   BPM: {bgm['bpm']}, 版权: {bgm['copyright']}")
        print(f"   热度: {bgm['hot']}")
        print()
