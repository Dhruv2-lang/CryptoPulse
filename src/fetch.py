import requests

def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # throws an error if the request failed
    return response.json()

if __name__ == "__main__":
    prices = get_prices()
    print(prices)