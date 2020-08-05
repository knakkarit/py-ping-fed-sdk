class DecryptionKeys():
    """ Decryption keys used to decrypt message content received from the partner.

    Attributes
    ----------
    primaryKeyRef : str
        The ID of the primary decryption key pair. It is also known as the alias and can be found by viewing the corresponding certificate under 'Signing & Decryption Keys & Certificates' in the PingFederate Administrative Console.
    secondaryKeyPairRef : str
        The ID of the secondary key pair used to decrypt message content received from the partner.

    """

    __slots__ = ["primaryKeyRef", "secondaryKeyPairRef"]
    def __init__(self, primaryKeyRef=None, secondaryKeyPairRef=None):
            self.primaryKeyRef = primaryKeyRef
            self.secondaryKeyPairRef = secondaryKeyPairRef
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, DecryptionKeys):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((primaryKeyRef, secondaryKeyPairRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
