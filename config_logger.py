import logging


def config():
    info_logger = logging.getLogger('info_logger')
    info_logger.setLevel(logging.INFO)

    info_logger_handler = logging.FileHandler(filename='loging.log', encoding="utf-8")
    info_logger_handler.setLevel(logging.INFO)
    info_logger.addHandler(info_logger_handler)

    info_logger_format = logging.Formatter(f"%(asctime)s [%(levelname)s] %(message)s")
    info_logger_handler.setFormatter(info_logger_format)

    error_logger = logging.getLogger('error_logger')
    error_logger.setLevel(logging.ERROR)

    error_logger_handler = logging.FileHandler(filename='loging.log', encoding="utf-8")
    error_logger_handler.setLevel(logging.ERROR)
    error_logger.addHandler(error_logger_handler)

    error_logger_format = logging.Formatter(f"%(asctime)s [%(levelname)s] %(message)s")
    error_logger_handler.setFormatter(error_logger_format)


