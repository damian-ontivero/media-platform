from src.contexts.catalog.movies.domain import MovieRepository
from src.contexts.catalog.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.event.event_bus import EventBus
from src.contexts.shared.domain.bus.query import QueryBus

from .update_command import MovieUpdateCommand


class MovieUpdateCommandHandler(CommandHandler):
    def __init__(self, repository: MovieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    def subscribed_to(self) -> Command:
        return MovieUpdateCommand

    async def handle(self, command: MovieUpdateCommand) -> None:
        movie = self._repository.search(command.id)
        if movie is not None:
            media = await self._query_bus.ask(MediaFindByIdQuery(command.media_id))
            movie.update(command.title, media.duration)
            self._repository.save(movie)
            await self._event_bus.publish(movie.pull_domain_events())
