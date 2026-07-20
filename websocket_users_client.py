import asyncio

import websockets

async def client():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        message = "Привет, сервер!"
        await websocket.send(message)
        for _ in range(5):
            message = await websocket.recv()
            print(message)

asyncio.run(client())