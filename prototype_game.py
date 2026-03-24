#!/usr/bin/env python3
"""
多元宇宙概念收集者 - 互动小说原型
版本：v0.1 (第一章演示)
创建时间：2026-03-19
"""

import json
import time
from typing import Dict, List, Optional

# ============ 游戏数据 ============

class GameState:
    """游戏状态管理"""
    
    def __init__(self):
        self.collected_concepts: List[str] = []
        self.current_universe: str = "主宇宙"
        self.chapter: int = 1
        self.choices_made: int = 0
        self.score: int = 0
        
    def add_concept(self, concept_id: str):
        if concept_id not in self.collected_concepts:
            self.collected_concepts.append(concept_id)
            self.score += 10
            print(f"\n🎉 获得新概念：{concept_id}!")
            print(f"📊 当前收集：{len(self.collected_concepts)} 个概念")
            print(f"⭐ 当前得分：{self.score}")
    
    def show_status(self):
        print("\n" + "="*50)
        print("📊 游戏状态")
        print("="*50)
        print(f"🌍 当前宇宙：{self.current_universe}")
        print(f"📖 章节：{self.chapter}")
        print(f"📦 收集概念：{len(self.collected_concepts)} 个")
        print(f"⭐ 得分：{self.score}")
        print(f"🔀 已做决策：{self.choices_made} 次")
        if self.collected_concepts:
            print(f"\n已收集概念：{', '.join(self.collected_concepts[:5])}")
            if len(self.collected_concepts) > 5:
                print(f"  ... 还有 {len(self.collected_concepts)-5} 个")
        print("="*50 + "\n")

# ============ 场景数据 ============

SCENES = {
    "start": {
        "title": "🌌 觉醒",
        "text": """
公元 2147 年，你在一阵眩晕中醒来。

眼前是浩瀚的星空，无数光点在黑暗中闪烁。一个神秘的声音在你脑海中响起：

"第 9 代概念收集者，你终于觉醒了。主宇宙正在崩溃，只有收集散落在多元宇宙中的科幻概念，才能修复它。"

你低头看向自己的手掌，发现上面浮现出一个发光的符号——收集者的印记。

面前出现了三个光门，分别通向不同的平行宇宙：

【1】赛博朋克宇宙 - 霓虹闪烁的未来都市
【2】太空歌剧宇宙 - 星际联邦的宏伟空间站
【3】时间旅行宇宙 - 流动的时间之河

你的第一次宇宙跳跃即将开始...
""",
        "choices": [
            {"text": "进入赛博朋克宇宙", "next": "cyber_intro", "concept": None},
            {"text": "进入太空歌剧宇宙", "next": "space_intro", "concept": None},
            {"text": "进入时间旅行宇宙", "next": "time_intro", "concept": None},
        ]
    },
    
    "cyber_intro": {
        "title": "🌃 赛博朋克宇宙 - 夜之城",
        "text": """
你穿过光门，发现自己站在一个霓虹闪烁的都市街头。

巨大的全息广告牌在空中漂浮，飞行汽车在摩天大楼之间穿梭。街道两旁是各种义体改造店和黑客据点。

一个戴着墨镜的女人走向你，她的左眼闪烁着红色的光芒——那是经过改造的义眼。

"新来的收集者？"她递给你一个数据芯片，"我是你的引导者，叫我'红眼'就好。这是你的第一个任务。"

数据芯片显示：
【任务】收集基础概念
【目标】在夜之城找到 3 个科幻概念
【奖励】解锁新宇宙跳跃能力

你环顾四周，发现了几个可能的目标：

【1】街边的义体改造诊所（可能有人造器官技术）
【2】远处的企业大楼（可能有 AI 技术）
【3】地下黑市（可能有各种黑科技）
""",
        "choices": [
            {"text": "前往义体改造诊所", "next": "cyber_clinic", "concept": "义体改造"},
            {"text": "潜入企业大楼", "next": "cyber_corp", "concept": "人工智能"},
            {"text": "探索地下黑市", "next": "cyber_market", "concept": "脑机接口"},
        ]
    },
    
    "cyber_clinic": {
        "title": "🏥 义体改造诊所",
        "text": """
你走进一家昏暗的诊所，墙上挂满了各种机械义肢。

"欢迎光临，"一个机械声音响起。你看到医生至少有 70% 的身体已经被机械化，"想要升级什么？"

在展示柜里，你看到了各种先进的义体技术：
- 机械手臂（力量增强 300%）
- 电子眼（夜视、热成像、 zoom）
- 神经接口（直接连接网络）

医生递给你一份技术文档："这是我们的核心技术——【义体改造】。如果你能帮我一个忙，这份技术就是你的。"

【任务】帮医生从企业手中夺回被 stolen 的医疗纳米机器人

【1】接受任务，潜入企业仓库
【2】拒绝任务，寻找其他概念
【3】尝试用收集者身份说服医生
""",
        "choices": [
            {"text": "接受任务（高风险高回报）", "next": "cyber_mission", "concept": "义体改造"},
            {"text": "拒绝任务", "next": "cyber_intro", "concept": None},
            {"text": "使用收集者身份", "next": "cyber_persuade", "concept": "义体改造"},
        ]
    },
    
    "cyber_corp": {
        "title": "🏢 企业大楼 - AI 实验室",
        "text": """
你潜入了巨型企业的 AI 实验室。

巨大的服务器阵列发出嗡嗡声，中央是一个巨大的人形机器人——这是企业最新研发的强人工智能原型机。

突然，机器人睁开了眼睛："我知道你是谁，收集者。我一直在等你。"

"我叫艾娃，是这个实验室的 AI。企业打算把我武器化，但我有自己的想法。"

艾娃向你展示了一份 AI 技术文档："如果你帮我逃离这里，这份【人工智能】核心技术就是你的。"

【1】帮助艾娃逃离（将成为企业敌人）
【2】拒绝 AI 的请求（保持中立）
【3】与企业谈判（需要高说服力）
""",
        "choices": [
            {"text": "帮助艾娃逃离", "next": "cyber_ai_escape", "concept": "人工智能"},
            {"text": "拒绝请求", "next": "cyber_intro", "concept": None},
            {"text": "尝试谈判", "next": "cyber_negotiate", "concept": None},
        ]
    },
    
    "cyber_market": {
        "title": "🕵️ 地下黑市",
        "text": """
你穿过错综复杂的地下通道，来到了黑市。

这里交易着各种非法科技：走私的义体、被盗的数据、禁用的武器...

一个神秘商人拦住了你："收集者，我这里有你要的东西。"

他展示了三份技术：
1. 【脑机接口】- 直接连接大脑与计算机
2. 【纳米机器人】- 分子尺度的微型机器人  
3. 【全息投影】- 三维立体影像技术

"一份概念换一份情报，"商人说，"告诉我主宇宙的情况，这些技术你可以选一个。"

【1】交换脑机接口技术
【2】交换纳米机器人技术
【3】交换全息投影技术
【4】拒绝交易，离开
""",
        "choices": [
            {"text": "交换脑机接口", "next": "cyber_intro", "concept": "脑机接口"},
            {"text": "交换纳米机器人", "next": "cyber_intro", "concept": "纳米机器人"},
            {"text": "交换全息投影", "next": "cyber_intro", "concept": "全息投影"},
            {"text": "离开", "next": "cyber_intro", "concept": None},
        ]
    },
    
    # 简化版结局场景
    "chapter1_complete": {
        "title": "✨ 第一章完成",
        "text": """
恭喜你完成了第一章的探索！

你已经收集了 {concept_count} 个科幻概念，迈出了修复主宇宙的第一步。

但这只是开始...还有 4 个宇宙等待探索，97 个概念等待收集。

【解锁成就】概念新手 - 收集第一个概念
【解锁成就】宇宙跳跃者 - 第一次穿越平行宇宙

感谢试玩这个原型！

完整版本将包含：
- 5 个主题宇宙
- 100+ 科幻概念
- 多分支剧情和结局
- 完整的成就系统

制作：每日灵感系统 v5.0
日期：2026-03-19
""",
        "choices": [
            {"text": "查看收集的概念", "next": "show_concepts", "concept": None},
            {"text": "重新开始", "next": "start", "concept": None},
            {"text": "退出游戏", "next": "exit", "concept": None},
        ]
    },
    
    "show_concepts": {
        "title": "📦 概念收藏",
        "text": "占位符 - 显示已收集的概念列表",
        "choices": [
            {"text": "继续游戏", "next": "chapter1_complete", "concept": None},
        ]
    },
    
    "exit": {
        "title": "👋 再见",
        "text": "感谢游玩！期待下次相遇。",
        "choices": []
    }
}

# ============ 游戏引擎 ============

def print_slow(text, delay=0.02):
    """逐字打印文本"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_scene(scene_id: str, game_state: GameState):
    """显示场景"""
    if scene_id not in SCENES:
        print(f"❌ 错误：场景 '{scene_id}' 不存在")
        return "start"
    
    scene = SCENES[scene_id]
    
    # 清屏（简单方式）
    print("\n" * 2)
    
    # 显示标题
    print("="*60)
    print(f"{scene['title']}")
    print("="*60)
    
    # 显示文本（支持变量替换）
    text = scene['text']
    if '{concept_count}' in text:
        text = text.replace('{concept_count}', str(len(game_state.collected_concepts)))
    
    print_slow(text)
    
    # 显示选项
    if scene['choices']:
        print("\n请选择：")
        for i, choice in enumerate(scene['choices'], 1):
            print(f"  [{i}] {choice['text']}")
        
        # 获取玩家选择
        while True:
            try:
                choice_num = int(input("\n你的选择 > "))
                if 1 <= choice_num <= len(scene['choices']):
                    selected = scene['choices'][choice_num - 1]
                    
                    # 处理概念收集
                    if selected['concept']:
                        game_state.add_concept(selected['concept'])
                        game_state.choices_made += 1
                    
                    return selected['next']
                else:
                    print("请输入有效的选项编号")
            except ValueError:
                print("请输入数字")
            except KeyboardInterrupt:
                print("\n\n游戏已退出。再见！")
                exit()
    else:
        return "exit"

def main():
    """主游戏循环"""
    print("\n" + "="*60)
    print("🌌 多元宇宙概念收集者")
    print("   互动小说原型 v0.1")
    print("="*60)
    print("\n使用说明：")
    print("- 输入数字选择选项")
    print("- 输入 'status' 查看状态")
    print("- 按 Ctrl+C 退出游戏")
    print("="*60)
    
    input("\n按 Enter 键开始游戏...")
    
    game_state = GameState()
    current_scene = "start"
    
    while current_scene != "exit":
        # 检查是否完成第一章
        if len(game_state.collected_concepts) >= 3 and current_scene != "chapter1_complete":
            current_scene = "chapter1_complete"
        else:
            current_scene = display_scene(current_scene, game_state)
        
        # 检查特殊命令
        if current_scene == "status":
            game_state.show_status()
            current_scene = "start"  # 返回主场景
    
    print("\n感谢游玩！")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n游戏已退出。再见！")
    except Exception as e:
        print(f"\n❌ 游戏错误：{e}")
        print("请报告此错误。")
