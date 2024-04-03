from src.contexts.channel.channel.domain import Channel, ChannelRepository


class ChannelCreator:

    def __init__(self, repository: ChannelRepository) -> None:
        self._repository = repository

    def run(self, title: str, languages: list[str], picture: str) -> None:
        channel = Channel.create(title, languages, picture)
        self._repository.save(channel)
