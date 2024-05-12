from src.backoffice.contexts.channel.channel.domain import ChannelRepository


class ChannelEliminator:
    def __init__(self, repository: ChannelRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> None:
        channel = self._repository.search(id)
        if channel is None:
            raise Exception(f"Channel: {id!r} not found")
        self._repository.delete(id)
