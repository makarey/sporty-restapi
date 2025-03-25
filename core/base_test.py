import logging


class BaseTest:

    def setup_method(self, method):
        """
        Sets up the test environment before each test method is executed.

        Args:
            method (function): The test method that is about to be executed.
        """
        logging.info(f"Setting up test: {method.__name__}")

    def teardown_method(self, method):
        """
        Teardown method that is called after each test method.

        This method logs the name of the test method that is being torn down.

        Args:
            method (function): The test method that has just been executed.
        """
        logging.info(f"Tearing down test: {method.__name__}")
