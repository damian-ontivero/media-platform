from src.contexts.channel.channel.domain import ChannelRepository


class ChannelUpdater:

    def __init__(self, repository: ChannelRepository) -> None:
        self._repository = repository

    def run(
        self, id: str, title: str, languages: list[str], picture: str
    ) -> None:
        channel = self._repository.search(id)
        if channel is None:
            raise Exception(f"Channel: {id!r} not found")
        channel.update(title, languages, picture)
        self._repository.save(channel)
