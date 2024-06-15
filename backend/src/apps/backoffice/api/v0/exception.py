from fastapi import status
from src.contexts.backoffice.media.domain import MediaAlreadyExists, MediaDoesNotExist
from src.contexts.backoffice.movies.domain import MovieAlreadyExists, MovieDoesNotExist
from src.contexts.backoffice.series.domain import SerieAlreadyExists, SerieDoesNotExist

EXCEPTION_TO_HTTP_STATUS_CODE = {
    Exception: status.HTTP_500_INTERNAL_SERVER_ERROR,
    PermissionError: status.HTTP_403_FORBIDDEN,
    MediaDoesNotExist: status.HTTP_404_NOT_FOUND,
    MediaAlreadyExists: status.HTTP_422_UNPROCESSABLE_ENTITY,
    MovieDoesNotExist: status.HTTP_404_NOT_FOUND,
    MovieAlreadyExists: status.HTTP_422_UNPROCESSABLE_ENTITY,
    SerieDoesNotExist: status.HTTP_404_NOT_FOUND,
    SerieAlreadyExists: status.HTTP_422_UNPROCESSABLE_ENTITY,
    ValueError: status.HTTP_400_BAD_REQUEST,
    TypeError: status.HTTP_400_BAD_REQUEST,
}
