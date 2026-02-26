# app.py
import streamlit as st
from bot.client import get_client
from bot.orders import place_order  # <- unified function
from bot.logging_config import setup_logger

# Page config
st.set_page_config(
    page_title="Binance Futures Bot",
    page_icon="📈",
    layout="centered"
)

# Custom Styling (Clean + Professional)
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 1rem;
        }
        .stButton>button {
            background-color: #f0b90b;
            color: black;
            font-weight: bold;
            border-radius: 8px;
            height: 3em;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #ffd54f;
        }
        .metric-box {
            background-color: #111;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("📊 Binance Futures Testnet Bot")
st.caption("Place Market and Limit Orders on Binance Futures Testnet")

# Initialize client
client = get_client()

st.markdown("---")

# ========== SYMBOL INPUT ==========
symbol = st.text_input("🔎 Symbol", value="BTCUSDT").upper()

# ========== LIVE PRICE ==========
try:
    ticker = client.futures_symbol_ticker(symbol=symbol)
    current_price = float(ticker["price"])
    st.success(f"📡 Current Price: {current_price:,.2f} USDT")
except Exception:
    st.error("Invalid symbol. Please check and try again.")
    st.stop()

st.markdown("---")

# ========== ORDER FORM ==========
col1, col2 = st.columns(2)
with col1:
    side = st.selectbox("Side", ["BUY", "SELL"])
with col2:
    order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])

quantity = st.number_input("Quantity", min_value=0.0, format="%.6f")

price = None
if order_type == "LIMIT":
    price = st.number_input("Limit Price", min_value=0.0, format="%.2f")

st.markdown("---")

# ========== PLACE ORDER BUTTON ==========
if st.button("🚀 Place Order"):

    # Setup logging per order type
    setup_logger(order_type)

    try:
        # Basic validation
        if quantity <= 0:
            st.warning("Please enter a valid quantity.")
            st.stop()

        if order_type == "LIMIT":
            if price is None or price <= 0:
                st.warning("Please enter a valid limit price.")
                st.stop()
            if price < current_price * 0.5 or price > current_price * 1.5:
                st.warning(
                    f"⚠ Limit price seems unrealistic.\n"
                    f"Current price is {current_price:,.2f}.\n"
                    f"Enter a reasonable price."
                )
                st.stop()

        # Execute order using unified function
        with st.spinner("Placing order..."):
            response = place_order(
                client=client,
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )

        # Show order success
        st.success("✅ Order Placed Successfully!")

        st.markdown("### 📋 Order Details")
        colA, colB = st.columns(2)
        with colA:
            st.metric("Order ID", response.get("orderId"))
            st.metric("Status", response.get("status"))
        with colB:
            st.metric("Executed Qty", response.get("executedQty"))
            st.metric("Avg Price", response.get("avgPrice"))

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")