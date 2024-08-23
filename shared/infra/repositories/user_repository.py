from sqlmodel import Session

from shared.infra.models import User


def create(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
