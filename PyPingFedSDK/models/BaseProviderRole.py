class BaseProviderRole():
    """ Base Provider Role.

    Attributes
    ----------
    enable : boolean
        
    enableSaml10 : boolean
        Enable SAML 1.0.
    enableSaml11 : boolean
        Enable SAML 1.1.
    enableWsFed : boolean
        Enable WS Federation.
    enableWsTrust : boolean
        Enable WS Trust.

    """

    __slots__ = ["enable", "enableSaml10", "enableSaml11", "enableWsFed", "enableWsTrust"]
    def __init__(self, enable=None, enableSaml10=None, enableSaml11=None, enableWsFed=None, enableWsTrust=None):
            self.enable = enable
            self.enableSaml10 = enableSaml10
            self.enableSaml11 = enableSaml11
            self.enableWsFed = enableWsFed
            self.enableWsTrust = enableWsTrust
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, BaseProviderRole):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((enable, enableSaml10, enableSaml11, enableWsFed, enableWsTrust))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
