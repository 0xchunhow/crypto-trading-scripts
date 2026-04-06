import pandas as pd

# Load data
df = pd.read_csv("btc_price_data.csv")

# Indicators
df['SMA_50'] = df['close'].rolling(50).mean()
df['SMA_200'] = df['close'].rolling(200).mean()

# Signals
df['signal'] = 0
df.loc[df['SMA_50'] > df['SMA_200'], 'signal'] = 1
df.loc[df['SMA_50'] < df['SMA_200'], 'signal'] = -1

# Returns
df['returns'] = df['close'].pct_change()
df['strategy_returns'] = df['returns'] * df['signal'].shift(1)

# Performance
df['cum_returns'] = (1 + df['strategy_returns']).cumprod()

print("Final Return:", df['cum_returns'].iloc[-1])
