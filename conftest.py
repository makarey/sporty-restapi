import os
import pytest
from core.logger import setup_logger


@pytest.fixture(scope="session", autouse=True)
def initialize_logger():
    """
    Automatically initialize the logger before any tests are executed.
    """
    setup_logger()


@pytest.fixture(scope="session", autouse=True)
def setup_env():
    """
    Sets up environment variables for the application.

    This function retrieves the values of specific environment variables
    and returns them in a dictionary. If an environment variable is not set,
    a default value of "default_value" is used.

    Returns:
        dict: A dictionary containing the environment variables and their values.
              Keys are the names of the environment variables, and values are
              their corresponding values.
    """
    env_vars = [
        "API_URL",
    ]
    env_dict = {var: os.getenv(var, "default_value") for var in env_vars}
    return env_dict


@pytest.fixture(scope="session", autouse=True)
def api_url(setup_env):
    """
    Fixture to provide the API URL for tests.

    Args:
        setup_env (dict): A dictionary containing environment configuration,
                          including the 'API_URL' key.

    Returns:
        str: The API URL extracted from the setup_env dictionary.
    """
    """Fixture to provide the API URL for tests."""
    return setup_env["API_URL"]
