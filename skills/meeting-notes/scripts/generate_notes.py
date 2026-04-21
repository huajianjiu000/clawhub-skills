#!/usr/bin/env python3
"""
会议纪要生成器
根据输入的会议内容生成结构化纪要
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Optional


class MeetingNotesGenerator:
    """会议纪要生成器类"""
    
    def __init__(self):
        self.template = self._load_template()
    
    def _load_template(self) -> str:
        """加载纪要模板"""
        return """# 会议纪要

## 基本信息
- **会议主题**：{topic}
- **时间**：{datetime}
- **参与者**：{participants}
- **记录人**：{recorder}

## 议程回顾
{agenda}

## 讨论要点
{discussion_points}

## 关键决策
{decisions}

## 行动项
{action_items}

## 下次会议安排
{next_meeting}

---
*生成时间：{generated_time}*
"""
    
    def parse_meeting_content(self, content: str) -> Dict:
        """解析会议内容"""
        result = {
            'topic': '',
            'datetime': '',
            'participants': [],
            'decisions': [],
            'action_items': [],
            'discussion_points': []
        }
        
        # 提取参与者
        participant_patterns = [
            r'参与[人员]*[：:]\s*(.+?)(?:\n|$)',
            r'出席[人员]*[：:]\s*(.+?)(?:\n|$)',
            r'参会[人员]*[：:]\s*(.+?)(?:\n|$)'
        ]
        for pattern in participant_patterns:
            match = re.search(pattern, content)
            if match:
                participants_text = match.group(1)
                result['participants'] = [p.strip() for p in re.split(r'[,，、；;]', participants_text)]
                break
        
        # 提取决策事项
        decision_keywords = ['决定', '决策', '通过', '同意', '批准', '确认']
        for keyword in decision_keywords:
            pattern = rf'{keyword}[：:]*\s*(.+?)(?:\n|$)'
            matches = re.findall(pattern, content)
            result['decisions'].extend(matches)
        
        # 提取行动项
        action_keywords = ['待办', '行动项', '任务', '需要', '负责', '执行']
        for keyword in action_keywords:
            pattern = rf'{keyword}[：:]*\s*(.+?)(?:\n|$)'
            matches = re.findall(pattern, content)
            result['action_items'].extend(matches)
        
        return result
    
    def generate_notes(self, 
                       content: str,
                       topic: str = "",
                       recorder: str = "AI助手") -> str:
        """生成会议纪要"""
        parsed = self.parse_meeting_content(content)
        
        # 构建讨论要点
        discussion_points = "\n".join([f"{i+1}. {p}" for i, p in enumerate(parsed['discussion_points'])])
        if not discussion_points:
            discussion_points = "（根据会议内容提取）"
        
        # 构建关键决策
        decisions = "\n".join([f"- {d}" for d in parsed['decisions']]) if parsed['decisions'] else "- （无明确决策事项）"
        
        # 构建行动项表格
        if parsed['action_items']:
            action_items = "| 序号 | 任务 | 负责人 | 截止日期 |\n|------|------|--------|----------|\n"
            for i, item in enumerate(parsed['action_items'], 1):
                action_items += f"| {i} | {item} | 待定 | 待定 |\n"
        else:
            action_items = "（无待办事项）"
        
        # 构建参与者列表
        participants = "、".join(parsed['participants']) if parsed['participants'] else "未指定"
        
        return self.template.format(
            topic=topic or "会议主题",
            datetime=parsed['datetime'] or datetime.now().strftime("%Y年%m月%d日"),
            participants=participants,
            recorder=recorder,
            agenda="（根据会议进程整理）",
            discussion_points=discussion_points,
            decisions=decisions,
            action_items=action_items,
            next_meeting="待定",
            generated_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )


if __name__ == "__main__":
    generator = MeetingNotesGenerator()
    
    # 示例输入
    sample_content = """
    会议主题：Q4产品规划讨论
    参与人员：张三、李四、王五
    时间：2024年1月15日 14:00-16:00
    
    讨论内容：
    1. 回顾Q3产品数据，用户增长达30%
    2. 决定在Q4上线新功能A
    3. 同意增加营销预算50%
    4. 待办：由李四负责新功能设计
    5. 需要王五协调技术团队
    """
    
    notes = generator.generate_notes(sample_content, topic="Q4产品规划讨论")
    print(notes)
