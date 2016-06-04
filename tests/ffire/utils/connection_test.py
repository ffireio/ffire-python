"""
project connection tests

tests.ffire.utils.connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests that the connection module operations are as expected
"""
from unittest import TestCase


from ffire.constants.fake import FAKE_PORT, FAKE_HOST, FAKE_BROKER_TYPE_RABBIT, FAKE_BROKER_TYPE_SQS, FAKE_ALIAS
from ffire.exc.invalid import InvalidInputError

from ffire.utils import connection


class ConnectionTest(TestCase):
    """
    Connection Test Class
    """

    def setUp(self):
        """
        Decalare reusable once
        """
        self.alias = FAKE_ALIAS
        self.broker_type_sqs = FAKE_BROKER_TYPE_SQS
        self.broker_type_rabbit = FAKE_BROKER_TYPE_RABBIT

        self.host = FAKE_HOST
        self.port = FAKE_PORT
        self.secure_connection = True

        #: Call init_connection here to ensure it is not dirtying a test case
        #: and to make sure that it actually persists across functions
        connection.init_connection(self.broker_type_sqs, self.host, self.port, self.secure_connection)

    def tearDown(self):
        """
        Teardown shared resources
        :return:
        """
        pass

    def test_get_default_broker_value(self):
        """
        Ensures getting of broker defaults returns valid defaults as dictated by input params
        :return:
        """
        self.assertRaises(InvalidInputError, connection._get_default_broker_value, 'vendor', 'sqs')
        self.assertRaises(InvalidInputError, connection._get_default_broker_value, 'password', 'kafka')

        rabbit_password = 'guest'
        default_password = connection._get_default_broker_value('password', 'rabbit')
        rabbit_username = 'guest'
        default_username = connection._get_default_broker_value('username', 'rabbit_mq')

        self.assertEquals(rabbit_password, default_password)
        self.assertEquals(rabbit_username, default_username)

        sqs_password = ''
        default_password = connection._get_default_broker_value('password', 'sqs')
        sqs_username = ''
        default_username = connection._get_default_broker_value('username', 'sqs')

        self.assertEquals(sqs_password, default_password)
        self.assertEquals(sqs_username, default_username)

    def test_init_connection(self):
        """
        Test that the initialize connection method of the connections modules works and actually connects
        to a backing broker. And raises the appropriate exceptions for respective abnormal cases.
        :return:
        """
        from ffire.utils.connection import _configuration

        #: change this later as right now it is redundant
        configuration = connection.get_configuration(self.alias)
        self.assertEquals(configuration, _configuration)
