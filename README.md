🪙 Crypto Price Tracker\
Track the real-time price of any cryptocurrency using the CoinGecko API.\
Get instant alerts when the price rises above or falls below your custom thresholds.\
Built in Python using requests --- simple, clean, and powerful.

Features

-   Real-time price lookup using CoinGecko API

-   Custom alert thresholds (above/below)

-   Loop with interval-based checks

-   Clear error handling

-   Easy to extend with notifications (email, push, etc.)

Getting Started\
Requirements

-   Python 3.8+

-   requests library

Setup

1.  Clone the repo\
    git clone <https://github.com/PajoHack/crypto-price-tracker.git>\
    cd crypto-price-tracker

2.  Create and activate virtual environment\
    python3 -m venv venv\
    source venv/bin/activate

3.  Install dependencies\
    pip install -r requirements.txt

4.  Run the tracker\
    python tracker.py

* * * * *

Usage (CLI Modes)

Run a One-Time Price Check\
Command:\
python tracker.py --once

Run in Loop Mode (checks every 10 minutes)\
Command:\
python tracker.py --loop

Run Loop Mode for N Times Only\
Command:\
python tracker.py --loop --limit 5

Available Flags\
--once -- Runs a single price check and exits\
--loop -- Runs every 10 minutes continuously\
--limit N -- Optional. Stops loop after N runs (used with --loop)\
If no flag is passed, the program will display a warning and exit

* * * * *

Example Output

🕒 2025-07-30 12:00:00\
Current Bitcoin price: $118,031.00\
🚀 ALERT: Price is ABOVE $118,000.00!\
✅ Price logged successfully.\
⏳ Waiting 10 minutes before next check...

* * * * *

Configuration (Coming Soon)

You'll soon be able to customize:

-   Tracked coin (e.g., bitcoin, ethereum)

-   Currency (e.g., usd, eur)

-   Alert thresholds

-   Check intervals

These settings will live inside config.py.

* * * * *

Contributing

Pull requests are welcome!\
Suggestions for improvement:

-   Add desktop or email notifications

-   Track multiple coins

-   Visualize historical data with matplotlib or pandas

-   Export logs to Google Sheets

* * * * *

License\
MIT License © PajoHack