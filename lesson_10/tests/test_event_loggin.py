import os
import logging
import pytest
from lesson_10.src.functions import log_event
def clear_loggers():
    """
    Clears the existing log handlers before each test to avoid conflicts.
    """
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)


def check_log_file_contains_message(expected_message):
    """
    Helper function to check if the log file contains the expected log message.
    """
    assert os.path.exists('login_system.log'), "Log file was not created."
    with open('login_system.log', 'r') as f:
        logs = f.read()
        assert expected_message in logs, f"Expected log message not found: {expected_message}"


def test_log_event_success():
    # clear loggers
    clear_loggers()

    # call the function that records the log
    log_event("test_user", "success")

    # check if the file contains the expected message
    check_log_file_contains_message("Login event - Username: test_user, Status: success")


def test_log_event_expired():

    clear_loggers()

    log_event("test_user", "expired")

    check_log_file_contains_message("Login event - Username: test_user, Status: expired")



def test_log_event_failed():

    clear_loggers()

    log_event("test_user", "failed")

    check_log_file_contains_message("Login event - Username: test_user, Status: failed")
