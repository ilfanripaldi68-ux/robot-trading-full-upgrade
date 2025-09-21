def generate_signal(pair, timeframe, last):
    direction = None
    entry = last['close']
    sl, tp_levels = None, []
    entry_info = None

    # aturan sederhana
    if last['ema50'] > last['ema200'] and last['rsi'] > 45:
        direction = "LONG"
        sl = entry - last['atr']
    elif last['ema50'] < last['ema200'] and last['rsi'] < 55:
        direction = "SHORT"
        sl = entry + last['atr']

    if direction:
        # hitung TP untuk R/R 1:2 sampai 1:5
        tp_levels = []
        for rr in [2,3,4,5]:
            risk = abs(entry - sl)
            tp = entry + (risk * rr) if direction == "LONG" else entry - (risk * rr)
            tp_levels.append((rr, tp))

        entry_info = {
            "entry": entry,
            "sl": sl,
            "tp_levels": tp_levels,
            "direction": direction
        }

        tps = "\n".join([f"TP (R/R 1:{rr}) : {round(tp, 2)}" for rr, tp in tp_levels])

        return f"""
[{pair} - TF {timeframe}]
Arah     : {direction}
Entry    : {round(entry, 2)}
StopLoss : {round(sl, 2)}
{tps}
RSI      : {round(last['rsi'], 2)}
EMA50    : {round(last['ema50'], 2)}
EMA200   : {round(last['ema200'], 2)}
""", entry_info
    else:
        return f"[{pair} - TF {timeframe}] Tidak ada sinyal valid.", None
