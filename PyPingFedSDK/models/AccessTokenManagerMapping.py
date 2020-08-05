class AccessTokenManagerMapping():
    """ A mapping in a connection that defines how access tokens are created.

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

    __slots__ = ["accessTokenManagerRef", "attributeContractFulfillment", "attributeSources", "issuanceCriteria"]
    def __init__(self, attributeContractFulfillment, accessTokenManagerRef=None, attributeSources=None, issuanceCriteria=None):
            self.accessTokenManagerRef = accessTokenManagerRef
            self.attributeContractFulfillment = attributeContractFulfillment
            self.attributeSources = attributeSources
            self.issuanceCriteria = issuanceCriteria
    
    def _validate(self):
        return any(x for x in ['attributeContractFulfillment'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AccessTokenManagerMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((accessTokenManagerRef, attributeContractFulfillment, attributeSources, issuanceCriteria))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
