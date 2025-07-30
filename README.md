# 🪙 Crypto Price Tracker

Track the real-time price of any cryptocurrency using the CoinGecko API.  
Get instant alerts when the price rises above or falls below your custom thresholds.  

> ⚡ Built in Python using requests — simple, clean, and powerful.

---

## 📦 Features

- ✅ Real-time price lookup using CoinGecko API
- ⚠️ Custom alert thresholds (above/below)
- 🔁 Loop with interval-based checks (coming soon)
- 💬 Clear error handling
- 🛠️ Easy to extend with notifications (email, push, etc.)

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- `requests` library

### 🧰 Setup

```bash
# Clone the repo
git clone https://github.com/PajoHack/crypto-price-tracker.git
cd crypto-price-tracker

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tracker
python tracker.py

## 📈 Example Output

```bash
Current Bitcoin price: $34,872.15


---

### ⚙️ Configuration (Coming Soon)
```markdown
## ⚙️ Configuration (Coming Soon)

Define your:
- Target coin (`bitcoin`, `ethereum`, etc.)
- Target currency (`usd`, `eur`, etc.)
- Alert thresholds
- Frequency of price checks

## 🤝 Contributing

Feel free to fork and open a PR! Ideas welcome:
- Add desktop/email notifications
- Support multiple coins
- Add historical charting with `matplotlib` or `pandas`

## 📜 License

MIT License © [PajoHack](https://github.com/PajoHack)
