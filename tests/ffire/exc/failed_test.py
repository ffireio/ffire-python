"""
Test failed exceptions

ffire.tests.exc.failed_test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure failed exceptions are as expected
"""
from unittest import TestCase


from ffire.exc.failed import AuthenticationError
from ffire.exc.invalid import InvalidEndpointError


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
        pass

    def test_authentication_error(self):
        """
        Ensures authentication error is raised and outputs appropriate message
        :return:
        """
        try:
            raise AuthenticationError()
        except AuthenticationError as e:
            self.assertTrue("Failed to authenticate" in e.message)

    def test_invalid_endpoint_error(self):
        """
        Ensures authentication error is raised and outputs appropriate message
        :return:
        """
        try:
            raise InvalidEndpointError()
        except InvalidEndpointError as e:
            self.assertTrue("not a valid http url" in e.message)
