class TokenExchangeProcessorMapping():
    """A Token Processor(s) mapping into an OAuth 2.0 Token Exchange Processor policy.

    Attributes
    ----------
    actorTokenProcessor : str
 The Token processor used to process the actor token
    actorTokenType : string
 The Actor token type
    attributeContractFulfillment : str
 A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
 A list of configured data stores to look up attributes from.
    issuanceCriteria : str
 The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    subjectTokenProcessor : str
 The Token processor used to process the subject token
    subjectTokenType : string
 The Subject token type

    """

<<<<<<< HEAD
    def __init__(self, attributeContractFulfillment, subjectTokenType, subjectTokenProcessor, actorTokenProcessor=None, actorTokenType=None, attributeSources=None, issuanceCriteria=None) -> None:
        self.actorTokenProcessor = actorTokenProcessor
        self.actorTokenType = actorTokenType
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.issuanceCriteria = issuanceCriteria
        self.subjectTokenProcessor = subjectTokenProcessor
        self.subjectTokenType = subjectTokenType
=======
    def __init__(self, attributeContractFulfillment, subjectTokenType, subjectTokenProcessor, actorTokenProcessor=None, actorTokenType=None, attributeSources=None, issuanceCriteria=None):
        self.actorTokenProcessor: str = actorTokenProcessor
        self.actorTokenType: str = actorTokenType
        self.attributeContractFulfillment: str = attributeContractFulfillment
        self.attributeSources: list = attributeSources
        self.issuanceCriteria: str = issuanceCriteria
        self.subjectTokenProcessor: str = subjectTokenProcessor
        self.subjectTokenType: str = subjectTokenType
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment", "subjectTokenType", "subjectTokenProcessor"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeProcessorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.actorTokenProcessor, self.actorTokenType, self.attributeContractFulfillment, self.attributeSources, self.issuanceCriteria, self.subjectTokenProcessor, self.subjectTokenType))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["actorTokenProcessor", "actorTokenType", "attributeContractFulfillment", "attributeSources", "issuanceCriteria", "subjectTokenProcessor", "subjectTokenType"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
