import logging
import inspect

def get_logger(name=None):
    logger = logging.getLogger(name or "smartlog")
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt = "%(asctime)s [%(levelname)s] %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger

logger = get_logger()