"""
SQS Module

ffire.brokers.sqssns
~~~~~~~~~~~~~~~~~~~~

Holds the common functionality specific to working with Amazon SQS and SNS service
"""
import boto3

sqs = boto3.resource('sqs')
sns = boto3.resource('sns')


def connect(configuration):
    """
    Establish a connection to aws in preparation for commands execution

    :param configuration:           Valid Ffire configuration object with necessary keys and values
                                    to facilitate connection with AWS sqs sns combo.
                                    :type <type, 'dict'>
    :return:
    """
    #: using the configuration object try to connect to aws
    #: raise connection error if connection fails
    #: do nothing i.e. no news is good news if connection succeeds
    pass


def _create_event(event_name, storage_queue, protected):
    """
    Create an event. Internally it is known as event, however to sqs and sns it is a topic
    and notification combo. Ffire abstracts away the internals and specifics of the backing
    systems to simplify and present a unified interface for events creation, firing, and
    subscription.

    :param event_name:              The unique name to identify the event with. This is
                                    the name that will be used from here on out to interact
                                    with the event.
                                    :type <type, 'str'>

    :param storage_queue:           The queue to save the event in.

    :param protected:               Should this event be protected from being recreated by
                                    other services. Defaults to True.
                                    :type <type, 'bool'>
    :return:
    """
    #: Create a topic on sns using the address information gotten from the connection
    #: that was created with the configuration object
    #: if the protected flag is true prevent that topic from receiving messages from any other service
    pass


def _fire_event(event_name):
    pass


def _subscribe_to_event(event_name):
    pass
