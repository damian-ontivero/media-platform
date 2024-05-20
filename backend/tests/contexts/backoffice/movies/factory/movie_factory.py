import factory
from src.contexts.backoffice.movies.domain import Movie


class MovieFactory:

    class Meta:
        model = Movie

    title = factory.Faker("sentence", nb_words=4)
    links = factory.Faker("url")
