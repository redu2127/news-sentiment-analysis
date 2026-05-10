import pandas as pd


def calculate_sma(data: pd.DataFrame, column: str = "Close", window: int = 20):
    return data[column].rolling(window=window).mean()


def calculate_ema(data: pd.DataFrame, column: str = "Close", span: int = 20):
    return data[column].ewm(span=span, adjust=False).mean()


def calculate_rsi(data: pd.DataFrame, column: str = "Close", window: int = 14):
    delta = data[column].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def calculate_macd(data: pd.DataFrame, column: str = "Close"):
    ema_12 = data[column].ewm(span=12, adjust=False).mean()
    ema_26 = data[column].ewm(span=26, adjust=False).mean()

    macd = ema_12 - ema_26
    signal = macd.ewm(span=9, adjust=False).mean()

    return macd, signal