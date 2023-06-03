# Overview

I wanted to create a script with Python and Pandas to analyze stock data. 

The dataset I found includes historical data from MarketWatch. It spans one year and includes prices for open, high, low, close as well as  overall volume.

[GOOG.csv](https://www.marketwatch.com/investing/stock/goog/download-data?mod=mw_quote_tab)

As part of my research, I wanted to figure out a longer term solution to get information. I created several test scripts that could scrape the web. I was able to find specific information and save the results to a file as csv, html, json.

I was really curious to see if there was a calculation I could implement that would predict the future price of a given stock. As part of this project, I learned to make a request for a webpage and search the page for specific data. I also learned to create files from the data and make graphs.

[Software Demo Video](https://blackadder-git.github.io/byui/cse310/stockmarket)

# Data Analysis Results

* The first question I asked to was to find the mean of the Open, High, Low and Close
* The second question I asked was how many days did stock trade with a volume greater than 30,000,000

# Development Environment
* Visual Studio Code 1.78.2

# Programing language and libraries
* Python 3.11.3
* Pandas 2.02
* Numpy 1.24.3
* Python-dateutil 2.8.2
* Pytz 2023.3
* Six 1.1.0
* Tzdata 2023.3
* Matplotlib
* BeautifulSoup 4.12.2
* Requests 2.31.0

# Useful Websites
* [Creation of virtual enviroments](https://docs.python.org/3/library/venv.html)
* [Using Python environments](https://code.visualstudio.com/docs/python/environments)
* [Guide to Python Virtual Environment](https://www.youtube.com/watch?v=KxvKCSwlUv8)
* [Pandas Datareader](https://thecleverprogrammer.com/2021/03/22/pandas-datareader-using-python-tutorial/)

# Future Work

* implement machine learning to estimate the future direction of a given stock
* look for a way to determine whether a stock is overvalued or undervalued