# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-08-12 17:04:34
 @Email: zeng.peng@hotmail.com
"""

class NewWorldConfig:
    def __init__(self):
        self.stories = {
            "冒险之旅": "你们是勇敢的骑士，被派遣到一个神秘的岛屿，寻找失落的宝藏。但这个岛屿上充满了危险...",
            "赛博朋克世界": "你们生活在2078年，世界变成了赛博朋克风的世界，充满了科技和腐朽..."
            # 在这里添加更多的故事背景
        }

    def get_story_prompt(self, story_name):
        return self.stories.get(story_name, "")
    
    def list_stories(self):
        return list(self.stories.keys())
