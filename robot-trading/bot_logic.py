import ccxt
import pandas as pd
import numpy as np
from strategy import generate_signal

exchange = ccxt.binance()

pairs = [
    "BTC/USDT",
    "ETH/USDT",
    "XAU/USDT",
    "EUR/USDT",
    "GBP/USDT",
]

def compute_indicators(df):
    df = df.copy()
    # EMA
    df['ema50'] = df['close'].ewm(span=50, adjust=False).mean()
    df['ema200'] = df['close'].ewm(span=200, adjust=False).mean()

    # RSI (classic simple SMA-based version)
    length = 14
    delta = df['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=length, min_periods=length).mean()
    avg_loss = loss.rolling(window=length, min_periods=length).mean()
    rs = avg_gain / avg_loss
    df['rsi'] = 100 - (100 / (1 + rs))
    # fill initial NaNs (before enough data) with neutral 50
    df['rsi'].fillna(50, inplace=True)

    # ATR (True Range then rolling mean)
    prev_close = df['close'].shift(1)
    tr1 = df['high'] - df['low']
    tr2 = (df['high'] - prev_close).abs()
    tr3 = (df['low'] - prev_close).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    df['atr'] = tr.rolling(window=14, min_periods=14).mean()
    # fallback for leading NaNs: use expanding mean of TR until ATR window fills
    df['atr'].fillna(tr.expanding().mean(), inplace=True)

    return df

def analyze_pair(pair, timeframe):
    bars = exchange.fetch_ohlcv(pair, timeframe=timeframe, limit=400)
    df = pd.DataFrame(bars, columns=['time','open','high','low','close','volume'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')

    df = compute_indicators(df)

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
