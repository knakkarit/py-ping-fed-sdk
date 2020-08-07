class ConditionalIssuanceCriteriaEntry():
    """An issuance criterion that checks a source attribute against a particular condition and the expected value. If the condition is true then this issuance criterion passes, otherwise the criterion fails.

    Attributes
    ----------
    attributeName : string
 The name of the attribute to use in this issuance criterion.
    condition : str
 The condition that will be applied to the source attribute's value and the expected value.
    errorResult : string
 The error result to return if this issuance criterion fails. This error result will show up in the PingFederate server logs.
    source : str
 The source of the attribute.
    value : string
 The expected value of this issuance criterion.

    """

<<<<<<< HEAD
    def __init__(self, source, attributeName, condition, value, errorResult=None) -> None:
        self.attributeName = attributeName
        self.condition = condition
        self.errorResult = errorResult
        self.source = source
        self.value = value
=======
    def __init__(self, source, attributeName, condition, value, errorResult=None):
        self.attributeName: str = attributeName
        self.condition: str = condition
        self.errorResult: str = errorResult
        self.source: str = source
        self.value: str = value
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["source", "attributeName", "condition", "value"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ConditionalIssuanceCriteriaEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeName, self.condition, self.errorResult, self.source, self.value))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeName", "condition", "errorResult", "source", "value"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
