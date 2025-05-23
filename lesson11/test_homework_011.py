import unittest
from homework_011 import log_event
import logging

class TestLogEvent(unittest.TestCase):

    def test_success_logs_info(self):
        with self.assertLogs('log_event', level='INFO') as log:
            log_event("john_doe", "success")
            self.assertIn("INFO:log_event:Login event - Username: john_doe, Status: success", log.output)

    def test_expired_logs_warning(self):
        with self.assertLogs('log_event', level='WARNING') as log:
            log_event("john_doe", "expired")
            self.assertIn("WARNING:log_event:Login event - Username: john_doe, Status: expired", log.output)

    def test_failed_logs_error(self):
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("john_doe", "failed")
            self.assertIn("ERROR:log_event:Login event - Username: john_doe, Status: failed", log.output)

    def test_unknown_status_raises_assertion(self):
        with self.assertRaises(AssertionError):
            log_event("john_doe", "unknown_status")

    def test_empty_username_raises_assertion(self):
        with self.assertRaises(AssertionError):
            log_event("", "success")

    def test_non_string_username_raises_assertion(self):
        with self.assertRaises(AssertionError):
            log_event(123, "success")

    def test_invalid_status_raises_assertion(self):
        with self.assertRaises(AssertionError):
            log_event("john_doe", "not_valid_status")


if __name__ == '__main__':
    unittest.main()
