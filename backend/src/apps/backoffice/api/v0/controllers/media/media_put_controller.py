from fastapi import Response, UploadFile, status
from src.contexts.backoffice.media.application.command import MediaUpdateCommand
from src.contexts.shared.domain.bus.command import CommandBus

from ...schemas import MediaWriteSchema
from ..controller import Controller


class MediaPutController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, id: str, media: MediaWriteSchema, file: UploadFile) -> Response:
        command = MediaUpdateCommand(id, media.title, file.filename, await file.read())
        await self._command_bus.dispatch(command)
        return Response(content=None, status_code=status.HTTP_200_OK, media_type=None)
