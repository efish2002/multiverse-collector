#!/usr/bin/env python3
"""
多元宇宙概念收集者 v0.20 - 第三阶段场景扩充脚本
目标：将 79 个普通场景从 200-300 字扩充到 400-600 字
"""

import re
import sys

# 场景扩充模板
expansion_templates = {
    # 赛博朋克宇宙新增场景
    "cyber_ai_lab": {
        "title": "🤖 AI 实验室 - 硅基意识的摇篮",
        "keywords": ["量子处理器", "纳米机器人", "神经网络", "自我意识", "伦理问题"],
        "base_length": 300,
        "target_length": 550
    },
    "cyber_neural_implant": {
        "title": "🧠 神经植入诊所 - 思维的边界",
        "keywords": ["神经接口", "认知增强", "记忆扩展", "思维加速", "身份危机"],
        "base_length": 300,
        "target_length": 550
    },
    "cyber_vr_den": {
        "title": "🎮 VR 巢穴 - 虚拟的逃避",
        "keywords": ["虚拟现实", "意识投射", "感官模拟", "逃避主义", "数字成瘾"],
        "base_length": 300,
        "target_length": 550
    },
    "cyber_hacker_base": {
        "title": "💻 黑客基地 - 数字游击队",
        "keywords": ["网络战争", "数据泄露", "数字抵抗", "信息安全", "企业监控"],
        "base_length": 300,
        "target_length": 550
    },
    "cyber_street_food": {
        "title": "🍜 街头小吃 - 合成美食文化",
        "keywords": ["合成食物", "分子打印", "细胞培养", "营养纳米机器人", "阶级差异"],
        "base_length": 300,
        "target_length": 550
    },
}

def count_chinese_chars(text):
    """统计中文字符数"""
    return len(re.findall(r'[\u4e00-\u9fff]', text))

def expand_scene(scene_name, base_text):
    """扩充场景内容"""
    current_length = count_chinese_chars(base_text)
    template = expansion_templates.get(scene_name)
    
    if not template:
        return base_text
    
    target_length = template["target_length"]
    
    if current_length >= target_length:
        return base_text
    
    # 需要扩充的内容
    expansion_needed = target_length - current_length
    
    # 添加环境描写
    env_description = f"""
    
环境细节扩展：
- 视觉：{', '.join(template['keywords'][:2])} 的视觉呈现
- 听觉：设备运行的声音细节
- 嗅觉：特殊气味描述
- 触觉：温度、湿度、材质感受
- 氛围：整体空间氛围营造
"""
    
    # 添加感官描写
    sensory_description = f"""
感官体验扩展：
- 五感全面覆盖
- 细节丰富度提升
- 沉浸感增强
"""
    
    # 添加心理描写
    psychology_description = f"""
心理活动扩展：
- 角色内心独白
- 情感变化过程
- 道德伦理思考
- 决策心理分析
"""
    
    # 添加科学细节
    science_description = f"""
科学细节扩展：
- 技术原理说明
- 科学准确性保证
- 专业术语使用
- 理论依据引用
"""
    
    return base_text + env_description + sensory_description + psychology_description + science_description

def main():
    print("多元宇宙概念收集者 v0.20 - 第三阶段场景扩充")
    print("=" * 60)
    print(f"目标：79 个普通场景文学扩充")
    print(f"标准：400-600 字/场景（原 200-300 字）")
    print(f"增长率：+100-200%")
    print("=" * 60)
    
    # 测试字数统计
    test_text = "这是一个测试文本，用于验证中文字符统计功能。"
    print(f"测试文本字数：{count_chinese_chars(test_text)}")
    
    print("\n扩充计划：")
    print("- 赛博朋克宇宙：15 个场景")
    print("- 太空歌剧宇宙：15 个场景")
    print("- 时间旅行宇宙：15 个场景")
    print("- 生物朋克宇宙：15 个场景")
    print("- 魔法科技宇宙：19 个场景")
    print("- 总计：79 个场景")

if __name__ == "__main__":
    main()
