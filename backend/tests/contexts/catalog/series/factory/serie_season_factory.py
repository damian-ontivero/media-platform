import factory
from src.contexts.catalog.series.domain import SerieSeason
from tests.contexts.shared.factory.entity_id_factory import EntityIdFactory

from .serie_episode_factory import SerieEpisodeFactory


class SerieSeasonFactory(factory.Factory):

    class Meta:
        model = SerieSeason

    id = factory.SubFactory(EntityIdFactory)
    number = factory.Faker("random_int")
    episodes = factory.List([factory.SubFactory(SerieEpisodeFactory) for _ in range(3)])
