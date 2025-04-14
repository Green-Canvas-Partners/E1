import pandas as pd
import multiprocessing
import pickle
import yfinance as yf
import sys
import os
import time

project_root = os.path.dirname(os.path.abspath(__file__))  # Current file directory
project_root = os.path.join(project_root, '..')  # Move one level up to the root
sys.path.append(project_root)


from definitions.constants import *




""" Download EPS data from eodhd.com , Now here are problems the tickers names here 
are not completely matching with the tickers names in the polygon api, we will deal that 
for now we have include all the tickers name we have including meta in it."""



"""Below are the all functions for downloading the financial data from eodhd.com, including
Earnings data, Divident, shares outstanding."""
def earning_data_downloader(tickers,api_key):
    
    stocks = tickers
    api_token = api_key
    
    
    # Dictionary to store EPS data for each stock
    eps_data_dict = {}

    for stock in stocks:
        ticker = f"{stock}.US"  # Add '.US' to the stock name for API
        url = f"https://eodhd.com/api/fundamentals/{ticker}?api_token={api_token}&fmt=json"
        try:
            response = requests.get(url)
            data = response.json()

            # Extract EPS history
            if "Earnings" in data and "History" in data["Earnings"]:
                eps_data = data["Earnings"]["History"]
                eps_records = [
                    {
                        "reportDate": record["reportDate"],
                        "epsActual": record["epsActual"],
                    }
                    for record in eps_data.values()
                ]

                # Convert to a DataFrame and store it
                eps_df = pd.DataFrame(eps_records).sort_values(by="reportDate", ascending=False)
                eps_data_dict[stock] = eps_df
        except Exception as e:
            print(f"Failed to fetch data for {stock}: {e}")
        
    with open('eps_data_testing.pkl', 'wb') as file:
        pickle.dump(eps_data_dict, file)


    return eps_data_dict


def divident_data_downloader(tickers,api_key):

    dividend_data = {}

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        try:
            dividends = stock.dividends  # Fetch historical dividend data
            dividends.index = dividends.index.tz_localize(None)
            dividend_data[ticker] = dividends  # Store in dictionary
            print(f"Fetched dividends for {ticker}")
        except Exception as e:
            print(f"Failed to fetch data for {ticker}: {e}")

    # Save the data to a pickle file
    with open('dividend_dataAAAAA.pkl', 'wb') as file:
        pickle.dump(dividend_data, file)

    return dividend_data


def shares_outstanding_data_downloader(tickers,api_key):

        # Dictionary to store data for each ticker
    shares_data = {}
    for ticker in tickers:
        # Define the URL for fundamental data
        url = f'https://eodhistoricaldata.com/api/fundamentals/{ticker}.US'

        # Parameters
        params = {
            'api_token': api_key,
        }

        # Fetch data
        response = requests.get(url, params=params)

        # Check if response is valid
        if response.status_code == 200:
            data = response.json()

            # Extract quarterly shares outstanding data
            shares_outstanding_data = data.get('outstandingShares', {}).get('quarterly', {}).values()

            # Convert to DataFrame if data is available
            if shares_outstanding_data:
                df = pd.DataFrame(shares_outstanding_data)

                # Use 'dateFormatted' as date and 'shares' as Shares Outstanding
                df = df[['dateFormatted', 'shares']].rename(columns={'dateFormatted': 'Date', 'shares': 'Shares Outstanding'})

                # Convert 'Date' column to datetime format
                df['Date'] = pd.to_datetime(df['Date'])

                # Sort DataFrame by date
                df.sort_values(by='Date', inplace=True)

                # Reset index
                df.reset_index(drop=True, inplace=True)

                # Convert 'Shares Outstanding' to integer
                df['Shares Outstanding'] = df['Shares Outstanding'].astype(int)

                # Store the DataFrame in the dictionary
                shares_data[ticker] = df
    #             print(f"AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH {ticker}")
            else:
                print(f"No shares outstanding data found for {ticker}")
        else:
            print(f"Failed to fetch data for {ticker}")

    # Save the data to a pickle file
    with open('shares_outstanding_data_250_testing.pkl', 'wb') as f:
        pickle.dump(shares_data, f)

    print("Data saved to 'shares_outstanding_data_250.pkl'")
    return shares_data


