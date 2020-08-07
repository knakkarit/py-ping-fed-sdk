class IdpWsTrust():
    """Ws-Trust STS provides validation of incoming tokens which enable SSO access to Web Services. It also allows generation of local tokens for Web Services.

    Attributes
    ----------
    attributeContract : str
 A set of user attributes that the SP receives in the incoming token.
    generateLocalToken : boolean
 Indicates whether a local token needs to be generated. The default value is false.
    tokenGeneratorMappings : array
 A list of token generators to generate local tokens. Required if a local token needs to be generated.

    """

<<<<<<< HEAD
    def __init__(self, attributeContract, generateLocalToken, tokenGeneratorMappings=None) -> None:
        self.attributeContract = attributeContract
        self.generateLocalToken = generateLocalToken
        self.tokenGeneratorMappings = tokenGeneratorMappings
=======
    def __init__(self, attributeContract, generateLocalToken, tokenGeneratorMappings=None):
        self.attributeContract: str = attributeContract
        self.generateLocalToken: bool = generateLocalToken
        self.tokenGeneratorMappings: list = tokenGeneratorMappings
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["attributeContract", "generateLocalToken"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpWsTrust):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeContract, self.generateLocalToken, self.tokenGeneratorMappings))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContract", "generateLocalToken", "tokenGeneratorMappings"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
