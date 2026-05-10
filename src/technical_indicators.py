import pandas as pd

def calculate_sma(data, column="Close", window=20):
    """
    Calculate Simple Moving Average (SMA)
    """

    return data[column].rolling(window=window).mean()
