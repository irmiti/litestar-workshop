from litestar import Litestar, get
from controllers.param_demo import ParamDemoController
from controllers.user import UserController


@get("/")
async def index() -> str:
    return "Hello, Litestar!"


app = Litestar([index, ParamDemoController, UserController])