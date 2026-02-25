def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_limit_price(order_type, price):
    if order_type.upper() == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")