import factory
from src.backoffice.contexts.shared.domain import Image


class ImageFactory(factory.Factory):

    class Meta:
        model = Image

    path = factory.Faker("file_path", extension="jpg")
