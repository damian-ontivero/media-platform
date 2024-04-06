import factory
from media_platform.backoffice.contexts.channel.channel.domain import Channel
from media_platform.backoffice.contexts.channel.channel.infrastructure.persistence.postgresql import (
    PostgreSQLChannelRepository,
)
from tests.conftest import SessionLocal
from tests.utils.factories.shared.entity_id_factory import EntityIdFactory
from tests.utils.factories.shared.image_factory import ImageFactory


class ChannelFactory(factory.Factory):

    class Meta:
        model = Channel

    id = factory.LazyFunction(EntityIdFactory)
    name = factory.Faker("name")
    image = factory.SubFactory(ImageFactory)

    @classmethod
    def _create(cls, model_class, *args, **kwargs) -> Channel:
        channel = model_class(*args, **kwargs)
        repository = PostgreSQLChannelRepository(SessionLocal)
        repository.save(channel)
        return channel

    @classmethod
    def _build(cls, model_class, *args, **kwargs) -> Channel:
        channel = model_class(*args, **kwargs)
        return channel
