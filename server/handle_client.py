from story_generator import generate_options, generate_story_based_on_choice
import json
connected_clients = set()
client_choices = {}  # 用于存储每个客户端的选择

async def handle_client(websocket, path):
    client_address, client_port = websocket.remote_address
    print(f"\n新客户端连接: IP地址 {client_address}, 端口 {client_port}")
    
    connected_clients.add(websocket)
    try:
        while True:
            options = await generate_options()
            await websocket.send(json.dumps({"type": "options", "data": options}))
            
            choice = await websocket.recv()
            client_choices[websocket] = choice  # 存储客户端的选择

            # 检查是否所有客户端都已选择
            if len(client_choices) == len(connected_clients):
                # 打印所有客户端的选择
                print("\n客户端选择：")
                for ws, ch in client_choices.items():
                    print(f"客户端 {id(ws)}: {ch}")

                # 计算故事续写
                story = await generate_story_based_on_choice(choice)
                for client in connected_clients:
                    await client.send(json.dumps({"type": "story", "data": story}))

                # 清空客户端选择以准备下一轮
                client_choices.clear()
            
    except:
        pass
    finally:
        print(f"\n客户端断开: IP地址 {client_address}, 端口 {client_port}")
        connected_clients.remove(websocket)
        if websocket in client_choices:
            del client_choices[websocket]
