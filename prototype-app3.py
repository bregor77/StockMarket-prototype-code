import requests
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import schedule
import time

def download_data():
    # Set the API endpoint and parameters
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': 'MSFT',
        'apikey': 'W0PSPCZ3U1JFB610',
        'outputsize': 'compact'
    }

    # Send a request to the API and retrieve the data
    response = requests.get(url, params=params)
    data = response.json()

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.astype(float)
    df = df.sort_index(ascending=True)

    # Save the data to a CSV file with the date as the filename
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    filename = f"MSFT_daily_adjusted_closing_prices_{date}.csv"
    df.to_csv(filename)


    # Plot the data using a line chart
    plt.plot(df.index, df['5. adjusted close'])
    plt.title('MSFT Daily Adjusted Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.show()

def job():
    print("Downloading data...")
    download_data()

# Schedule the job to run every day at a specified time
schedule.every().day.at("13:58").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
