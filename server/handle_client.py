from story_generator import generate_options, generate_story_based_on_choice
import json
from actor import Actor

connected_clients = set()
client_choices = {}  # 用于存储每个客户端的选择
actors = {}

async def handle_client(websocket, path):
    client_address, client_port = websocket.remote_address
    print(f"\n有新玩家的加入！连接: IP地址 {client_address}, 端口 {client_port}")
    
    # 提示玩家输入名字
    await websocket.send(json.dumps({"type": "name", "data": "请输入你的名字:"}))
    name = await websocket.recv()
    
    # 创建一个新的 Actor 实例
    player = Actor(name, client_address, client_port)
    actors[websocket] = player  # 将 Actor 实例存储在全局字典中

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
                print("\n所有玩家已经选择完毕：")
                for ws, ch in client_choices.items():
                    print(f"{actors[ws].name}选择了: {ch}")

                # 计算故事续写
                story = await generate_story_based_on_choice(choice)
                for client in connected_clients:
                    await client.send(json.dumps({"type": "story", "data": story}))

                # 清空客户端选择以准备下一轮
                client_choices.clear()
            
    except:
        pass
    finally:
        print(f"\n有玩家离开了游戏: IP地址 {client_address}, 端口 {client_port}")
        connected_clients.remove(websocket)
        if websocket in client_choices:
            del client_choices[websocket]
