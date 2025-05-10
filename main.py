import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        print("Received pose:", message)
        # TODO: parse and act on pose data here

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("✅ WebSocket server running on ws://0.0.0.0:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())

