# INF601 - Advance Programming with Python
# Jeramee Oliver
# Mini Project 2

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.


def getClosing(ticker):
    # Get the closing price for the last 10 trading days
    stock = yf.Ticker(ticker)
    # get historical market data
    hist = stock.history(period="10d")

    closingList = []

    for price in hist['Close']:
        closingList.append(round(price, 2))

    return closingList

def printGraph(stock):

    stockClosing = np.array(getClosing(stock))

    days = list(range(1, len(stockClosing) + 1))

    # This plots the graph
    plt.plot(days, stockClosing)

    # Get our min and max for Y
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    # Set our X axis min and max
    # form[xmin, xmax, ymin, ymax]
    plt.axis([1, 10, low_price, high_price])
    # plt.axis([1, 10, low_price-2, high_price+2])

    # Set our labels for the graph
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    # Saves Plot
    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)

    # Finally show the graph
    plt.show()

def getStocks():

    stocks = []

    print("Please enter 5 stocks to graph:")
    for i in range(1, 6):

        while True:
            # it's not a number like in the video tickers are value with letters mostly.
            print("Enter stock ticker value " + str(i))
            ticker = input("> ")
            try:
                stock = yf.Ticker(ticker)
                stock.info
                stocks.append(ticker)
                break
            except:
                print("That is not a valid stock. Please enter another.")

    return stocks


# Start of program
# Create our charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

for stock in getStocks():
    getClosing(stock)
    printGraph(stock)



