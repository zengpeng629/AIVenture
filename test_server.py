# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-08-11 12:33:46
 @Email: zeng.peng@hotmail.com
"""
import asyncio
import websockets
import json

async def test_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = await websocket.recv()
        data = json.loads(message)
        
        assert data["type"] == "options"
        print(f"Received options: {data['data']}")
        
        await websocket.send("选择1")
        
        story_message = await websocket.recv()
        story_data = json.loads(story_message)
        
        assert story_data["type"] == "story"
        print(f"Received story: {story_data['data']}")

def run_test():
    asyncio.get_event_loop().run_until_complete(test_client())

if __name__ == "__main__":
    run_test()
