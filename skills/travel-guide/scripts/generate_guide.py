#!/usr/bin/env python3
"""
旅行攻略生成器
根据目的地生成完整旅行攻略
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional


class TravelGuideGenerator:
    """旅行攻略生成器类"""
    
    def __init__(self):
        self.template = self._load_template()
    
    def _load_template(self) -> str:
        """加载旅行攻略模板"""
        return """# {destination} 旅行攻略

## 📍 目的地概览
- **目的地**：{destination}
- **旅行天数**：{days}天{days_nights}
- **出行人数**：{travelers}人
- **旅行类型**：{travel_type}
- **预算范围**：{budget}
- **最佳季节**：{best_season}

---

## 🚗 交通指南

### 到达方式
| 交通方式 | 耗时 | 费用参考 | 特点 |
|----------|------|----------|------|
| 飞机 | {flight_time} | {flight_cost} | 快捷 |
| 高铁 | {train_time} | {train_cost} | 舒适 |
| 自驾 | {drive_time} | {drive_cost} | 自由 |

### 市内交通
- 公共交通：地铁/公交（推荐使用交通卡）
- 打车：起步价约{taxi_start}元
- 租车：建议在正规平台预约

---

## 🏨 住宿推荐

### 推荐住宿区域
| 区域 | 特点 | 适合人群 |
|------|------|----------|
| {hotel_area1} | {hotel_area1_desc} | {hotel_area1_suit} |
| {hotel_area2} | {hotel_area2_desc} | {hotel_area2_suit} |

### 住宿建议
- {hotel_tip}

---

## 📅 每日行程

### Day 1：抵达日 + {day1_theme}

| 时间 | 活动 | 地点 | 备注 |
|------|------|------|------|
| 上午 | 抵达{destination} | {day1_arrival} |  |
| 中午 | 午餐 | {day1_lunch} | {day1_lunch_tip} |
| 下午 | {day1_afternoon} | {day1_afternoon_place} |  |
| 晚上 | 晚餐+休息 | {day1_dinner} |  |

**今日亮点**：
- {day1_highlight}

---

### Day 2：{day2_theme}

| 时间 | 活动 | 地点 | 备注 |
|------|------|------|------|
| 上午 | {day2_morning} | {day2_morning_place} |  |
| 中午 | 午餐 | {day2_lunch} | 特色美食 |
| 下午 | {day2_afternoon} | {day2_afternoon_place} |  |
| 晚上 | {day2_evening} | {day2_evening_place} |  |

**今日亮点**：
- {day2_highlight}

---

### Day 3：{day3_theme}

| 时间 | 活动 | 地点 | 备注 |
|------|------|------|------|
| 上午 | {day3_morning} | {day3_morning_place} |  |
| 中午 | 午餐 | {day3_lunch} |  |
| 下午 | {day3_afternoon} | {day3_afternoon_place} |  |
| 晚上 | 返程准备 | {day3_evening} |  |

**今日亮点**：
- {day3_highlight}

---

## 🍜 美食推荐

### 必尝美食
| 美食 | 推荐店铺 | 人均 | 地址 |
|------|----------|------|------|
| {food1} | {food1_place} | {food1_cost} | {food1_addr} |
| {food2} | {food2_place} | {food2_cost} | {food2_addr} |

### 美食街区
- {food_street1}
- {food_street2}

---

## 💰 预算清单

### 费用预估（{travelers}人{tays}天）

| 类别 | 单价 | 数量 | 小计 |
|------|------|------|------|
| 往返交通 | {交通单价} | {travelers}人 | {交通小计} |
| 住宿 | {住宿单价}/晚 | {住宿晚数}晚 | {住宿小计} |
| 餐饮 | {餐饮单价}/人/天 | {travelers}人×{days}天 | {餐饮小计} |
| 门票 | {门票总价} | 套票 | {门票小计} |
| 市内交通 | {市内交通费} | - | {市内交通小计} |
| 购物 | {购物费} | - | {购物小计} |
| **总计** | | | **{total_budget}** |

---

## ⚠️ 注意事项

1. **必备物品**
   - 身份证/护照
   - 换洗衣物
   - 洗漱用品
   - 常用药品
   - 充电设备

2. **安全提示**
   - 注意人身财物安全
   - 遵守景区规定
   - 保持通讯畅通

3. **气候提醒**
   - {weather_tip}

4. **预订建议**
   - 提前预订机票/酒店
   - 热门景点提前购票
   - 关注退改政策

---

## 📱 实用信息

- 紧急电话：{emergency_phone}
- 旅游投诉：{complaint_phone}
- 天气查询：{weather_query}
- 必备App：{useful_apps}

---

*攻略生成时间：{generate_date}*
*祝您旅途愉快！*
"""
    
    def generate_guide(self,
                      destination: str,
                      days: int = 3,
                      travelers: int = 1,
                      travel_type: str = "品质游",
                      budget_per_day: int = 1000,
                      start_date: Optional[str] = None,
                      preferences: Dict = None) -> str:
        """生成旅行攻略"""
        
        preferences = preferences or {}
        
        # 计算夜晚数
        nights = max(0, days - 1)
        days_nights = f"({nights}晚)" if nights > 0 else ""
        
        # 估算总预算
        total_budget = self._estimate_budget(days, travelers, budget_per_day, travel_type)
        
        # 根据目的地类型填充内容
        content = self._generate_content_by_type(destination, days, travel_type)
        
        return self.template.format(
            destination=destination,
            days=days,
            days_nights=days_nights,
            travelers=travelers,
            travel_type=travel_type,
            budget=f"人均{total_budget // travelers}元",
            best_season=content.get('best_season', '春秋季'),
            flight_time="2-4小时",
            flight_cost="500-1500元",
            train_time="5-10小时",
            train_cost="300-800元",
            drive_time="4-8小时",
            drive_cost="300-500元油费",
            taxi_start="10",
            hotel_area1=content.get('hotel_area1', '市中心'),
            hotel_area1_desc=content.get('hotel_area1_desc', '交通便利，靠近景点'),
            hotel_area1_suit=content.get('hotel_area1_suit', '观光游客'),
            hotel_area2=content.get('hotel_area2', '景区周边'),
            hotel_area2_desc=content.get('hotel_area2_desc', '环境清幽，适合度假'),
            hotel_area2_suit=content.get('hotel_area2_suit', '度假游客'),
            hotel_tip=content.get('hotel_tip', '建议选择评价4.5星以上酒店'),
            **content,
            days_nights2=days_nights,
            tays=days,
            total_budget=total_budget,
            weather_tip=content.get('weather_tip', '关注天气预报，准备合适衣物'),
            emergency_phone="110/120",
            complaint_phone="12301",
            weather_query="中国天气网",
            useful_apps="高德地图、大众点评、携程旅行",
            generate_date=datetime.now().strftime("%Y-%m-%d")
        )
    
    def _estimate_budget(self, days: int, travelers: int, per_day: int, travel_type: str) -> int:
        """估算预算"""
        multipliers = {
            '穷游': 0.5,
            '品质游': 1.0,
            '豪华游': 2.0,
            '亲子游': 1.2,
            '蜜月游': 1.5
        }
        multiplier = multipliers.get(travel_type, 1.0)
        return int(days * travelers * per_day * multiplier)
    
    def _generate_content_by_type(self, destination: str, days: int, travel_type: str) -> Dict:
        """根据目的地类型生成内容"""
        dest_lower = destination.lower()
        
        # 根据目的地关键词匹配
        if any(k in dest_lower for k in ['北京', '故宫', '长城']):
            return {
                'best_season': '春秋季',
                'hotel_area1': '东城/西城区',
                'hotel_area1_desc': '靠近故宫、天安门',
                'hotel_area1_suit': '观光游客',
                'hotel_area2': '朝阳/海淀区',
                'hotel_area2_desc': '商圈发达，交通便利',
                'hotel_area2_suit': '商务游客',
                'hotel_tip': '建议住地铁沿线，出行方便',
                'day1_theme': '经典初探',
                'day1_arrival': '首都机场/北京站',
                'day1_lunch': '王府井/前门',
                'day1_lunch_tip': '老字号美食',
                'day1_afternoon': '天安门广场+故宫',
                'day1_afternoon_place': '故宫博物院',
                'day1_dinner': '簋街',
                'day1_highlight': '天安门降旗仪式（视季节）',
                'day2_theme': '文化之旅',
                'day2_morning': '八达岭长城',
                'day2_morning_place': '八达岭长城',
                'day2_lunch': '长城脚下农家乐',
                'day2_afternoon': '颐和园',
                'day2_afternoon_place': '颐和园',
                'day2_evening': '国家大剧院演出',
                'day2_evening_place': '国家大剧院',
                'day2_highlight': '长城好汉坡打卡',
                'day3_theme': '京城韵味',
                'day3_morning': '天坛公园',
                'day3_morning_place': '天坛',
                'day3_lunch': '南锣鼓巷',
                'day3_afternoon': '胡同游',
                'day3_afternoon_place': '什刹海',
                'day3_evening': '返程',
                'day3_highlight': '后海酒吧街夜景',
                'food1': '北京烤鸭',
                'food1_place': '全聚德/便宜坊',
                'food1_cost': '150-300元',
                'food1_addr': '多家分店',
                'food2': '老北京炸酱面',
                'food2_place': '海碗居',
                'food2_cost': '30-50元',
                'food2_addr': '东四店',
                'food_street1': '王府井小吃街',
                'food_street2': '簋街美食街',
                '交通单价': '800',
                'travelers': travelers if 'travelers' in dir() else 1,
                '住宿晚数': max(0, days-1),
                '住宿单价': '500',
                '餐饮单价': '150',
                '门票总价': '300',
                '市内交通费': '200',
                '购物费': '500'
            }
        else:
            # 默认通用模板
            return {
                'best_season': '春秋季',
                'hotel_area1': '市中心',
                'hotel_area1_desc': '交通便利',
                'hotel_area1_suit': '观光游客',
                'hotel_area2': '景区附近',
                'hotel_area2_desc': '环境优美',
                'hotel_area2_suit': '度假游客',
                'hotel_tip': '建议提前预订',
                'day1_theme': '初探目的地',
                'day1_arrival': destination,
                'day1_lunch': '推荐餐厅',
                'day1_lunch_tip': '当地特色',
                'day1_afternoon': '游览',
                'day1_afternoon_place': '推荐景点',
                'day1_dinner': '美食街',
                'day1_highlight': '标志性景点',
                'day2_theme': '深度体验',
                'day2_morning': '游览',
                'day2_morning_place': '推荐景点',
                'day2_lunch': '特色餐厅',
                'day2_afternoon': '探索',
                'day2_afternoon_place': '推荐地点',
                'day2_evening': '夜生活',
                'day2_evening_place': '推荐场所',
                'day2_highlight': '特色体验',
                'day3_theme': '休闲返程',
                'day3_morning': '购物',
                'day3_morning_place': '商业区',
                'day3_lunch': '告别美食',
                'day3_afternoon': '返程',
                'day3_afternoon_place': '准备离开',
                'day3_evening': '返程',
                'day3_highlight': '带走美好回忆',
                'food1': '当地特色美食',
                'food1_place': '推荐餐厅',
                'food1_cost': '50-100元',
                'food1_addr': '市中心',
                'food2': '街头小吃',
                'food2_place': '美食街',
                'food2_cost': '20-50元',
                'food2_addr': '步行街',
                'food_street1': '美食街1',
                'food_street2': '美食街2',
                'weather_tip': '关注天气预报，准备合适衣物',
                '交通单价': '800',
                'travelers': travelers if 'travelers' in dir() else 1,
                '住宿晚数': max(0, days-1),
                '住宿单价': '400',
                '餐饮单价': '100',
                '门票总价': '200',
                '市内交通费': '150',
                '购物费': '300'
            }


if __name__ == "__main__":
    generator = TravelGuideGenerator()
    
    guide = generator.generate_guide(
        destination="北京",
        days=3,
        travelers=2,
        travel_type="品质游",
        budget_per_day=800
    )
    
    print(guide)
