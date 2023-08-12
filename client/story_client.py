import asyncio
import websockets
import json

async def story_client():
    async with websockets.connect("ws://127.0.0.1:8765") as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            
            if data["type"] == "name":
                response = input(data["data"])
                await websocket.send(response)

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
                await websocket.send(chosen_option)
            
            elif data["type"] == "story":
                print("\n故事继续:")
                print(data["data"])

def run_client():
    asyncio.get_event_loop().run_until_complete(story_client())

if __name__ == "__main__":
    run_client()
