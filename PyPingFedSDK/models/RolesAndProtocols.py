class RolesAndProtocols():
    """Roles and protocols settings.

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

<<<<<<< HEAD
    def __init__(self, enableIdpDiscovery=None, idpRole=None, oauthRole=None, spRole=None) -> None:
        self.enableIdpDiscovery = enableIdpDiscovery
        self.idpRole = idpRole
        self.oauthRole = oauthRole
        self.spRole = spRole
=======
    def __init__(self, enableIdpDiscovery=None, idpRole=None, oauthRole=None, spRole=None):
        self.enableIdpDiscovery: bool = enableIdpDiscovery
        self.idpRole: str = idpRole
        self.oauthRole: str = oauthRole
        self.spRole: str = spRole
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, RolesAndProtocols):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.enableIdpDiscovery, self.idpRole, self.oauthRole, self.spRole))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enableIdpDiscovery", "idpRole", "oauthRole", "spRole"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
