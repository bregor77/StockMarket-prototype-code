import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Fetching data for Apple Inc. for the past 5 years
aapl = yf.Ticker("AAPL")
data = aapl.history(period="5y")

# Plotting the closing price
plt.plot(data["Close"])
plt.title("AAPL Closing Prices")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.show()

# Calculating and plotting the 50-day moving average
ma = data["Close"].rolling(window=50).mean()
plt.plot(data["Close"])
plt.plot(ma)
plt.title("AAPL Moving Average")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend(["Close", "50-Day MA"])
plt.show()

# Calculating and plotting the relative strength index (RSI)
delta = data["Close"].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean().abs()
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))
plt.plot(rsi)
plt.title("AAPL RSI")
plt.xlabel("Date")
plt.ylabel("RSI")
plt.show()


# This code uses the yfinance package to fetch financial data for Apple Inc. for the past 5 years. It then plots the closing price, calculates and plots the 50-day moving average, and calculates and plots the relative strength index (RSI). The graphs are displayed using the matplotlib package.
# Note that you'll need to install the yfinance and matplotlib packages before running this code. You can do this using the following commands: