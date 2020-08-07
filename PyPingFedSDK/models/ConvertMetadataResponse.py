class ConvertMetadataResponse():
    """A response from converting SAML connection metadata into a JSON connection. It includes the converted connection and the authenticity information of the metadata.

    Attributes
    ----------
    certExpiration : string
 The metadata certificate's expiry date.
    certSerialNumber : string
 The metadata certificate's serial number.
    certSubjectDn : string
 The metadata certificate's subject DN.
    certTrustStatus : str
 The metadata certificate's trust status, i.e. If the partner's certificate can be trusted or not.
    connection : str
 The converted API connection.
    signatureStatus : str
 The metadata's digital signature status.

    """

<<<<<<< HEAD
    def __init__(self, certExpiration=None, certSerialNumber=None, certSubjectDn=None, certTrustStatus=None, connection=None, signatureStatus=None) -> None:
        self.certExpiration = certExpiration
        self.certSerialNumber = certSerialNumber
        self.certSubjectDn = certSubjectDn
        self.certTrustStatus = certTrustStatus
        self.connection = connection
        self.signatureStatus = signatureStatus
=======
    def __init__(self, certExpiration=None, certSerialNumber=None, certSubjectDn=None, certTrustStatus=None, connection=None, signatureStatus=None):
        self.certExpiration: str = certExpiration
        self.certSerialNumber: str = certSerialNumber
        self.certSubjectDn: str = certSubjectDn
        self.certTrustStatus: str = certTrustStatus
        self.connection: str = connection
        self.signatureStatus: str = signatureStatus
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ConvertMetadataResponse):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.certExpiration, self.certSerialNumber, self.certSubjectDn, self.certTrustStatus, self.connection, self.signatureStatus))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["certExpiration", "certSerialNumber", "certSubjectDn", "certTrustStatus", "connection", "signatureStatus"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
