from src.backoffice.contexts.channel.channel.domain import Channel, ChannelRepository


class ChannelFinder:
    def __init__(self, repository: ChannelRepository) -> None:
        self.repository = repository

    def run(self, id: str) -> Channel:
        channel = self.repository.search(id)
        if channel is None:
            raise ValueError(f"Channel: {id!r} not found")
        return channel
