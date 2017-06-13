#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.handlers
from config import LOGGING_FILE, LOGGING_LEVEL

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)
handler = logging.handlers.RotatingFileHandler(LOGGING_FILE,
                                               maxBytes=100000,
                                               backupCount=24,)
logger_format = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
handler.setFormatter(logger_format)
logger.addHandler(handler)
