import requests

def fetch_price(coin_id="bitcoin", vs_currency="usd"):
    """
    Fetches the current market price of a cryptocurrency in a specified currency
    using the CoinGecko API.

    Args:
        coin_id (str): The ID of the cryptocurrency (e.g., 'bitcoin', 'ethereum').
        vs_currency (str): The fiat currency to convert to (e.g., 'usd', 'eur').

    Returns:
        float: The current price of the coin in the given currency, or
        None if the API call fails.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": vs_currency
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[coin_id][vs_currency]
    except requests.RequestException as e:
        print(f"❌ Error fetching price: {e}")
        return None
    
# Run check manually
if __name__ == "__main__":
    price = fetch_price("bitcoin", "usd")
    if price is not None:
        print(f"Current Bitcoin price: ${price:.2f}")
