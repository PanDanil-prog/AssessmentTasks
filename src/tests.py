import httpx
import asyncio
import uvicorn


async def async_send_request(client: httpx.AsyncClient) -> None:
    response = await client.get("http://127.0.0.1:8000/test", timeout=10)
    data = response.json()
    print(f"Response: {data}")


async def test_concurrent_requests() -> None:
    async with httpx.AsyncClient() as client:
        tasks = [async_send_request(client) for _ in range(3)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(test_concurrent_requests())


