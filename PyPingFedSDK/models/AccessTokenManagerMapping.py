class AccessTokenManagerMapping():
    """A mapping in a connection that defines how access tokens are created.

    Attributes
    ----------
    accessTokenManagerRef : str
 The access token manager used in OAuth attribute mapping.
    attributeContractFulfillment : str
 A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
 A list of configured data stores to look up attributes from.
    issuanceCriteria : str
 The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    """

<<<<<<< HEAD
    def __init__(self, attributeContractFulfillment, accessTokenManagerRef=None, attributeSources=None, issuanceCriteria=None) -> None:
        self.accessTokenManagerRef = accessTokenManagerRef
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.issuanceCriteria = issuanceCriteria
=======
    def __init__(self, attributeContractFulfillment, accessTokenManagerRef=None, attributeSources=None, issuanceCriteria=None):
        self.accessTokenManagerRef: str = accessTokenManagerRef
        self.attributeContractFulfillment: str = attributeContractFulfillment
        self.attributeSources: list = attributeSources
        self.issuanceCriteria: str = issuanceCriteria
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AccessTokenManagerMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.accessTokenManagerRef, self.attributeContractFulfillment, self.attributeSources, self.issuanceCriteria))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["accessTokenManagerRef", "attributeContractFulfillment", "attributeSources", "issuanceCriteria"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
