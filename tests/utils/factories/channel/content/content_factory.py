import factory

from src.contexts.channel.content.domain import Content
from src.contexts.channel.content.infrastructure.persistence.sqlite import (
    SqliteContentRepository,
)
from tests.conftest import SessionLocal
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

    @classmethod
    def _create(cls, model_class, *args, **kwargs) -> Content:
        content = model_class(*args, **kwargs)
        repository = SqliteContentRepository(SessionLocal)
        repository.save(content)
        return content

    @classmethod
    def _build(cls, model_class, *args, **kwargs) -> Content:
        content = model_class(*args, **kwargs)
        return content
