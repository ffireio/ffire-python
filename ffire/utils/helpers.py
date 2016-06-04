"""
Collection of helper functions

ffire.utils.helpers
~~~~~~~~~~~~~~~~~~~

Holds functionality for reuse across many other functions or methods
"""


def encode_payload(payload):
    """
    Encodes the payload from python internal type to language agnostic and
    broker send-able interchange format.

    :param payload:             The payload to encode. Inspects this payload and
                                based on its base type encodes appropriately.

    :return encoded_payload:    The encoded payload ready to be returned to the
                                calling context for transmission.
    """
    pass
