class SpAdapterTargetApplicationInfo():
    """Target Application Information exposed by an SP adapter.

    Attributes
    ----------
    applicationIconUrl : string
        The application icon URL.    applicationName : string
        The application name.    inherited : boolean
        Specifies Whether target application information is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.
    """

    __slots__ = ["applicationIconUrl", "applicationName", "inherited"]

    def __init__(self, applicationIconUrl=None, applicationName=None, inherited=None):
        self.applicationIconUrl: str = applicationIconUrl
        self.applicationName: str = applicationName
        self.inherited: bool = inherited

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SpAdapterTargetApplicationInfo):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.applicationIconUrl, self.applicationName, self.inherited))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["applicationIconUrl", "applicationName", "inherited"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__