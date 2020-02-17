import yfinance as yf

ticker = yf.Ticker("MSFT")
history = ticker.history(period="max")
print(history)