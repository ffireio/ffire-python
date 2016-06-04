"""
Failed exceptions module

ffire.exc.failed
~~~~~~~~~~~~~~~~

Collection of exceptions that are raised as a result of an operation or
function call not succeeding due to internal or external error.

"""


class BrokerConnectionError(Exception):
    """
    Raised when the underlying broker could not be connected to
    """

    def __init__(self, *args, **kwargs):
        self.message = 'Failed to establish a connection with the broker'
        if len(args) > 0:
            self.message = args[0]
        super(BrokerConnectionError, self).__init__(self.message)
