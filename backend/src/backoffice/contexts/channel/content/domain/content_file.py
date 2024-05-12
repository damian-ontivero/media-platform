class ContentFile:

    __slots__ = ("_name", "_path", "_media_type")

    def __new__(cls, name: str, path: str, media_type: str) -> "ContentFile":
        if name is None:
            raise ValueError("File name is required")
        if not isinstance(name, str):
            raise ValueError("File name must be a string")
        if len(name) == 0:
            raise ValueError("File name must not be empty")
        if path is None:
            raise ValueError("File path is required")
        if not isinstance(path, str):
            raise ValueError("File path must be a string")
        if len(path) == 0:
            raise ValueError("File path must not be empty")
        if media_type is None:
            raise ValueError("File type is required")
        if not isinstance(media_type, str):
            raise ValueError("File type must be a string")
        if len(media_type) == 0:
            raise ValueError("File type must not be empty")
        instance = super().__new__(cls)
        instance._name = name
        instance._path = path
        instance._media_type = media_type
        return instance

    @property
    def name(self) -> str:
        return self._name

    @property
    def path(self) -> str:
        return self._path

    @property
    def media_type(self) -> str:
        return self._media_type

    @property
    def __dict__(self) -> dict:
        return {"name": self._name, "path": self._path, "media_type": self._media_type}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ContentFile):
            return NotImplemented
        return self._name == other._name and self._path == other._path and self._media_type == other._media_type

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._name, self._path, self._media_type))

    def __repr__(self) -> str:
        return ("{c}(name={name!r}, path={path!r}, media_type={media_type!r})").format(
            c=self.__class__.__name__, name=self._name, path=self._path, media_type=self._media_type
        )
