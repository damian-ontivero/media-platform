from src.contexts.catalog.media.application.services.media_finder import MediaFinder
from src.contexts.catalog.movies.domain.movie_repository import MovieRepository
from src.contexts.shared.domain.event_bus.event_bus import EventBus


class MovieUpdater:
    def __init__(self, repository: MovieRepository, media_finder: MediaFinder, event_bus: EventBus) -> None:
        self._repository = repository
        self._media_finder = media_finder
        self._event_bus = event_bus

    async def run(self, id: str, title: str, media_id: str) -> None:
        media = await self._media_finder.run(media_id)
        movie = self._repository.search(id)
        movie.update(title, media.duration)
        self._repository.save(movie)
        await self._event_bus.publish(movie.pull_domain_events())
