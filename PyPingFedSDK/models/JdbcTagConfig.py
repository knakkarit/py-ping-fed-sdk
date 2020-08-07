class JdbcTagConfig():
    """A JDBC data store's connection URLs and tags configuration. This is required if no default JDBC database location is specified.

    Attributes
    ----------
    connectionUrl : string
        The location of the JDBC database.    defaultSource : boolean
        Whether this is the default connection. Defaults to false if not specified.    tags : string
        Tags associated with this data source.
    """

    __slots__ = ["connectionUrl", "defaultSource", "tags"]

    def __init__(self, connectionUrl, defaultSource=None, tags=None):
        self.connectionUrl: str = connectionUrl
        self.defaultSource: bool = defaultSource
        self.tags: str = tags

    def _validate(self):
        return any(x for x in ['connectionUrl'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, JdbcTagConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.connectionUrl, self.defaultSource, self.tags))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["connectionUrl", "defaultSource", "tags"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__