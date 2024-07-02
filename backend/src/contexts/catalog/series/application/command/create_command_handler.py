from src.contexts.catalog.series.domain import Serie, SerieRepository
from src.contexts.catalog.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.event.event_bus import EventBus
from src.contexts.shared.domain.bus.query import QueryBus

from .create_command import SerieCreateCommand


class SerieCreateCommandHandler(CommandHandler):
    def __init__(self, repository: SerieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    def subscribed_to(self) -> Command:
        return SerieCreateCommand

    async def handle(self, command: SerieCreateCommand) -> None:
        serie = Serie.create(command.title, command.seasons)
        self._repository.save(serie)
        await self._event_bus.publish(serie.pull_domain_events())

    async def _ensure_media_is_available(self, command: SerieCreateCommand) -> None:
        for season in command.seasons:
            for episode in season["episodes"]:
                await self._query_bus.ask(MediaFindByIdQuery(episode["media_id"]))
