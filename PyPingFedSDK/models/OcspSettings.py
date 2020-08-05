class OcspSettings():
    """ OCSP settings.

    Attributes
    ----------
    actionOnResponderUnavailable : string
        Action on responder unavailable. This value defaults to  "CONTINUE".
    actionOnStatusUnknown : string
        Action on status unknown. This value defaults to  "FAIL".
    actionOnUnsuccessfulResponse : string
        Action on unsuccessful response. This value defaults to  "FAIL".
    currentUpdateGracePeriod : integer
        Current update grace period in minutes. This value defaults to "5".
    nextUpdateGracePeriod : integer
        Next update grace period in minutes. This value defaults to "5".
    requesterAddNonce : boolean
        Do not allow responder to use cached responses. This setting defaults to disabled.
    responderCertReference : str
        Resource link to OCSP responder signature verification certificate. A previously selected certificate will be deselected if this attribute is not defined.
    responderTimeout : integer
        Responder connection timeout in seconds. This value defaults to "5".
    responderUrl : string
        Responder URL address. This field is required if OCSP revocation is enabled.
    responseCachePeriod : integer
        Response cache period in hours. This value defaults to "48".

    """

    __slots__ = ["actionOnResponderUnavailable", "actionOnStatusUnknown", "actionOnUnsuccessfulResponse", "currentUpdateGracePeriod", "nextUpdateGracePeriod", "requesterAddNonce", "responderCertReference", "responderTimeout", "responderUrl", "responseCachePeriod"]
    def __init__(self, responderUrl, actionOnResponderUnavailable=None, actionOnStatusUnknown=None, actionOnUnsuccessfulResponse=None, currentUpdateGracePeriod=None, nextUpdateGracePeriod=None, requesterAddNonce=None, responderCertReference=None, responderTimeout=None, responseCachePeriod=None):
            self.actionOnResponderUnavailable = actionOnResponderUnavailable
            self.actionOnStatusUnknown = actionOnStatusUnknown
            self.actionOnUnsuccessfulResponse = actionOnUnsuccessfulResponse
            self.currentUpdateGracePeriod = currentUpdateGracePeriod
            self.nextUpdateGracePeriod = nextUpdateGracePeriod
            self.requesterAddNonce = requesterAddNonce
            self.responderCertReference = responderCertReference
            self.responderTimeout = responderTimeout
            self.responderUrl = responderUrl
            self.responseCachePeriod = responseCachePeriod
    
    def _validate(self):
        return any(x for x in ['responderUrl'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, OcspSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((actionOnResponderUnavailable, actionOnStatusUnknown, actionOnUnsuccessfulResponse, currentUpdateGracePeriod, nextUpdateGracePeriod, requesterAddNonce, responderCertReference, responderTimeout, responderUrl, responseCachePeriod))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
