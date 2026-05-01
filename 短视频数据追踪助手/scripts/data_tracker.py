#!/usr/bin/env python3
"""
短视频数据追踪助手脚本
分析视频数据并生成优化建议
"""

import json
import random
from datetime import datetime, timedelta

def calculate_metrics(views, likes, comments, shares, saves, followers, duration):
    """计算核心数据指标"""
    metrics = {
        "like_rate": round(likes / views * 100, 2) if views > 0 else 0,
        "comment_rate": round(comments / views * 100, 2) if views > 0 else 0,
        "share_rate": round(shares / views * 100, 2) if views > 0 else 0,
        "save_rate": round(saves / views * 100, 2) if views > 0 else 0,
        "follow_rate": round(followers / views * 100, 2) if views > 0 else 0,
        "engagement_rate": round((likes + comments + shares + saves) / views * 100, 2) if views > 0 else 0
    }
    return metrics

def evaluate_metrics(metrics, platform):
    """评估指标表现"""
    thresholds = {
        "douyin": {
            "like_rate": {"excellent": 8, "good": 5, "warning": 3},
            "comment_rate": {"excellent": 1.5, "good": 0.8, "warning": 0.5},
            "share_rate": {"excellent": 1, "good": 0.5, "warning": 0.3},
            "engagement_rate": {"excellent": 10, "good": 6, "warning": 3}
        },
        "kuaishou": {
            "like_rate": {"excellent": 5, "good": 3, "warning": 2},
            "comment_rate": {"excellent": 1, "good": 0.6, "warning": 0.4},
            "share_rate": {"excellent": 1, "good": 0.5, "warning": 0.3},
            "engagement_rate": {"excellent": 8, "good": 5, "warning": 3}
        },
        "videonum": {
            "like_rate": {"excellent": 4, "good": 2.5, "warning": 1.5},
            "comment_rate": {"excellent": 0.8, "good": 0.4, "warning": 0.2},
            "share_rate": {"excellent": 1.5, "good": 0.8, "warning": 0.4},
            "engagement_rate": {"excellent": 8, "good": 5, "warning": 3}
        }
    }
    
    platform_thresholds = thresholds.get(platform, thresholds["douyin"])
    evaluation = {}
    
    for metric, value in metrics.items():
        if metric in platform_thresholds:
            threshold = platform_thresholds[metric]
            if value >= threshold["excellent"]:
                level = "excellent"
            elif value >= threshold["good"]:
                level = "good"
            else:
                level = "warning"
            
            evaluation[metric] = {
                "value": value,
                "level": level,
                "status": "✅" if level != "warning" else "⚠️"
            }
    
    return evaluation

def generate_optimization_suggestions(evaluation, metrics):
    """生成优化建议"""
    suggestions = []
    
    for metric, data in evaluation.items():
        if data["level"] == "warning":
            if metric == "like_rate":
                suggestions.append({
                    "metric": "点赞率",
                    "issue": "点赞率偏低，内容认可度不够",
                    "suggestions": [
                        "优化视频开头，前3秒抓住注意力",
                        "增加内容价值，让用户觉得值得点赞",
                        "适当引导点赞，如'觉得有用点个赞'",
                        "提高内容质量，增加实用性或娱乐性"
                    ]
                })
            elif metric == "comment_rate":
                suggestions.append({
                    "metric": "评论率",
                    "issue": "评论互动较少，用户参与度低",
                    "suggestions": [
                        "在视频中设置话题引导，如'你们觉得呢？'",
                        "结尾提出问题，引导用户评论",
                        "主动回复评论，引导二次互动",
                        "选择有争议性或共鸣感的话题"
                    ]
                })
            elif metric == "share_rate":
                suggestions.append({
                    "metric": "转发率",
                    "issue": "转发分享较少，社交传播力弱",
                    "suggestions": [
                        "内容要有利他性，让用户觉得值得分享",
                        "增加实用价值，如'收藏起来慢慢看'",
                        "制造社交货币，让用户有分享的资本",
                        "设置分享诱饵，如'转发有惊喜'"
                    ]
                })
            elif metric == "engagement_rate":
                suggestions.append({
                    "metric": "综合互动率",
                    "issue": "整体互动偏低，需要全面优化",
                    "suggestions": [
                        "从选题开始优化，选择更有吸引力的话题",
                        "提升内容质量，增加观看价值",
                        "优化发布时间，选择用户活跃时段",
                        "加强人设塑造，增加用户情感连接"
                    ]
                })
    
    if not suggestions:
        suggestions.append({
            "metric": "整体表现",
            "issue": "数据表现良好，继续保持！",
            "suggestions": [
                "总结成功经验，形成内容方法论",
                "保持更新频率，稳定输出",
                "持续测试新形式，拓展内容边界",
                "关注竞品动态，学习优秀玩法"
            ]
        })
    
    return suggestions

def format_number(num):
    """格式化数字显示"""
    if num >= 100000000:
        return f"{num/100000000:.1f}亿"
    elif num >= 10000:
        return f"{num/10000:.1f}万"
    else:
        return str(num)

def generate_data_report(video_title, platform, views, likes, comments, shares, saves, followers, duration, publish_time):
    """生成完整数据分析报告"""
    
    metrics = calculate_metrics(views, likes, comments, shares, saves, followers, duration)
    evaluation = evaluate_metrics(metrics, platform)
    suggestions = generate_optimization_suggestions(evaluation, metrics)
    
    report = {
        "basic_info": {
            "video_title": video_title,
            "platform": platform,
            "duration": f"{duration}秒",
            "publish_time": publish_time,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "core_data": {
            "views": format_number(views),
            "likes": format_number(likes),
            "comments": format_number(comments),
            "shares": format_number(shares),
            "saves": format_number(saves),
            "followers": format_number(followers)
        },
        "calculated_metrics": {
            "like_rate": f"{metrics['like_rate']}%",
            "comment_rate": f"{metrics['comment_rate']}%",
            "share_rate": f"{metrics['share_rate']}%",
            "save_rate": f"{metrics['save_rate']}%",
            "follow_rate": f"{metrics['follow_rate']}%",
            "engagement_rate": f"{metrics['engagement_rate']}%"
        },
        "evaluation": evaluation,
        "optimization_suggestions": suggestions,
        "tips": [
            "完播率是推荐算法的核心权重指标",
            "互动率影响二次推荐流量",
            "转发分享是社交流量的关键",
            "保持稳定更新，培养粉丝习惯"
        ]
    }
    
    return report

def main():
    """测试脚本"""
    report = generate_data_report(
        video_title="3个技巧让你的视频播放量翻倍！",
        platform="douyin",
        views=50000,
        likes=2500,
        comments=300,
        shares=200,
        saves=500,
        followers=100,
        duration=60,
        publish_time="2026-04-28 14:30"
    )
    
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
