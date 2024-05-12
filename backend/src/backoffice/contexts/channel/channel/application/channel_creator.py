from src.backoffice.contexts.channel.channel.domain import Channel, ChannelRepository


class ChannelCreator:
    def __init__(self, repository: ChannelRepository) -> None:
        self._repository = repository

    def run(self, name: str, image: str) -> None:
        channel = Channel.create(name, image)
        self._repository.save(channel)
