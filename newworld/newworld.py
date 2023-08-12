# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-08-12 15:02:58
 @Email: zeng.peng@hotmail.com
"""
import sys
sys.path.append("..")

import asyncio
import websockets
import json
from player.player import Player
from newworld_config import NewWorldConfig

class NewWorld:
    def __init__(self, master):
        self.master = master
        self.connected_players = {}  # 使用字典存储 {websocket: Player对象}
        self.players_who_made_choices = set()
        self.config = NewWorldConfig()

    def display_message(self, msg, separator=True):
        if separator:
            print("=" * 50)
        print(msg)
        if separator:
            print("=" * 50)

    async def handle_player(self, websocket, path):
        client_address, client_port = websocket.remote_address

        # 提示玩家输入名字
        await websocket.send(json.dumps({"type": "name", "data": "请输入你的名字:"}))
        player_name = await websocket.recv()
        player = Player(player_name, client_address, client_port)
        self.connected_players[websocket] = player

        # 通知所有玩家新玩家的加入
        self.display_message(f"{player_name} 加入了游戏！")

        try:
            while True:
                # 为每个玩家生成不同的选择
                options = await self.master.generate_options_for_player(player)
                await websocket.send(json.dumps({"type": "options", "data": options}))

                choice = await websocket.recv()
                player.add_memory(choice)
                self.players_who_made_choices.add(player)

                # 检查所有玩家是否都已做出选择
                if len(self.players_who_made_choices) == len(self.connected_players):
                    all_choices = [p.memory[-1] for p in self.connected_players.values()]
                    story = await self.master.generate_story_based_on_choices(all_choices)
                    self.display_message(story)
                    self.players_who_made_choices.clear()  # 清空集合，为下一轮做准备
        except:
            pass
        finally:
            del self.connected_players[websocket]

    def run(self):
        # 输出CLI界面
        print("=============================================")
        print("              一个新世界即将开启                ")
        print("=============================================")
         # 获取所有可用的故事
        available_stories = self.config.list_stories()

        print("请选择一个故事开始:")
        for idx, story in enumerate(available_stories, 1):
            print(f"{idx}. {story}")

        chosen_idx = -1
        while chosen_idx < 0 or chosen_idx >= len(available_stories):
            try:
                chosen_idx = int(input(f"\n请选择一个故事: ")) - 1
            except ValueError:
                pass

        chosen_story = available_stories[chosen_idx]
        prompt = self.config.get_story_prompt(chosen_story)
        self.master.set_backgound(prompt)

        start_server = websockets.serve(self.handle_player, "127.0.0.1", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()