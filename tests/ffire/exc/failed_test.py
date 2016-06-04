"""
Test failed exceptions

ffire.tests.exc.failed_test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure failed exceptions are as expected
"""
from unittest import TestCase


class FailedExceptionTest(TestCase):
    """
    Class container for all tests pertaining to failed exceptions
    """

    def setUp(self):
        """
        Setup resources for reuse across failing tests
        :return:
        """
        pass

    def tearDown(self):
        """
        Teardown expensive resources if any
        :return:
        """

    def test_broker_connection_error(self):
        """
        Tests the broker connection error
        :return:
        """
        pass
