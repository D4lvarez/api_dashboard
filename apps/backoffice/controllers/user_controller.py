from fastapi import status
from fastapi.exceptions import HTTPException
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, DataError, DatabaseError, SQLAlchemyError
from sqlmodel import Session

from apps.backoffice.services import UserService
from apps.shared.dto.user_dto import UserCreate, UserRead
from shared.libs import setup_logger

logger = setup_logger(__name__, __name__)


def create_user(session: Session, data: UserCreate) -> UserRead:
    try:
        user = UserService.create_user(session, data)
        return user
    except ValidationError as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error on request body: {str(e)}",
        )
    except IntegrityError as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User already exists: {str(e)}",
        )
    except DataError as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_CONFLICT, detail=f"Invalid data: {str(e)}"
        )
    except DatabaseError as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Service Unavailable",
        )
    except SQLAlchemyError as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error on server. Try again",
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error on server. Try again.",
        )
