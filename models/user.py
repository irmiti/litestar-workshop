from enum import Enum
from uuid import UUID, uuid4
from msgspec import Struct, field
from litestar.dto.msgspec_dto import MsgspecDTO
from litestar.dto.config import DTOConfig


class UserRole(Enum):
    admin = "admin"
    moderator = "moderator"
    editor = "editor"
    viewer = "viewer"


class User(Struct):
    name: str
    role: UserRole
    id: UUID = field(default_factory=uuid4)


class UserCreateDTO(MsgspecDTO[User]):
    config = DTOConfig(exclude={"id"})

class UserReadDTO(MsgspecDTO[User]): ...