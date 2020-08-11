class LocalIdentityProfile():
    """A local identity profile.

    Attributes
    ----------
    apcId : str
 The reference to the authentication profile contract to use for this local identity profile.
    authSourceUpdatePolicy : str
 The attribute update policy for authentication sources.
    authSources : array
 The local identity authentication sources. Sources are unique.
    dataStoreConfig : str
 The local identity profile data store configuration.
    emailVerificationConfig : str
 The local identity email verification configuration.
    fieldConfig : str
 The local identity profile field configuration.
    id : string
 The persistent, unique ID for the local identity profile. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    name : string
 The local identity profile name. Name is unique.
    profileConfig : str
 The local identity profile management configuration.
    profileEnabled : boolean
 Whether the profile configuration is enabled or not.
    registrationConfig : str
 The local identity profile registration configuration.
    registrationEnabled : boolean
 Whether the registration configuration is enabled or not.

    """

    def __init__(self, name:str, apcId, authSourceUpdatePolicy=None, authSources:list=None, dataStoreConfig=None, emailVerificationConfig=None, fieldConfig=None, var_id:str=None, profileConfig=None, profileEnabled:bool=None, registrationConfig=None, registrationEnabled:bool=None) -> None:
        self.apcId = apcId
        self.authSourceUpdatePolicy = authSourceUpdatePolicy
        self.authSources = authSources
        self.dataStoreConfig = dataStoreConfig
        self.emailVerificationConfig = emailVerificationConfig
        self.fieldConfig = fieldConfig
        self.var_id = var_id
        self.name = name
        self.profileConfig = profileConfig
        self.profileEnabled = profileEnabled
        self.registrationConfig = registrationConfig
        self.registrationEnabled = registrationEnabled

    def _validate(self) -> bool:
        return any(x for x in ["name", "apcId"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, LocalIdentityProfile):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.apcId, self.authSourceUpdatePolicy, self.authSources, self.dataStoreConfig, self.emailVerificationConfig, self.fieldConfig, self.var_id, self.name, self.profileConfig, self.profileEnabled, self.registrationConfig, self.registrationEnabled))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["apcId", "authSourceUpdatePolicy", "authSources", "dataStoreConfig", "emailVerificationConfig", "fieldConfig", "var_id", "name", "profileConfig", "profileEnabled", "registrationConfig", "registrationEnabled"]}

        return cls(**valid_data)