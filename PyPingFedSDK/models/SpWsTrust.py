class SpWsTrust():
    """Ws-Trust STS provides security-token validation and creation to extend SSO access to identity-enabled Web Services

    Attributes
    ----------
    abortIfNotFulfilledFromRequest : boolean
 If the attribute contract cannot be fulfilled using data from the Request, abort the transaction.
    attributeContract : str
 A set of user attributes that the IdP sends in the token.
    defaultTokenType : str
 The default token type when a web service client (WSC) does not specify in the token request which token type the STS should issue. Defaults to SAML 2.0.
    encryptSaml2Assertion : boolean
 When selected, the STS encrypts the SAML 2.0 assertion. Applicable only to SAML 2.0 security token.  This option does not apply to OAuth assertion profiles.
    generateKey : boolean
 When selected, the STS generates a symmetric key to be used in conjunction with the "Holder of Key" (HoK) designation for the assertion's Subject Confirmation Method.  This option does not apply to OAuth assertion profiles.
    messageCustomizations : array
 The message customizations for WS-Trust. Depending on server settings, connection type, and protocol this may or may not be supported.
    minutesAfter : integer
 The amount of time after the SAML token was issued during which it is to be considered valid. The default value is 30.
    minutesBefore : integer
 The amount of time before the SAML token was issued during which it is to be considered valid. The default value is 5.
    oAuthAssertionProfiles : boolean
 When selected, four additional token-type requests become available.
    partnerServiceIds : array
 The partner service identifiers.
    requestContractRef : str
 Request Contract to be used to map attribute values into the security token.
    tokenProcessorMappings : array
 A list of token processors to validate incoming tokens.

    """

<<<<<<< HEAD
    def __init__(self, partnerServiceIds, attributeContract, tokenProcessorMappings, abortIfNotFulfilledFromRequest=None, defaultTokenType=None, encryptSaml2Assertion=None, generateKey=None, messageCustomizations=None, minutesAfter=None, minutesBefore=None, oAuthAssertionProfiles=None, requestContractRef=None) -> None:
        self.abortIfNotFulfilledFromRequest = abortIfNotFulfilledFromRequest
        self.attributeContract = attributeContract
        self.defaultTokenType = defaultTokenType
        self.encryptSaml2Assertion = encryptSaml2Assertion
        self.generateKey = generateKey
        self.messageCustomizations = messageCustomizations
        self.minutesAfter = minutesAfter
        self.minutesBefore = minutesBefore
        self.oAuthAssertionProfiles = oAuthAssertionProfiles
        self.partnerServiceIds = partnerServiceIds
        self.requestContractRef = requestContractRef
        self.tokenProcessorMappings = tokenProcessorMappings
=======
    def __init__(self, partnerServiceIds, attributeContract, tokenProcessorMappings, abortIfNotFulfilledFromRequest=None, defaultTokenType=None, encryptSaml2Assertion=None, generateKey=None, messageCustomizations=None, minutesAfter=None, minutesBefore=None, oAuthAssertionProfiles=None, requestContractRef=None):
        self.abortIfNotFulfilledFromRequest: bool = abortIfNotFulfilledFromRequest
        self.attributeContract: str = attributeContract
        self.defaultTokenType: str = defaultTokenType
        self.encryptSaml2Assertion: bool = encryptSaml2Assertion
        self.generateKey: bool = generateKey
        self.messageCustomizations: list = messageCustomizations
        self.minutesAfter: str = minutesAfter
        self.minutesBefore: str = minutesBefore
        self.oAuthAssertionProfiles: bool = oAuthAssertionProfiles
        self.partnerServiceIds: list = partnerServiceIds
        self.requestContractRef: str = requestContractRef
        self.tokenProcessorMappings: list = tokenProcessorMappings
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["partnerServiceIds", "attributeContract", "tokenProcessorMappings"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpWsTrust):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.abortIfNotFulfilledFromRequest, self.attributeContract, self.defaultTokenType, self.encryptSaml2Assertion, self.generateKey, self.messageCustomizations, self.minutesAfter, self.minutesBefore, self.oAuthAssertionProfiles, self.partnerServiceIds, self.requestContractRef, self.tokenProcessorMappings))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["abortIfNotFulfilledFromRequest", "attributeContract", "defaultTokenType", "encryptSaml2Assertion", "generateKey", "messageCustomizations", "minutesAfter", "minutesBefore", "oAuthAssertionProfiles", "partnerServiceIds", "requestContractRef", "tokenProcessorMappings"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
