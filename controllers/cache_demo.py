from litestar.types import HTTPScope
from litestar import Controller, Request, get
from asyncio import sleep

def key_builder(request: Request) -> str:
    return request.url.path + request.headers.get("my-header", "")



class CacheDemoController(Controller):
    path = "/cache-demo"

    @get("/yes", cache=15, cache_key_builder=key_builder)
    async def cached_during_15s_handler(self) -> str:
        await sleep(2)
        return "cached"

    @get("/no")
    async def not_cached_handler(self) -> str:
        await sleep(2)
        return "not cached"