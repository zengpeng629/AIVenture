import asyncio
import websockets
from handle_client import handle_client

def run_server():
    start_server = websockets.serve(handle_client, "127.0.0.1", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    run_server()
