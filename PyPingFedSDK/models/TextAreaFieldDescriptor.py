class TextAreaFieldDescriptor():
    """A field intended to be rendered as a text box in a UI.

    Attributes
    ----------
    advanced : boolean
 Whether this is an advanced field or not.
    columns : integer
 The number of columns for the text box.
    defaultValue : string
 Default value of the field.
    description : string
 Description of the field.
    label : string
 Label of the field to be displayed in the administrative console.
    name : string
 Name of the field.
    required : boolean
 Whether a value is required for this field or not.
    rows : integer
 The number of rows for the text box.
    type : str
 The type of field descriptor.

    """

<<<<<<< HEAD
    def __init__(self, advanced=None, columns=None, defaultValue=None, description=None, label=None, name=None, required=None, rows=None, var_type=None) -> None:
        self.advanced = advanced
        self.columns = columns
        self.defaultValue = defaultValue
        self.description = description
        self.label = label
        self.name = name
        self.required = required
        self.rows = rows
        self.var_type = var_type
=======
    def __init__(self, advanced=None, columns=None, defaultValue=None, description=None, label=None, name=None, required=None, rows=None, type=None):
        self.advanced: bool = advanced
        self.columns: str = columns
        self.defaultValue: str = defaultValue
        self.description: str = description
        self.label: str = label
        self.name: str = name
        self.required: bool = required
        self.rows: str = rows
        self.type: str = type
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TextAreaFieldDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.advanced, self.columns, self.defaultValue, self.description, self.label, self.name, self.required, self.rows, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["advanced", "columns", "defaultValue", "description", "label", "name", "required", "rows", "var_type"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
