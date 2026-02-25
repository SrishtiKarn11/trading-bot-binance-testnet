import logging

def setup_logger():
    logging.basicConfig(
        filename="trading_bot.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        filemode="a"
    )

    # Reduce noisy logs from python-binance
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("binance").setLevel(logging.WARNING)

    logging.info("Logging initialized successfully")