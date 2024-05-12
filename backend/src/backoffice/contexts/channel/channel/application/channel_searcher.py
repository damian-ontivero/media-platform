from src.backoffice.contexts.channel.channel.domain import Channel, ChannelRepository


class ChannelSearcher:
    def __init__(self, repository: ChannelRepository) -> None:
        self.repository = repository

    def run(self) -> list[Channel]:
        channels = self.repository.search_all()
        return channels
