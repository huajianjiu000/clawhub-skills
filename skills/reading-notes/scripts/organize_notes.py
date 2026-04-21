#!/usr/bin/env python3
"""
阅读笔记整理器
整理阅读内容，生成结构化笔记
"""

import re
from datetime import datetime
from typing import Dict, List, Optional


class ReadingNotesOrganizer:
    """阅读笔记整理器类"""
    
    def __init__(self):
        self.book_template = self._load_book_template()
        self.article_template = self._load_article_template()
    
    def _load_book_template(self) -> str:
        """加载书籍笔记模板"""
        return """# {title} - 读书笔记

## 📚 书籍信息
- **书名**：{title}
- **作者**：{author}
- **出版社**：{publisher}
- **阅读日期**：{read_date}
- **阅读时长**：约{reading_hours}小时

---

## 🎯 阅读目的
{reading_purpose}

---

## 📖 内容概要

### 一句话总结
{one_sentence_summary}

### 结构框架
{structure_framework}

---

## 💡 核心知识点

{knowledge_points}

---

## 📝 精华摘录

### 金句
{quotes}

### 精彩案例
{cases}

---

## 🧠 核心框架（思维导图）

{mindmap}

---

## 🚀 实践应用

### 可立即行动
{immediate_actions}

### 短期计划（1个月）
{short_term_plan}

### 长期规划（3-6个月）
{long_term_plan}

---

## 💭 个人感悟

### 阅读感受
{reading_feeling}

### 最大收获
{max_gain}

### 不足之处
{shortcomings}

---

## 📊 评估与打分

| 维度 | 评分 | 说明 |
|------|------|------|
| 内容质量 | {content_rating} |      |
| 实用性   | {practicality_rating} |      |
| 可读性   | {readability_rating} |      |
| 总体评分 | {overall_rating} |      |

**推荐指数**：{recommendation}

---

*笔记整理时间：{generate_date}*
"""
    
    def _load_article_template(self) -> str:
        """加载文章笔记模板"""
        return """# {title} - 要点整理

## 基本信息
- **来源**：{source}
- **作者**：{author}
- **发布时间**：{publish_date}
- **阅读时间**：{reading_time}

---

## 一句话总结
{one_sentence_summary}

---

## 核心要点

{core_points}

---

## 值得记录

**金句**：
> {highlight_quote}

**数据/事实**：
{statistics}

---

## 我的思考
{reflection}

---

## 可行动项
{action_items}

---

*整理时间：{generate_date}*
"""
    
    def organize_book_notes(self,
                          title: str,
                          content: str = "",
                          author: str = "未知",
                          publisher: str = "未知",
                          reading_purpose: str = "学习提升",
                          note_depth: str = "详细") -> str:
        """整理书籍笔记"""
        
        # 提取内容要点
        summary = self._extract_summary(content)
        knowledge_points = self._extract_knowledge_points(content)
        quotes = self._extract_quotes(content)
        mindmap = self._generate_mindmap(summary, knowledge_points)
        
        # 生成各部分内容
        knowledge_section = self._format_knowledge_points(knowledge_points)
        quotes_section = self._format_quotes(quotes)
        cases_section = "| 案例 | 核心启示 |\n|------|----------|\n| [精彩案例] | [启示点] |"
        actions_section = self._format_actions(knowledge_points)
        
        return self.book_template.format(
            title=title,
            author=author,
            publisher=publisher,
            read_date=datetime.now().strftime("%Y-%m-%d"),
            reading_hours="5-8" if note_depth == "详细" else "1-2",
            reading_purpose=reading_purpose,
            one_sentence_summary=summary.get('one_sentence', '待阅读后补充'),
            structure_framework=summary.get('structure', '待补充'),
            knowledge_points=knowledge_section,
            quotes=quotes_section,
            cases=cases_section,
            mindmap=mindmap,
            immediate_actions=actions_section.get('immediate', '1. 暂无立即可执行项'),
            short_term_plan=actions_section.get('short_term', '1. 暂无短期计划'),
            long_term_plan=actions_section.get('long_term', '1. 暂无长期规划'),
            reading_feeling=summary.get('feeling', '待补充阅读感受'),
            max_gain=knowledge_points[0].get('point', '待发现最大收获') if knowledge_points else '待发现最大收获',
            shortcomings='待发现不足之处',
            content_rating='⭐⭐⭐⭐⭐',
            practicality_rating='⭐⭐⭐⭐⭐',
            readability_rating='⭐⭐⭐⭐⭐',
            overall_rating='⭐⭐⭐⭐⭐',
            recommendation='推荐',
            generate_date=datetime.now().strftime("%Y-%m-%d %H:%M")
        )
    
    def organize_article_notes(self,
                              title: str,
                              content: str = "",
                              source: str = "网络",
                              author: str = "未知") -> str:
        """整理文章笔记"""
        
        # 提取要点
        summary = self._extract_summary(content)
        core_points = self._extract_core_points(content)
        
        # 格式化核心要点
        points_section = ""
        for i, point in enumerate(core_points, 1):
            points_section += f"### 要点{i}：{point.get('title', '待整理')}\n{point.get('content', '')}\n\n"
        
        return self.article_template.format(
            title=title,
            source=source,
            author=author,
            publish_date=datetime.now().strftime("%Y-%m-%d"),
            reading_time="5-10分钟",
            one_sentence_summary=summary.get('one_sentence', '待整理'),
            core_points=points_section or "待整理核心要点",
            highlight_quote="待摘录金句",
            statistics="- 待补充数据\n- 待补充事实",
            reflection="待撰写个人思考",
            action_items="- 待制定行动计划",
            generate_date=datetime.now().strftime("%Y-%m-%d %H:%M")
        )
    
    def _extract_summary(self, content: str) -> Dict:
        """提取摘要信息"""
        # 简单实现：根据内容长度和关键词生成摘要
        if not content:
            return {
                'one_sentence': '本书探讨了核心主题的多个方面',
                'structure': '全书分为若干章节，循序渐进展开论述',
                'feeling': '内容充实，值得深入阅读'
            }
        
        # 简单关键词提取
        words = content.split()
        if len(words) > 100:
            return {
                'one_sentence': f'本书围绕"{words[10] if len(words) > 10 else "核心主题"}"展开讨论',
                'structure': '包含理论阐述、案例分析、实践指导等多个部分',
                'feeling': '内容丰富，需要反复研读'
            }
        
        return {
            'one_sentence': '待根据内容整理',
            'structure': '待根据目录整理',
            'feeling': '待阅读后补充'
        }
    
    def _extract_summary(self, content: str) -> Dict:
        """提取摘要信息"""
        if not content:
            return {
                'one_sentence': '本书深入探讨了核心主题的多重维度',
                'structure': '全书结构清晰，分章节系统阐述观点',
                'feeling': '内容深度与广度兼具，值得品读'
            }
        
        words = content.split()
        if len(words) > 100:
            return {
                'one_sentence': f'本书围绕核心观点，通过多个维度展开深入探讨',
                'structure': '包含引言、理论框架、案例分析、实践建议、总结等部分',
                'feeling': '理论结合实际，干货满满'
            }
        
        return {
            'one_sentence': '待根据内容整理核心观点',
            'structure': '待根据目录整理章节结构',
            'feeling': '待阅读后补充感受'
        }
    
    def _extract_knowledge_points(self, content: str) -> List[Dict]:
        """提取知识点"""
        # 返回默认知识点
        return [
            {'title': '核心概念', 'point': '理解基础定义和核心观点', 'application': ['场景1', '场景2']},
            {'title': '方法论', 'point': '掌握解决问题的思路和方法', 'application': ['实践1', '实践2']},
            {'title': '实践指南', 'point': '学会将理论应用到实际', 'application': ['应用1', '应用2']}
        ]
    
    def _extract_quotes(self, content: str) -> List[str]:
        """提取金句"""
        # 返回示例金句
        return [
            '"这是值得深思的一句话"',
            '"另一句发人深省的观点"'
        ]
    
    def _extract_core_points(self, content: str) -> List[Dict]:
        """提取文章核心要点"""
        return [
            {'title': '核心观点', 'content': '文章的主要论点，需要细细品味'}
        ]
    
    def _generate_mindmap(self, summary: Dict, points: List[Dict]) -> str:
        """生成思维导图文本"""
        mindmap = """```
中心：[全书核心主题]
├─ 分支1：[知识点1]
│  ├─ 子主题1.1：[相关概念]
│  └─ 子主题1.2：[延伸思考]
├─ 分支2：[知识点2]
│  ├─ 子主题2.1：[方法论]
│  └─ 子主题2.2：[实践应用]
└─ 分支3：[知识点3]
   ├─ 子主题3.1：[案例分析]
   └─ 子主题3.2：[总结升华]
```"""
        return mindmap
    
    def _format_knowledge_points(self, points: List[Dict]) -> str:
        """格式化知识点"""
        section = ""
        for i, point in enumerate(points, 1):
            section += f"""### 知识点{i}：{point.get('title', f'知识点{i}')}

**核心内容**：{point.get('point', '')}

**我的理解**：
[需要根据原文理解后补充]

**应用场景**：
- {point.get('application', ['待补充'])[0]}
- {point.get('application', ['待补充'])[1] if len(point.get('application', [])) > 1 else '待补充应用场景'}

"""
        return section
    
    def _format_quotes(self, quotes: List[str]) -> str:
        """格式化金句"""
        section = ""
        for i, quote in enumerate(quotes, 1):
            section += f'{i}. {quote} - P.[页码]\n   > 感悟：[为什么这句打动你]\n\n'
        return section if section else "待摘录精彩语句"
    
    def _format_actions(self, points: List[Dict]) -> Dict:
        """格式化行动项"""
        return {
            'immediate': "1. [根据第一个知识点制定立即行动]",
            'short_term': "1. [制定1个月内的学习计划]",
            'long_term': "1. [规划3-6个月的实践方向]"
        }


if __name__ == "__main__":
    organizer = ReadingNotesOrganizer()
    
    # 示例：书籍笔记
    book_notes = organizer.organize_book_notes(
        title="《高效能人士的七个习惯》",
        author="史蒂芬·柯维",
        publisher="中国青年出版社",
        reading_purpose="提升个人效能和领导力"
    )
    
    print(book_notes)
    print("\n" + "="*50 + "\n")
    
    # 示例：文章笔记
    article_notes = organizer.organize_article_notes(
        title="如何提升团队协作效率",
        source="微信公众号"
    )
    
    print(article_notes)
