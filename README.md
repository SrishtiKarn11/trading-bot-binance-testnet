# Binance Futures Testnet Trading Bot

##  Overview

This project is a simplified trading bot built in Python that places orders on Binance Futures Testnet (USDT-M).

It supports:

- Market Orders
- Limit Orders
- BUY and SELL sides
- CLI-based execution (argparse)
- Logging of requests, responses, and errors
- Exception handling
- Lightweight Streamlit UI (Bonus Feature)

The project follows a structured and reusable code design with separation of concerns.

---

##  Tech Stack

- Python 3.x
- python-binance
- python-dotenv
- Streamlit 

---

##  Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── logs/
│
├── cli.py
├── app.py
├── requirements.txt
├── .env.example
├── README.md
```

---

##  Setup Instructions

### 1️ Clone or Download the Project

Download ZIP or clone repository.

---

### 2️ Create Virtual Environment

Windows:
```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️ Configure Environment Variables

Rename `.env.example` to `.env` and replace with your Binance Futures Testnet credentials:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

Testnet Base URL used:
https://testnet.binancefuture.com

---

##  Running the CLI

###  Market Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

###  Limit Order Example

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000
```

The CLI prints:

- Order request summary
- Order response details (orderId, status, executedQty, avgPrice)
- Success / failure message

---

##  Running the UI (Bonus)

```
streamlit run app.py
```

Features:

- Live market price display
- Market and Limit order placement
- Input validation
- Clean UI layout

---

##  Logging

Logs are stored inside the `logs/` directory.

Includes:

- One successful MARKET order log
- One successful LIMIT order log
- Error logging (if applicable)

---

##  Assumptions

- Binance Futures Testnet account is active
- API credentials are valid
- Minimum notional requirement (100 USDT) is respected
- Internet connection is available

---

##  Evaluation Criteria Covered

✔ Correct order placement on testnet  
✔ Structured code (separation of layers)  
✔ CLI validation  
✔ Logging implementation  
✔ Error handling  
✔ Clear documentation  
✔ Bonus UI feature  

---