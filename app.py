from litestar import Litestar, get
from litestar.exceptions import ValidationException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR

from controllers.param_demo import ParamDemoController
from controllers.user import UserController
from controllers.error_demo import ErrorDemoController
import error_handler


@get("/")
async def index() -> str:
    return "Hello, Litestar!"


app = Litestar(
    route_handlers=[index, ParamDemoController, UserController, ErrorDemoController],
    exception_handlers={
        ValueError: error_handler.value_error_handler,
        ValidationException: error_handler.validation_exception_handler,
        HTTP_500_INTERNAL_SERVER_ERROR: error_handler.internal_server_error_handler,
    }
)