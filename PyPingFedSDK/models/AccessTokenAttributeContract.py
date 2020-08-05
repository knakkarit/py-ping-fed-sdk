class AccessTokenAttributeContract():
    """ A set of attributes exposed by an Access Token Manager.

    Attributes
    ----------
    coreAttributes : array
        A list of core token attributes that are associated with the access token management plugin type. This field is read-only and is ignored on POST/PUT.
    defaultSubjectAttribute : string
        Default subject attribute to use for audit logging when validating the access token. Blank value means to use USER_KEY attribute value after grant lookup.
    extendedAttributes : array
        A list of additional token attributes that are associated with this access token management plugin instance.
    inherited : boolean
        Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.

    """

    __slots__ = ["coreAttributes", "defaultSubjectAttribute", "extendedAttributes", "inherited"]
    def __init__(self, coreAttributes=None, defaultSubjectAttribute=None, extendedAttributes=None, inherited=None):
            self.coreAttributes = coreAttributes
            self.defaultSubjectAttribute = defaultSubjectAttribute
            self.extendedAttributes = extendedAttributes
            self.inherited = inherited
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AccessTokenAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((coreAttributes, defaultSubjectAttribute, extendedAttributes, inherited))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
