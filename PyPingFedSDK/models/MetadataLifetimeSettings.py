class MetadataLifetimeSettings():
    """Metadata lifetime settings.

    Attributes
    ----------
    cacheDuration : integer
 This field adjusts the validity of your metadata in minutes. The default value is 1440 (1 day).
    reloadDelay : integer
 This field adjusts the frequency of automatic reloading of SAML metadata in minutes. The default value is 1440 (1 day).

    """

    def __init__(self, cacheDuration=None, reloadDelay=None) -> None:
        self.cacheDuration = cacheDuration
        self.reloadDelay = reloadDelay

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, MetadataLifetimeSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.cacheDuration, self.reloadDelay))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["cacheDuration", "reloadDelay"]}

        return cls(**valid_data)