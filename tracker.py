import requests
import time
import argparse
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


def run_once():
    """
    Executes a single price check:
    - Fetches current price
    - Prints formatted result
    - Logs the result to a CSV
    - Triggers alerts if thresholds are crossed

    Returns:
        None
    """
    price = fetch_price()
    if price is not None:
        print(f"\n🕒 {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Current Bitcoin price: {format_price(price)}")
        check_thresholds(price)
        log_price(price, COIN_ID)
        print("✅ Price logged successfully.")
    else:
        print("❌ Failed to fetch price data.")

def run_loop(limit=None):
    """
    Repeatedly executes the run_once() function every 10 minutes.

    Args:
        limit (int, optional): Number of times to run before stopping.
                               If None, runs indefinitely.

    Returns:
        None
    """
    count = 0
    while True:
        run_once()
        count += 1
        if limit and count >= limit:
            print(f"\n🔚 Stopping after {limit} runs.")
            break
        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crypto Price Tracker")
    parser.add_argument("--once", action="store_true", help="Run tracker once and exit")
    parser.add_argument("--loop", action="store_true", help="Run tracker in 10-minute loop")
    parser.add_argument("--limit", type=int, help="Number of loops before stopping")

    args = parser.parse_args()

    if args.once:
        run_once()
    elif args.loop:
        run_loop(limit=args.limit)
    else:
        print("⚠️ No mode selected. Use --once or --loop.")

