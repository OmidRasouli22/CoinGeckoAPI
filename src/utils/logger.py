import logging

# Create a reusable logger for the whole project
def get_logger(name: str):
    logger = logging.getLogger(name)

    # Avoid duplicate logs
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger