class RolesAndProtocols():
    """ Roles and protocols settings.

    Attributes
    ----------
    enableIdpDiscovery : boolean
        Enable IdP Discovery.
    idpRole : str
        Identity Provider (IdP) settings.
    oauthRole : str
        OAuth role settings.
    spRole : str
        Service Provider (SP) settings.

    """

    __slots__ = ["enableIdpDiscovery", "idpRole", "oauthRole", "spRole"]
    def __init__(self, enableIdpDiscovery=None, idpRole=None, oauthRole=None, spRole=None):
            self.enableIdpDiscovery = enableIdpDiscovery
            self.idpRole = idpRole
            self.oauthRole = oauthRole
            self.spRole = spRole
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, RolesAndProtocols):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((enableIdpDiscovery, idpRole, oauthRole, spRole))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
