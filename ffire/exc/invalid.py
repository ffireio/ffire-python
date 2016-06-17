"""
Invalid Exceptions Module

ffire.exc.invalid
~~~~~~~~~~~~~~~~~

Parent module of all exceptions arising from invalid artifact usage
"""


class InvalidInputError(AttributeError):
    """
    Raised when an invalid attribute is passed into a method or class for initialization
    """

    def __init__(self, *args, **kwargs):
        self.message = 'Invalid attribute error: '
        if len(args) > 0:
            self.message += args[0]

        super(InvalidInputError, self).__init__(self.message)


#: Invalid payload : i.e. payload is not http encode-able by our automatic encoding
#: If you can encode it your self and send via one of our supported formats i.e. json or form multipart
#: then this exception will not be thrown


#: Invalid endpoint type i.e endpoint is not a valid url, no ip addresses allowed


class NotSupportedError(Exception):
    """
    Exception raised when an action not supported by ffire is explored
    """

    def __init__(self, *args, **kwargs):
        self.message = 'The action you are trying to perform is not supported: '
        if len(args) > 0:
            self.message += args[0]

        super(NotSupportedError, self).__init__(self.message)
