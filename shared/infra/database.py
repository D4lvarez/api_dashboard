from sqlmodel import create_engine, SQLModel, Session

from shared.config import DatabaseConstants

engine = create_engine(DatabaseConstants.url, echo=DatabaseConstants.echo)


def create_models():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
