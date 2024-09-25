import os
import logging
import pytest
from lesson_10.src.functions import log_event

def test_log_event_success():
    # clear the logger before starting the test
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # call the function that records the log
    log_event("test_user", "success")

    # check if the file has been created
    assert os.path.exists('login_system.log')

    # check if the file contains the expected message
    with open('login_system.log', 'r') as f:
        logs = f.read()
        assert "Login event - Username: test_user, Status: success" in logs

def test_log_event_expired():

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    log_event("test_user", "expired")

    assert os.path.exists('login_system.log')

    with open('login_system.log', 'r') as f:
        logs = f.read()
        assert "Login event - Username: test_user, Status: expired" in logs


def test_log_event_failed():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    log_event("test_user", "failed")

    assert os.path.exists('login_system.log')

    with open('login_system.log', 'r') as f:
        logs = f.read()
        assert "Login event - Username: test_user, Status: failed" in logs
