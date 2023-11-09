"""Common utility functions and classes"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os
import yfinance as yf

def load_ticker_ts_df(ticker, start_date, end_date):
    """
    Load and cache time series financial data from Yahoo Finance API.
    Parameters:
    - ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple Inc.).
    - start_date (str): The start date in 'YYYY-MM-DD' format for data retrieval.
    - end_date (str): The end date in 'YYYY-MM-DD' format for data retrieval.
    Returns:
    - df (pandas.DataFrame): A DataFrame containing the financial time series data.

    """
    dir_path = './data'
    cached_file_path = f'{dir_path}/{ticker}_{start_date}_{end_date}.pkl'
    try:
        if os.path.exists(cached_file_path):
            df = pd.read_pickle(cached_file_path)
        else:
            df = yf.download(ticker, start=start_date, end=end_date)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            df.to_pickle(cached_file_path)
    except FileNotFoundError:
        print(
            f'Error downloading and caching or loading file with ticker: {ticker}')

    return df


def load_ticker_prices_ts_df(tickers, start_date, end_date):
    """Load and cache time series financial data from Yahoo Finance API.

    Parameters:
    - tickers (list): A list of stock ticker symbols (e.g., ['AAPL', 'TSLA'] for Apple and Tesla).
    - start_date (str): The start date in 'YYYY-MM-DD' format for data retrieval. 
    - end_date (str): The end date in 'YYYY-MM-DD' format for data retrieval.

    Returns:
    - df (pandas.DataFrame): A DataFrame containing the financial time series data.
    """
    
    dir_path = './data'
    df = pd.DataFrame()
    for ticker in tickers:
        cached_file_path = f'{dir_path}/{ticker}_{start_date}_{end_date}.pkl'

        try:
            if os.path.exists(cached_file_path):
                temp_df = pd.read_pickle(cached_file_path)
            else:
                temp_df = yf.download(ticker, start=start_date, end=end_date)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                temp_df.to_pickle(cached_file_path)
            temp_df = temp_df.rename(columns={'Adj Close': ticker})[ticker]
            df = pd.concat([df, temp_df], axis=1)
        except Exception as e:
            print(f'Error downloading data for {ticker}: {e}')

    return df

def calculate_profit(signals, prices):
    """
    Calculate cumulative profit based on trading signals and stock prices.
    Parameters:
    - signals (pandas.DataFrame): A DataFrame containing trading signals (1 for buy, -1 for sell).
    - prices (pandas.Series): A Series containing stock prices corresponding to the signal dates.
    Returns:
    - cum_profit (pandas.Series): A Series containing cumulative profit over time.
    """
    profit = pd.Series(index=prices.index)
    profit.fillna(0, inplace=True)

    buys = signals[signals['orders'] == 1].index
    sells = signals[signals['orders'] == -1].index
    skip = 0
    for bi in buys:
        if skip > 0:
            skip -= 1
            continue
        sis = sells[sells > bi]
        if len(sis) > 0:
            si = sis[0]
            profit[si] = prices[si] - prices[bi]
            skip = len(buys[(buys > bi) & (buys < si)])
        else:
            profit[-1] = prices[-1] - prices[bi]
    cum_profit = profit.cumsum()

    return cum_profit


def plot_strategy(prices_df, signal_df, profit):
    """
    Plot a trading strategy with buy and sell signals and cumulative profit.
    Parameters:
    - prices (pandas.Series): A Series containing stock prices.
    - signals (pandas.DataFrame): A DataFrame with buy (1) and sell (-1) signals.
    - profit (pandas.Series): A Series containing cumulative profit over time.
    Returns:
    - ax1 (matplotlib.axes.Axes): The top subplot displaying stock prices and signals.
    - ax2 (matplotlib.axes.Axes): The bottom subplot displaying cumulative profit.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': (3, 1)},
                                   figsize=(24, 12))

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price in $')
    ax1.plot(prices_df.index, prices_df, color='g', lw=0.25)

    # Plot the Buy and Sell signals
    ax1.plot(signal_df.loc[signal_df.orders == 1.0].index,
             prices_df[signal_df.orders == 1.0],
             '^', markersize=12, color='blue', label='Buy')
    ax1.plot(signal_df.loc[signal_df.orders == -1.0].index,
             prices_df[signal_df.orders == -1.0],
             'v', markersize=12, color='red', label='Sell')

    ax2.plot(profit.index, profit, color='b')
    ax2.set_ylabel('Cumulative Profit (%)')
    ax2.set_xlabel('Date')

    return ax1, ax2