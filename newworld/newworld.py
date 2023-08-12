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

class NewWorld:
    def __init__(self, master):
        self.master = master
        self.connected_players = {}  # 使用字典存储 {websocket: Player对象}

    async def handle_player(self, websocket, path):
        client_address, client_port = websocket.remote_address

        # 提示玩家输入名字
        await websocket.send(json.dumps({"type": "name", "data": "请输入你的名字:"}))
        player_name = await websocket.recv()
        player = Player(player_name, client_address, client_port)
        self.connected_players[websocket] = player

        # 通知所有玩家新玩家的加入
        print(f"{player_name} 加入了游戏！")

        try:
            while True:
                # 为每个玩家生成不同的选择
                options = await self.master.generate_options_for_player(player)
                await websocket.send(json.dumps({"type": "options", "data": options}))

                choice = await websocket.recv()
                player.add_memory(choice)

        except:
            pass
        finally:
            del self.connected_players[websocket]

    def run(self):
        # 输出CLI界面
        print("=============================================")
        print("              一个新世界即将开启                ")
        print("=============================================")
        print("\n游戏背景：\n")
        print("在一个遥远的王国，冒险者们聚集在一起，为了寻找传说中的宝藏...")
        print("\n正在等待玩家加入...\n")

        start_server = websockets.serve(self.handle_player, "127.0.0.1", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()