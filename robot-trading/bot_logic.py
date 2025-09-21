import ccxt
import pandas as pd
import pandas_ta as ta
from strategy import generate_signal

exchange = ccxt.binance()

pairs = [
    "BTC/USDT",   # crypto
    "ETH/USDT",   # crypto
    "XAU/USDT",   # gold
    "EUR/USDT",   # forex
    "GBP/USDT",   # forex
]

def analyze_pair(pair, timeframe):
    bars = exchange.fetch_ohlcv(pair, timeframe=timeframe, limit=200)
    df = pd.DataFrame(bars, columns=['time','open','high','low','close','volume'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')

    # indikator
    df['ema50'] = ta.ema(df['close'], length=50)
    df['ema200'] = ta.ema(df['close'], length=200)
    df['rsi'] = ta.rsi(df['close'], length=14)
    df['atr'] = ta.atr(df['high'], df['low'], df['close'], length=14)

    last = df.iloc[-1]
    signal, entry_info = generate_signal(pair, timeframe, last)
    return signal, df, entry_info

def get_signals_and_data(timeframe="15m"):
    results = []
    data_dict = {}
    entries = {}
    for pair in pairs:
        try:
            signal, df, entry_info = analyze_pair(pair, timeframe)
            results.append(signal)
            data_dict[pair] = df
            if entry_info:
                entries[pair] = entry_info
        except Exception as e:
            results.append(f"[{pair}] Error: {e}")
    return "\n".join(results), data_dict, entries
