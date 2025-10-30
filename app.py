from litestar import Litestar, get, Request
from litestar.exceptions import ValidationException
from litestar.logging import LoggingConfig
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR

from controllers.param_demo import ParamDemoController
from controllers.user import UserController
from controllers.error_demo import ErrorDemoController
import error_handler


@get("/")
async def index(request: Request) -> str:
    request.logger.info("Nice log message")
    return "Hello, Litestar!"


logging_config = LoggingConfig(
    root={"level": "INFO", "handlers": ["queue_listener"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    log_exceptions="always",
)


app = Litestar(
    route_handlers=[index, ParamDemoController, UserController, ErrorDemoController],
    exception_handlers={
        ValueError: error_handler.value_error_handler,
        ValidationException: error_handler.validation_exception_handler,
        HTTP_500_INTERNAL_SERVER_ERROR: error_handler.internal_server_error_handler,
    },
    logging_config=logging_config,
)