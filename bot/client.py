import os
from binance.client import Client
from dotenv import load_dotenv
import logging

load_dotenv()

def get_client():
    try:
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API credentials not found in .env file")

        client = Client(
            api_key,
            api_secret,
            testnet=True
        )

        logging.info("Binance Testnet Client initialized successfully")
        return client

    except Exception as e:
        logging.error(f"Error initializing client: {str(e)}")
        raise