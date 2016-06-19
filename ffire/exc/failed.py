"""
Failed exceptions module

ffire.exc.failed
~~~~~~~~~~~~~~~~

Collection of exceptions that are raised as a result of an operation or
function call not succeeding due to internal or external error.

"""


class AuthenticationError(Exception):
    """
    Raised when the underlying broker could not be connected to
    """

    def __init__(self, *args, **kwargs):
        self.message = 'Failed to authenticate a connection with the ffire api'
        if len(args) > 0:
            self.message = args[0]
        super(AuthenticationError, self).__init__(self.message)


class ConnectionError(Exception):
    """
    Raised when the underlying broker could not be connected to
    """

    def __init__(self, *args, **kwargs):
        self.message = 'Failed to establish a connection with the broker'
        if len(args) > 0:
            self.message = args[0]
        super(ConnectionError, self).__init__(self.message)


#: Event not found


#: Unregistered endpoint : When you try to subscribe an endpoint not from a verified domain in you registry
