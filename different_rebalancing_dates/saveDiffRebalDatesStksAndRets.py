import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Append the project root to sys.path
project_root = os.path.dirname(os.path.abspath(__file__))  # Current file directory
project_root = os.path.join(project_root, '..')  # Move one level up to the root
sys.path.append(project_root)


import pickle
from definitions.constants import DIFF_REBALANCING_COMBINED_DATA_ALL_PKL, DIFF_REBALANCING_COMBINED_DATA_CSV, DIFF_REBALANCING_RETURNS_ALL_PKL, DIFF_REBALANCING_STOCK_DICT_ALL_PKL, DIFF_REBALANCING_RETURNS_PKL, DIFF_REBALANCING_STOCK_DICT_PKL

# -------------------------------------------------
# Main script for loading, processing, and analyzing data
# -------------------------------------------------

if __name__ == "__main__":
    """
    Entry point for the script. Executes the main function.
    """
    retss=[]
    stks=[]
    picasodfs=[]
    for number in range(18):
        filename=DIFF_REBALANCING_COMBINED_DATA_CSV + str(number) + ".csv"
        df=pd.read_csv(filename)
        picasodfs.append(df)

        stock_dict_filename=DIFF_REBALANCING_STOCK_DICT_PKL + str(number) + ".pkl"
        stk=pd.read_pickle(stock_dict_filename)
        stks.append(stk)

        returns_filename=DIFF_REBALANCING_RETURNS_PKL + str(number) + ".pkl"
        rets=pd.read_pickle(returns_filename)

        rets=pd.DataFrame(rets, columns=['returns'])
        rets.reset_index(inplace=True)
        rets.rename(columns={'index':'t'}, inplace=True)
        rets.set_index('t', inplace=True)
        retss.append(rets)

    dfsfilename=DIFF_REBALANCING_COMBINED_DATA_ALL_PKL
    pd.to_pickle(picasodfs, dfsfilename)

    stock_dict_filename=DIFF_REBALANCING_STOCK_DICT_ALL_PKL
    pd.to_pickle(stks, stock_dict_filename)

    rets_filename=DIFF_REBALANCING_RETURNS_ALL_PKL
    pd.to_pickle(retss, rets_filename)

