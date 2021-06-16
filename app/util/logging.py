import logging
import sys
from datetime import datetime
from typing import Any, Dict


import json_logging
from json_logging import BaseJSONFormatter, JSONLogFormatter, util
from flask import Flask


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    return logger




