# 🧠 cryptosapien

`cryptosapien` — розумний Python-інструмент для аналізу настроїв на крипторинку на основі реальних даних: CoinGecko, Google Trends, обʼємів торгів та змін цін.

## 🚀 Як це працює?

1. Збирає дані про BTC, ETH (ціна, обʼєм, зміна).
2. Збирає Google Trends на запити "Buy Bitcoin", "Sell Bitcoin", "Crypto", "Bitcoin".
3. Розраховує індекс настроїв — **RSI (Real Sentiment Index)**.
4. Виводить результат у терміналі з емоційною інтерпретацією.

## 🛠 Встановлення

```bash
git clone https://github.com/yourusername/cryptosapien.git
cd cryptosapien
pip install -r requirements.txt

