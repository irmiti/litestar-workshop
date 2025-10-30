from litestar import Controller, get
from litestar.exceptions import HTTPException

class ErrorDemoController(Controller):
    path = "/error-demo"

    @get("/validation-error")
    async def validation_error(self, some_query_param: int) -> int:
        return some_query_param

    @get("/server-error")
    async def server_error(self) -> None:
        raise HTTPException()

    @get("/value-error")
    async def value_error(self) -> None:
        raise ValueError("this is wrong")