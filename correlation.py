# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:57:26 2023

@author: nchin
"""

import yfinance as yf
import pandas as pd


# create list of stocks
# tickers = ["AMZN", "MSFT", "GOOG", "D05.SI", "BABA" ]
tickers = [
    "AAPL", "TSLA", "NFLX", "META", "AMZN", "GOOGL", "MSFT", "D05.SI", "BABA", "GOOG",
    "NVDA", "AMD", "JPM", "V", "MA", "DIS", "WMT", "COST", "IBM", "INTC",
    "PFE", "JNJ", "GE", "C", "XOM", "KO", "PEP", "MCD", "BA", "GS"
]

ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period="3mo", interval="1d")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp


adj_close_data = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in ohlcv_data.items()})
adj_close_data
correlation_matrix = adj_close_data.corr()
covariance_matrix =  adj_close_data.cov()

print(correlation_matrix)
print(covariance_matrix)


# Set the correlation threshold
correlation_threshold = 0.7

# Find pairs with correlation greater than or equal to the threshold
high_correlation_pairs = []

for i in range(len(correlation_matrix.columns)):
    for j in range(i + 1, len(correlation_matrix.columns)):
        if correlation_matrix.iloc[i, j] >= correlation_threshold:
            ticker1 = correlation_matrix.columns[i]
            ticker2 = correlation_matrix.columns[j]
            correlation_value = correlation_matrix.iloc[i, j]
            high_correlation_pairs.append((ticker1, ticker2, correlation_value))

# Print the pairs with high correlation
for pair in high_correlation_pairs:
    print(f"High correlation ({pair[2]}): {pair[0]} and {pair[1]}")
    # print(f"High correlation ({correlation_matrix.loc[pair[0], pair[1]]}): {pair[0]} and {pair[1]}")


