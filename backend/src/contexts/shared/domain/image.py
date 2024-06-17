class Image:
    """
    Value object that represents an image.
    """

    __slots__ = ("_value",)

    def __new__(cls, value: str) -> "Image":
        if not isinstance(value, str):
            raise TypeError("Image must be a string")
        if not len(value) > 0:
            raise ValueError("Image cannot be empty")
        instance = super().__new__(cls)
        instance._value = value
        return instance

    @property
    def value(self) -> str:
        return self._value

    @classmethod
    def from_path(cls, path: str) -> "Image":
        return cls(path)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Image):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(tuple(sorted(self._value)))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={self._value!r})"
