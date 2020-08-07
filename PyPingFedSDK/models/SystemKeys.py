class SystemKeys():
    """Secrets that are used in cryptographic operations to generate and consume internal tokens

    Attributes
    ----------
    current : str
        The current secret.    pending : str
        The next secret.    previous : str
        Previously used secret.
    """

    __slots__ = ["current", "pending", "previous"]

    def __init__(self, current, pending, previous=None):
        self.current: str = current
        self.pending: str = pending
        self.previous: str = previous

    def _validate(self):
        return any(x for x in ['current', 'pending'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SystemKeys):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.current, self.pending, self.previous))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["current", "pending", "previous"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__