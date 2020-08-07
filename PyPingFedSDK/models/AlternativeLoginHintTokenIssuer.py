class AlternativeLoginHintTokenIssuer():
    """JSON Web Key Set Settings.

    Attributes
    ----------
    issuer : string
 The issuer. Issuer is unique.
    jwks : string
 The JWKS.
    jwksURL : string
 The JWKS URL.

    """

<<<<<<< HEAD
    def __init__(self, issuer, jwks=None, jwksURL=None) -> None:
        self.issuer = issuer
        self.jwks = jwks
        self.jwksURL = jwksURL
=======
    def __init__(self, issuer, jwks=None, jwksURL=None):
        self.issuer: str = issuer
        self.jwks: str = jwks
        self.jwksURL: str = jwksURL
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["issuer"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AlternativeLoginHintTokenIssuer):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.issuer, self.jwks, self.jwksURL))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["issuer", "jwks", "jwksURL"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
