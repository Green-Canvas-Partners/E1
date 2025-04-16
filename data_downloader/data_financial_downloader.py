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


from definitions.constants_V import DATA_L1_TICKERS_REFINED, L1_TICKERS, API_KEY_EODHD
from utils.custom import update_data, update_dividend_data, earning_data_downloader, divident_data_downloader, shares_outstanding_data_downloader


""" Download EPS data from eodhd.com , Now here are problems the tickers names here 
are not completely matching with the tickers names in the polygon api, we will deal that 
for now we have include all the tickers name we have including meta in it."""



"""Below are the all functions for downloading the financial data from eodhd.com, including
Earnings data, Divident, shares outstanding."""

earning_data_downloader(L1_TICKERS,API_KEY_EODHD)
divident_data_downloader(L1_TICKERS)
shares_outstanding_data_downloader(L1_TICKERS,API_KEY_EODHD)


df = DATA_L1_TICKERS_REFINED
# print('y')
update_data('shares_outstanding_data_250_testing.pkl', df, 'updated_shares_outstanding_data_250.pkl')
update_data('eps_data_testing.pkl', df, 'updated_eps_data.pkl')
update_dividend_data('dividend_dataAAAAA.pkl', df, 'updated_dividend_data.pkl')