"""
Test the main module: i.e. fire

ffire.tests.core.fire_test
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensures the main module is as expected
"""
from unittest import TestCase


from ffire.core.fire import Fire


class FireTest(TestCase):
    """
    Fire class tests collection effort.
    """

    def setUp(self):
        """
        Set up potentially repeated values
        :return:
        """
        self.ffire = Fire()
        self.ffire.init(username="test", password="test")

    def tearDown(self):
        """
        Remove expensive resources if any
        :return:
        """
        pass

    def test_init(self):
        """
        Tests to ensure that configuration works correctly
        :return:
        """
        initialized = self.ffire.init("test-username", "test-password")
        self.assertTrue(initialized)

    def test_fire_event(self):
        """
        Ensures that the event can be ffired
        :return:
        """
        self.assertTrue(self.ffire.event("test_order_created", {"story": "ali is an un-serious person"}))

    def test_is_sendable(self):
        """
        Tests to ensure that the is sendable method allows only sendable types to be sent
        :return:
        """
        self.assertTrue(self.ffire._is_sendable(2))
        self.assertTrue(self.ffire._is_sendable("two"))
        self.assertTrue(self.ffire._is_sendable({"status": "success"}))
        self.assertFalse(self.ffire._is_sendable(self.ffire))

    def test_subscribe_event(self):
        """
        Ensures that subscription of endpoints to events do not fail
        :return:
        """
        good = self.ffire.subscribe("order_picked_up", "http://google.com/handlers/order-picked")
        self.assertTrue(good)
