import asyncio
import aiohttp
import random
import time

URLS = [
    "https://httpbin.org/get",
    "https://example.com",
    "https://jsonplaceholder.typicode.com/posts",
]

USER_AGENTS = [
    "Mozilla/5.0 Android",
    "Dalvik/2.1.0 (Linux; Android)",
    "Mozilla/5.0 Linux"
]

async def client(client_id: int):
    async with aiohttp.ClientSession() as session:
        while True:
            url = random.choice(URLS)

            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "X-Client-ID": str(client_id)
            }

            try:
                start = time.time()
                async with session.get(url, headers=headers, timeout=10) as resp:
                    await resp.text()
                    latency = round(time.time() - start, 3)

                    print(f"[Client {client_id}] {url} "
                          f"| Status={resp.status} | Latency={latency}s")

            except Exception as e:
                print(f"[Client {client_id}] ERROR: {e}")

            await asyncio.sleep(random.uniform(1, 4))


async def main():
    clients = [client(i) for i in range(5)]  # simulate 5 VM clients
    await asyncio.gather(*clients)


if __name__ == "__main__":
    asyncio.run(main())