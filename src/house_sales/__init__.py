"""House Sales."""
import logging
from importlib import metadata

from house_sales.config.core import config


# It is strongly advised that you do not add any handlers other than
# NullHandler to your library’s loggers. This is because the configuration
# of handlers is the prerogative of the application developer who uses your
# library. The application developer knows their target audience and what
# handlers are most appropriate for their application: if you add handlers
# ‘under the hood’, you might well interfere with their ability to carry out
# unit tests and deliver logs which suit their requirements.
# https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
logging.getLogger(config.app_config.package_name).addHandler(logging.NullHandler())

__version__ = metadata.version(__package__)

print(__version__)
