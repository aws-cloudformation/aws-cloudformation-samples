"""Unit tests for Logger."""


from ..logger import LOG


def test_given_log_instance_when_created_then_should_have_method_for_info_log_level():  # noqa: E501
    assert hasattr(LOG, "info")


def test_given_log_instance_when_created_then_should_have_method_for_error_log_level():  # noqa: E501
    assert hasattr(LOG, "error")


def test_given_log_instance_when_created_then_should_have_method_for_debug_log_level():  # noqa: E501
    assert hasattr(LOG, "debug")


def test_given_logger_is_defined_when_code_runs_should_use_info_log_level():
    # Assert that log level is 20 (INFO) for normal, current operation.
    # See: https://docs.python.org/3/library/logging.html#logging-levels
    assert LOG.getEffectiveLevel() == 20
