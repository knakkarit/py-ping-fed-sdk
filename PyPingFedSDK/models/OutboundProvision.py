class OutboundProvision():
    """Outbound Provisioning allows an IdP to create and maintain user accounts at standards-based partner sites using SCIM as well as select-proprietary provisioning partner sites that are protocol-enabled.

    Attributes
    ----------
    channels : array
        Includes settings of a source data store, managing provisioning threads and mapping of attributes.    customSchema : str
        Custom SCIM attribute configuration.    targetSettings : array
        Configuration fields that includes credentials to target SaaS application.    type : string
        The SaaS plugin type.
    """

    __slots__ = ["channels", "customSchema", "targetSettings", "type"]

    def __init__(self, type, targetSettings, channels, customSchema=None):
        self.channels: list = channels
        self.customSchema: str = customSchema
        self.targetSettings: list = targetSettings
        self.type: str = type

    def _validate(self):
        return any(x for x in ['type', 'targetSettings', 'channels'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, OutboundProvision):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.channels, self.customSchema, self.targetSettings, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["channels", "customSchema", "targetSettings", "type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__