from fastapi import status
from src.contexts.shared.domain.exception import EntityAlreadyExists, EntityNotFound

EXCEPTION_TO_HTTP_STATUS_CODE = {
    Exception: status.HTTP_500_INTERNAL_SERVER_ERROR,
    PermissionError: status.HTTP_403_FORBIDDEN,
    EntityNotFound: status.HTTP_404_NOT_FOUND,
    EntityAlreadyExists: status.HTTP_422_UNPROCESSABLE_ENTITY,
    ValueError: status.HTTP_400_BAD_REQUEST,
    TypeError: status.HTTP_400_BAD_REQUEST,
}
