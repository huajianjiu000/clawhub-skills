#!/usr/bin/env python3
"""
产品PRD生成器
快速生成专业的产品需求文档
"""

import re
from datetime import datetime
from typing import Dict, List, Optional


class PRDGenerator:
    """PRD生成器类"""
    
    def __init__(self):
        self.template = self._load_template()
    
    def _load_template(self) -> str:
        """加载PRD模板"""
        return """# 产品需求文档 (PRD)

## 文档信息
- **文档版本**：v1.0
- **创建日期**：{create_date}
- **产品名称**：{product_name}
- **状态**：草稿

---

## 1. 产品概述

### 1.1 产品简介
{product_intro}

### 1.2 产品背景
{product_background}

### 1.3 产品愿景
{product_vision}

### 1.4 成功指标
| 指标 | 目标值 | 衡量方式 |
|------|--------|----------|
| 用户增长 | {growth_target} |  |
| 活跃度   | {activity_target} |  |
| 满意度   | {satisfaction_target} |  |

---

## 2. 目标与范围

### 2.1 产品目标

**业务目标**
- {business_goal_1}
- {business_goal_2}

**用户目标**
- {user_goal_1}
- {user_goal_2}

### 2.2 项目范围

**包含范围**
- {in_scope_1}
- {in_scope_2}

**不包含范围**
- {out_of_scope}

### 2.3 MVP定义
{mvp_definition}

---

## 3. 用户分析

### 3.1 目标用户画像

**核心用户画像**
- **用户类型**：{user_type}
- **年龄范围**：{age_range}
- **核心痛点**：{pain_points}
- **使用场景**：{use_scenario}

### 3.2 用户需求

**核心需求（Must Have）**
1. {core_need_1}
2. {core_need_2}

**重要需求（Should Have）**
1. {important_need_1}
2. {important_need_2}

---

## 4. 功能需求

### 4.1 功能总览

| 模块 | 功能 | 优先级 | 描述 |
|------|------|--------|------|
| {module_1} | {feature_1} | P0 | {feature_desc_1} |
| {module_2} | {feature_2} | P1 | {feature_desc_2} |

### 4.2 功能详细说明

#### 功能模块：{module_name}

**功能描述**
{function_description}

**用户故事**
```
作为 {actor}
我想要 {feature}
以便 {value}
```

**业务流程**
{workflow}

**验收标准**
- [标准1]
- [标准2]

---

## 5. 非功能需求

### 5.1 性能要求
| 指标 | 要求值 |
|------|--------|
| 页面加载时间 | < 3秒 |
| API响应时间 | < 500ms |
| 系统可用性 | ≥ 99.9% |

### 5.2 安全性要求
- 用户数据加密存储
- 传输层使用HTTPS
- 身份认证与授权

### 5.3 兼容性要求
- 浏览器：Chrome/Firefox/Safari/Edge最新版本
- 移动端：iOS 12+/Android 8+

---

## 6. 验收标准

### 6.1 功能验收清单
| 序号 | 功能点 | 验收条件 | 测试状态 |
|------|--------|----------|----------|
| 1    |        |          | 待测试   |

### 6.2 性能验收标准
- [性能指标要求]

---

## 7. 风险评估

| 风险项 | 影响程度 | 发生概率 | 应对策略 |
|--------|----------|----------|----------|
| 技术风险 | 中 | 低 | {risk_response} |

---

## 8. 附录

### 8.1 术语表
| 术语 | 定义 |
|------|------|
|      |      |

### 8.2 修订历史
| 版本 | 日期 | 修改人 | 修改内容 |
|------|------|--------|----------|
| v1.0 | {create_date} | {author} | 初始版本 |
"""
    
    def generate_prd(self,
                    product_name: str,
                    product_intro: str = "",
                    product_background: str = "",
                    product_vision: str = "",
                    user_type: str = "",
                    features: List[Dict] = None,
                    author: str = "AI助手") -> str:
        """生成PRD文档"""
        
        if features is None:
            features = [
                {"module": "核心功能", "feature": "基础功能", "priority": "P0", "desc": "核心业务功能"}
            ]
        
        features_table = "\n".join([
            f"| {f.get('module', '')} | {f.get('feature', '')} | {f.get('priority', 'P1')} | {f.get('desc', '')} |"
            for f in features
        ])
        
        return self.template.format(
            create_date=datetime.now().strftime("%Y-%m-%d"),
            product_name=product_name,
            product_intro=product_intro or "一款解决[核心问题]的[产品类型]",
            product_background=product_background or "基于市场需求和用户痛点开发",
            product_vision=product_vision or "成为[领域]领先的产品",
            growth_target="10万+",
            activity_target="DAU > 1万",
            satisfaction_target="≥ 4.5分",
            business_goal_1="满足用户核心需求",
            business_goal_2="实现商业价值",
            user_goal_1="解决实际问题",
            user_goal_2="获得良好体验",
            in_scope_1="核心功能模块",
            in_scope_2="基础用户体验",
            out_of_scope="高级功能/增值服务",
            mvp_definition="MVP包含核心功能，确保用户可以使用产品完成主要任务",
            user_type=user_type or "目标用户群体",
            age_range="20-45岁",
            pain_points="[用户痛点描述]",
            use_scenario="[使用场景描述]",
            core_need_1="快速完成任务",
            core_need_2="获得清晰反馈",
            important_need_1="个性化设置",
            important_need_2="数据导出",
            module_1=features[0].get('module', '模块1') if features else '模块1',
            feature_1=features[0].get('feature', '功能1') if features else '功能1',
            feature_desc_1=features[0].get('desc', '') if features else '',
            module_2=features[1].get('module', '模块2') if len(features) > 1 else '模块2',
            feature_2=features[1].get('feature', '功能2') if len(features) > 1 else '功能2',
            feature_desc_2=features[1].get('desc', '') if len(features) > 1 else '',
            module_name=features[0].get('module', '功能模块') if features else '功能模块',
            function_description="[功能详细描述]",
            actor="[用户类型]",
            feature="[功能描述]",
            value="[用户价值]",
            workflow="[业务流程描述]",
            risk_response="[风险应对措施]",
            author=author
        )


if __name__ == "__main__":
    generator = PRDGenerator()
    
    prd = generator.generate_prd(
        product_name="智能笔记App",
        product_intro="一款帮助用户高效整理和回顾知识的笔记应用",
        product_background="用户面临信息过载问题，需要更好的知识管理工具",
        product_vision="成为最受知识工作者喜爱的笔记应用",
        user_type="知识工作者/学生",
        features=[
            {"module": "笔记管理", "feature": "创建笔记", "priority": "P0", "desc": "创建和编辑富文本笔记"},
            {"module": "知识库", "feature": "标签系统", "priority": "P0", "desc": "使用标签组织和分类笔记"},
            {"module": "回顾功能", "feature": "间隔复习", "priority": "P1", "desc": "基于遗忘曲线安排复习"}
        ]
    )
    
    print(prd)
