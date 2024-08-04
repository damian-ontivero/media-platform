import factory

from src.contexts.backoffice.movies.domain.movie import Movie
from tests.contexts.shared.factory.entity_id_factory import EntityIdFactory


class MovieFactory(factory.Factory):
    class Meta:
        model = Movie

    id = factory.SubFactory(EntityIdFactory)
    title = factory.Faker("name")
    media_id = factory.SubFactory(EntityIdFactory)
