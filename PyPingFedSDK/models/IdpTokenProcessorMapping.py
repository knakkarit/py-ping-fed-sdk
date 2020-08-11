class IdpTokenProcessorMapping():
    """The IdP Token Processor Mapping.

    Attributes
    ----------
    attributeContractFulfillment : str
 A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
 A list of configured data stores to look up attributes from.
    idpTokenProcessorRef : str
 Reference to the associated token processor.
    issuanceCriteria : str
 The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    restrictedVirtualEntityIds : array
 The list of virtual server IDs that this mapping is restricted to.

    """

    def __init__(self, idpTokenProcessorRef, attributeContractFulfillment, attributeSources:list=None, issuanceCriteria=None, restrictedVirtualEntityIds:list=None) -> None:
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.idpTokenProcessorRef = idpTokenProcessorRef
        self.issuanceCriteria = issuanceCriteria
        self.restrictedVirtualEntityIds = restrictedVirtualEntityIds

    def _validate(self) -> bool:
        return any(x for x in ["idpTokenProcessorRef", "attributeContractFulfillment"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpTokenProcessorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeContractFulfillment, self.attributeSources, self.idpTokenProcessorRef, self.issuanceCriteria, self.restrictedVirtualEntityIds))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "idpTokenProcessorRef", "issuanceCriteria", "restrictedVirtualEntityIds"]}

        return cls(**valid_data)