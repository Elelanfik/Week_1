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


def plot_univariate(data, column, plot_type="histogram", bins=10, kde=True):
    """
    Generates a univariate plot for a given column in the dataset.
    
    Parameters:
    - data: DataFrame containing the data
    - column: Column name (str) to plot
    - plot_type: Type of plot to create ("histogram", "box", "violin", etc.)
    - bins: Number of bins for histogram (optional)
    - kde: Boolean indicating whether to add a KDE plot (default True)
    """
    plt.figure(figsize=(10, 6))
    
    if plot_type == "histogram":
        sns.histplot(data[column], bins=bins, kde=kde, color="skyblue")
        plt.title(f"Histogram of {column}")
    elif plot_type == "box":
        sns.boxplot(x=data[column], color="lightgreen")
        plt.title(f"Box Plot of {column}")
    elif plot_type == "violin":
        sns.violinplot(x=data[column], color="lightcoral")
        plt.title(f"Violin Plot of {column}")
    else:
        raise ValueError("Unsupported plot type. Choose from 'histogram', 'box', or 'violin'.")
    
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_bivariate(data, column1, column2, plot_type="scatter", corr_method="pearson"):
    """
    Generates a bivariate plot to visualize the relationship between two columns.
    
    Parameters:
    - data: DataFrame containing the data
    - column1: First column name (str)
    - column2: Second column name (str)
    - plot_type: Type of plot to create ("scatter", "heatmap", etc.)
    - corr_method: Correlation method to display in scatter plot (default "pearson")
    """
    plt.figure(figsize=(10, 6))
    
    if plot_type == "scatter":
        sns.scatterplot(x=data[column1], y=data[column2], color="darkblue")
        plt.title(f"Scatter Plot of {column1} vs {column2}")
        plt.xlabel(column1)
        plt.ylabel(column2)
        
        # Display correlation
        correlation = data[[column1, column2]].corr(method=corr_method).iloc[0, 1]
        plt.figtext(0.15, 0.85, f"Correlation ({corr_method}): {correlation:.2f}", fontsize=12)
    
    elif plot_type == "heatmap":
        correlation_matrix = data[[column1, column2]].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
        plt.title(f"Correlation Heatmap of {column1} and {column2}")
        
    else:
        raise ValueError("Unsupported plot type. Choose from 'scatter' or 'heatmap'.")
    
    plt.show()

# Univariate Visualization: Histogram
def plot_histogram(data, column, bins=30, color='blue'):
    """
    Plots a histogram for a single column.

    Parameters:
    - data: pandas DataFrame containing the data.
    - column: str, name of the column to plot.
    - bins: int, number of bins for the histogram (default: 30).
    - color: str, color of the histogram (default: 'blue').
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], bins=bins, color=color, kde=True)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

# Bivariate Visualization: Scatter Plot
def plot_scatter(data, x_column, y_column, color='blue', alpha=0.7):
    """
    Plots a scatter plot between two columns.

    Parameters:
    - data: pandas DataFrame containing the data.
    - x_column: str, name of the column for the x-axis.
    - y_column: str, name of the column for the y-axis.
    - color: str, color of the points (default: 'blue').
    - alpha: float, transparency of the points (default: 0.7).
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x=x_column, y=y_column, color=color, alpha=alpha)
    plt.title(f"Scatter Plot of {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    plt.show()

# Univariate Visualization: Box Plot
def plot_box(data, column, color='blue'):
    """
    Plots a box plot for a single column.

    Parameters:
    - data: pandas DataFrame containing the data.
    - column: str, name of the column to plot.
    - color: str, color of the box plot (default: 'blue').
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data, y=column, color=color)
    plt.title(f"Box Plot of {column}")
    plt.ylabel(column)
    plt.grid(True)
    plt.show()

# Bivariate Visualization: Heatmap
def plot_heatmap(data, columns=None):
    """
    Plots a heatmap for the correlation matrix of the selected columns.

    Parameters:
    - data: pandas DataFrame containing the data.
    - columns: list of str, columns to include in the heatmap (default: None, uses all columns).
    """
    if columns:
        corr = data[columns].corr()
    else:
        corr = data.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()


