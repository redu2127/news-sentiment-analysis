import pandas as pd

from src.technical_indicators import calculate_sma


def test_calculate_sma():

    df = pd.DataFrame({
        "Close": [1, 2, 3, 4, 5]
    })

    sma = calculate_sma(df, "Close", 3)

    assert round(sma.iloc[-1], 2) == 4.00
