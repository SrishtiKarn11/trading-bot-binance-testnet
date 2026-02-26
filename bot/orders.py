# bot/orders.py
from bot.logging_config import setup_logger
import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    # Initialize logging for this order type
    setup_logger(order_type)

    logging.info("Placing %s order: %s %s %s", order_type, symbol, side, quantity)

    try:
        if order_type.upper() == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logging.info("Market Order Response: %s", order)

        elif order_type.upper() == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logging.info("Limit Order Response: %s", order)

        print("✅ Order placed successfully!")
        return order

    except Exception as e:
        logging.error("%s Order Error: %s", order_type, e)
        print(f"❌ {order_type} Order Error: {e}")