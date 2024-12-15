import pandas as pd 
def calculate_moving_average(data, window):
    # Convert data to a pandas Series if it's not already
    if not isinstance(data, pd.Series):
        data = pd.Series(data)
    
    # Calculate the rolling mean (moving average)
    moving_average = data.rolling(window=window).mean()
    
    return moving_average
