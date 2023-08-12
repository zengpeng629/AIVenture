import asyncio
import websockets
from handle_client import handle_client

def run_server():
    # 输出CLI界面
    print("=============================================")
    print("               文字冒险游戏                  ")
    print("=============================================")
    print("\n游戏背景：\n")
    print("在一个遥远的王国，冒险者们聚集在一起，为了寻找传说中的宝藏...")
    print("\n正在等待玩家加入...\n")
    
    # 启动WebSocket服务器
    start_server = websockets.serve(handle_client, "127.0.0.1", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    run_server()
