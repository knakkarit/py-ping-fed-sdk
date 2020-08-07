class LicenseView():
    """PingFederate License details.

    Attributes
    ----------
    enforcementType : string
        The enforcement type is a 3-bit binary value, expressed as a decimal digit. The bits from left to right are: <br>1: Shutdown on expire <br>2: Notify on expire <br>4: Enforce minor version <br>if all three enforcements are active, the enforcement type will be 7 (1 + 2 + 4); if only the first two are active, you have an enforcement type of 3 (1 + 2).    expirationDate : string
        The expiration date value from the license file (if applicable).    gracePeriod : integer
        Number of days provided as grace period, past the expiration date (if applicable).    id : string
        Unique identifier of a license.    issueDate : string
        The issue date value from the license file.    licenseGroups : array
        License connection groups, if applicable.    maxConnections : integer
        Maximum number of connections that can be created under this license (if applicable).    name : string
        Name of the person the license was issued to.    nodeLimit : integer
        Maximum number of clustered nodes allowed under this license (if applicable).    oauthEnabled : boolean
        Indicates whether OAuth role is enabled for this license.    organization : string
        The organization value from the license file.    product : string
        The Ping Identity product value from the license file.    provisioningEnabled : boolean
        Indicates whether Provisioning role is enabled for this license.    tier : string
        The tier value from the license file. The possible values are FREE, PERPETUAL or SUBSCRIPTION.    version : string
        The Ping Identity product version from the license file.    wsTrustEnabled : boolean
        Indicates whether WS-Trust role is enabled for this license.
    """

    __slots__ = ["enforcementType", "expirationDate", "gracePeriod", "id", "issueDate", "licenseGroups", "maxConnections", "name", "nodeLimit", "oauthEnabled", "organization", "product", "provisioningEnabled", "tier", "version", "wsTrustEnabled"]

    def __init__(self, enforcementType=None, expirationDate=None, gracePeriod=None, id=None, issueDate=None, licenseGroups=None, maxConnections=None, name=None, nodeLimit=None, oauthEnabled=None, organization=None, product=None, provisioningEnabled=None, tier=None, version=None, wsTrustEnabled=None):
        self.enforcementType: str = enforcementType
        self.expirationDate: str = expirationDate
        self.gracePeriod: str = gracePeriod
        self.id: str = id
        self.issueDate: str = issueDate
        self.licenseGroups: list = licenseGroups
        self.maxConnections: str = maxConnections
        self.name: str = name
        self.nodeLimit: str = nodeLimit
        self.oauthEnabled: bool = oauthEnabled
        self.organization: str = organization
        self.product: str = product
        self.provisioningEnabled: bool = provisioningEnabled
        self.tier: str = tier
        self.version: str = version
        self.wsTrustEnabled: bool = wsTrustEnabled

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, LicenseView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.enforcementType, self.expirationDate, self.gracePeriod, self.id, self.issueDate, self.licenseGroups, self.maxConnections, self.name, self.nodeLimit, self.oauthEnabled, self.organization, self.product, self.provisioningEnabled, self.tier, self.version, self.wsTrustEnabled))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enforcementType", "expirationDate", "gracePeriod", "id", "issueDate", "licenseGroups", "maxConnections", "name", "nodeLimit", "oauthEnabled", "organization", "product", "provisioningEnabled", "tier", "version", "wsTrustEnabled"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__