from fastapi import Request, Response, status

from .controller import Controller


class HealthCheckController(Controller):

    def run(self, request: Request | None) -> Response:
        return Response(
            content="The Media Platform API is running.",
            status_code=status.HTTP_200_OK,
            media_type="text/plain",
        )
