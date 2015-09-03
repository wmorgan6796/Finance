from pymongo import MongoClient
import time
from yahoo_finance import Share, Currency

client = MongoClient()
db = client['test_database']
collection = db['tickerInfo']

stockTickers = []

with open('nasdaqlisted.txt', 'r') as f1:
	for line in f1:
		ticker = line.split("|")[0]
		name = line.split("|")[1].split(" - ")[0]
		tempStock = {"ticker": ticker, "name":name}
		stockTickers.append(tempStock)
		if ticker == "ZYNE":
			break

sortedStockTickers = sorted(stockTickers, key=lambda k: k['ticker'])
# collection.insert_many(sortedStockTickers)

currentDate = time.strftime("%Y-%m-%d")

# collection = db['HISTORICAL_DATA']

# for stock in sortedStockTickers:
# 	tempStock = Share(stock["ticker"])
# 	histoy = tempStock.get_historical

tempStock = Share("AAPL")
print tempStock.get_historical('1990-01-01', currentDate)