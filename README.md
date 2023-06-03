# Overview

I wanted to create a script with Python and Pandas to analyze stock data. 

The dataset I found includes historical data from MarketWatch. It spans one year and includes prices for open, high, low, close as well as  overall volume.

[GOOG.csv](https://www.marketwatch.com/investing/stock/goog/download-data?mod=mw_quote_tab)

I was curious to see if there was a calculation I could implement that would predict the future price of a given stock. As part of my research, I learned to make a request for a webpage and search the page for specific data. I also learned to create files from the data, setup a virtual python enviroment and also make graphs.

[Software Demo Video](https://blackadder-git.github.io/byui/cse310/stockmarket)

# Data Analysis Results

* The first question I asked was how to get the mean of the Open, High, Low and Close. 
  * Answer: $103.91, $105.48, $102.7, $104.12
* The second question I asked was how many days did stock trade with a volume greater than 30,000,000. 
  * Answer: 77
* The third question I asked was how to sum the data in open. 
  * Answer: $26184.92

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
* [Python Doc](https://docs.python.org/3/)
* [Creation of virtual enviroments](https://docs.python.org/3/library/venv.html)
* [Using Python environments](https://code.visualstudio.com/docs/python/environments)
* [Guide to Python Virtual Environment](https://www.youtube.com/watch?v=KxvKCSwlUv8)
* [Data Science in VS Code tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial)

# Future Work
* implement machine learning to estimate the future direction of a given stock
* look for a way to determine whether a stock is overvalued or undervalued