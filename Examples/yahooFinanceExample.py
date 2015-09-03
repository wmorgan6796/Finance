from yahoo_finance import Share, Currency



yahoo = Share('AAPL')

yahoo.refresh()

print yahoo.get_info()
print yahoo.get_avg_daily_volume()
print yahoo.get_stock_exchange()
print yahoo.get_book_value()
print yahoo.get_ebitda()
print yahoo.get_dividend_share()
print yahoo.get_price_earnings_ratio()
print yahoo.get_short_ratio()
print yahoo.get_price_book()

# f = open('nasdaqlisted.txt', 'r')

# print (f.readline())
# print (f.readline())
