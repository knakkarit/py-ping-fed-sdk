class FieldConfig():
    """A local identity profile field configuration.

    Attributes
    ----------
    fields : array
 The field configuration for the local identity profile.

    """

<<<<<<< HEAD
    def __init__(self, fields=None) -> None:
        self.fields = fields
=======
    def __init__(self, fields=None):
        self.fields: list = fields
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, FieldConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.fields))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["fields"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
