"""
project connection tests

tests.ffire.utils.connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests that the connection module operations are as expected
"""
from unittest import TestCase


class UtilsTest(TestCase):
    """
    Connection Test Class
    """

    def setUp(self):
        """
        Decalare reusable once
        """
        pass

        #: Call init_connection here to ensure it is not dirtying a test case
        #: and to make sure that it actually persists across functions

    def tearDown(self):
        """
        Teardown shared resources
        :return:
        """
        pass

    def test_init_connection(self):
        """
        Test that the initialize connection method of the utils module works and actually connects
        to the ffire api. And raises the appropriate exceptions for respective abnormal cases.
        :return:
        """
        pass
