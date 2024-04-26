import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    ax = plt.axes()
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    
    # Create first line of best fit
    slope1, intercept1, r_val1, p_val1, slope_std_err = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x_fit1 = list(range(1880, 2051))
    y_fit1 = [(intercept1 + slope1 * year) for year in x_fit1]
    plt.plot(x_fit1, y_fit1, 'r', label="Line of best fit 1")

    # Create second line of best fit
    fit_frame = df[df['Year'] >= 2000]
    slope2, intercept2, r_val2, p_val2, slope_std_err = linregress(x=fit_frame['Year'], y=fit_frame['CSIRO Adjusted Sea Level'])
    
    x_fit2 = list(range(2000,2051))
    y_fit2 = [(intercept2 + slope2 * year) for year in x_fit2]
    plt.plot(x_fit2, y_fit2, 'b', label="Line of best fit 2")
    plt.legend()

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()