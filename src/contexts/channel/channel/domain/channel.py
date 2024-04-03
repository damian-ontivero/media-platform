from src.contexts.shared.domain import AggregateRoot, EntityId, Image


class Channel(AggregateRoot):

    def __init__(
        self, id: EntityId, title: str, languages: list[str], picture: Image
    ) -> None:
        self._id = id
        self._title = title
        self._languages = languages
        self._picture = picture

    @property
    def id(self) -> EntityId:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def languages(self) -> list[str]:
        return self._languages

    @property
    def picture(self) -> Image:
        return self._picture

    @classmethod
    def create(
        cls, title: str, languages: list[str], picture: dict
    ) -> "Channel":
        return cls(
            EntityId.generate(),
            title,
            languages,
            Image(picture["path"]) if picture else None,
        )

    @classmethod
    def from_primitives(
        cls, id: str, title: str, languages: list[str], picture: dict
    ) -> "Channel":
        return cls(
            EntityId(id),
            title,
            languages,
            Image(picture["path"]) if picture else None,
        )

    def update(self, title: str, languages: list[str], picture: dict) -> None:
        if not title == self._title:
            self._title = title
        if not languages == self._languages:
            self._languages = languages
        if not picture == self._picture:
            self._picture = Image(picture["path"]) if picture else None

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "title": self._title,
            "languages": self._languages,
            "picture": self._picture.__dict__ if self._picture else None,
        }

    def __repr__(self) -> str:
        return (
            "{c}(id={id!r}, title={title!r}, "
            "languages={languages!r}, picture={picture!r})"
        ).format(
            c=self.__class__.__name__,
            id=self._id,
            title=self._title,
            languages=self._languages,
            picture=self._picture,
        )
