# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-08-12 16:29:03
 @Email: zeng.peng@hotmail.com
"""

import asyncio
import websockets
import json

class PlayerDevice:
    def __init__(self):
        self.websocket = None

    async def connect(self):
        self.websocket = await websockets.connect("ws://127.0.0.1:8765")

    async def listen(self):
        while True:
            message = await self.websocket.recv()
            data = json.loads(message)

            if data["type"] == "name":
                player_name = input(data["data"])
                await self.websocket.send(player_name)

            elif data["type"] == "options":
                print("\n新的选择到来:")
                for idx, option in enumerate(data["data"], 1):
                    print(f"{idx}. {option}")

                choice_idx = -1
                while choice_idx < 0 or choice_idx >= len(data["data"]):
                    try:
                        choice_idx = int(input("\n请选择一个选项 (1-4): ")) - 1
                    except ValueError:
                        pass

                chosen_option = data["data"][choice_idx]
                await self.websocket.send(chosen_option)

            elif data["type"] == "story":
                print("\n故事继续:")
                print(data["data"])

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.listen())
