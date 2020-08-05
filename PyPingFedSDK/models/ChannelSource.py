class ChannelSource():
    """ The source data source and LDAP settings.

    Attributes
    ----------
    accountManagementSettings : str
        Account management settings that includes the status and algorithms.
    baseDn : string
        The base DN where the user records are located.
    changeDetectionSettings : str
        Settings to detect a during provisioning.
    dataSource : str
        Reference to an LDAP datastore.
    groupMembershipDetection : str
        Settings to detect group memberships.
    groupSourceLocation : str
        The group provisioning source location settings.
    guidAttributeName : string
        the GUID attribute name.
    guidBinary : boolean
        Indicates whether the GUID is stored in binary format.
    userSourceLocation : str
        The user provisioning source location settings.

    """

    __slots__ = ["accountManagementSettings", "baseDn", "changeDetectionSettings", "dataSource", "groupMembershipDetection", "groupSourceLocation", "guidAttributeName", "guidBinary", "userSourceLocation"]
    def __init__(self, dataSource, guidAttributeName, guidBinary, changeDetectionSettings, groupMembershipDetection, accountManagementSettings, baseDn, userSourceLocation, groupSourceLocation=None):
            self.accountManagementSettings = accountManagementSettings
            self.baseDn = baseDn
            self.changeDetectionSettings = changeDetectionSettings
            self.dataSource = dataSource
            self.groupMembershipDetection = groupMembershipDetection
            self.groupSourceLocation = groupSourceLocation
            self.guidAttributeName = guidAttributeName
            self.guidBinary = guidBinary
            self.userSourceLocation = userSourceLocation
    
    def _validate(self):
        return any(x for x in ['dataSource', 'guidAttributeName', 'guidBinary', 'changeDetectionSettings', 'groupMembershipDetection', 'accountManagementSettings', 'baseDn', 'userSourceLocation'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ChannelSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((accountManagementSettings, baseDn, changeDetectionSettings, dataSource, groupMembershipDetection, groupSourceLocation, guidAttributeName, guidBinary, userSourceLocation))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
