import pandas as pd
import sqlite3

DB_PATH = "data/prices.db"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM prices", conn)
    conn.close()

    # Convert timestamp column to actual datetime objects
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed", utc=True)

    # Sort so rolling calculations happen in correct time order
    df = df.sort_values(["coin", "timestamp"])
    return df

def add_analytics(df):
    # Group by coin so each coin's stats are calculated independently
    grouped = df.groupby("coin")

    # Rolling average price (window of 3 fetches — adjust once you have more data)
    df["rolling_avg_price"] = grouped["price_usd"].transform(
        lambda x: x.rolling(window=3, min_periods=1).mean()
    )

    # % change from the previous fetch for that coin
    df["pct_change"] = grouped["price_usd"].transform(
        lambda x: x.pct_change() * 100
    )

    # Rolling volatility (standard deviation over the window)
    df["volatility"] = grouped["price_usd"].transform(
        lambda x: x.rolling(window=3, min_periods=1).std()
    )

    return df

if __name__ == "__main__":
    df = load_data()
    df = add_analytics(df)
    print(df[["coin", "timestamp", "price_usd", "rolling_avg_price", "pct_change", "volatility"]])