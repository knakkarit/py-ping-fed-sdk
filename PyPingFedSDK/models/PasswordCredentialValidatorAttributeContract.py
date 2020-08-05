class PasswordCredentialValidatorAttributeContract():
    """ 

    Attributes
    ----------
    coreAttributes : array
        A list of read-only attributes that are automatically populated by the password credential validator descriptor.
    extendedAttributes : array
        A list of additional attributes that can be returned by the password credential validator. The extended attributes are only used if the adapter supports them.
    inherited : boolean
        Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.

    """

    __slots__ = ["coreAttributes", "extendedAttributes", "inherited"]
    def __init__(self, coreAttributes=None, extendedAttributes=None, inherited=None):
            self.coreAttributes = coreAttributes
            self.extendedAttributes = extendedAttributes
            self.inherited = inherited
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, PasswordCredentialValidatorAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((coreAttributes, extendedAttributes, inherited))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
