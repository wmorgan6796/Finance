from datetime import timedelta, date
import time

def dateRange ():
	start_date = date(1950, 1, 1)
	end_date = date (2015, 9, 12)
	dates = []
	for n in range(int ((end_date - start_date).days)):
		dates.append((start_date + timedelta(n)).strftime("%Y-%m-%d"))
	return dates

