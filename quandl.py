from Quandl import Quandl
import pandas as pd
from dateIteration import dateRange

authtoken = "WBgHDMPaAsQ_FMPGo-NH" # Quandl API Key: WBgHDMPaAsQ_FMPGo-NH
stockHeaders = ["Open", "High", "Low", "Close", "Volume", "Adjusted Close"]
dates = dateRange() #Starts in 1990-1-1

def getHistoricalData(ticker):
	onlineData = Quandl.get("YAHOO/" + ticker, authtoken = authtoken, collapse='daily')
	localData = []
	for i in dates:
		singleDayData = {'Date': i}
		for j in stockHeaders:
			try:
				singleDayData[j] = str(onlineData.loc[i, j])
			except KeyError:
				# print "The date " + i + " has no data."
				break
		else:
			localData.append(singleDayData)
	return localData