class LocalIdentityMappingPolicyAction():
    """A local identity profile selection action.

    Attributes
    ----------
    context : string
 The result context.
    inboundMapping : str
 Inbound mappings into the local identity profile fields.
    localIdentityRef : str
 Reference to the associated local identity profile.
    outboundAttributeMapping : str
 Authentication policy contract mappings associated with this local Identity profile.
    type : str
 The authentication selection type.

    """

<<<<<<< HEAD
    def __init__(self, var_type, localIdentityRef, outboundAttributeMapping, context=None, inboundMapping=None) -> None:
        self.context = context
        self.inboundMapping = inboundMapping
        self.localIdentityRef = localIdentityRef
        self.outboundAttributeMapping = outboundAttributeMapping
        self.var_type = var_type
=======
    def __init__(self, type, localIdentityRef, outboundAttributeMapping, context=None, inboundMapping=None):
        self.context: str = context
        self.inboundMapping: str = inboundMapping
        self.localIdentityRef: str = localIdentityRef
        self.outboundAttributeMapping: str = outboundAttributeMapping
        self.type: str = type
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "localIdentityRef", "outboundAttributeMapping"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, LocalIdentityMappingPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.context, self.inboundMapping, self.localIdentityRef, self.outboundAttributeMapping, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["context", "inboundMapping", "localIdentityRef", "outboundAttributeMapping", "var_type"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
