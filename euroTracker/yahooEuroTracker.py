import yfinance as yf

ticker = yf.Ticker("FBK.MI")
history = ticker.history(period="max")
print(history)