import asyncio

import websockets


async def websocket_client():
    uri = "ws://localhost:5000"  # Change this to your WebSocket server URL

    while True:
        async with websockets.connect(uri) as websocket:
            ask = input()
            await websocket.send(ask)
            print(f"Sent: {ask}")

            response = await websocket.recv()
            print(f"Received: {response}")


if __name__ == "__main__":
    asyncio.run(websocket_client())
