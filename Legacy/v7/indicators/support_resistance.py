def calculate(df, window=20):
    return df.Low.rolling(window).min(), df.High.rolling(window).max()
