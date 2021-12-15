import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    res = linregress(x,y)
    x1 = pd.Series([i for i in range(1880,2051)])
    y1 = res.slope*x1 + res.intercept
    plt.plot(x1, y1, 'g')

    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]
    x2 = df_2000['Year']
    y2 = df_2000['CSIRO Adjusted Sea Level']

    res2 = linregress(x2,y2)
    x3 = pd.Series([i for i in range(2000,2051)])
    y3 = res2.slope*x3 + res2.intercept
    plt.plot(x3, y3, 'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()