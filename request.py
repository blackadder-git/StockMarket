import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
url = 'https://www.marketwatch.com/investing/stock/goog'
response = requests.get(url)

# create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# write response to file
# with open("data/test.txt", "w") as f:
#    f.write(response.text)

# open file
# find data by class: company__name, company__ticker, table__cell u-semi
companyName = soup.find_all("h1", {"class": "company__name"})
for name in companyName:
    # is there a way to get find just one element?
    print(f"company name: {name.get_text()}")

companyTicker = soup.find_all("span", {"class": "company__ticker"})
for ticker in companyTicker:
    # is there a way to get find just one element?
    print(f"company ticker: {ticker.get_text()}")

stockClose = soup.find_all("td", {"class": "table__cell u-semi"})
for close in stockClose:
    # is there a way to get find just one element?
    print(f"stock close: {close.get_text()}")

# TODO: create a list with different stock symbols, scape the web and build a dataset with different values
# this script to process, below is a sample of how I would build the dataset and save it to disk

#rowNames = ['Tom', 'Bombadil']
#rowTickers = ['T', 'B']
#rowCloses = ['3.9', '2.3']

# TODO: add this to a loop
rowNames = []
rowNames.append('Tom')
rowNames.append('Bombadil')
rowNames.append('Saruman')

rowTickers = []
rowTickers.append('T')
rowTickers.append('B')
rowTickers.append('S')

rowCloses = []
rowCloses.append('3.9')
rowCloses.append('2.9')
rowCloses.append('1.9')

newdf = pd.DataFrame({'Name' : rowNames,
                     'Ticker' : rowTickers,
                     'Close' : rowCloses})

print(newdf)

newdf.to_csv("stocks.csv")
newdf.to_json("stocks.json")
newdf.to_html("stocks.html")
"""

# TODO: iterate files in a directory, this would wrap the code that scrapes and reads data into the code above
# find next after text: P/E Ratio
# import required module
import os
# assign directory
directory = 'data'
 
# iterate over files in a directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)