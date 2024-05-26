class Image:
    """
    Value object that represents an image.
    """

    __slots__ = ("_path",)

    def __new__(cls, path: str) -> "Image":
        if not isinstance(path, str):
            raise TypeError("Image path must be a string")
        if not len(path) > 0:
            raise ValueError("Image path cannot be empty")
        instance = super().__new__(cls)
        instance._path = path
        return instance

    @property
    def path(self) -> str:
        return self._path

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Image):
            return NotImplemented
        return self._path == other._path

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(tuple(sorted(self._path)))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(path={self._path!r})"
