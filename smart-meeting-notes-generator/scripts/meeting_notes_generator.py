#!/usr/bin/env python3
"""
智能会议纪要生成器
自动分析会议内容，提取关键信息，生成结构化纪要
"""

import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import random


@dataclass
class Speaker:
    """发言人"""
    name: str
    role: str = ""
    statements: List[str] = None
    
    def __post_init__(self):
        if self.statements is None:
            self.statements = []


@dataclass
class Decision:
    """决策"""
    content: str
    basis: str = ""
    expected_effect: str = ""
    approved_by: str = ""


@dataclass
class ActionItem:
    """待办事项"""
    task: str
    assignee: str
    deadline: str
    priority: str = "中"
    status: str = "待开始"
    related_issue: str = ""


class MeetingParser:
    """会议解析器"""
    
    # 常见发言人识别模式
    SPEAKER_PATTERNS = [
        r'^([A-Z]{1}[a-z]+)[:：]',
        r'^【([^】]+)】',
        r'^<([^>]+)>',
        r'^（([^）]+)）',
    ]
    
    # 决策关键词
    DECISION_KEYWORDS = [
        '决定', '通过', '确认', '同意', '批准', '达成共识',
        '最终方案', '采用', '选择', '我们要', '确定'
    ]
    
    # 待办关键词
    ACTION_KEYWORDS = [
        '需要做', '负责', '执行', '完成', '跟进', '提交',
        '制定', '准备', '安排', '协调', '落实', '推进'
    ]
    
    # 时间表达模式
    TIME_PATTERNS = [
        (r'(\d+)月(\d+)日', '%m月%d日'),
        (r'(\d+)号', '%d号'),
        (r'下[一二三四五]天', 'next_weekday'),
        (r'本[一二三四五]天', 'this_weekday'),
        (r'(\d+)天[以内/后]', 'days_later'),
        (r'尽快', 'asap'),
    ]
    
    def __init__(self):
        self.speakers: Dict[str, Speaker] = {}
        self.decisions: List[Decision] = []
        self.action_items: List[ActionItem] = []
        self.issues: List[str] = []
        self.discussion_points: Dict[str, List[str]] = {}
    
    def parse(self, content: str) -> Dict:
        """
        解析会议内容
        
        Args:
            content: 会议记录文本
            
        Returns:
            解析结果字典
        """
        lines = content.strip().split('\n')
        current_topic = "会议讨论"
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # 识别发言人
            speaker, clean_line = self._extract_speaker(line)
            if speaker:
                self._add_statement(speaker, clean_line)
            
            # 识别议题
            if self._is_topic_line(line):
                current_topic = self._extract_topic(line)
                if current_topic not in self.discussion_points:
                    self.discussion_points[current_topic] = []
            
            # 识别决策
            decision = self._extract_decision(line)
            if decision:
                self.decisions.append(decision)
            
            # 识别待办
            action = self._extract_action(line)
            if action:
                self.action_items.append(action)
            
            # 识别问题
            if self._is_issue(line):
                self.issues.append(self._extract_issue(line))
            
            # 添加讨论要点
            if clean_line and current_topic:
                self.discussion_points[current_topic].append(clean_line)
        
        return self._generate_result()
    
    def _extract_speaker(self, line: str) -> Tuple[Optional[str], str]:
        """提取发言人"""
        for pattern in self.SPEAKER_PATTERNS:
            match = re.search(pattern, line)
            if match:
                speaker_name = match.group(1)
                clean_line = line[match.end():].strip()
                return speaker_name, clean_line
        return None, line
    
    def _add_statement(self, speaker: str, statement: str):
        """添加发言"""
        if speaker not in self.speakers:
            self.speakers[speaker] = Speaker(name=speaker)
        self.speakers[speaker].statements.append(statement)
    
    def _is_topic_line(self, line: str) -> bool:
        """判断是否为议题行"""
        topic_markers = ['议题', '主题', '讨论', '关于', '第一点', '第二点', '首先', '其次']
        return any(marker in line for marker in topic_markers) and len(line) < 50
    
    def _extract_topic(self, line: str) -> str:
        """提取议题"""
        # 移除常见前缀
        for marker in ['议题', '主题', '关于', '第一点', '第二点', '第三点', '首先', '其次']:
            if marker in line:
                parts = line.split(marker)
                if len(parts) > 1:
                    return parts[-1].strip('：:、')
        return line[:30]
    
    def _extract_decision(self, line: str) -> Optional[Decision]:
        """提取决策"""
        if any(keyword in line for keyword in self.DECISION_KEYWORDS):
            return Decision(
                content=line,
                basis="根据讨论结果",
                expected_effect="待评估"
            )
        return None
    
    def _extract_action(self, line: str) -> Optional[ActionItem]:
        """提取待办"""
        if any(keyword in line for keyword in self.ACTION_KEYWORDS):
            assignee = self._extract_assignee(line)
            deadline = self._extract_deadline(line)
            return ActionItem(
                task=line,
                assignee=assignee,
                deadline=deadline,
                priority=self._extract_priority(line)
            )
        return None
    
    def _extract_assignee(self, line: str) -> str:
        """提取责任人"""
        # 简化实现
        names = re.findall(r'([A-Z]{1}[a-z]+)', line)
        if names:
            return names[0]
        return "待指定"
    
    def _extract_deadline(self, line: str) -> str:
        """提取截止时间"""
        today = datetime.now()
        
        if '本周' in line:
            day = int(re.search(r'本周([一二三四五])', line).group(1))
            return (today + timedelta(days=day-today.weekday())).strftime('%m-%d')
        elif '下周' in line:
            day = int(re.search(r'下周([一二三四五六日])', line).group(1))
            return (today + timedelta(weeks=1, days=day-today.weekday())).strftime('%m-%d')
        elif '尽快' in line or 'ASAP' in line:
            return "尽快"
        else:
            return "待确定"
    
    def _extract_priority(self, line: str) -> str:
        """提取优先级"""
        if any(kw in line for kw in ['紧急', '马上', '立即', '加急']):
            return "高"
        elif any(kw in line for kw in ['不急', '慢慢', '有空']):
            return "低"
        return "中"
    
    def _is_issue(self, line: str) -> bool:
        """判断是否为问题"""
        issue_markers = ['问题', '待定', '需讨论', '有分歧', '争议', '难点']
        return any(marker in line for marker in issue_markers)
    
    def _extract_issue(self, line: str) -> str:
        """提取问题"""
        return line
    
    def _generate_result(self) -> Dict:
        """生成解析结果"""
        return {
            'speakers': list(self.speakers.values()),
            'decisions': self.decisions,
            'action_items': self.action_items,
            'issues': self.issues,
            'discussion_points': self.discussion_points
        }


class MeetingNotesGenerator:
    """会议纪要生成器"""
    
    def __init__(self):
        self.parser = MeetingParser()
    
    def generate(self, content: str, topic: str = "", format: str = "详细") -> str:
        """
        生成会议纪要
        
        Args:
            content: 会议内容
            topic: 会议主题
            format: 输出格式（详细/简洁/要点）
            
        Returns:
            格式化会议纪要
        """
        result = self.parser.parse(content)
        
        if not topic:
            topic = self._infer_topic(result)
        
        # 生成markdown格式纪要
        report = f"""# 会议纪要

**会议主题**: {topic}
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 📋 会议概览

"""
        
        # 计算统计
        total_duration = len(content) // 50  # 粗略估算
        num_decisions = len(result['decisions'])
        num_actions = len(result['action_items'])
        
        report += f"""| 项目 | 数值 |
|------|------|
| 预估时长 | {total_duration}分钟 |
| 参会人员 | {len(result['speakers'])}人 |
| 讨论要点 | {len(result['discussion_points'])}个 |
| 形成决策 | {num_decisions}项 |
| 新增待办 | {num_actions}项 |

"""
        
        # 参会人员
        if result['speakers']:
            report += "## 👥 参会人员\n\n"
            for speaker in result['speakers']:
                report += f"- {speaker.name}"
                if speaker.role:
                    report += f" ({speaker.role})"
                report += "\n"
            report += "\n"
        
        # 讨论要点
        if result['discussion_points']:
            report += "## 💬 讨论要点\n\n"
            for i, (topic_name, points) in enumerate(result['discussion_points'].items(), 1):
                report += f"### 议题{i}: {topic_name}\n\n"
                for point in points[:3]:  # 限制每个议题显示3个要点
                    report += f"- {point}\n"
                report += "\n"
        
        # 关键决策
        if result['decisions']:
            report += "## ✅ 关键决策\n\n"
            for i, decision in enumerate(result['decisions'], 1):
                report += f"{i}. **{decision.content}**\n"
                if decision.basis:
                    report += f"   - 依据: {decision.basis}\n"
                if decision.expected_effect:
                    report += f"   - 预期效果: {decision.expected_effect}\n"
            report += "\n"
        
        # 行动待办
        if result['action_items']:
            report += "## 📌 行动待办\n\n"
            report += "| 序号 | 事项 | 责任人 | 截止时间 | 优先级 | 状态 |\n"
            report += "|------|------|-------|---------|-------|------|\n"
            for i, action in enumerate(result['action_items'], 1):
                report += f"| {i} | {action.task[:30]}... | {action.assignee} | {action.deadline} | {action.priority} | {action.status} |\n"
            report += "\n"
        
        # 待解决问题
        if result['issues']:
            report += "## ⚠️ 待解决问题\n\n"
            for issue in result['issues']:
                report += f"- {issue}\n"
            report += "\n"
        
        # 下次会议
        report += """## 📅 下次会议

- 时间：待定
- 议题：待确定
- 需要跟进：[事项]

---

*本纪要由智能会议纪要生成器自动生成*\n"""
        
        return report
    
    def _infer_topic(self, result: Dict) -> str:
        """推断会议主题"""
        if result['discussion_points']:
            topics = list(result['discussion_points'].keys())
            if topics:
                return topics[0]
        return "项目会议"


def main():
    """主函数示例"""
    generator = MeetingNotesGenerator()
    
    # 示例会议内容
    sample_meeting = """
大家好，今天我们来讨论一下Q2季度的产品规划。

议题一：用户增长策略
张明：目前用户增长主要依赖渠道投放，成本比较高
李华：建议加强内容运营，获取自然流量
王芳：同意，可以尝试短视频方向

议题二：技术架构升级
刘强：现有架构扩展性不够，需要重构
陈伟：重构风险太大，建议渐进式改造
刘强：可以分阶段进行

决定：采用渐进式架构改造方案
决定：优先改造用户模块

需要做用户调研，张明负责，2天内完成
需要制定详细方案，刘强负责，本周内完成
需要协调资源，陈伟负责跟进

下周继续讨论资源分配问题
    """
    
    print("📝 智能会议纪要生成器\n")
    
    topic = input("请输入会议主题（直接回车使用默认）: ").strip() or "Q2产品规划会议"
    
    print("\n正在生成会议纪要...\n")
    
    notes = generator.generate(sample_meeting, topic=topic)
    print(notes)


if __name__ == "__main__":
    main()
