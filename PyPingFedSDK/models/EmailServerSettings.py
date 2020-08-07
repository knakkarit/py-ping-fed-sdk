class EmailServerSettings():
    """Email server configuration settings.

    Attributes
    ----------
    emailServer : string
        The IP address or hostname of your email server.    encryptedPassword : string
        For GET requests, this field contains the encrypted password, if one exists.  For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged.    password : string
        User password.  To update the password, specify the plaintext value in this field.  This field will not be populated for GET requests.    port : integer
        The SMTP port on your email server. Allowable values: 1 - 65535. The default value is 25.    retryAttempts : integer
        The number of times PingFederate tries to resend an email upon unsuccessful delivery. The default value is 2.    retryDelay : integer
        The number of minutes PingFederate waits before the next retry attempt. The default value is 2.    sourceAddr : string
        The email address that appears in the 'From' header line in email messages generated by PingFederate.  The address must be in valid format but need not be set up on your system.    sslPort : integer
        The secure SMTP port on your email server. This field is not active unless Use SSL is enabled. Allowable values: 1 - 65535. The default value is  465.    timeout : integer
        The amount of time in seconds that PingFederate will wait before it times out connecting to the SMTP server. Allowable values: 0 - 3600. The default value is 30.    useDebugging : boolean
        Turns on detailed error messages for the PingFederate server log to help troubleshoot any problems.    useSSL : boolean
        Requires the use of SSL/TLS on the port specified by 'sslPort'. If this option is enabled, it overrides the 'useTLS' option.    useTLS : boolean
        Requires the use of the STARTTLS protocol on the port specified by 'port'.    username : string
        Authorized email username. Required if the password is provided.    verifyHostname : boolean
        If useSSL or useTLS is enabled, this flag determines whether the email server hostname is verified against the server's SMTPS certificate.
    """

    __slots__ = ["emailServer", "encryptedPassword", "password", "port", "retryAttempts", "retryDelay", "sourceAddr", "sslPort", "timeout", "useDebugging", "useSSL", "useTLS", "username", "verifyHostname"]

    def __init__(self, sourceAddr, emailServer, port, encryptedPassword=None, password=None, retryAttempts=None, retryDelay=None, sslPort=None, timeout=None, useDebugging=None, useSSL=None, useTLS=None, username=None, verifyHostname=None):
        self.emailServer: str = emailServer
        self.encryptedPassword: str = encryptedPassword
        self.password: str = password
        self.port: str = port
        self.retryAttempts: str = retryAttempts
        self.retryDelay: str = retryDelay
        self.sourceAddr: str = sourceAddr
        self.sslPort: str = sslPort
        self.timeout: str = timeout
        self.useDebugging: bool = useDebugging
        self.useSSL: bool = useSSL
        self.useTLS: bool = useTLS
        self.username: str = username
        self.verifyHostname: bool = verifyHostname

    def _validate(self):
        return any(x for x in ['sourceAddr', 'emailServer', 'port'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, EmailServerSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.emailServer, self.encryptedPassword, self.password, self.port, self.retryAttempts, self.retryDelay, self.sourceAddr, self.sslPort, self.timeout, self.useDebugging, self.useSSL, self.useTLS, self.username, self.verifyHostname))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["emailServer", "encryptedPassword", "password", "port", "retryAttempts", "retryDelay", "sourceAddr", "sslPort", "timeout", "useDebugging", "useSSL", "useTLS", "username", "verifyHostname"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__