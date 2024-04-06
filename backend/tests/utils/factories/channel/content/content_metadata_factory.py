import factory
from media_platform.backoffice.contexts.channel.content.domain import (
    ContentMetadata,
)


class ContentMetadataFactory(factory.Factory):

    class Meta:
        model = ContentMetadata

    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("sentence", nb_words=10)
    author = factory.Faker("name")
