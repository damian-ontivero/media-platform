import factory

from src.contexts.backoffice.series.domain import Serie
from tests.contexts.shared.factory.entity_id_factory import EntityIdFactory

from .serie_season_factory import SerieSeasonFactory


class SerieFactory(factory.Factory):

    class Meta:
        model = Serie

    id = factory.SubFactory(EntityIdFactory)
    title = factory.Faker("name")
    seasons = factory.List([factory.SubFactory(SerieSeasonFactory) for _ in range(3)])
