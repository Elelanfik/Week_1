import matplotlib.pyplot as plt
import seaborn as sns

def plot_stock_data(data):
    """
    Plot stock data including the Moving Average.

    Args:
    - data (pd.DataFrame): Stock data with 'Date', 'Close', and 'Moving Average'.

    Returns:
    - A plot displaying Close Price and Moving Average.
    """
    plt.figure(figsize=(12, 6))  # Define the figure size
    
    # Plot Close Price
    plt.plot(data['Date'], data['Close'], label='Close Price', color='blue', linewidth=2)
    
    # Plot Moving Average
    plt.plot(data['Date'], data['Moving Average'], label='Moving Average', color='red', linewidth=2)
    
    # Add labels and title
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Stock Price with Moving Average")
    
    # Add grid, legend, and display
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_univariate(data, column, title=None):
   
    plt.figure(figsize=(8, 6))  # Set figure size
    sns.histplot(data[column], kde=True, bins=30, color='blue')  # Histogram with KDE
    plt.title(title if title else f"Univariate Analysis of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_bivariate(data, x_column, y_column, title=None):

    plt.figure(figsize=(8, 6))  # Set figure size
    plt.scatter(data[x_column], data[y_column], color='brown', alpha=0.6)
    plt.title(title if title else f"Bivariate Analysis: {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
