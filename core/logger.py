import logging
import os
import configparser

config = configparser.ConfigParser()
config.read("pytest.ini")


def setup_logger(log_file=config.get("pytest", "log_file")):
    """
    Configures a centralized logger for the framework.

    Args:
        log_file (str): The file path where logs should be written. Defaults to the value from the 'pytest' configuration.

    Returns:
        None
    """
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        handlers=[
            logging.FileHandler(log_file, mode="w"),
            logging.StreamHandler(),
        ]
    )

    logging.info("Starting New Test Execution Session")
