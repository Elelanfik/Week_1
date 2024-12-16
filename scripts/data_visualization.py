import matplotlib.pyplot as plt
import seaborn as sns

def plot_univariate(data, column, title=None):
   
    plt.figure(figsize=(6, 4))  # Set figure size
    sns.histplot(data[column], kde=True, bins=30, color='blue')  # Histogram with KDE
    plt.title(title if title else f"Univariate Analysis of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# Function to plot bivariate analysis (assumed to be defined already)
def plot_bivariate(data, x_column, y_column, title=None):
    plt.scatter(data[x_column], data[y_column], color='brown', alpha=0.6)
    plt.title(title if title else f"Bivariate Analysis: {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)


  # Define the function to plot stock data with moving average
def plot_stock_data(data, window, ax):
    # Plot the Open price and Moving Average
    ax.plot(data['Open'], label='Open Price', color='blue')
    ax.plot(data['Moving Average'], label=f'Moving Average (window={window})', color='red', linestyle='--')
    ax.set_title("Stock Data with Moving Average")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()    


# Define the plot function with ma_window as argument
def plot_stock_with_indicators(data, ma_window, rsi_window, title="Stock Data with Indicators"):
    plt.figure(figsize=(10, 8))

    # Plot Closing Price
    plt.subplot(3, 1, 1)
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.title(f"{title} - Close Price")
    plt.legend()

    # Plot Moving Average
    plt.subplot(3, 1, 2)
    plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.6)
    plt.plot(data['Moving Average'], label=f"{ma_window}-Day Moving Average", color='orange')
    plt.title(f"{title} - Moving Average")
    plt.legend()

    # Plot RSI
    plt.subplot(3, 1, 3)
    plt.plot(data['RSI'], label=f"RSI ({rsi_window} Days)", color='green')
    plt.axhline(30, color='red', linestyle='--', label='Oversold (30)')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.title(f"{title} - RSI")
    plt.legend()

    plt.tight_layout()
    plt.show()