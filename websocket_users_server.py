import asyncio
import websockets

from websockets import ServerConnection

DEFAULT_RESPONSE_COUNT = 5

async def websocket_server(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for index in range(1, DEFAULT_RESPONSE_COUNT + 1):
            response = f"{index} Сообщение пользователя: {message}"
            await websocket.send(response)

async def main():
    server = await websockets.serve(websocket_server, "localhost", 8765)
    await server.wait_closed()

asyncio.run(main())

