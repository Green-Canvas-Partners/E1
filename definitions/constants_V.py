from datetime import datetime, timedelta
import os

# Root directories
ROOT_DIR = '/home/iyad/V1_DIR'
DATA_DIR_V = os.path.join(ROOT_DIR, 'data_V')

# single run dirs
SINGLE_RUN_DIR_V = os.path.join(DATA_DIR_V, 'single_run')
SINGLE_RUN_BONDS_DIR_V = os.path.join(SINGLE_RUN_DIR_V, 'bonds')
SINGLE_RUN_STOCKS_DIR_V = os.path.join(SINGLE_RUN_DIR_V, 'stocks')
SINGLE_RUN_COMBINED_DIR_V = os.path.join(SINGLE_RUN_DIR_V, 'combined')

# diff rebalancing dirs
DIFF_REBALANCING_DIR_V = os.path.join(DATA_DIR_V, 'different_rebalancing_dates')
DIFF_REBALANCING_BONDS_DIR_V = os.path.join(DIFF_REBALANCING_DIR_V, 'bonds')
DIFF_REBALANCING_STOCKS_DIR_V = os.path.join(DIFF_REBALANCING_DIR_V, 'stocks')
DIFF_REBALANCING_COMBINED_DIR_V = os.path.join(DIFF_REBALANCING_DIR_V, 'combined')
DIFF_REBALANCING_PICASSO_DIR_V = os.path.join(DIFF_REBALANCING_DIR_V, 'picasso')

# sensitivity dirs
SENSITIVITY_DIR_V = os.path.join(DATA_DIR_V, 'sensitivity_analysis')
SENSITIVITY_BONDS_DIR_V = os.path.join(SENSITIVITY_DIR_V, 'bonds')
SENSITIVITY_STOCKS_DIR_V = os.path.join(SENSITIVITY_DIR_V, 'stocks')
SENSITIVITY_COMBINED_DIR_V = os.path.join(SENSITIVITY_DIR_V, 'combined')

# GS dirs
GS_DIR_V = os.path.join(DATA_DIR_V, 'grid_search')
GS_BONDS_DIR_V = os.path.join(GS_DIR_V, 'bonds')
GS_STOCKS_DIR_V = os.path.join(GS_DIR_V, 'stocks')
GS_COMBINED_DIR_V = os.path.join(GS_DIR_V, 'combined')

# Create directories if they do not exist
dirs_to_create = [
    SINGLE_RUN_DIR_V, SINGLE_RUN_BONDS_DIR_V, SINGLE_RUN_STOCKS_DIR_V, SINGLE_RUN_COMBINED_DIR_V,
    DIFF_REBALANCING_DIR_V, DIFF_REBALANCING_BONDS_DIR_V, DIFF_REBALANCING_STOCKS_DIR_V, DIFF_REBALANCING_COMBINED_DIR_V, DIFF_REBALANCING_PICASSO_DIR_V,
    SENSITIVITY_DIR_V, SENSITIVITY_BONDS_DIR_V, SENSITIVITY_STOCKS_DIR_V, SENSITIVITY_COMBINED_DIR_V,
    GS_DIR_V, GS_BONDS_DIR_V, GS_STOCKS_DIR_V, GS_COMBINED_DIR_V
]

for directory in dirs_to_create:
    if not os.path.exists(directory):
        os.makedirs(directory)

# single run
# Paths for returns and stock dicts and year stocks in single run
SINGLE_RUN_LIVE_STOCK_DICT_PKL_V = os.path.join(SINGLE_RUN_DIR_V, 'stock_dict_for_live.pkl')
SINGLE_RUN_STOCK_DICT_PKL_V = os.path.join(SINGLE_RUN_DIR_V, 'stock_dict.pkl')

SINGLE_RUN_YEARSTOCKS_PKL_V = os.path.join(SINGLE_RUN_DIR_V, 'stockstobeused1.pkl')
SINGLE_RUN_YEARSTOCKS_LIVE_PKL_V = os.path.join(SINGLE_RUN_DIR_V, 'stockstobeused1_for_live.pkl')
SINGLE_RUN_RETURNS_PKL_V = os.path.join(SINGLE_RUN_DIR_V, 'returns.pkl')
SINGLE_RUN_LIVE_RETURNS_PKL_V = os.path.join(SINGLE_RUN_DIR_V, 'returns_for_live.pkl')
# Paths for bond data in single run
SINGLE_RUN_BONDS_DATA_RAW_PKL_V = os.path.join(SINGLE_RUN_BONDS_DIR_V, 'bonds_data.pkl')
SINGLE_RUN_BONDS_DATA_RAW_LIVE_PKL_V = os.path.join(SINGLE_RUN_BONDS_DIR_V, 'bonds_data_for_live.pkl')
SINGLE_RUN_BONDS_DATA_ENRICHED_CSV_V = os.path.join(SINGLE_RUN_BONDS_DIR_V, 'dummy1_return_bonds.csv')
SINGLE_RUN_BONDS_DATA_ENRICHED_LIVE_CSV_V = os.path.join(SINGLE_RUN_BONDS_DIR_V, 'dummy1_return_bonds_for_live.csv')

# Paths for stock data in single run
SINGLE_RUN_STOCKS_DATA_ENRICHED_CSV_V = os.path.join(SINGLE_RUN_STOCKS_DIR_V, 'dummy1_final.csv')
SINGLE_RUN_STOCKS_DATA_ENRICHED_LIVE_CSV_V = os.path.join(SINGLE_RUN_STOCKS_DIR_V, 'dummy1_final_for_live.csv')

# Paths for combined data in single run
SINGLE_RUN_COMBINED_DATA_CSV_V = os.path.join(SINGLE_RUN_COMBINED_DIR_V, 'dummy1_return_bonds_stocks_forPicasso.csv')
SINGLE_RUN_COMBINED_DATA_LIVE_CSV_V = os.path.join(SINGLE_RUN_COMBINED_DIR_V, 'dummy1_return_bonds_stocks_forPicasso_for_live.csv')

# Different rebalancing dates

# Paths for returns and stock dicts and year stocks in bonds
DIFF_REBALANCING_STOCK_DICT_PKL_V = os.path.join(DIFF_REBALANCING_DIR_V, 'stock_dict') # + str(number) + ".pkl" to be appended in file 
DIFF_REBALANCING_STOCK_DICT_ALL_PKL_V = os.path.join(DIFF_REBALANCING_DIR_V, 'stock_dict.pkl')

DIFF_REBALANCING_RETURNS_PKL_V = os.path.join(DIFF_REBALANCING_DIR_V, 'returns') # + str(number) + ".pkl" to be appended in file
DIFF_REBALANCING_RETURNS_ALL_PKL_V = os.path.join(DIFF_REBALANCING_DIR_V, 'returns.pkl')

# Paths for combined data in different rebalancing dates
DIFF_REBALANCING_COMBINED_DATA_CSV_V = os.path.join(DIFF_REBALANCING_COMBINED_DIR_V, 'dummy1_return_bonds_stocks_forPicasso') # + str(number) + ".csv" to be appended in file
DIFF_REBALANCING_COMBINED_DATA_ALL_PKL_V = os.path.join(DIFF_REBALANCING_COMBINED_DIR_V, 'dummy1_return_bonds_stocks_forPicasso.pkl')

# Paths for bond data in different rebalancing dates
DIFF_REBALANCING_BONDS_DATA_RAW_PKL_V = os.path.join(DIFF_REBALANCING_BONDS_DIR_V, 'bonds_data.pkl')
DIFF_REBALANCING_BONDS_DATA_ENRICHED_CSV_V = os.path.join(DIFF_REBALANCING_BONDS_DIR_V, 'dummy1_return_bonds') # + str(number) + ".csv" to be appended in file

# Paths for stock data in different rebalancing dates
DIFF_REBALANCING_STOCKS_DATA_ENRICHED_CSV_V = os.path.join(DIFF_REBALANCING_STOCKS_DIR_V, 'dummy1_final') # + str(number) + ".csv" to be appended in file


# Paths for sensitivity analysis
SENSITIVITY_BONDS_DATA_ENRICHED_CSV_V = os.path.join(SENSITIVITY_BONDS_DIR_V, 'dummy1_return_bonds.csv')
SENSITIVITY_BONDS_DATA_RAW_PKL_V = os.path.join(SENSITIVITY_BONDS_DIR_V, 'bonds_data.pkl')

SENSITIVITY_STOCKS_DATA_ENRICHED_CSV_V = os.path.join(SENSITIVITY_STOCKS_DIR_V, 'dummy1_final.csv')
SENSITIVITY_COMBINED_DATA_CSV_V = os.path.join(SENSITIVITY_COMBINED_DIR_V, 'dummy1_return_bonds_stocks_forPicasso.csv')

# Paths for grid search
GS_ITS_V=os.path.join(GS_DIR_V, 'its.pkl')
GS_RES_V=os.path.join(GS_DIR_V,'gs_df.csv')

GS_BONDS_DATA_ENRICHED_CSV_V = os.path.join(GS_BONDS_DIR_V, 'dummy1_return_bonds.csv')
GS_BONDS_DATA_RAW_PKL_V = os.path.join(GS_BONDS_DIR_V, 'bonds_data.pkl')
GS_STOCKS_DATA_ENRICHED_CSV_V = os.path.join(GS_STOCKS_DIR_V, 'dummy1_final.csv')


DV_QUANTILE_THRESHOLD_MAKE_YS=[0.05, 0.2, 0.33, 0.5, 0.66, 0.75, 0.9]
SELECTED_TOP_VOL_STOCKS_MAKE_YS=[11]#, 20, 27, 35, 40, 50, 75, 100, 125, 150, 200

# GS
DATE_GS_CUTOFF='2018-01-01'
MOMENTUM_WINDOWS_GS = [30, 63, 90, 126, 150, 200, 252, 504]#
HALF_LIVES_GS = [30, 63, 90, 126, 150, 200, 250]#
SELECTED_N_STOCK_POSITIVE_GS=[1,3,5,7,11,15,25,50,75,100]#
SELECTED_N_STOCK_CHOSE_GS=[1,3,5,7,10,16,21,25,30,50]#
EXP_WEIGHT_GS=[0.5, 0.7, 0.85, 0.95, 0.9999999999]

#  SENS
DATES_SENS=[DATE_GS_CUTOFF, '2025-01-01']
DV_QUANTILE_THRESHOLD_SENS=[0.05, 0.2, 0.33, 0.5, 0.66, 0.75, 0.9]#
SELECTED_TOP_VOL_STOCKS_SENS=[11, 20, 27, 35, 40, 50, 75, 100, 125, 150, 200]#10,  
MOMENTUM_WINDOWS_SENS=[[30], [63], [90], [126], [150], [200], [252], [504]]#
HALF_LIVES_SENS=[[30], [63], [90], [126], [150], [200], [250]]#
SELECTED_N_STOCK_POSITIVE_SENS=[7, 8, 9, 10, 11]#30, 37, 45, 50, 55, 60
SELECTED_N_STOCK_CHOSE_SENS=[1, 2, 3, 4, 5, 6, 7, 8, 9]#, 13, 15, 20, 
EXP_WEIGHT_SENS=[0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.9999999999]

SENS_PARAMETER_CONFIG = {
    'dvqt': {
        'anrets': ('Annual Returns', 'Annual Return', 'blue'),
        'sharpes': ('Sharpe Ratios', 'Sharpe Ratio', 'green'),
        'maxdraws': ('Maximum Drawdowns', 'Max Drawdown', 'red'),
        'calmars': ('Calmar Ratios', 'Calmar Ratio', 'cyan'),
        'sortinos': ('Sortino Ratios', 'Sortino Ratio', 'magenta')
    },
    'topvolstocks': {
        'anrets': ('Annual Returns', 'Annual Return', 'blue'),
        'sharpes': ('Sharpe Ratios', 'Sharpe Ratio', 'green'),
        'maxdraws': ('Maximum Drawdowns', 'Max Drawdown', 'red'),
        'calmars': ('Calmar Ratios', 'Calmar Ratio', 'cyan'),
        'sortinos': ('Sortino Ratios', 'Sortino Ratio', 'magenta')
    },
    'exp_weight': {
        'anrets': ('Annual Returns', 'Annual Return', 'blue'),
        'sharpes': ('Sharpe Ratios', 'Sharpe Ratio', 'green'),
        'maxdraws': ('Maximum Drawdowns', 'Max Drawdown', 'red'),
        'calmars': ('Calmar Ratios', 'Calmar Ratio', 'cyan'),
        'sortinos': ('Sortino Ratios', 'Sortino Ratio', 'magenta')
    },
    'n_stock_chose': {
        'anrets': ('Annual Returns', 'Annual Return', 'blue'),
        'sharpes': ('Sharpe Ratios', 'Sharpe Ratio', 'green'),
        'maxdraws': ('Maximum Drawdowns', 'Max Drawdown', 'red'),
        'calmars': ('Calmar Ratios', 'Calmar Ratio', 'cyan'),
        'sortinos': ('Sortino Ratios', 'Sortino Ratio', 'magenta')
    },
    'n_stock_positive': {
        'anrets': ('Annual Returns', 'Annual Return', 'blue'),
        'sharpes': ('Sharpe Ratios', 'Sharpe Ratio', 'green'),
        'maxdraws': ('Maximum Drawdowns', 'Max Drawdown', 'red'),
        'calmars': ('Calmar Ratios', 'Calmar Ratio', 'cyan'),
        'sortinos': ('Sortino Ratios', 'Sortino Ratio', 'magenta')
    },
    'mom_window': {
        'anrets': ('Annual Returns (Momentum Window)', 'Annual Return', 'blue'),
        'sharpes': ('Sharpe Ratios (Momentum Window)', 'Sharpe Ratio', 'green'),
        'maxdraws': ('Max Drawdowns (Momentum Window)', 'Max Drawdown', 'red'),
        'calmars': ('Calmar Ratios (Momentum Window)', 'Calmar Ratio', 'cyan'),
        'sortinos': ('Sortino Ratios (Momentum Window)', 'Sortino Ratio', 'magenta')
    },
    'half_life': {
        'anrets': ('Annual Returns (Half Life)', 'Annual Return', 'blue'),
        'sharpes': ('Sharpe Ratios (Half Life)', 'Sharpe Ratio', 'green'),
        'maxdraws': ('Max Drawdowns (Half Life)', 'Max Drawdown', 'red'),
        'calmars': ('Calmar Ratios (Half Life)', 'Calmar Ratio', 'cyan'),
        'sortinos': ('Sortino Ratios (Half Life)', 'Sortino Ratio', 'magenta')
    }
}

# Exclusions and thresholds
DV_QUANTILE_THRESHOLD_V = 0.33

# Momentum and half-life settings
MOMENTUM_WINDOWS_V = [252] #30, 63, 90, 126, 150, 200, 252, 504
HALF_LIVES_V = [150] #30, 42, 63, 90, 126, 150, 200, 250
MULT_V = [1.01] #1.01, 1.5, 2.0, 4.0, 6.0
WEIGHT_V = [0.9] #0.1, 0.5, 0.9

# Selection criteria
SELECTED_TOP_VOL_STOCKS_V = 25
SELECTED_MOM_WINDOW_V = 252
SELECTED_HALF_LIFE_WINDOW_V = 150
SELECTED_N_STOCK_POSITIVE_V = 15
SELECTED_N_STOCK_CHOSE_V = 10
EXP_WEIGHT_V = 0.7
SELECTED_MULT_V = 1.01
SELECTED_WEIGHT_V = 0.9