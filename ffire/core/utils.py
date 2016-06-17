"""
Connection renegade util

ffire.connection
~~~~~~~~~~~~~~~~

Responsible for all connections made within the fire library
"""
import requests

_connection = dict()
_configuration = dict()


def get_configuration(config):
    """
    Returns the global configuration collection object

    :param config:              The name of the config settings to retrieve
                                :type <type, 'str'>
    :return:
    """
    return _configuration.get(config)


def get_connection(alias=None):
    """
    Gets a connection to the broker using either of the trio of alias, connection, or broker
    and returns to the calling context.

    :param alias:
    :return:
    """
    pass


def resolve_json_response(json_response):
    """
    Resolves the json response for success or failure status and returns the correct
    response based on the outcome of said resolution

    :param json_response:       The json response gotten from a remote host, an overzealous typist
                                or some loosely available file
                                :type <type, 'str'>

    :return status:             The status of the json message which could be one of `success` or `failure`
                                :type <type, 'str'>
    """
    #: Is the json response success or failure json
    #: if success get the data
    #: If failure return the message
    pass
