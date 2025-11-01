from litestar import Litestar, get, Request
from litestar.contrib.opentelemetry import OpenTelemetryConfig, OpenTelemetryPlugin
from litestar.exceptions import ValidationException
from litestar.di import Provide
from litestar.logging import LoggingConfig
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar.types import ASGIApp, Scope, Receive, Send

from controllers.param_demo import ParamDemoController
from controllers.user import UserController
from controllers.error_demo import ErrorDemoController
from controllers.cache_demo import CacheDemoController
import error_handler


@get("/")
async def index(request: Request) -> str:
    request.logger.info("Nice log message")
    return "Hello, Litestar!"


@get("/di-demo", dependencies={"app_config": Provide(lambda: "Another name")})
async def di_demo(app_config: str) -> str:
    return f"I am {app_config}"


def middleware_factory(app: ASGIApp) -> ASGIApp:
    async def my_middleware(scope: Scope, receive: Receive, send: Send) -> None:
        print("Avant")
        await app(scope, receive, send)
        print("Après")

    return my_middleware


logging_config = LoggingConfig(
    root={"level": "INFO", "handlers": ["queue_listener"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    log_exceptions="always",
)


app = Litestar(
    route_handlers=[index, di_demo, ParamDemoController, UserController, ErrorDemoController, CacheDemoController],
    exception_handlers={
        ValueError: error_handler.value_error_handler,
        ValidationException: error_handler.validation_exception_handler,
        HTTP_500_INTERNAL_SERVER_ERROR: error_handler.internal_server_error_handler,
    },
    logging_config=logging_config,
    dependencies={"app_config": Provide(lambda: "Litestar demo app")},
    plugins=[OpenTelemetryPlugin(OpenTelemetryConfig())],
    middleware=[middleware_factory],
)