import asyncio
import json

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connected to {addr}")
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            message = data.decode()
            try:
                message_json = json.loads(message)
                timestamp = message_json.get("timestamp")
                system_data = message_json.get("data")
                print(f"Received at {timestamp}:")
                print(json.dumps(system_data, indent=4))
            except json.JSONDecodeError:
                print("Failed to decode message as JSON")
    except (ConnectionResetError, OSError) as e:
        print(f"Connection error: {e}")
    finally:
        print(f"Connection closed from {addr}")
        writer.close()
        await writer.wait_closed()

async def run_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    async with server:
        print("Server is running and waiting for connections...")
        try:
            await server.serve_forever()
        except Exception as e:
            print(f"Server error: {e}")

if __name__ == "__main__":
    while True:
        try:
            asyncio.run(run_server())
        except Exception as e:
            print(f"Restarting server due to error: {e}")
