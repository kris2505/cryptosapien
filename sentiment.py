import requests
from datetime import datetime
from pytrends.request import TrendReq


def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum',
        'vs_currencies': 'usd',
        'include_24hr_vol': 'true',
        'include_24hr_change': 'true'
    }
    response = requests.get(url, params=params)
    return response.json()


def fetch_google_trends_score():
    pytrends = TrendReq()
    kw_list = ["Buy Bitcoin", "Sell Bitcoin", "Crypto", "Bitcoin"]
    pytrends.build_payload(kw_list, cat=0, timeframe='now 1-H', geo='', gprop='')
    data = pytrends.interest_over_time()
    if data.empty:
        return 50  # нейтральне значення, якщо нічого не знайдено

    avg_score = data[kw_list].mean().mean()
    return avg_score


def calculate_sentiment_index(price_data, trend_score):
    btc = price_data["bitcoin"]
    vol = btc["usd_24h_vol"]
    change = btc["usd_24h_change"]

    # простий індекс емоцій: комбінація трендів, обʼєму і зміни ціни
    index = 0.4 * (trend_score / 100) + 0.3 * min(max(change / 10, -1), 1) + 0.3 * min(max(vol / 1e10, 0), 1)
    return round(index * 100, 2)
