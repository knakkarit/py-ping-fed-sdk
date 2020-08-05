class CustomAttributeSource():
    """ The configured settings used to look up attributes from a custom data store.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values. This field is only valid for the SP Connection's Browser SSO mappings
    dataStoreRef : str
        Reference to the associated data store.
    description : string
        The description of this attribute source. The description needs to be unique amongst the attribute sources for the mapping.<br>Note: Required for APC-to-SP Adapter Mappings
    filterFields : array
        The list of fields that can be used to filter a request to the custom data store.
    id : string
        The ID that defines this attribute source. Only alphanumeric characters allowed.<br>Note: Required for OpenID Connect policy attribute sources, OAuth IdP adapter mappings, OAuth access token mappings and APC-to-SP Adapter Mappings. IdP Connections will ignore this property since it only allows one attribute source to be defined per mapping. IdP-to-SP Adapter Mappings can contain multiple attribute sources.
    type : str
        The data store type of this attribute source.

    """

    __slots__ = ["attributeContractFulfillment", "dataStoreRef", "description", "filterFields", "id", "type"]
    def __init__(self, type, dataStoreRef, attributeContractFulfillment=None, description=None, filterFields=None, id=None):
            self.attributeContractFulfillment = attributeContractFulfillment
            self.dataStoreRef = dataStoreRef
            self.description = description
            self.filterFields = filterFields
            self.id = id
            self.type = type
    
    def _validate(self):
        return any(x for x in ['type', 'dataStoreRef'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, CustomAttributeSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((attributeContractFulfillment, dataStoreRef, description, filterFields, id, type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
