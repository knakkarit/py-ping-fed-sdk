class ConnectionMetadataUrl():
    """ Configuration settings to enable automatic reload of partner's metadata.

    Attributes
    ----------
    enableAutoMetadataUpdate : boolean
        Specifies whether the metadata of the connection will be automatically reloaded. The default value is true.
    metadataUrlRef : str
        ID of the saved Metadata URL.

    """

    __slots__ = ["enableAutoMetadataUpdate", "metadataUrlRef"]
    def __init__(self, metadataUrlRef, enableAutoMetadataUpdate=None):
            self.enableAutoMetadataUpdate = enableAutoMetadataUpdate
            self.metadataUrlRef = metadataUrlRef
    
    def _validate(self):
        return any(x for x in ['metadataUrlRef'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConnectionMetadataUrl):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((enableAutoMetadataUpdate, metadataUrlRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
