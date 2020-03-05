import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send(message)

# def echo(websocket, path):
#     for message in websocket:
#         print(message)
#         websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 4200)
)
asyncio.get_event_loop().run_forever()
