from sqlmodel import Session

from apps.shared.dto.user_dto import UserCreate, UserRead
from shared.infra.models import User
from shared.infra.repositories import UserRepository


def create_user(session: Session, data: UserCreate) -> UserRead:
    user = User.model_validate(data)
    db_user = UserRepository.create(session, user)
    return UserRead(**db_user.model_dump())
