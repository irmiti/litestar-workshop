from litestar import Request, Response, MediaType
from litestar.exceptions import ValidationException


def validation_exception_handler(request: Request, exc: ValidationException) -> Response:
    return Response(media_type=MediaType.TEXT,
                    content=f"validation error: {exc.detail}",
                    status_code=400,
    )

def internal_server_error_handler(request: Request, exc: Exception) -> Response:
    return Response(media_type=MediaType.TEXT,
                    content=f"server error: {exc}",
                    status_code=500,
    )


def value_error_handler(request: Request, exc: ValueError) -> Response:
    return Response(media_type=MediaType.TEXT,
                    content=f"value error: {exc}",
                    status_code=400,
    )