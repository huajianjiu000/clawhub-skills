#!/usr/bin/env python3
"""
直播话术生成器脚本
根据产品信息和场景自动生成直播话术
"""

import json
import random
from datetime import datetime

# 话术模板库
OPENING_TEMPLATES = {
    "douyin": [
        "大家好！欢迎来到{host}的直播间！我是你们的老朋友{host}，今天给大家带来一款超值的福利产品！",
        "进来的宝宝们把\"想要\"打在公屏上，人数到了1000我们直接抽免单！",
        "感谢所有进到直播间的家人们，今天我们准备了超多福利，一定要看到最后！"
    ],
    "kuaishou": [
        "老铁们！欢迎回家！{host}回来了，想我没？把\"想\"打在评论区！",
        "今天这场直播给大家准备了三波大福利，错过等一周！",
        "老铁们把关注点一点，明天还来！"
    ],
    "videonum": [
        "欢迎各位朋友来到{host}的直播间！感谢平台提供的直播环境！",
        "今天我们会分享一些实用的内容，希望能帮到大家！",
        "进来的朋友们记得点个关注，每天都有新内容！"
    ]
}

FAB_TEMPLATES = [
    "【特性】{feature}\n【优势】{advantage}\n【利益】{benefit}",
]

PROMOTION_TEMPLATES = {
    "limited": [
        "只剩最后{count}单了！",
        "过了今天恢复原价{original_price}，今天只要{price}！",
        "再不买就没了，手慢无！"
    ],
    "value": [
        "你知道这款产品专柜卖多少吗？{original_price}！",
        "今天在我直播间只要{price}，还送{bonus}赠品！",
        "价值{value}的东西今天免费送！"
    ],
    "action": [
        "想要的宝宝把\"想要\"打在公屏上！",
        "没关注的点下关注，明天还来给你们送福利！",
        "把定金打在公屏上，我给你们改价格！"
    ]
}

def generate_opening_script(platform, host_name):
    """生成开场话术"""
    templates = OPENING_TEMPLATES.get(platform, OPENING_TEMPLATES["douyin"])
    scripts = []
    for i, template in enumerate(templates):
        script = template.format(host=host_name)
        scripts.append({
            "order": i + 1,
            "content": script,
            "duration": "30-60秒",
            "tips": "保持热情，与观众互动"
        })
    return scripts

def generate_product_script(product_name, feature, advantage, benefit, price, original_price):
    """生成产品介绍话术"""
    scripts = []
    
    # FAB法则介绍
    fab_script = f"""
【特性】{product_name}采用的是{feature}...
【优势】这个配置让{product_name}比同类产品更{advantage}...
【利益】用这款产品你可以{benefit}...
"""
    scripts.append({
        "type": "FAB法则介绍",
        "content": fab_script.strip(),
        "duration": "2-3分钟"
    })
    
    # 价格对比
    price_script = f"""
来！家人们！重点来了！
今天这款{product_name}我给你们{price}！
外面你买都买不到这个价格！
专柜要{original_price}，今天直接{price}！
我今天不赚钱，就为了交个朋友！
"""
    scripts.append({
        "type": "价格对比",
        "content": price_script.strip(),
        "duration": "1-2分钟"
    })
    
    return scripts

def generate_promotion_script(count, price, original_price, bonus):
    """生成促单话术"""
    scripts = []
    
    # 限时限量
    limited_templates = [
        f"只剩最后{count}单了！",
        f"过了今天恢复原价{original_price}，今天只要{price}！",
        "再不买就没了，手慢无！"
    ]
    scripts.append({
        "type": "限时限量",
        "content": "\n".join(limited_templates),
        "tips": "倒计时54321制造紧迫感"
    })
    
    # 价值塑造
    value_templates = [
        f"你知道这款产品专柜卖多少吗？{original_price}！",
        f"今天在我直播间只要{price}，还送{bonus}赠品！",
        f"价值超过{price}的东西今天免费送！"
    ]
    scripts.append({
        "type": "价值塑造",
        "content": "\n".join(value_templates),
        "tips": "强调性价比，让用户觉得值"
    })
    
    # 行动指令
    action_templates = [
        "想要的宝宝把\"想要\"打在公屏上！",
        "没关注的点下关注，明天还来给你们送福利！",
        "把定金打在公屏上，我给你们改价格！"
    ]
    scripts.append({
        "type": "行动指令",
        "content": "\n".join(action_templates),
        "tips": "明确告诉用户下一步行动"
    })
    
    return scripts

def generate_closing_script(host_name, next_live_time):
    """生成收尾话术"""
    scripts = []
    
    script = f"""
好了，今天的直播就到这里了！
感谢所有陪伴到现在的宝宝们！
关注{host_name}，下期我们再见！
明天下午{next_live_time}我们继续开播，下期给大家准备了更多福利！
拜拜~（挥手）
"""
    scripts.append({
        "type": "标准收尾",
        "content": script.strip(),
        "duration": "1分钟"
    })
    
    return scripts

def generate_full_script(platform, host_name, product_name, feature, advantage, benefit, 
                        price, original_price, bonus, next_live_time, stock):
    """生成完整直播话术脚本"""
    result = {
        "basic_info": {
            "platform": platform,
            "host_name": host_name,
            "product_name": product_name,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "opening_scripts": generate_opening_script(platform, host_name),
        "product_scripts": generate_product_script(product_name, feature, advantage, benefit, price, original_price),
        "promotion_scripts": generate_promotion_script(stock, price, original_price, bonus),
        "closing_scripts": generate_closing_script(host_name, next_live_time)
    }
    
    return result

def main():
    """测试脚本"""
    result = generate_full_script(
        platform="douyin",
        host_name="XX主播",
        product_name="智能手表",
        feature="全触控高清屏幕，支持心率监测",
        advantage="功能全面、续航持久、防水等级高",
        benefit="随时了解健康数据，运动时不用带手机",
        price="299",
        original_price="699",
        bonus="贴膜+表带",
        next_live_time="2点",
        stock="50"
    )
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
