from src.contexts.shared.domain import AggregateRoot, EntityId

from .content_file import ContentFile
from .content_metadata import ContentMetadata


class Content(AggregateRoot):

    def __init__(
        self,
        id: EntityId,
        files: list[ContentFile],
        rating: float,
        metadata_: ContentMetadata,
        channel_id: EntityId,
    ) -> None:
        self._id = id
        self._files = files
        self._rating = rating
        self._metadata_ = metadata_
        self._channel_id = channel_id

    @property
    def id(self) -> EntityId:
        return self._id

    @property
    def files(self) -> list[ContentFile]:
        return self._files

    @property
    def rating(self) -> float:
        return self._rating

    @property
    def metadata_(self) -> ContentMetadata:
        return self._metadata_

    @property
    def channel_id(self) -> EntityId:
        return self._channel_id

    @classmethod
    def create(
        cls,
        files: list[dict],
        rating: float,
        metadata_: dict,
        channel_id: str,
    ) -> "Content":
        return cls(
            EntityId.generate(),
            [ContentFile(**file) for file in files],
            rating,
            ContentMetadata(**metadata_),
            EntityId(channel_id),
        )

    @classmethod
    def from_primitives(
        cls,
        id: str,
        files: list[dict],
        rating: float,
        metadata_: dict,
        channel_id: str,
    ) -> "Content":
        return cls(
            EntityId(id),
            [ContentFile(**file) for file in files],
            rating,
            ContentMetadata(**metadata_),
            EntityId(channel_id),
        )

    def update(
        self,
        files: list[dict],
        rating: float,
        metadata_: dict,
        channel_id: str,
    ) -> None:
        if not files == [file.__dict__ for file in self._files]:
            self._files = [ContentFile(**file) for file in files]
        if not rating == self._rating:
            self._rating = rating
        if not metadata_ == self._metadata_.value:
            self._metadata_ = ContentMetadata(**metadata_)
        if not channel_id == self._channel_id:
            self._channel_id = EntityId(channel_id)

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "files": [file.__dict__ for file in self._files],
            "rating": self._rating,
            "metadata_": self._metadata_.value,
            "channel_id": self._channel_id.value,
        }

    def __repr__(self) -> str:
        return (
            "{c}(id={id!r}, files={files!r}, rating={rating!r}, "
            "metadata_={metadata_!r} channel_id={channel_id!r})"
        ).format(
            c=self.__class__.__name__,
            id=self._id,
            files=self._files,
            rating=self._rating,
            metadata_=self._metadata_,
            channel_id=self._channel_id,
        )
