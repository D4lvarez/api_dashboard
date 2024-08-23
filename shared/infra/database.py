from sqlmodel import create_engine, SQLModel

from shared.config import DatabaseConstants
from . import models

engine = create_engine(DatabaseConstants.url, echo=DatabaseConstants.echo)


def create_models():
    SQLModel.metadata.create_all(engine)
