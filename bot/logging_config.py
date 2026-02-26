# bot/logging_config.py
import logging
import os

def setup_logger(order_type):
    # Ensure logs folder exists
    os.makedirs("logs", exist_ok=True)

    # Log file per order type
    log_file = os.path.join("logs", f"{order_type.lower()}_orders.log")

    # Clear previous handlers to avoid duplicate logs
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        filemode="a"
    )

    # Reduce noisy logs from libraries
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("binance").setLevel(logging.WARNING)

    logging.info(f"{order_type.upper()} Logging initialized successfully")