import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
filename = './data/msft_daily.csv'
df = pd.read_csv(filename, index_col=0, parse_dates=True)

# Plot the data using a line chart
plt.plot(df.index, df['5. adjusted close'])
plt.title('MSFT Daily Adjusted Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.show()