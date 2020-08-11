class AuthnSourcePolicyAction():
    """An authentication source selection action.

    Attributes
    ----------
    attributeRules : str
 The authentication policy rules.
    authenticationSource : str
 The associated authentication source.
    context : string
 The result context.
    inputUserIdMapping : str
 The input user id mapping.
    type : str
 The authentication selection type.

    """

    def __init__(self, var_type, authenticationSource, attributeRules=None, context:str=None, inputUserIdMapping=None) -> None:
        self.attributeRules = attributeRules
        self.authenticationSource = authenticationSource
        self.context = context
        self.inputUserIdMapping = inputUserIdMapping
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "authenticationSource"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthnSourcePolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeRules, self.authenticationSource, self.context, self.inputUserIdMapping, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeRules", "authenticationSource", "context", "inputUserIdMapping", "var_type"]}

        return cls(**valid_data)