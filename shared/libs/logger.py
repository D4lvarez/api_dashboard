import logging
import sys

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def setup_logger(logger_name: str, filename: str | None = None):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)

    logger.addHandler(sh)

    if filename:
        fh = logging.FileHandler(f"./logs/{filename}.log")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
