import pandas as pd
import matplotlib.pyplot as plt
def calculate_moving_average(data, window):
    # Convert data to a pandas Series if it's not already
    if not isinstance(data, pd.Series):
        data = pd.Series(data)
    
    # Calculate the rolling mean (moving average)
    moving_average = data.rolling(window=window).mean()
    
    return moving_average
# Define the function to plot stock data (assuming it is already defined)
def plot_stock_data(data):
    # Plot the Open price and Moving Average
    plt.figure(figsize=(10, 6))
    plt.plot(data['Open'], label='Open Price', color='blue')
    plt.plot(data['Moving Average'], label=f'Moving Average (window={window})', color='red', linestyle='--')
    plt.title("Stock Data with Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
