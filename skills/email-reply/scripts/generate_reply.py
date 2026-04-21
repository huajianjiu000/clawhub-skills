#!/usr/bin/env python3
"""
邮件智能回复生成器
根据邮件内容生成专业回复
"""

import re
from datetime import datetime
from typing import Dict, List, Optional


class EmailReplyGenerator:
    """邮件回复生成器类"""
    
    def __init__(self):
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """加载邮件模板"""
        return {
            'formal_opening': [
                "尊敬的{}：",
                "尊敬的{}先生/女士：",
                "您好，{}："
            ],
            'informal_opening': [
                "亲爱的{}：",
                "嗨，{}："
            ],
            'closing': {
                'formal': ["此致敬礼", "祝您商祺", "顺颂商祺"],
                'informal': ["祝好", "Best", "Cheers"],
                'business': ["祝商祺", "顺祝商安", "致以诚挚的问候"]
            }
        }
    
    def analyze_email(self, content: str) -> Dict:
        """分析邮件内容"""
        result = {
            'intent': 'general',
            'sentiment': 'neutral',
            'urgency': 'normal',
            'needs': []
        }
        
        # 分析意图
        intent_keywords = {
            'inquiry': ['咨询', '请问', '了解', '想知道', '能否'],
            'cooperation': ['合作', '商务', '业务', '洽谈'],
            'complaint': ['投诉', '不满', '问题', '反馈'],
            'thanks': ['感谢', '谢谢', '致谢'],
            'interview': ['面试', '求职', '应聘', '简历'],
            'invitation': ['邀请', '邀请您', '诚邀']
        }
        
        for intent, keywords in intent_keywords.items():
            if any(k in content for k in keywords):
                result['intent'] = intent
                break
        
        # 分析紧急程度
        if any(k in content for k in ['紧急', '尽快', '急', 'ASAP']):
            result['urgency'] = 'high'
        
        return result
    
    def generate_reply(self,
                      original_email: str,
                      recipient_name: str = "",
                      sender_name: str = "",
                      tone: str = "formal",
                      context: Optional[Dict] = None) -> str:
        """生成邮件回复"""
        analysis = self.analyze_email(original_email)
        
        # 选择称呼
        if recipient_name:
            if tone == "formal":
                greeting = f"尊敬的{recipient_name}："
            else:
                greeting = f"您好，{recipient_name}："
        else:
            greeting = "尊敬的先生/女士："
        
        # 选择结尾
        closing_options = self.templates['closing'].get(
            'formal' if tone == 'formal' else 'informal',
            self.templates['closing']['formal']
        )
        closing = closing_options[0]
        
        # 根据意图生成回复内容
        reply_body = self._generate_body(original_email, analysis, tone)
        
        # 构建完整邮件
        reply = f"""
{greeting}

您好！

{reply_body}

{closing}

{sender_name if sender_name else '[您的姓名]'}
{datetime.now().strftime("%Y年%m月%d日")}
""".strip()
        
        return reply
    
    def _generate_body(self, original: str, analysis: Dict, tone: str) -> str:
        """根据邮件分析结果生成回复内容"""
        intent = analysis['intent']
        
        templates = {
            'inquiry': "感谢您的来信咨询。\n\n关于您询问的内容，我们已悉知。\n\n如需进一步了解更多信息，请告知。",
            'cooperation': "感谢您对合作事宜的关注。\n\n我们已收到您的来信，非常期待与您进一步探讨合作可能。\n\n请告知您方便的时间，我们将尽快安排沟通。",
            'complaint': "感谢您的反馈，我们高度重视您提出的问题。\n\n针对您提到的情况，我们将立即跟进处理。\n\n给您带来的不便，我们深表歉意。",
            'thanks': "感谢您的来信。\n\n您的肯定是我们前进的动力。\n\n期待为您继续提供优质服务。",
            'interview': "感谢您的来信。\n\n我们已收到您的求职申请，将尽快审核并回复。\n\n如有任何问题，请随时与我们联系。",
            'invitation': "感谢您的邀请。\n\n[确认参加/遗憾无法参加]。\n\n期待活动顺利！",
            'general': "感谢您的来信。\n\n我们已收到您的邮件，将尽快处理并回复。\n\n如有进一步的问题，请随时联系。"
        }
        
        return templates.get(intent, templates['general'])


if __name__ == "__main__":
    generator = EmailReplyGenerator()
    
    # 示例输入
    sample_email = """
    您好，
    
    我们是ABC公司，想了解一下贵司的产品报价。
    请尽快告知，谢谢！
    
    张三
    """
    
    reply = generator.generate_reply(
        sample_email,
        recipient_name="李经理",
        sender_name="王五",
        tone="formal"
    )
    print(reply)
