"""
Broker Information File

ffire.constants.broker_info
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Holds sharable broker information
"""
from ffire.constants import PASSWORD, PORT, USERNAME

sqs = {
    USERNAME: '',
    PASSWORD: '',
    PORT: 8800
}
rabbit = {
    USERNAME: 'guest',
    PASSWORD: 'guest',
    PORT: 8800
}

AMAZON = 'aws'
SQS = 'sqs'
SNS = 'sns'
RABBIT = 'rabbit'
RABBIT_MQ = 'rabbit_mq'


BROKERS = {
    "sqs": sqs,
    "sns": sqs,
    "rabbit": rabbit,
    "rabbitmq": rabbit,
    "rabbit_mq": rabbit
}

BROKER_DEFAULTS = {
    SQS: 4500,
    SNS: 8800,
    RABBIT: 9900,
    RABBIT_MQ: 9900
}

__all__ = [
    'AMAZON',
    'BROKERS',
    'BROKER_DEFAULTS',
    'SQS',
    'SNS',
    'RABBIT',
    'RABBIT_MQ',
]
