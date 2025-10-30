from uuid import UUID

from litestar import Controller, get, post, delete

from models.user import User, UserCreateDTO, UserReadDTO, UserRole

USERS = [
    User(name="John", role=UserRole.admin),
    User(name="Smith", role=UserRole.viewer),
    User(name="Joe", role=UserRole.editor),
]


class UserController(Controller):
    path = "/users"
    dto = UserCreateDTO
    return_dto = UserReadDTO

    @get()
    async def get_users(self) -> list[User]:
        return USERS

    @post()
    async def create_user(self, data: User) -> User:
        USERS.append(data)
        return data

    @get("/{user_id:uuid}")
    async def get_user_by_id(self, user_id: UUID) -> User:
        return next(filter(lambda u: u.id == user_id, USERS))

    @delete("/{user_id:uuid}")
    async def delete_user_by_id(self, user_id: UUID) -> None:
        user_to_remove = next(filter(lambda u: u.id == user_id, USERS))
        USERS.remove(user_to_remove)
