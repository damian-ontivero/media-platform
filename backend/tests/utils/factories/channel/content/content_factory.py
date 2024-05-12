import factory
from src.backoffice.contexts.channel.content.domain import Content
from tests.utils.factories.shared.entity_id_factory import EntityIdFactory

from .content_file_factory import ContentFileFactory
from .content_metadata_factory import ContentMetadataFactory


class ContentFactory(factory.Factory):

    class Meta:
        model = Content

    id = factory.LazyFunction(EntityIdFactory)
    files = factory.List([factory.SubFactory(ContentFileFactory)])
    rating = factory.Faker("pyfloat", min_value=0, max_value=10)
    metadata_ = factory.SubFactory(ContentMetadataFactory)
    channel_id = factory.LazyFunction(EntityIdFactory)
