import asyncio
import psutil
import json
from datetime import datetime
import socket

queue = asyncio.Queue()

async def collect_system_info():
        system_info = {
            "machine_ip": socket.gethostbyname(socket.gethostname()),
            "cpu": {
                "usage_percent": psutil.cpu_percent(interval=1),
                "cores_logical": psutil.cpu_count(logical=True),
                "cores_physical": psutil.cpu_count(logical=False),
                "freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            },
            "memory": psutil.virtual_memory()._asdict(),
            "swap": psutil.swap_memory()._asdict(),
            "disk": {disk.device: psutil.disk_usage(disk.mountpoint)._asdict() for disk in psutil.disk_partitions()},
            "network": psutil.net_io_counters()._asdict(),
            "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat()  
        }
        message_with_timestamp = {
            "timestamp": datetime.now().isoformat(),
            "data": system_info
        }
        message = json.dumps(message_with_timestamp)
        await queue.put(message)
        await asyncio.sleep(5)

async def send_system_info():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    while True:
        message = await queue.get()
        writer.write(message.encode())
        await writer.drain()

    writer.close()
    await writer.wait_closed()

async def main():
    await asyncio.gather(collect_system_info(), send_system_info())

if __name__ == "__main__":
    asyncio.run(main())
