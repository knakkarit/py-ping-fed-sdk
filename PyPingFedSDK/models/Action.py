class Action():
    """ A read-only plugin action that either represents a file download or an arbitrary invocation performed by the plugin.

    Attributes
    ----------
    description : string
        The description of this action.
    download : boolean
        Whether this action will trigger a download or invoke an internal action that will return a string result.
    id : string
        The ID of this action.
    invocationRef : str
        Whether this action will trigger a download or invoke an internal action that will return a string result.
    name : string
        The name of this action.

    """

    __slots__ = ["description", "download", "id", "invocationRef", "name"]
    def __init__(self, description=None, download=None, id=None, invocationRef=None, name=None):
            self.description = description
            self.download = download
            self.id = id
            self.invocationRef = invocationRef
            self.name = name
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, Action):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((description, download, id, invocationRef, name))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
