import feedparser

url_8btc = 'http://www.8btc.com/feed'
url_nbtc = 'http://www.newsbtc.com/feed/'

print('parsing 8btc')
req_8btc = feedparser.parse(url_8btc)
print('parsing newsbtc')
req_nbtc = feedparser.parse(url_nbtc)

print(req_8btc)
print(req_nbtc)