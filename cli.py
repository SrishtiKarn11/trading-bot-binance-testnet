import argparse
import logging
import sys

from bot.client import get_client
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type, validate_limit_price
from bot.logging_config import setup_logger


def main():
    setup_logger()
    logging.info("Starting Trading Bot CLI")

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side (BUY or SELL)")
    parser.add_argument("--type", required=True, help="Order type (MARKET or LIMIT)")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # Validate inputs
        validate_side(args.side)
        validate_order_type(args.type)
        validate_limit_price(args.type, args.price)

        client = get_client()

        print("\n===== Order Request Summary =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        # Place order
        if args.type.upper() == "MARKET":
            response = place_market_order(
                client,
                args.symbol,
                args.side,
                args.quantity
            )
        else:
            response = place_limit_order(
                client,
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\n===== Order Response =====")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        print("\n✅ Order placed successfully!")

    except Exception as e:
        logging.error(f"CLI Error: {str(e)}")
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()