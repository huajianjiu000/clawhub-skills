#!/usr/bin/env python3
"""
合同条款审查器
审查合同条款，识别风险点
"""

import re
from datetime import datetime
from typing import Dict, List, Optional


class ContractReviewer:
    """合同审查器类"""
    
    def __init__(self):
        self.risk_patterns = self._load_risk_patterns()
        self.review_template = self._load_template()
    
    def _load_risk_patterns(self) -> Dict:
        """加载风险模式"""
        return {
            'high_risk': [
                (r'无条件|不可撤销|不得.*提出', '单方面加重责任'),
                (r'违约金[^\d]*\d{3,}[%％]', '违约金过高'),
                (r'永久|无限期|不得.*终止', '期限约定过长'),
                (r'一切.*损失|全部.*责任', '责任范围过宽'),
                (r'放弃.*权利|同意.*安排', '权利放弃条款'),
            ],
            'medium_risk': [
                (r'\d{1,2}[%％].*违约金', '违约金比例偏高'),
                (r'先.*后.*(?:付|付.*)[^\d]', '付款顺序不利'),
                (r'经.*方.*同意', '单方决定权'),
                (r'解释权|决定权', '解释权归一方'),
                (r'单方.*解除|随时.*解除', '解除权不对等'),
            ],
            'attention': [
                (r'管辖.*(?:法院|仲裁)', '争议管辖条款'),
                (r'保密.*\d+年', '保密期限'),
                (r'竞业.*\d+年', '竞业限制期限'),
                (r'知识产权.*归属', '知识产权条款'),
                (r'不可抗力', '不可抗力条款'),
            ]
        }
    
    def _load_template(self) -> str:
        """加载审查报告模板"""
        return """# 合同条款审查报告

## 📋 基本信息
- **合同类型**：{contract_type}
- **审查立场**：{review_position}
- **审查时间**：{review_date}
- **合同文本长度**：约{content_length}字

---

## ⚠️ 风险概览

| 风险等级 | 数量 | 说明 |
|----------|------|------|
| 🔴 高风险 | {high_risk_count} | 必须修改 |
| 🟡 中风险 | {medium_risk_count} | 建议修改 |
| 🟢 需关注 | {attention_count} | 注意防范 |

---

## 🔴 高风险条款

{high_risk_sections}

---

## 🟡 中风险条款

{medium_risk_sections}

---

## 🟢 需关注条款

{attention_sections}

---

## ✅ 正常条款

{normal_clauses}

---

## 📝 修改建议汇总

{modification_suggestions}

---

## 💡 特别提示

{special_notices}

---

## ⚖️ 法律依据参考

{legal_references}

---

## 📊 总体评估

**风险等级**：{overall_risk_level}

**建议**：
{overall_suggestion}

---

⚠️ **重要声明**
- 本报告仅供参考，不构成法律意见
- 重要合同建议咨询专业律师
- 请根据实际情况综合判断

---

*报告生成时间：{generate_date}*
"""
    
    def review_contract(self,
                       content: str,
                       contract_type: str = "商务合同",
                       position: str = "乙方") -> str:
        """审查合同"""
        
        # 检测风险条款
        high_risk_findings = self._find_risks(content, 'high_risk')
        medium_risk_findings = self._find_risks(content, 'medium_risk')
        attention_findings = self._find_risks(content, 'attention')
        
        # 生成各部分内容
        high_risk_sections = self._format_findings(high_risk_findings, 'high')
        medium_risk_sections = self._format_findings(medium_risk_findings, 'medium')
        attention_sections = self._format_findings(attention_findings, 'attention')
        normal_clauses = self._generate_normal_clauses(content)
        suggestions = self._generate_suggestions(high_risk_findings, medium_risk_findings)
        notices = self._generate_special_notices(contract_type, position)
        legal_refs = self._generate_legal_references()
        
        # 评估总体风险
        overall_risk = self._evaluate_overall_risk(
            high_risk_findings, medium_risk_findings, attention_findings
        )
        
        return self.review_template.format(
            contract_type=contract_type,
            review_position=position,
            review_date=datetime.now().strftime("%Y-%m-%d"),
            content_length=len(content),
            high_risk_count=len(high_risk_findings),
            medium_risk_count=len(medium_risk_findings),
            attention_count=len(attention_findings),
            high_risk_sections=high_risk_sections or "✅ 未发现高风险条款",
            medium_risk_sections=medium_risk_sections or "✅ 未发现中风险条款",
            attention_sections=attention_sections or "✅ 无需特别关注的条款",
            normal_clauses=normal_clauses,
            modification_suggestions=suggestions,
            special_notices=notices,
            legal_references=legal_refs,
            overall_risk_level=overall_risk.get('level', '中风险'),
            overall_suggestion=overall_risk.get('suggestion', '建议谨慎处理'),
            generate_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    
    def _find_risks(self, content: str, risk_level: str) -> List[Dict]:
        """查找风险条款"""
        findings = []
        patterns = self.risk_patterns.get(risk_level, [])
        
        for pattern, description in patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                # 获取上下文
                start = max(0, match.start() - 50)
                end = min(len(content), match.end() + 50)
                context = content[start:end]
                
                findings.append({
                    'pattern': description,
                    'matched_text': match.group(),
                    'context': f"...{context}...",
                    'position': match.start()
                })
        
        return findings
    
    def _format_findings(self, findings: List[Dict], level: str) -> str:
        """格式化风险发现"""
        if not findings:
            return ""
        
        section = ""
        risk_icons = {'high': '🔴', 'medium': '🟡', 'attention': '🟢'}
        icon = risk_icons.get(level, '⚪')
        
        for i, finding in enumerate(findings, 1):
            section += f"""### {icon} 风险{i}：{finding['pattern']}

**匹配内容**：`{finding['matched_text']}`

**上下文**：
```
{finding['context']}
```

**建议**：
{finding.get('suggestion', '建议与对方协商修改该条款')}

---

"""
        
        return section
    
    def _generate_normal_clauses(self, content: str) -> str:
        """生成正常条款说明"""
        return """合同中其他条款未见明显风险，建议：
- 确保合同主体信息准确
- 核实签章和骑缝章是否完整
- 保留合同原件和签收记录"""
    
    def _generate_suggestions(self, high: List[Dict], medium: List[Dict]) -> str:
        """生成修改建议"""
        suggestions = "### 重点修改建议\n\n"
        
        all_findings = high + medium
        for i, finding in enumerate(all_findings[:5], 1):
            suggestions += f"""**{i}. {finding['pattern']}**
- 位置：第{self._estimate_line(finding['position'])}行附近
- 问题：{finding['pattern']}
- 建议：与对方协商修改为对等条款
- 参考：如协商不成，可考虑放弃该笔业务或寻求专业法律意见

"""
        
        if len(all_findings) > 5:
            suggestions += f"\n另有{len(all_findings) - 5}处较小风险点，建议逐一处理。\n"
        
        return suggestions
    
    def _generate_special_notices(self, contract_type: str, position: str) -> str:
        """生成特别提示"""
        notices = []
        
        if contract_type == "劳动合同":
            notices.extend([
                "⚠️ 劳动合同受《劳动合同法》严格保护",
                "⚠️ 试用期内工资不得低于正式工资的80%",
                "⚠️ 不得约定员工承担违约金（培训费、服务期除外）",
                "⚠️ 竞业限制期限不超过2年，需支付经济补偿"
            ])
        elif contract_type == "商务合同":
            notices.extend([
                "⚠️ 明确约定付款条件，避免先票后款",
                "⚠️ 验收标准要可量化、可操作",
                "⚠️ 违约金上限通常为损失的30%",
                "⚠️ 争取对我方有利的管辖法院"
            ])
        elif contract_type == "租赁合同":
            notices.extend([
                "⚠️ 押金退还条件和时限要明确",
                "⚠️ 提前解约的违约金是否合理",
                "⚠️ 维修责任划分是否公平",
                "⚠️ 租金递增幅度要有上限"
            ])
        else:
            notices.append("⚠️ 建议在签署前咨询专业律师")
        
        notices.append("⚠️ 保留好合同原件和所有往来文件")
        
        return "\n".join(notices)
    
    def _generate_legal_references(self) -> str:
        """生成法律依据参考"""
        return """### 主要适用法律

**《中华人民共和国民法典》**
- 合同编通则：第463-509条
- 合同订立原则：第143条（民事法律行为有效条件）

**商务合同常用条款**
- 违约金上限：损失+30%（参照相关司法解释）
- 格式条款：《民法典》第496-498条

**劳动合同相关**
- 《中华人民共和国劳动合同法》
- 试用期限：第19条
- 违约金规定：第22-25条

*注：具体条文请以最新版本为准*"""
    
    def _evaluate_overall_risk(self, high: List, medium: List, attention: List) -> Dict:
        """评估总体风险"""
        score = len(high) * 3 + len(medium) * 2 + len(attention) * 1
        
        if score >= 10 or len(high) >= 3:
            return {
                'level': '🔴 高风险',
                'suggestion': '合同存在较多风险条款，建议务必修改后再签署，或寻求专业法律帮助'
            }
        elif score >= 5 or len(high) >= 1:
            return {
                'level': '🟡 中风险',
                'suggestion': '合同存在一定风险，建议与对方协商修改关键条款'
            }
        else:
            return {
                'level': '🟢 低风险',
                'suggestion': '合同整体风险可控，可谨慎签署，注意保留相关证据'
            }
    
    def _estimate_line(self, position: int, avg_line_length: int = 50) -> int:
        """估算行号"""
        return position // avg_line_length + 1


if __name__ == "__main__":
    reviewer = ContractReviewer()
    
    # 示例合同内容
    sample_contract = """
    劳动合同
    
    甲方（用人单位）：XX科技有限公司
    乙方（员工）：张三
    
    第一条 工作内容
    乙方同意在甲方担任高级工程师职务。
    
    第二条 合同期限
    本合同期限为三年，自2024年1月1日起至2026年12月31日止。
    
    第三条 工作时间
    乙方同意无条件服从甲方安排的工作时间，包括但不限于加班和节假日工作。
    
    第四条 劳动报酬
    乙方月薪为税前25000元。
    
    第五条 违约责任
    如乙方提前解除合同，应向甲方支付违约金500000元。
    
    第六条 竞业限制
    乙方同意在离职后永久不得从事与甲方业务相关的任何工作。
    
    第七条 争议解决
    如发生争议，由甲方所在地人民法院管辖。
    
    甲方（盖章）：
    乙方（签字）：
    日期：
    """
    
    report = reviewer.review_contract(
        sample_contract,
        contract_type="劳动合同",
        position="乙方"
    )
    
    print(report)
