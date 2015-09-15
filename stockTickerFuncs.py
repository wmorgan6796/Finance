def listTickers():
	stockTickers = []
	with open('nasdaqlisted.txt', 'r') as f1:
		for line in f1:
			ticker = line.split("|")[0]
			stockTickers.append(ticker)
		else:
			del stockTickers[0]
			del stockTickers[-1]
	return stockTickers