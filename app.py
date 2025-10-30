from litestar import Litestar, get

@get("/")
async def index() -> str:
    return "Hello, Litestar!"


app = Litestar([index])