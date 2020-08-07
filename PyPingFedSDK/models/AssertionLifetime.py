class AssertionLifetime():
    """The timeframe of validity before and after the issuance of the assertion.

    Attributes
    ----------
    minutesAfter : integer
 Assertion validity in minutes after the assertion issuance.
    minutesBefore : integer
 Assertion validity in minutes before the assertion issuance.

    """

<<<<<<< HEAD
    def __init__(self, minutesBefore, minutesAfter) -> None:
        self.minutesAfter = minutesAfter
        self.minutesBefore = minutesBefore
=======
    def __init__(self, minutesBefore, minutesAfter):
        self.minutesAfter: str = minutesAfter
        self.minutesBefore: str = minutesBefore
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["minutesBefore", "minutesAfter"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AssertionLifetime):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.minutesAfter, self.minutesBefore))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["minutesAfter", "minutesBefore"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
