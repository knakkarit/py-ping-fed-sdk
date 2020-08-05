class AttributeRules():
    """ A collection of attribute rules

    Attributes
    ----------
    fallbackToSuccess : boolean
        When all the rules fail, you may choose to default to the general success action or fail. Default to success.
    items : array
        The actual list of attribute rules.

    """

    __slots__ = ["fallbackToSuccess", "items"]
    def __init__(self, fallbackToSuccess=None, items=None):
            self.fallbackToSuccess = fallbackToSuccess
            self.items = items
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AttributeRules):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((fallbackToSuccess, items))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
