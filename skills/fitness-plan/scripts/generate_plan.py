#!/usr/bin/env python3
"""
健身计划定制器
根据目标生成个性化健身计划
"""

from datetime import datetime
from typing import Dict, List, Optional


class FitnessPlanGenerator:
    """健身计划生成器类"""
    
    def __init__(self):
        self.template = self._load_template()
    
    def _load_template(self) -> str:
        """加载健身计划模板"""
        return """# {goal}健身计划

## 基本信息
- **健身目标**：{goal}
- **训练周期**：{duration}
- **每周训练**：{days_per_week}天
- **计划开始日期**：{start_date}

## 身体状况评估
| 项目 | 数值 | 评估 |
|------|------|------|
| 身高 | {height}cm |  |
| 体重 | {weight}kg |  |
| BMI | {bmi} | {bmi_result} |
| 健身基础 | {fitness_level} |  |

---

## 训练计划概览

### 每周训练安排
| 星期 | 训练内容 | 主要目标 |
|------|----------|----------|
| {week_schedule} |

---

## 热身方案（每次训练前5-10分钟）

1. **慢速有氧**：{warmup_cardio}
2. **关节活动**：{warmup_joints}
3. **动态拉伸**：{warmup_stretch}

---

## 每日训练详情

### {day1_name}：{day1_focus}

**训练部位**：{day1_target}

**训练动作**：
| 动作 | 组数 | 次数 | 组间休息 | 要点 |
|------|------|------|----------|------|
| {day1_ex1_name} | {day1_ex1_sets} | {day1_ex1_reps} | {day1_ex1_rest} | {day1_ex1_tip} |
| {day1_ex2_name} | {day1_ex2_sets} | {day1_ex2_reps} | {day1_ex2_rest} | {day1_ex2_tip} |
| {day1_ex3_name} | {day1_ex3_sets} | {day1_ex3_reps} | {day1_ex3_rest} | {day1_ex3_tip} |
| {day1_ex4_name} | {day1_ex4_sets} | {day1_ex4_reps} | {day1_ex4_rest} | {day1_ex4_tip} |
| {day1_ex5_name} | {day1_ex5_sets} | {day1_ex5_reps} | {day1_ex5_rest} | {day1_ex5_tip} |

**有氧训练**：{day1_cardio}

---

### {day2_name}：{day2_focus}

**训练部位**：{day2_target}

**训练动作**：
| 动作 | 组数 | 次数 | 组间休息 | 要点 |
|------|------|------|----------|------|
| {day2_ex1_name} | {day2_ex1_sets} | {day2_ex1_reps} | {day2_ex1_rest} | {day2_ex1_tip} |
| {day2_ex2_name} | {day2_ex2_sets} | {day2_ex2_reps} | {day2_ex2_rest} | {day2_ex2_tip} |
| {day2_ex3_name} | {day2_ex3_sets} | {day2_ex3_reps} | {day2_ex3_rest} | {day2_ex3_tip} |
| {day2_ex4_name} | {day2_ex4_sets} | {day2_ex4_reps} | {day2_ex4_rest} | {day2_ex4_tip} |
| {day2_ex5_name} | {day2_ex5_sets} | {day2_ex5_reps} | {day2_ex5_rest} | {day2_ex5_tip} |

**有氧训练**：{day2_cardio}

---

### {day3_name}：{day3_focus}

**训练部位**：{day3_target}

**训练动作**：
| 动作 | 组数 | 次数 | 组间休息 | 要点 |
|------|------|------|----------|------|
| {day3_ex1_name} | {day3_ex1_sets} | {day3_ex1_reps} | {day3_ex1_rest} | {day3_ex1_tip} |
| {day3_ex2_name} | {day3_ex2_sets} | {day3_ex2_reps} | {day3_ex2_rest} | {day3_ex2_tip} |
| {day3_ex3_name} | {day3_ex3_sets} | {day3_ex3_reps} | {day3_ex3_rest} | {day3_ex3_tip} |
| {day3_ex4_name} | {day3_ex4_sets} | {day3_ex4_reps} | {day3_ex4_rest} | {day3_ex4_tip} |
| {day3_ex5_name} | {day3_ex5_sets} | {day3_ex5_reps} | {day3_ex5_rest} | {day3_ex5_tip} |

**有氧训练**：{day3_cardio}

---

## 拉伸放松（每次训练后10-15分钟）

1. 胸部拉伸：{stretch_chest}（30秒/侧）
2. 背部拉伸：{stretch_back}（30秒/侧）
3. 腿部拉伸：{stretch_legs}（30秒/侧）
4. 肩部拉伸：{stretch_shoulders}（30秒/侧）

---

## 饮食建议

### 营养目标
| 营养素 | 每日摄入 | 说明 |
|--------|----------|------|
| 蛋白质 | {protein_intake}g | 体重×{protein_ratio} |
| 碳水 | {carb_intake}g | 主要能量来源 |
| 脂肪 | {fat_intake}g | 健康脂肪为主 |
| 总热量 | {total_calories}kcal | {calorie_tip} |

### 饮食原则
1. **蛋白质**：{protein_principle}
2. **碳水**：{carb_principle}
3. **脂肪**：{fat_principle}
4. **饮水**：每天{water_intake}ml

### 食物选择
- **优质蛋白**：{protein_foods}
- **复合碳水**：{carb_foods}
- **健康脂肪**：{fat_foods}

---

## 注意事项

### 训练安全
- {safety_tip1}
- {safety_tip2}
- {safety_tip3}

### 生活习惯
- 保证每天{睡眠时长}小时睡眠
- 训练后补充蛋白质
- 避免过度训练

### 进度评估
- {evaluation_tip}

---

## 进度跟踪表

| 周次 | 体重 | 体脂 | 围度 | 训练感受 |
|------|------|------|------|----------|
| 第1周 |      |      |      |          |
| 第2周 |      |      |      |          |
| 第4周 |      |      |      |          |
| 第8周 |      |      |      |          |
| 第12周 |      |      |      |          |

---

*计划生成时间：{generate_date}*
*坚持就是胜利，加油！💪*
"""
    
    def calculate_bmi(self, height: float, weight: float) -> tuple:
        """计算BMI"""
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        
        if bmi < 18.5:
            result = "偏瘦"
        elif bmi < 24:
            result = "正常"
        elif bmi < 28:
            result = "偏胖"
        else:
            result = "肥胖"
        
        return round(bmi, 1), result
    
    def generate_plan(self,
                     goal: str = "增肌",
                     height: float = 170,
                     weight: float = 70,
                     age: int = 25,
                     gender: str = "男",
                     fitness_level: str = "新手",
                     available_equipment: List[str] = None,
                     days_per_week: int = 4,
                     duration: str = "12周",
                     start_date: Optional[str] = None) -> str:
        """生成健身计划"""
        
        if available_equipment is None:
            available_equipment = ["哑铃", "杠铃", "龙门架"]
        
        if start_date is None:
            start_date = datetime.now().strftime("%Y-%m-%d")
        
        # 计算BMI
        bmi, bmi_result = self.calculate_bmi(height, weight)
        
        # 根据目标调整内容
        if goal == "减脂":
            return self._generate_fat_loss_plan(
                height, weight, age, gender, fitness_level,
                days_per_week, duration, start_date, bmi, bmi_result
            )
        elif goal == "增肌":
            return self._generate_muscle_gain_plan(
                height, weight, age, gender, fitness_level,
                days_per_week, duration, start_date, bmi, bmi_result
            )
        else:
            return self._generate_body_shaping_plan(
                height, weight, age, gender, fitness_level,
                days_per_week, duration, start_date, bmi, bmi_result
            )
    
    def _generate_muscle_gain_plan(self, height, weight, age, gender, fitness_level, days, duration, start_date, bmi, bmi_result) -> str:
        """生成增肌计划"""
        protein_intake = int(weight * 2.0)
        carb_intake = int(weight * 4.0)
        fat_intake = int(weight * 0.8)
        total_calories = protein_intake * 4 + carb_intake * 4 + fat_intake * 9
        
        return self.template.format(
            goal="增肌",
            duration=duration,
            days_per_week=days,
            start_date=start_date,
            height=height,
            weight=weight,
            bmi=bmi,
            bmi_result=bmi_result,
            fitness_level=fitness_level,
            week_schedule="周一 胸+三头 | 周二 背+二头 | 周三 休息 | 周四 肩+腹 | 周五 腿 | 周六 有氧+核心 | 周日 休息",
            warmup_cardio="跑步机慢跑5分钟",
            warmup_joints="肩关节绕环、髋关节激活",
            warmup_stretch="腿部摆动、臂大肌激活",
            day1_name="周一",
            day1_focus="推类训练",
            day1_target="胸大肌、三头肌",
            day1_ex1_name="杠铃卧推", day1_ex1_sets="4", day1_ex1_reps="8-12", day1_ex1_rest="90秒", day1_ex1_tip="控制下落速度",
            day1_ex2_name="哑铃上斜卧推", day1_ex2_sets="4", day1_ex2_reps="10-12", day1_ex2_rest="90秒", day1_ex2_tip="凳子倾斜30度",
            day1_ex3_name="蝴蝶机夹胸", day1_ex3_sets="3", day1_ex3_reps="12-15", day1_ex3_rest="60秒", day1_ex3_tip="顶峰收缩",
            day1_ex4_name="绳索下压", day1_ex4_sets="3", day1_ex4_reps="12-15", day1_ex4_rest="60秒", day1_ex4_tip="手肘固定",
            day1_ex5_name="过头臂屈伸", day1_ex5_sets="3", day1_ex5_reps="12-15", day1_ex5_rest="60秒", day1_ex5_tip="手臂贴近耳朵",
            day1_cardio="训练后20分钟低强度有氧",
            day2_name="周二",
            day2_focus="拉类训练",
            day2_target="背阔肌、二头肌",
            day2_ex1_name="引体向上/高位下拉", day2_ex1_sets="4", day2_ex1_reps="8-12", day2_ex1_rest="90秒", day2_ex1_tip="挺胸沉肩",
            day2_ex2_name="坐姿划船", day2_ex2_sets="4", day2_ex2_reps="10-12", day2_ex2_rest="90秒", day2_ex2_tip="夹肘而非甩臂",
            day2_ex3_name="哑铃划船", day2_ex3_sets="3", day2_ex3_reps="10-12", day2_ex3_rest="60秒", day2_ex3_tip="单手支撑",
            day2_ex4_name="杠铃弯举", day2_ex4_sets="3", day2_ex4_reps="12-15", day2_ex4_rest="60秒", day2_ex4_tip="顶峰收缩",
            day2_ex5_name="锤式弯举", day2_ex5_sets="3", day2_ex5_reps="12-15", day2_ex5_rest="60秒", day2_ex5_tip="手腕固定",
            day2_cardio="训练后20分钟低强度有氧",
            day3_name="周三",
            day3_focus="休息与恢复",
            day3_target="全身拉伸与放松",
            day3_ex1_name="全身拉伸", day3_ex1_sets="1", day3_ex1_reps="30分钟", day3_ex1_rest="-", day3_ex1_tip="充分放松",
            day3_ex2_name="泡沫轴放松", day3_ex2_sets="1", day3_ex2_reps="20分钟", day3_ex2_rest="-", day3_ex2_tip="针对酸痛部位",
            day3_ex3_name="散步/轻度活动", day3_ex3_sets="1", day3_ex3_reps="30分钟", day3_ex3_rest="-", day3_ex3_tip="促进血液循环",
            day3_ex4_name="-", day3_ex4_sets="-", day3_ex4_reps="-", day3_ex4_rest="-", day3_ex4_tip="-",
            day3_ex5_name="-", day3_ex5_sets="-", day3_ex5_reps="-", day3_ex5_rest="-", day3_ex5_tip="-",
            day3_cardio="可选择30分钟轻松有氧",
            stretch_chest="门框胸部拉伸",
            stretch_back="猫式伸展",
            stretch_legs="股四头肌拉伸",
            stretch_shoulders="交叉手臂肩部拉伸",
            protein_intake=protein_intake,
            protein_ratio="2.0g",
            carb_intake=carb_intake,
            fat_intake=fat_intake,
            total_calories=total_calories,
            calorie_tip="热量盈余约300-500kcal",
            protein_principle="每餐摄入优质蛋白（鸡胸肉、鱼、蛋、牛肉）",
            carb_principle="训练前后补充碳水（米饭、面条、红薯）",
            fat_principle="适量健康脂肪（坚果、牛油果、橄榄油）",
            water_intake="2500-3000",
            protein_foods="鸡胸肉、牛肉、鱼、鸡蛋、牛奶、豆制品",
            carb_foods="米饭、面条、红薯、燕麦、全麦面包",
            fat_foods="坚果、橄榄油、牛油果、三文鱼",
            safety_tip1="训练前充分热身，避免受伤",
            safety_tip2="使用合适重量，先求动作标准再增加重量",
            safety_tip3="感到不适立即停止，必要时寻求专业帮助",
            睡眠时长="7-9",
            evaluation_tip="每4周评估一次体重、围度和力量进步",
            generate_date=datetime.now().strftime("%Y-%m-%d")
        )
    
    def _generate_fat_loss_plan(self, height, weight, age, gender, fitness_level, days, duration, start_date, bmi, bmi_result) -> str:
        """生成减脂计划"""
        protein_intake = int(weight * 2.2)
        carb_intake = int(weight * 2.5)
        fat_intake = int(weight * 0.6)
        total_calories = protein_intake * 4 + carb_intake * 4 + fat_intake * 9
        
        return self.template.format(
            goal="减脂",
            duration=duration,
            days_per_week=days,
            start_date=start_date,
            height=height,
            weight=weight,
            bmi=bmi,
            bmi_result=bmi_result,
            fitness_level=fitness_level,
            week_schedule="周一 全身力量 | 周二 HIIT训练 | 周三 休息 | 周四 全身力量 | 周五 有氧+核心 | 周六 低强度有氧 | 周日 休息",
            warmup_cardio="跑步机快走或椭圆机10分钟",
            warmup_joints="全身关节活动",
            warmup_stretch="动态拉伸",
            day1_name="周一",
            day1_focus="全身力量训练",
            day1_target="全身主要肌群",
            day1_ex1_name="深蹲", day1_ex1_sets="4", day1_ex1_reps="15-20", day1_ex1_rest="60秒", day1_ex1_tip="膝盖不内扣",
            day1_ex2_name="哑铃卧推", day1_ex2_sets="4", day1_ex2_reps="12-15", day1_ex2_rest="60秒", day1_ex2_tip="控制速度",
            day1_ex3_name="哑铃划船", day1_ex3_sets="4", day1_ex3_reps="12-15", day1_ex3_rest="60秒", day1_ex3_tip="背部挺直",
            day1_ex4_name="平板支撑", day1_ex4_sets="3", day1_ex4_reps="45-60秒", day1_ex4_rest="30秒", day1_ex4_tip="核心收紧",
            day1_ex5_name="罗马椅挺身", day1_ex5_sets="3", day1_ex5_reps="15", day1_ex5_rest="60秒", day1_ex5_tip="控制幅度",
            day1_cardio="训练后30分钟有氧",
            day2_name="周二",
            day2_focus="HIIT高强度训练",
            day2_target="心肺功能+燃脂",
            day2_ex1_name="热身", day2_ex1_sets="1", day2_ex1_reps="5分钟", day2_ex1_rest="-", day2_ex1_tip="动态拉伸",
            day2_ex2_name="波比跳", day2_ex2_sets="4", day2_ex2_reps="20秒全力/40秒休息", day2_ex2_rest="循环10次", day2_ex2_tip="量力而行",
            day2_ex3_name="高抬腿", day2_ex3_sets="4", day2_ex3_reps="30秒全力/30秒休息", day2_ex3_rest="循环8次", day2_ex3_tip="膝盖抬高",
            day2_ex4_name="开合跳", day2_ex4_sets="3", day2_ex4_reps="30秒/组", day2_ex4_rest="30秒", day2_ex4_tip="手脚协调",
            day2_ex5_name="冲刺跑", day2_ex5_sets="6", day2_ex5_reps="20秒全力/40秒走路", day2_ex5_rest="循环6次", day2_ex5_tip="安全场地",
            day2_cardio="无（已是高强度）",
            day3_name="周三",
            day3_focus="休息与恢复",
            day3_target="主动恢复",
            day3_ex1_name="瑜伽/拉伸", day3_ex1_sets="1", day3_ex1_reps="40分钟", day3_ex1_rest="-", day3_ex1_tip="全身放松",
            day3_ex2_name="散步", day3_ex2_sets="1", day3_ex2_reps="30-60分钟", day3_ex2_rest="-", day3_ex2_tip="促进恢复",
            day3_ex3_name="-", day3_ex3_sets="-", day3_ex3_reps="-", day3_ex3_rest="-", day3_ex3_tip="-",
            day3_ex4_name="-", day3_ex4_sets="-", day3_ex4_reps="-", day3_ex4_rest="-", day3_ex4_tip="-",
            day3_ex5_name="-", day3_ex5_sets="-", day3_ex5_reps="-", day3_ex5_rest="-", day3_ex5_tip="-",
            day3_cardino="40分钟轻松有氧（可选）",
            stretch_chest="门框拉伸+墙面拉伸",
            stretch_back="婴儿式+猫式伸展",
            stretch_legs="股四头肌+腘绳肌拉伸",
            stretch_shoulders="肩部绕环+交叉手臂",
            protein_intake=protein_intake,
            protein_ratio="2.2g",
            carb_intake=carb_intake,
            fat_intake=fat_intake,
            total_calories=total_calories,
            calorie_tip="热量缺口约300-500kcal",
            protein_principle="高蛋白饮食，保持肌肉（鸡胸肉、鱼、蛋白）",
            carb_principle="放在训练前后，避免精制糖",
            fat_principle="适量优质脂肪，减少饱和脂肪",
            water_intake="3000+",
            protein_foods="鸡胸肉、鱼、虾、蛋清、低脂奶",
            carb_foods="红薯、燕麦、蔬菜、全麦",
            fat_foods="坚果、橄榄油、鱼油",
            safety_tip1="HIIT训练根据身体状况调整强度",
            safety_tip2="保持水分，少量多次饮水",
            safety_tip3="保证充足睡眠，促进恢复",
            睡眠时长="7-8",
            evaluation_tip="每周称重记录，关注体脂变化而非单纯体重",
            generate_date=datetime.now().strftime("%Y-%m-%d")
        )
    
    def _generate_body_shaping_plan(self, height, weight, age, gender, fitness_level, days, duration, start_date, bmi, bmi_result) -> str:
        """生成塑形计划"""
        protein_intake = int(weight * 2.0)
        carb_intake = int(weight * 3.0)
        fat_intake = int(weight * 0.7)
        total_calories = protein_intake * 4 + carb_intake * 4 + fat_intake * 9
        
        return self.template.format(
            goal="塑形",
            duration=duration,
            days_per_week=days,
            start_date=start_date,
            height=height,
            weight=weight,
            bmi=bmi,
            bmi_result=bmi_result,
            fitness_level=fitness_level,
            week_schedule="周一 臀腿 | 周二 胸肩 | 周三 休息 | 周四 背手臂 | 周五 核心+有氧 | 周六 全身 | 周日 休息",
            warmup_cardio="椭圆机5-10分钟",
            warmup_joints="全身关节激活",
            warmup_stretch="动态拉伸",
            day1_name="周一",
            day1_focus="臀腿塑形",
            day1_target="臀大肌、股四头肌、腘绳肌",
            day1_ex1_name="深蹲", day1_ex1_sets="4", day1_ex1_reps="15", day1_ex1_rest="60秒", day1_ex1_tip="膝盖与脚尖同向",
            day1_ex2_name="臀桥", day1_ex2_sets="4", day1_ex2_reps="15", day1_ex2_rest="60秒", day1_ex2_tip="顶峰收紧",
            day1_ex3_name="保加利亚深蹲", day1_ex3_sets="3", day1_ex3_reps="12/侧", day1_ex3_rest="60秒", day1_ex3_tip="后脚抬高",
            day1_ex4_name="腿弯举", day1_ex4_sets="3", day1_ex4_reps="15", day1_ex4_rest="45秒", day1_ex4_tip="控制下落",
            day1_ex5_name="侧卧抬腿", day1_ex5_sets="3", day1_ex5_reps="15/侧", day1_ex5_rest="30秒", day1_ex5_tip="腿部伸直",
            day1_cardio="训练后20分钟有氧",
            day2_name="周二",
            day2_focus="上肢塑形",
            day2_target="胸、肩、手臂",
            day2_ex1_name="上斜哑铃卧推", day2_ex1_sets="4", day2_ex1_reps="12", day2_ex1_rest="60秒", day2_ex1_tip="控制幅度",
            day2_ex2_name="侧平举", day2_ex2_sets="4", day2_ex2_reps="15", day2_ex2_rest="45秒", day2_ex2_tip="小臂低于肘",
            day2_ex3_name="绳索夹胸", day2_ex3_sets="3", day2_ex3_reps="15", day2_ex3_rest="45秒", day2_ex3_tip="手臂微屈",
            day2_ex4_name="哑铃锤式弯举", day2_ex4_sets="3", day2_ex4_reps="12", day2_ex4_rest="45秒", day2_ex4_tip="顶峰收缩",
            day2_ex5_name="过头臂屈伸", day2_ex5_sets="3", day2_ex5_reps="12", day2_ex5_rest="45秒", day2_ex5_tip="控制速度",
            day2_cardio="训练后20分钟有氧",
            day3_name="周三",
            day3_focus="休息与恢复",
            day3_target="放松与拉伸",
            day3_ex1_name="瑜伽", day3_ex1_sets="1", day3_ex1_reps="40分钟", day3_ex1_rest="-", day3_ex1_tip="放松身心",
            day3_ex2_name="-", day3_ex2_sets="-", day3_ex2_reps="-", day3_ex2_rest="-", day3_ex2_tip="-",
            day3_ex3_name="-", day3_ex3_sets="-", day3_ex3_reps="-", day3_ex3_rest="-", day3_ex3_tip="-",
            day3_ex4_name="-", day3_ex4_sets="-", day3_ex4_reps="-", day3_ex4_rest="-", day3_ex4_tip="-",
            day3_ex5_name="-", day3_ex5_sets="-", day3_ex5_reps="-", day3_ex5_rest="-", day3_ex5_tip="-",
            day3_cardio="可选择30分钟轻松有氧",
            stretch_chest="门框胸部拉伸",
            stretch_back="婴儿式伸展",
            stretch_legs="腿部拉伸",
            stretch_shoulders="肩部交叉拉伸",
            protein_intake=protein_intake,
            protein_ratio="2.0g",
            carb_intake=carb_intake,
            fat_intake=fat_intake,
            total_calories=total_calories,
            calorie_tip="维持或轻微缺口",
            protein_principle="适量蛋白，支持肌肉线条",
            carb_principle="训练前后补充，适量即可",
            fat_principle="优质脂肪，适量摄入",
            water_intake="2500",
            protein_foods="鸡胸肉、鱼、蛋、奶",
            carb_foods="红薯、糙米、燕麦",
            fat_foods="坚果、橄榄油、牛油果",
            safety_tip1="塑形以多次数、轻重量为主",
            safety_tip2="注意肌肉发力感",
            safety_tip3="训练后充分拉伸，避免肌肉僵硬",
            睡眠时长="7-8",
            evaluation_tip="关注体型变化和穿衣效果",
            generate_date=datetime.now().strftime("%Y-%m-%d")
        )


if __name__ == "__main__":
    generator = FitnessPlanGenerator()
    
    plan = generator.generate_plan(
        goal="增肌",
        height=175,
        weight=70,
        age=25,
        gender="男",
        fitness_level="新手",
        days_per_week=4,
        duration="12周"
    )
    
    print(plan)
