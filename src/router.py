import asyncio
from time import monotonic
from fastapi import APIRouter

from utils import work

from models import TestResponse

router = APIRouter(tags=['Tests'])

async_lock = asyncio.Lock()


@router.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()
    async with async_lock:
        await work()
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)
