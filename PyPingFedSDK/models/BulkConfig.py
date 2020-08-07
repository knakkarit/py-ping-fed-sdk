class BulkConfig():
    """Model describing a series of configuration operations.

    Attributes
    ----------
    metadata : str
 The metadata detailing how this config was generated.
    operations : array
 A list of configuration operations.

    """

<<<<<<< HEAD
    def __init__(self, metadata, operations) -> None:
        self.metadata = metadata
        self.operations = operations
=======
    def __init__(self, metadata, operations):
        self.metadata: str = metadata
        self.operations: list = operations
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["metadata", "operations"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, BulkConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.metadata, self.operations))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["metadata", "operations"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
