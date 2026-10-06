def calculate(close, period=20, std=2):
    middle=close.rolling(period).mean()
    upper=middle+std*close.rolling(period).std()
    lower=middle-std*close.rolling(period).std()
    return middle,upper,lower
