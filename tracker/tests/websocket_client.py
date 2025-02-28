import asyncio

import websockets


async def websocket_client():
    uri = "ws://localhost:5000"  # Change this to your WebSocket server URL

    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, Server!")
        print("Sent: Hello, Server!")

        response = await websocket.recv()
        print(f"Received: {response}")


if __name__ == "__main__":
    asyncio.run(websocket_client())
