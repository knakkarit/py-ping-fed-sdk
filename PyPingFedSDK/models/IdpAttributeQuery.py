class IdpAttributeQuery():
    """The attribute query profile supports local applications in requesting user attributes from an attribute authority.

    Attributes
    ----------
    nameMappings : array
 The attribute name mappings between the SP and the IdP.
    policy : str
 The attribute query profile's security policy.
    url : string
 The URL at your IdP partner's site where attribute queries are to be sent.

    """

<<<<<<< HEAD
    def __init__(self, url, nameMappings=None, policy=None) -> None:
        self.nameMappings = nameMappings
        self.policy = policy
        self.url = url
=======
    def __init__(self, url, nameMappings=None, policy=None):
        self.nameMappings: list = nameMappings
        self.policy: str = policy
        self.url: str = url
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["url"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpAttributeQuery):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.nameMappings, self.policy, self.url))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["nameMappings", "policy", "url"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
