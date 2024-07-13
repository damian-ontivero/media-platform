from fastapi import Response, UploadFile, status
from src.apps.backoffice.api.v0.schemas import MediaWriteSchema
from src.apps.shared.api.v0.controller import Controller
from src.contexts.backoffice.media.application.commands import MediaCreateCommand
from src.contexts.shared.domain.bus.command import CommandBus


class MediaPostController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, media: MediaWriteSchema, file: UploadFile) -> Response:
        command = MediaCreateCommand(media.title, file.filename, await file.read())
        await self._command_bus.dispatch(command)
        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type=None)
