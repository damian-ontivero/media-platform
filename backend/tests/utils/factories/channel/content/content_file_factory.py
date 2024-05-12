import factory
from src.backoffice.contexts.channel.content.domain import ContentFile


class ContentFileFactory(factory.Factory):

    class Meta:
        model = ContentFile

    name = factory.Faker("name")
    path = factory.Faker("file_path")
    media_type = factory.Faker("mime_type")
