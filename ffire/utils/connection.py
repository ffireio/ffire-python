"""
Connection renegade util

ffire.connection
~~~~~~~~~~~~~~~~

Responsible for all connections made within the fire library
"""
from ffire.constants import SQS, SNS, RABBIT, RABBIT_MQ, BROKERS, PASSWORD, PORT, USERNAME
from ffire.exc.invalid import NotSupportedError, InvalidInputError

_connection = dict()
_configuration = dict()


def _get_default_broker_value(attribute, broker):
    """
    Returns the vendor default option

    :param attribute:       The broker being looked up. i.e. `port` for getting default port
                            and `password` for getting default password.
                            :type <type, 'str'>

    :param broker:          The broker with which to use to lookup the default attribute value
                            wanted.
                            :type <type, 'str'>
    :return:
    """
    brokers = BROKERS

    if attribute not in [PORT, USERNAME, PASSWORD]:
        raise InvalidInputError('{0} attribute not valid for broker lookup'.format(attribute or 'Empty'))

    if broker in [SNS, SQS, RABBIT, RABBIT_MQ]:
        return brokers.get(broker).get(attribute)
    raise InvalidInputError('Filter parameter not passed')


def get_configuration(config):
    """
    Returns the global configuration collection object

    :param config:              The name of the config settings to retrieve
                                :type <type, 'str'>
    :return:
    """
    return _configuration.get(config)


def get_connection(alias=None, connection=None, broker_name=None):
    """
    Gets a connection to the broker using either of the trio of alias, connection, or broker
    and returns to the calling context.

    :param alias:
    :param connection:
    :param broker_name:
    :return:
    """
    pass


def init_connection(name=None, host=None, port=None, secure=True,
                    username=None, password=None):
    """
    Initialize the connections necessary to use ffire for communication with
    necessary brokers and backing systems.

    :param name:                    The particular broker technology used to power
                                    firing and subscribing of events

    :param host:                    The hostname of the machine where the broker is
                                    expected to be up and running

    :param port:                    An open port on the host where communication to
                                    the broker is allowed

    :param secure:                  Sign and seal resources to prevent cross service event
                                    recreation and resource tampering
    :return:
    """
    global _configuration
    if name not in ('sqssns', 'rabbitmq'):
        raise NotSupportedError('Invalid Broker Type')

    config = {
        'host': host or 'localhost',
        'port': port or _get_default_broker_value(name),
        'broker': name,
        'username': username,
        'password': password
    }
    _configuration['config'] = config
