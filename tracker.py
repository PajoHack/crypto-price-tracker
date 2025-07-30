import requests
from config import COIN_ID, CURRENCY, ALERT_IF_ABOVE, ALERT_IF_BELOW
from notify import sound_alert
from utils import format_price, log_price

def fetch_price(coin_id=COIN_ID, vs_currency=CURRENCY):
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
    params = {"ids": coin_id, "vs_currencies": vs_currency}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[coin_id][vs_currency]
    except requests.RequestException as e:
        print(f"❌ Error fetching price: {e}")
        return None
    

def check_thresholds(price):
    """
    Compares the current cryptocurrency price against predefined thresholds
    and prints an alert message if the price is outside the target range.

    Args:
        price (float): The current price of the cryptocurrency.

    Returns:
        None
    """
    if price >= ALERT_IF_ABOVE:
        print(f"🚀 ALERT: Price is ABOVE {format_price(ALERT_IF_ABOVE)}!")
        sound_alert()
    elif price <= ALERT_IF_BELOW:
        print(f"🔻 ALERT: Price is BELOW {format_price(ALERT_IF_BELOW)}!")
        sound_alert()
    else:
        print(f"✅ Price is within range ({format_price(ALERT_IF_BELOW)} - {format_price(ALERT_IF_ABOVE)})")


# Run check manually
if __name__ == "__main__":
    price = fetch_price()
    if price is not None:
        print(f"Current Bitcoin price: {format_price(price)}")
        check_thresholds(price)
        log_price(price, COIN_ID)
        print("Price logged successfully.")
    else:
        print("Failed to fetch price data.")
