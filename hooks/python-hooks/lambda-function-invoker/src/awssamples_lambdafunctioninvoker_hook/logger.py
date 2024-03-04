"""Logger module."""


import logging

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)

LOG.setLevel(logging.INFO)
# LOG.setLevel(logging.DEBUG)
