import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'stock_data.csv'
df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')


plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Close Price')
plt.title('Stock Price Movement')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()


df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()
df['RSI'] = 100 - (100 / (1 + df['Close'].pct_change().rolling(14).mean() / df['Close'].pct_change().rolling(14).std()))
df['MACD'] = df['Close'].ewm(span=12, adjust=False).mean() - df['Close'].ewm(span=26, adjust=False).mean()

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Close Price', alpha=0.5)
plt.plot(df['SMA_50'], label='50-Day SMA', linestyle='dashed')
plt.plot(df['SMA_200'], label='200-Day SMA', linestyle='dotted')
plt.title('Stock Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

fig, ax = plt.subplots(2, 1, figsize=(12, 8))
ax[0].plot(df['MACD'], label='MACD', color='purple')
ax[0].axhline(0, color='black', linestyle='dashed', linewidth=1)
ax[0].set_title('MACD Indicator')
ax[0].legend()

ax[1].plot(df['RSI'], label='RSI', color='green')
ax[1].axhline(70, color='red', linestyle='dashed', linewidth=1)
ax[1].axhline(30, color='blue', linestyle='dashed', linewidth=1)
ax[1].set_title('Relative Strength Index (RSI)')
ax[1].legend()

plt.tight_layout()
plt.show()

print(df[['Close', 'SMA_50', 'SMA_200', 'RSI', 'MACD']].dropna().tail())
