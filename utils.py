# utils.py --- Utility functions for crypto price tracker
# This module provides utility functions for formatting prices and logging
# price data to a CSV file.

def format_price(price):
    """
    Formats the price with dollar sign, commas and 2 decimal places.

    Args:
        price (float): The price to format.

    Returns:
        str: Formatted price string.
    """
    return f"${price:,.2f}"


def log_price(price, coin):
    """
    Logs price to a CSV file for historical tracking.

    Args:
        price (float): The price to log.
        coin (str): Coin name/id.
    """
    from datetime import datetime
    with open("price_log.csv", "a") as f:
        f.write(f"{datetime.now()},{coin},{price}\n")
