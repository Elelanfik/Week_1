import pandas as pd
import talib
import matplotlib.pyplot as plt
def calculate_moving_average(data, window):
    # Convert data to a pandas Series if it's not already
    if not isinstance(data, pd.Series):
        data = pd.Series(data)
    
    # Calculate the rolling mean (moving average)
    moving_average = data.rolling(window=window).mean()
    
    return moving_average

# Function to calculate Moving Average
def calculate_moving_averagetalib(data, window):
    return talib.SMA(data, timeperiod=window)

# Function to calculate RSI (Relative Strength Index)
def calculate_rsi(data, window):
    return talib.RSI(data, timeperiod=window)

# Function to calculate MACD (Moving Average Convergence Divergence)
def calculate_macd(data):
    macd, macdsignal, macdhist = talib.MACD(data, fastperiod=12, slowperiod=26, signalperiod=9)
    return macd, macdsignal, macdhist

 
