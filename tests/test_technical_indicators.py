import pandas as pd

from src.technical_indicators import (
    calculate_sma,
    calculate_ema,
    calculate_rsi,
    calculate_macd,
)


def test_calculate_sma():
    df = pd.DataFrame({"Close": [1, 2, 3, 4, 5]})
    sma = calculate_sma(df, "Close", 3)
    assert round(sma.iloc[-1], 2) == 4.00


def test_calculate_ema():
    df = pd.DataFrame({"Close": [1, 2, 3, 4, 5]})
    ema = calculate_ema(df, "Close", 3)
    assert len(ema) == 5


def test_calculate_rsi():
    df = pd.DataFrame({"Close": [1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]})
    rsi = calculate_rsi(df, "Close", 14)
    assert len(rsi) == len(df)


def test_calculate_macd():
    df = pd.DataFrame({"Close": list(range(1, 40))})
    macd, signal = calculate_macd(df, "Close")
    assert len(macd) == len(df)
    assert len(signal) == len(df)