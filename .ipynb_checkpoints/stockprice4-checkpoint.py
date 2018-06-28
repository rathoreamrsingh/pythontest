#import pandas.io.data as web
#import datetime
#start = datetime.datetime(2010, 1, 1)
#end = datetime.datetime(2013, 1, 27)
#df=web.DataReader("BVMF:ABRE11", 'google', start, end)
#print(df.head(10))

"""import pandas
import requests
import io

stock = 'GOOG'
startdate = 'Jul 08, 2017'
enddate = 'Aug 08, 2017'

rooturl = 'http://www.google.com/finance/historical?q='
query = stock + '&startdate=' + startdate +'&enddate=' + enddate + '&output=csv'

url = rooturl + query
response = requests.get(url)
df = pandas.read_csv(io.StringIO(response.content.decode('utf-8')))

print(df)"""


#import external pandas_datareader library with alias of web
import pandas_datareader as web

#import datetime internal datetime module
#datetime is a Python module
import datetime

#datetime.datetime is a data type within the datetime module
start = datetime.datetime(2017, 9, 1)
end = datetime.datetime(2017, 12, 31)

#DataReader method name is case sensitive
df = web.DataReader("nvda", 'yahoo', start, end)

#invoke to_csv for df dataframe object from
#DataReader method in the pandas_datareader library

#..\first_yahoo_prices_to_csv_demo.csv must not
#be open in another app, such as Excel

df.to_csv('first_yahoo_prices_volumes_to_csv_demo.csv')