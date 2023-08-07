import yfinance as yf
import plotly.graph_objs as go

# Retrieve data from Yahoo Finance API
# company = yf.Ticker("AAPL")
company = yf.Ticker("IBM")
# companypy = yf.Ticker("TSLA")
data = company.history(period="1y")

# ==========
# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data.index,
                                      open=data['Open'],
                                      high=data['High'],
                                      low=data['Low'],
                                      close=data['Close'])])

# Add title and axis labels
fig.update_layout(title="Candlestick Chart",
                   xaxis_title="Date",
                   yaxis_title="Price ($)")

# Display the chart
fig.show()

# ==========
# Create line chart of closing prices
fig = go.Figure(data=go.Scatter(x=data.index,
                                y=data['Close']))

# Add title and axis labels
fig.update_layout(title="Closing Prices",
                   xaxis_title="Date",
                   yaxis_title="Price ($)")

# Display the chart
fig.show()
