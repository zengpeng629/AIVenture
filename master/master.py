# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-08-12 15:03:33
 @Email: zeng.peng@hotmail.com
"""

import openai
import os
from dotenv import load_dotenv
from master_prompt import get_options_prompt
load_dotenv()

class Master:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

        self.api_base = os.getenv("OPENAI_API_BASE", openai.api_base)
        openai.api_base = self.api_base

    def set_backgound(self, backgound):
        self.backgound = backgound

    async def generate_options_for_player(self, player):
        # 这里只是一个示例，你可以基于玩家的属性或历史来生成不同的选项
        # base_options = ["选择1", "选择2", "选择3", "选择4"]
        # personalized_options = [f"{option} for {player.name}" for option in base_options]
        # return personalized_options
    
        prompt = get_options_prompt.format(self.backgound, player.name, player.memory)


    async def generate_story_based_on_choices(self, choice):
        prompt = f"玩家选择了{choice}。接着..."
        print(prompt)
        # completion = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        # messages=[
        #     {"role": "system", "content": "You are a helpful assistant."},
        #     {"role": "user", "content": "Hello!"}
        # ]
        # )

        # print(completion.choices[0].message)
