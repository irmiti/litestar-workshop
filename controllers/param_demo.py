from datetime import date
from typing import Annotated, Any
from litestar import Controller, get
from litestar.params import Parameter
from litestar.exceptions import PermissionDeniedException


VALID_TOKEN = "super-secret-secret"
VALID_COOKIE_VALUE = "cookie-secret"
USER_DB = {1: { "id": 1, "name": "John Doe" }}

class ParamDemoController(Controller):
    path = "/param-demo"

    @get(path="/path-date/{your_date:str}")
    async def path_date(self, your_date: date) -> int:
        return (date.today() - your_date).days

    @get(path="/path-int/{version:int}")
    async def path_int(
            self,
            version: Annotated[
                int,
                Parameter(
                    ge=3,
                    le=13,
                    description="Validation & documentation for path params",
                )
            ]
    ) -> int:
        return version

    @get(path="/query-str")
    async def query_str(self, name: str) -> str:
        return f"Hi there, {name}"

    @get("/query-coercion")
    async def query_coercion(self, number: int, floating_number: float, strings: list[str]) -> dict[str, Any]:
        return {
            "int": number,
            "float": floating_number,
            "list": strings,
        }

    @get(path="/header-cookies/{user_id:int}/")
    async def get_user(
            self,
            user_id: int,
            token: Annotated[str, Parameter(header="X-API-KEY")],
            # cookie: Annotated[str, Parameter(cookie="my-cookie-param")],  Does not work in Swagger UI
    ) -> dict[str, str]:
        if token != VALID_TOKEN:
            raise PermissionDeniedException
        return USER_DB[user_id]
