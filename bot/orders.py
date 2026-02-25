import logging

def place_market_order(client, symbol, side, quantity):
    try:
        logging.info(f"Placing MARKET order: {symbol} {side} {quantity}")

        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"Market Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Market Order Error: {str(e)}")
        raise


def place_limit_order(client, symbol, side, quantity, price):
    try:
        logging.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")

        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )

        logging.info(f"Limit Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Limit Order Error: {str(e)}")
        raise