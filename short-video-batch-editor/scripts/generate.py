#!/usr/bin/env python3
"""
短视频批量剪辑脚本生成器
支持一键生成多个视频的剪辑脚本，包含分镜、转场、字幕、音乐等完整剪辑方案
"""

import json
import random
from datetime import datetime

# 剪辑模板库
TEMPLATES = {
    "反转剧情": {
        "name": "爆款反转型",
        "duration_range": (15, 30),
        "structure": "铺垫→冲突→反转→结尾",
        "适用": "剧情号、搞笑号",
        "transitions": ["闪白", "跳切", "快速切换"],
        "subtitle_style": "大字+动态效果"
    },
    "知识干货": {
        "name": "知识干货型",
        "duration_range": (30, 60),
        "structure": "痛点→知识点→案例→总结",
        "适用": "教育号、科普号",
        "transitions": ["淡入淡出", "滑动", "缩放"],
        "subtitle_style": "分条列出+图标"
    },
    "种草安利": {
        "name": "种草安利型",
        "duration_range": (10, 20),
        "structure": "吸引→痛点解决→产品展示→号召",
        "适用": "带货号、好物分享",
        "transitions": ["叠化", "快速切换", "缩放"],
        "subtitle_style": "大字+高亮框"
    },
    "日常记录": {
        "name": "日常记录型",
        "duration_range": (15, 45),
        "structure": "开头hook→主体记录→结尾互动",
        "适用": "生活号、Vlog",
        "transitions": ["自然过渡", "叠化", "慢动作"],
        "subtitle_style": "简洁白字+时间戳"
    },
    "热点挑战": {
        "name": "挑战/热点型",
        "duration_range": (10, 15),
        "structure": "热点引入→内容承接→互动引导",
        "适用": "热点追踪账号",
        "transitions": ["跳切", "节奏切换", "闪白"],
        "subtitle_style": "热点字幕+互动提示"
    }
}

# 背景音乐建议
BGM_SUGGESTIONS = {
    "反转剧情": ["欢快搞笑BGM", "反转专用音效", "悬念配乐"],
    "知识干货": ["轻快背景音乐", "学习氛围BGM", "专业感配乐"],
    "种草安利": ["种草背景音乐", "带货节奏BGM", "轻快流行"],
    "日常记录": ["生活感BGM", "日常记录音乐", "温暖轻音乐"],
    "热点挑战": ["热门BGM", "挑战配乐", "节奏感强的音乐"]
}

# 热门标签库
POPULAR_TAGS = [
    "#短视频", "#热门", "#推荐", "#dou+", "#上热门", "#流量密码",
    "#vlog", "#记录生活", "#干货分享", "#知识分享", "#必看",
    "#种草", "#好物分享", "#购物分享", "#美食", "#教程",
    "#技巧", "#建议", "#收藏", "#关注"
]

# 场景描述库
SCENE_TEMPLATES = [
    "室内场景，{主体}特写",
    "室外环境，{主体}展示",
    "工作室，{主体}操作演示",
    "生活场景，{主体}日常",
    "街头/外景，{主体}动态",
    "特写镜头，细节展示",
    "全景展示，{主体}全貌",
    "近景拍摄，{主体}互动"
]

def generate_batch_scripts(
    count: int = 5,
    template_type: str = None,
    topic: str = None,
    main_subject: str = None
) -> dict:
    """
    批量生成剪辑脚本
    
    Args:
        count: 生成数量
        template_type: 模板类型
        topic: 主题/话题
        main_subject: 主体内容
    """
    if template_type and template_type not in TEMPLATES:
        template_type = None
    
    scripts = []
    for i in range(count):
        template_key = template_type or random.choice(list(TEMPLATES.keys()))
        template = TEMPLATES[template_key]
        
        duration = random.randint(*template["duration_range"])
        scene = random.choice(SCENE_TEMPLATES).format(主体=main_subject or "主体内容")
        
        script = {
            "index": i + 1,
            "title": f"{topic or '视频'}_{i+1}" if topic else f"视频_{i+1}",
            "template": template["name"],
            "duration": duration,
            "scene": scene,
            "segments": generate_segments(duration, template),
            "transitions": template["transitions"],
            "subtitle_style": template["subtitle_style"],
            "bgm": random.choice(BGM_SUGGESTIONS[template_key]),
            "tags": random.sample(POPULAR_TAGS, 5),
            "structure": template["structure"],
            "applicable": template["适用"]
        }
        scripts.append(script)
    
    return {
        "total_count": count,
        "template_type": template_type or "智能匹配",
        "generated_at": datetime.now().isoformat(),
        "scripts": scripts
    }

def generate_segments(duration: int, template: dict) -> list:
    """生成分镜段落"""
    segments = []
    if template["name"] == "爆款反转型":
        # 铺垫20% → 冲突40% → 反转30% → 结尾10%
        segs = [
            (0, duration * 0.2, "开场铺垫", "设置场景/吸引注意力"),
            (duration * 0.2, duration * 0.6, "主体内容", "冲突/矛盾建立"),
            (duration * 0.6, duration * 0.9, "反转时刻", "意想不到的转折"),
            (duration * 0.9, duration, "结尾收束", "点题/引导互动")
        ]
    elif template["name"] == "知识干货型":
        # 痛点15% → 知识点35% → 案例35% → 总结15%
        segs = [
            (0, duration * 0.15, "痛点引入", "引起共鸣/问题抛出"),
            (duration * 0.15, duration * 0.5, "核心知识点", "讲解干货内容"),
            (duration * 0.5, duration * 0.85, "案例展示", "实际案例/应用演示"),
            (duration * 0.85, duration, "总结收尾", "要点回顾/行动号召")
        ]
    elif template["name"] == "种草安利型":
        # 吸引20% → 痛点解决25% → 产品展示40% → 号召15%
        segs = [
            (0, duration * 0.2, "吸引开场", "抓住眼球/制造好奇"),
            (duration * 0.2, duration * 0.45, "痛点解决", "解决用户痛点"),
            (duration * 0.45, duration * 0.85, "产品展示", "详细展示/卖点强调"),
            (duration * 0.85, duration, "行动号召", "引导购买/关注")
        ]
    elif template["name"] == "日常记录型":
        # hook20% → 主体60% → 结尾20%
        segs = [
            (0, duration * 0.2, "开头Hook", "吸引停留"),
            (duration * 0.2, duration * 0.8, "主体记录", "核心内容"),
            (duration * 0.8, duration, "结尾互动", "引导互动/关注")
        ]
    else:  # 热点挑战
        # 热点15% → 内容40% → 互动45%
        segs = [
            (0, duration * 0.15, "热点引入", "关联热点话题"),
            (duration * 0.15, duration * 0.55, "内容承接", "完成挑战/内容创作"),
            (duration * 0.55, duration, "互动引导", "引导互动参与")
        ]
    
    for start, end, title, desc in segs:
        start_time = int(start)
        end_time = int(end)
        if end_time > start_time:
            segments.append({
                "time_range": f"{start_time:02d}:{start_time%60:02d}-{end_time//60:02d}:{end_time%60:02d}",
                "title": title,
                "description": desc,
                "duration": f"{end_time - start_time}秒"
            })
    
    return segments

def format_report(report: dict) -> str:
    """格式化输出报告"""
    lines = []
    lines.append("🎬 短视频批量剪辑脚本")
    lines.append("═" * 50)
    lines.append(f"📅 生成时间：{report['generated_at'][:19]}")
    lines.append(f"📊 总视频数：{report['total_count']}条")
    lines.append(f"🎨 模板类型：{report['template_type']}")
    lines.append("")
    
    for script in report["scripts"]:
        lines.append("═" * 50)
        lines.append(f"📹 视频{script['index']}：《{script['title']}》")
        lines.append("─" * 50)
        lines.append(f"⏱ 时长：{script['duration']}秒")
        lines.append(f"🎭 模板：{script['template']}")
        lines.append(f"📍 场景：{script['scene']}")
        lines.append(f"🏗 结构：{script['structure']}")
        lines.append(f"📌 适用：{script['applicable']}")
        lines.append("")
        
        lines.append("🎬 分镜脚本：")
        for seg in script["segments"]:
            lines.append(f"  ⏱ {seg['time_range']} | {seg['title']} | {seg['description']} ({seg['duration']})")
        lines.append("")
        
        lines.append(f"🔀 推荐转场：{' | '.join(script['transitions'])}")
        lines.append(f"💬 字幕样式：{script['subtitle_style']}")
        lines.append(f"🎵 推荐音乐：{script['bgm']}")
        lines.append(f"🏷️ 建议标签：{' '.join(script['tags'])}")
        lines.append("")
    
    lines.append("═" * 50)
    lines.append("💡 使用建议：")
    lines.append("1. 可将分镜脚本导入剪映/快影等App")
    lines.append("2. 按脚本顺序添加素材和转场")
    lines.append("3. 批量处理可大幅提升剪辑效率")
    lines.append("4. 根据实际素材微调细节")
    
    return "\n".join(lines)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="短视频批量剪辑脚本生成器")
    parser.add_argument("--count", "-c", type=int, default=5, help="生成数量")
    parser.add_argument("--template", "-t", choices=list(TEMPLATES.keys()), help="模板类型")
    parser.add_argument("--topic", help="主题/话题")
    parser.add_argument("--subject", "-s", help="主体内容")
    parser.add_argument("--format", "-f", choices=["json", "text"], default="text", help="输出格式")
    
    args = parser.parse_args()
    
    report = generate_batch_scripts(
        count=args.count,
        template_type=args.template,
        topic=args.topic,
        main_subject=args.subject
    )
    
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(format_report(report))
