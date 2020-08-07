class TokenExchangeProcessorAttributeContract():
    """A set of attributes exposed by an OAuth 2.0 Token Exchange Processor policy.

    Attributes
    ----------
    coreAttributes : array
        A list of read-only attributes (for example, subject) that are automatically populated by PingFederate.    extendedAttributes : array
        A list of additional attributes.
    """

    __slots__ = ["coreAttributes", "extendedAttributes"]

    def __init__(self, coreAttributes=None, extendedAttributes=None):
        self.coreAttributes: list = coreAttributes
        self.extendedAttributes: list = extendedAttributes

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenExchangeProcessorAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.coreAttributes, self.extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__