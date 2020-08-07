class AuthenticationSelector():
    """An Authentication Selector instance.

    Attributes
    ----------
    attributeContract : str
 The list of attributes that the Authentication Selector provides.
    configuration : str
 Plugin instance configuration.
    id : string
 The ID of the plugin instance. The ID cannot be modified once the instance is created.<br>Note: Ignored when specifying a connection's adapter override.
    name : string
 The plugin instance name. The name cannot be modified once the instance is created.<br>Note: Ignored when specifying a connection's adapter override.
    pluginDescriptorRef : str
 Reference to the plugin descriptor for this instance. The plugin descriptor cannot be modified once the instance is created.<br>Note: Ignored when specifying a connection's adapter override.

    """

<<<<<<< HEAD
    def __init__(self, var_id, name, pluginDescriptorRef, configuration, attributeContract=None) -> None:
        self.attributeContract = attributeContract
        self.configuration = configuration
        self.var_id = var_id
        self.name = name
        self.pluginDescriptorRef = pluginDescriptorRef
=======
    def __init__(self, id, name, pluginDescriptorRef, configuration, attributeContract=None):
        self.attributeContract: str = attributeContract
        self.configuration: str = configuration
        self.id: str = id
        self.name: str = name
        self.pluginDescriptorRef: str = pluginDescriptorRef
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["var_id", "name", "pluginDescriptorRef", "configuration"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationSelector):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeContract, self.configuration, self.var_id, self.name, self.pluginDescriptorRef))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContract", "configuration", "var_id", "name", "pluginDescriptorRef"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
