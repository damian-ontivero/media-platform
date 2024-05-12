import factory
from src.backoffice.contexts.channel.channel.domain import Channel
from tests.utils.factories.shared.entity_id_factory import EntityIdFactory
from tests.utils.factories.shared.image_factory import ImageFactory


class ChannelFactory(factory.Factory):

    class Meta:
        model = Channel

    id = factory.LazyFunction(EntityIdFactory)
    name = factory.Faker("name")
    image = factory.SubFactory(ImageFactory)
