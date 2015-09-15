from pymongo import MongoClient
from quandlExample import getHistoricalData
from stockTickerFuncs import listTickers
from Quandl import Quandl

client = MongoClient()
db = client['test_database']

stockTickers = listTickers()

def saveAllHistoricalData():
	numOfTickers = len(stockTickers)
	notFound = []
	count = 0
	for ticker in stockTickers:
		print str(count) + " of " + str(numOfTickers) + " done."
		try:
			print ticker + ": Pulling data..."
			historicalData = getHistoricalData(ticker)
		except Quandl.DatasetNotFound:
			print ticker + ": Data not found"
			tempNotFound = {"TICKER":ticker}
			notFound.append(tempNotFound)
		else:
			print ticker + ": Saving data to database..."
			collection = db['HISTORY_'+ticker]
			collection.insert_many(historicalData)
		if count == 10:
			break
		count+=1
	print notFound
	notFoundCollection = db['TICKER_NOT_FOUND']
	notFoundCollection.insert_many(notFound)

saveAllHistoricalData()