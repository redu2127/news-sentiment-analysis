import pandas as pd


def calculate_sma(data: pd.DataFrame, column: str = "Close", window: int = 20):
    """
    Calculate Simple Moving Average (SMA).

    SMA smooths price data over a fixed window to identify trend direction.
    """
    try:
        return data[column].rolling(window=window).mean()
    except KeyError:
        raise KeyError(f"Column '{column}' not found in dataframe.")


def calculate_ema(data: pd.DataFrame, column: str = "Close", span: int = 20):
    """
    Calculate Exponential Moving Average (EMA).

    EMA gives more weight to recent prices and reacts faster than SMA.
    """
    try:
        return data[column].ewm(span=span, adjust=False).mean()
    except KeyError:
        raise KeyError(f"Column '{column}' not found in dataframe.")


def calculate_rsi(data: pd.DataFrame, column: str = "Close", window: int = 14):
    """
    Calculate Relative Strength Index (RSI).

    RSI helps identify overbought and oversold conditions.
    """
    try:
        delta = data[column].diff()

        gain = delta.where(delta > 0, 0)

        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=window).mean()

        avg_loss = loss.rolling(window=window).mean()

        rs = avg_gain / avg_loss

        return 100 - (100 / (1 + rs))

    except KeyError:
        raise KeyError(f"Column '{column}' not found in dataframe.")


def calculate_macd(data: pd.DataFrame, column: str = "Close"):
    """
    Calculate MACD and signal line.

    MACD helps identify momentum shifts and possible trend reversals.
    """
    try:
        ema_12 = data[column].ewm(span=12, adjust=False).mean()

        ema_26 = data[column].ewm(span=26, adjust=False).mean()

        macd = ema_12 - ema_26

        signal = macd.ewm(span=9, adjust=False).mean()

        return macd, signal

    except KeyError:
        raise KeyError(f"Column '{column}' not found in dataframe.")
