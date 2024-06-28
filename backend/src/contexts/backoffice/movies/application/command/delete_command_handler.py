from src.contexts.backoffice.movies.domain import MovieDeleted, MovieDoesNotExist, MovieRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.event.event_bus import EventBus

from .delete_command import MovieDeleteCommand


class MovieDeleteCommandHandler(CommandHandler):
    def __init__(self, repository: MovieRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    def subscribed_to(self) -> Command:
        return MovieDeleteCommand

    def handle(self, command: MovieDeleteCommand) -> None:
        movie = self._repository.search(command.id)
        if movie is None:
            raise MovieDoesNotExist(f"Movie with id {command.id!r} does not exist")
        self._repository.delete(command.id)
        self._event_bus.publish([MovieDeleted.create({"id": command.id})])
