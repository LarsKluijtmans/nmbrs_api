"""This module provides access to various services and utilities related to Nmbrs."""

from .api import Nmbrs
from .__version__ import (
    __version__,
    __title__,
    __description__,
    __author__,
    __author_email__,
)
from .__logging__ import logger_config
from .service.sso_service import SingleSingOnService
from .data_classes.serialize import serialize
