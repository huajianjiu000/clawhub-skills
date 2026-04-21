#!/usr/bin/env python3
"""
周报自动生成器
根据工作内容生成结构化周报
"""

import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class WeeklyReportGenerator:
    """周报生成器类"""
    
    def __init__(self):
        self.template = self._load_template()
    
    def _load_template(self) -> str:
        """加载周报模板"""
        return """# 周报

**姓名**：{name}
**部门**：{department}
**汇报周期**：{start_date} - {end_date}

---

## 一、本周工作总结

### 1.1 重点项目进展
{project_progress}

### 1.2 日常工作
{daily_work}

### 1.3 其他工作
{other_work}

---

## 二、数据统计

{statistics}

---

## 三、问题与风险

{issues}

---

## 四、下周工作计划

{next_week_plan}

---

## 五、所需支持

{support_needed}

---

*汇报人：{name}*
*汇报时间：{report_date}*
"""
    
    def parse_work_content(self, content: str) -> Dict:
        """解析工作内容"""
        result = {
            'projects': [],
            'daily': [],
            'issues': [],
            'data': {}
        }
        
        lines = content.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 识别项目相关
            if any(k in line for k in ['完成', '上线', '交付', '发布']):
                result['projects'].append(line)
            # 识别日常工作
            elif any(k in line for k in ['维护', '处理', '回复', '会议']):
                result['daily'].append(line)
            # 识别问题
            elif any(k in line for k in ['问题', '风险', '阻塞', '延期']):
                result['issues'].append(line)
        
        return result
    
    def generate_report(self,
                        name: str = "",
                        department: str = "",
                        work_content: str = "",
                        report_type: str = "general",
                        start_date: Optional[datetime] = None,
                        end_date: Optional[datetime] = None) -> str:
        """生成周报"""
        
        # 默认本周日期
        if end_date is None:
            end_date = datetime.now()
        if start_date is None:
            start_date = end_date - timedelta(days=end_date.weekday())
        
        # 解析工作内容
        parsed = self.parse_work_content(work_content)
        
        # 构建项目进展
        if parsed['projects']:
            project_progress = "\n".join([f"- {p}" for p in parsed['projects']])
        else:
            project_progress = "- 暂无重大项目进展"
        
        # 构建日常工作
        if parsed['daily']:
            daily_work = "\n".join([f"- {d}" for d in parsed['daily']])
        else:
            daily_work = "- 日常工作正常进行"
        
        # 构建其他工作
        other_items = set(parsed['projects'] + parsed['daily'])
        other_work = "- 无" if len(other_items) >= 3 else "- 持续优化工作流程"
        
        # 构建数据统计
        statistics = "| 指标 | 数值 | 备注 |\n|------|------|------|\n| 工作完成率 | 95% | 正常 |\n| 会议参与 | 5场 | 正常 |"
        
        # 构建问题与风险
        if parsed['issues']:
            issues = "\n".join([f"- {i}" for i in parsed['issues']])
        else:
            issues = "- 无重大问题或风险"
        
        # 构建下周计划
        next_week_plan = "| 序号 | 工作内容 | 优先级 |\n|------|----------|--------|\n| 1 | 跟进本周遗留任务 | P0 |"
        
        # 构建所需支持
        support_needed = "- 暂无特殊支持需求"
        
        return self.template.format(
            name=name or "同事",
            department=department or "通用部门",
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d"),
            project_progress=project_progress,
            daily_work=daily_work,
            other_work=other_work,
            statistics=statistics,
            issues=issues,
            next_week_plan=next_week_plan,
            support_needed=support_needed,
            report_date=datetime.now().strftime("%Y年%m月%d日")
        )


if __name__ == "__main__":
    generator = WeeklyReportGenerator()
    
    # 示例输入
    sample_work = """
    1. 完成用户中心2.0版本开发并上线
    2. 修复支付模块的bug
    3. 参加产品评审会议
    4. 日常工单处理
    5. 登录功能存在性能问题需要优化
    """
    
    report = generator.generate_report(
        name="张三",
        department="研发部",
        work_content=sample_work
    )
    
    print(report)
