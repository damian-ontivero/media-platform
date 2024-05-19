import factory

from src.backoffice.contexts.shared.domain import EntityId


class EntityIdFactory(factory.Factory):

    class Meta:
        model = EntityId

    value = factory.Faker("uuid4")
