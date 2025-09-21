import requests
from bs4 import BeautifulSoup

def get_latest_news():
    try:
        news_texts = []

        # Crypto news (Coindesk)
        url_crypto = "https://www.coindesk.com/arc/outboundfeeds/rss/"
        r1 = requests.get(url_crypto, timeout=10)
        soup1 = BeautifulSoup(r1.content, features="xml")
        items1 = soup1.findAll("item")[:2]
        news_texts.append("[Crypto News]")
        for item in items1:
            news_texts.append(f"- {item.title.text}")

        # Forex/Gold news (Investing.com RSS)
        url_fx = "https://www.investing.com/rss/news_301.rss"
        r2 = requests.get(url_fx, timeout=10)
        soup2 = BeautifulSoup(r2.content, features="xml")
        items2 = soup2.findAll("item")[:2]
        news_texts.append("\n[Forex & Gold News]")
        for item in items2:
            news_texts.append(f"- {item.title.text}")

        return "\n".join(news_texts)

    except Exception as e:
        return f"Error ambil berita: {e}"
