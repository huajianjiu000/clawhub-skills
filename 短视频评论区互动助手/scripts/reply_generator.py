#!/usr/bin/env python3
"""
短视频评论区互动助手
根据评论内容生成多种风格的回复
"""

def generate_reply(comment: str, style: str = "幽默搞笑") -> dict:
    """根据评论内容和风格生成回复"""
    
    replies = {
        "幽默搞笑": [
            f"哈哈哈哈{comment}这个{get_reaction(comment)}笑死我了😂",
            f"说得好像{comment}很有道理的样子（并没有）",
            f"你这评论{comment}比我的枕头还有分量",
            f"{comment}？我不听我不听，王八讲故事~"
        ],
        "暖心回复": [
            f"感谢支持！你的{comment}让我很开心 😊",
            f"有你们真好~{comment}一起加油",
            f"同感同感！{comment}说到心坎里了",
            f"谢谢你的{comment}，我会继续努力的"
        ],
        "引导关注": [
            f"{comment}说得对！想看更多精彩内容就关注我吧~",
            f"喜欢这种风格？点个关注不迷路",
            f"{comment}！关注我，每天分享有趣内容",
            f"想持续看到这类内容？右上角点关注哦"
        ],
        "神回复": [
            f"{comment}？我的沉默震耳欲聋",
            f"你这{comment}，让我陷入了沉思（并没有）",
            f"{comment}——来自灵魂的拷问",
            f"你这评论{comment}，我愿称之为经典"
        ],
        "回怼杠精": [
            f"你说的{comment}，牛顿听了会沉默，爱因斯坦会流泪",
            f"{comment}？建议先把九年义务教育上完再来",
            f"你的{comment}很有想象力，建议去写小说",
            f"{comment}——我从未见过如此厚颜无耻之人"
        ]
    }
    
    style_replies = replies.get(style, replies["幽默搞笑"])
    return {
        "comment": comment,
        "style": style,
        "replies": style_replies
    }

def get_reaction(comment: str) -> str:
    """根据评论内容生成反应词"""
    keywords = ["搞笑", "有趣", "好", "棒", "厉害", "牛", "赞", "帅", "美", "可爱"]
    for kw in keywords:
        if kw in comment:
            return f"说到{kw}的地方"
    return "吐槽的地方"

if __name__ == "__main__":
    # 测试
    result = generate_reply("这个视频太搞笑了吧", "幽默搞笑")
    print(f"评论: {result['comment']}")
    print(f"风格: {result['style']}")
    print("推荐回复:")
    for i, reply in enumerate(result['replies'], 1):
        print(f"{i}. {reply}")
