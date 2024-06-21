from src.contexts.backoffice.series.domain import SerieAlreadyExists, SerieDoesNotExist, SerieRepository
from src.contexts.backoffice.shared.media.application.query import MediaFindByIdQuery
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.bus.query import QueryBus
from src.contexts.shared.domain.criteria import Criteria

from .update_command import SerieUpdateCommand


class SerieUpdateCommandHandler(CommandHandler):
    def __init__(self, repository: SerieRepository, query_bus: QueryBus) -> None:
        self._repository = repository
        self._query_bus = query_bus

    def subscribed_to(self) -> Command:
        return SerieUpdateCommand

    def handle(self, command: SerieUpdateCommand) -> None:
        self._ensure_title_is_available(command)
        self._ensure_media_is_available(command)
        serie = self._repository.search(command.id)
        if serie is None:
            raise SerieDoesNotExist(f"Serie with id {command.id!r} does not exist")
        serie.update(command.title, command.seasons)
        self._repository.save(serie)

    def _ensure_title_is_available(self, command: SerieUpdateCommand) -> None:
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

    def _ensure_media_is_available(self, command: SerieUpdateCommand) -> None:
        for season in command.seasons:
            for episode in season.episodes:
                self._query_bus.ask(MediaFindByIdQuery(episode.media_id))
