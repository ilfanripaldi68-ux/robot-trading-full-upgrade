import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

def plot_chart(pair, df, entry_info=None):
    df_plot = df.tail(50).copy()
    df_plot['time_num'] = mdates.date2num(df_plot['time'])
    ohlc = df_plot[['time_num','open','high','low','close']].values

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6), sharex=True,
                                   gridspec_kw={'height_ratios':[3,1]})

    # candlestick
    candlestick_ohlc(ax1, ohlc, width=0.0008, colorup='g', colordown='r')
    ax1.plot(df_plot['time_num'], df_plot['ema50'], label="EMA50", color="blue")
    ax1.plot(df_plot['time_num'], df_plot['ema200'], label="EMA200", color="orange")

    # tanda entry, SL, TP
    if entry_info:
        entry = entry_info["entry"]
        sl = entry_info["sl"]
        tps = entry_info["tp_levels"]

        color = "green" if entry_info["direction"] == "LONG" else "red"
        marker = "^" if entry_info["direction"] == "LONG" else "v"
        ax1.scatter(df_plot['time_num'].iloc[-1], entry, color=color, marker=marker, s=100, label="ENTRY")
        ax1.axhline(sl, color="red", linestyle="--", label="SL")
        for rr, tp in tps:
            ax1.axhline(tp, linestyle="--", alpha=0.6, label=f"TP 1:{rr}")

    ax1.legend()
    ax1.set_title(f"{pair} - Candlestick + EMA + Entry/SL/TP")
    ax1.set_ylabel("Harga")

    # RSI subplot
    ax2.plot(df_plot['time_num'], df_plot['rsi'], color="purple", label="RSI")
    ax2.axhline(70, color="red", linestyle="--", alpha=0.7)
    ax2.axhline(30, color="green", linestyle="--", alpha=0.7)
    ax2.set_ylabel("RSI")
    ax2.legend()

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    plt.tight_layout()
    return fig
