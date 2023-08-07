import requests
import pandas as pd
import time
import os

# Set the API endpoint and parameters
url = 'https://www.alphavantage.co/query'
params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'MSFT',
    'apikey': 'W0PSPCZ3U1JFB610',
    'outputsize': 'compact'
}

# Set the path and filename for the CSV file
data_dir = './data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
filename = os.path.join(data_dir, 'msft_daily.csv')

# Set the delay time in seconds between API calls (86400 seconds = 1 day)
delay = 86400

while True:
    # Send a request to the API and retrieve the data
    response = requests.get(url, params=params)
    data = response.json()

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.astype(float)
    df = df.sort_index(ascending=True)

    # Save the data to the CSV file
    if not os.path.exists(filename):
        df.to_csv(filename)
    else:
        df.to_csv(filename, mode='a', header=False)

    # Wait for the specified delay time before making the next API call
    time.sleep(delay)
