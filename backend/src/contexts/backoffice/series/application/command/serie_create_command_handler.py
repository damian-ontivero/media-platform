from src.contexts.backoffice.series.domain import Serie, SerieAlreadyExists, SerieRepository
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.event.event_bus import EventBus
from src.contexts.shared.domain.bus.query import QueryBus
from src.contexts.shared.domain.criteria import Criteria

from .serie_create_command import SerieCreateCommand


class SerieCreateCommandHandler(CommandHandler):
    def __init__(self, repository: SerieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    def subscribed_to(self) -> Command:
        return SerieCreateCommand

    async def handle(self, command: SerieCreateCommand) -> None:
        self._ensure_title_is_available(command)
        self._ensure_media_is_available(command)
        serie = Serie.create(command.title, command.seasons)
        self._repository.save(serie)
        await self._event_bus.publish(serie.pull_domain_events())

    def _ensure_title_is_available(self, command: SerieCreateCommand) -> None:
        criteria = Criteria.from_primitives(
            filter={
                "conjunction": "AND",
                "conditions": [{"field": "title", "operator": "EQUALS", "value": command.title}],
            },
            sort=None,
            page_size=None,
            page_number=None,
        )
        series = self._repository.matching(criteria)
        if series:
            raise SerieAlreadyExists("A serie with the same title already exists")

    async def _ensure_media_is_available(self, command: SerieCreateCommand) -> None:
        for season in command.seasons:
            for episode in season["episodes"]:
                await self._query_bus.ask(MediaFindByIdQuery(episode["media_id"]))
