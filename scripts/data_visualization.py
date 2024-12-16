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