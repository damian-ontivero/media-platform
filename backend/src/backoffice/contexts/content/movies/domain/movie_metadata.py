class MovieMetadata:
    def __init__(self, **kwargs) -> "MovieMetadata":
        if kwargs is None:
            raise ValueError("Metadata is required")
        self._value = kwargs

    @property
    def value(self) -> dict:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MovieMetadata):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._value,))

    def __repr__(self) -> str:
        return "{c}({args})".format(
            c=self.__class__.__name__,
            args=", ".join("{key}={value!r}".format(key=key, value=value) for key, value in self.value.items()),
        )
