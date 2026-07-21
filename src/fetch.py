import requests
import sqlite3
from datetime import datetime,timezone

DB_PATH = "data/prices.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin TEXT NOT NULL,
            price_usd REAL NOT NULL,
            change_24h REAL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def save_prices(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.now(timezone.utc).isoformat()
    for coin, values in data.items():
        cursor.execute(
            "INSERT INTO prices (coin, price_usd, change_24h, timestamp) VALUES (?, ?, ?, ?)",
            (coin, values["usd"], values.get("usd_24h_change"), timestamp)
        )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    prices = get_prices()
    save_prices(prices)
    print(f"Saved prices at {datetime.now(timezone.utc).isoformat()}: {prices}")