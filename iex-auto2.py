import urllib.request
from bs4 import BeautifulSoup
import mariadb
import sys
import datetime
import nasdaqdatalink
import ndl
import time
nasdaqdatalink.read_key("C:/bin/api-keys/nasdaq-data-link")

date = datetime.datetime.now().date()
timex = datetime.datetime.now().time()
timestamp = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
timestr = str(timex)
timesplit = timestr.split(":")
hour = timesplit[0]
# pi IP: 192.168.190.198
# mariadb root password - birdhouse
# mariadb user: 'Win' and password: 'birdhouse'

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) \
Gecko/20100101 Firefox/48.0"

url1 = "https://cloud.iexapis.com/stable"
stockUrl = "/stock/"
price = "/price"
financials = "/financials"
# tickerList = ['GME','TSLA','TTD','HD','BBBy','CS']
pk = "?token=pk_aff16f9ea7754a39bd53879c47f24714"
# query = "auto"

# nasdaq_info = nasdaqdatalink.get_table('SHARADAR/TICKERS',ticker=ticker)
# if not nasdaq_info.empty:
#     company = nasdaq_info.iloc[1]
#     name = company.loc['name']
#     sicsector = company.loc['sicsector']
#     sicindustry = company.loc['sicindustry']
#     famaindustry = company.loc['famaindustry']
#     sector = company.loc['sector']
#     industry = company.loc['industry']
#     scalemarketcap = company.loc['scalemarketcap']
#     scalerevenue = company.loc['scalerevenue']
# nasdaq_financials = nasdaqdatalink.get_table('SHARADAR/SF1',ticker=ticker)

# def search_ticker():
#     if query.lower() == 'price':
#         get_price_db()
#     elif query.lower() == 'financials':
#         ndl.print_fin(ticker)
#     elif ticker.lower() == 'auto' or query.lower() == 'auto':
with open('C:/Users/dkrol/Desktop/coding/github-sql/tickers.txt') as f:
    lines=f.readlines()
    z = 0
    for x in lines:
        z = z+1
        a = x.split('\n')
        tock = a[0]
        url = url1+stockUrl+tock+price+pk
        conn = urllib.request.Request(url, headers = headers)
        html = urllib.request.urlopen(conn).read()
        priceHTML = BeautifulSoup(html,features="html.parser")
        parsed_price = priceHTML.get_text()
        print("\nTicker:",tock,"; price:",parsed_price)
        time.sleep(.2)

        try:
            conn = mariadb.connect(
                user = 'Win',
                password = 'birdhouse',
                host = '192.168.190.198',
                port = 3306,
                database = 'stocks',
            )
            cur = conn.cursor()
        except mariadb.Error as e:
            print(f"Failed to connect to database for automatic posting: {e}")

        statement = "SELECT * FROM current_price where ticker='"+tock+"'"
        cur.execute(statement)
        rows = cur.fetchall()
        exists = False

        # checks if date & hour in entry are the same as current date & hour
        for row in rows:
            print(row)
            if tock == row[0]:
                exists = True
                break
        if exists == True:
            # the ticker has already been entered today
            print("\nData for "+str(z)+" "+tock+" already exists on date "+\
            str(date)+" in the current hour: "+hour)
            # insert the date, ticker, & price into 'stocks' table
            try:
                statement = "UPDATE current_price SET current_price="+\
                parsed_price+" WHERE ticker='"+tock+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added stock "+str(z)+", ticker: "+tock+" to the database AUTOMATICALLY.")
            except mariadb.Error as e:
                print(f"Error adding entry to database: {e}")
                sys.exit(1)
            # try:
            #     statement = "UPDATE current_price SET datetime="+\
            #     str(timestamp)+"' WHERE ticker='"+tock+"'"
            #     cur.execute(statement)
            #     conn.commit()
            #     print("Successfully added stock "+str(z)+", ticker: "+tock+" to the database AUTOMATICALLY.")
            # except mariadb.Error as e:
            #     print(f"Error adding entry to database: {e}")
            #     sys.exit(1)


        conn.close()

# def get_price_db():
#     n = 0
#     # for ticker in tickerList:
#         # ticker = tickerList[n]
#     n = n+1
#     url = url1+stockUrl+ticker+price+pk
#     conn = urllib.request.Request(url, headers = headers)
#     html = urllib.request.urlopen(conn).read()
#     priceHTML = BeautifulSoup(html,features="html.parser")
#     parsed_price = priceHTML.get_text()
#     print("Ticker:",ticker,"; price:",parsed_price)
# # connect to the database
#     try:
#         conn = mariadb.connect(
#             user = 'Win',
#             password = 'birdhouse',
#             host = '192.168.190.198',
#             port = 3306,
#             database = 'stocks'
#         )
#     except mariadb.Error as e:
#         print(f"Error connecting to MariaDB Platform: {e}")
#         sys.exit(1)
#     cur = conn.cursor()
#
# # check db for requested query in current hour
#     statement = "SELECT * FROM stocks where ticker='"+ticker+"' and date='"+\
#     str(date)+"'"
#     cur.execute(statement)
#     rows = cur.fetchall()
#     exists = False
#
#     # checks if date & hour in entry are the same as current date & hour
#     for row in rows:
#         db_date = row[1]
#         db_timestr = str(row[2])
#         db_timesplit = db_timestr.split(":")
#         db_hour = db_timesplit[0]
#         if db_date == date and db_hour == hour:
#             exists = True
#             break
#     if exists == True:
#         # the ticker has already been entered today
#         print("\nData for "+ticker+" already exists on date "+str(date)+\
#         " in the current hour: "+hour)
#     else:
#         # insert the date, ticker, & price into 'stocks' table, if dataframe is occupied
#         if not nasdaq_info.empty:
#             try:
#                 statement = "INSERT INTO stocks (date, time, name, ticker, price ,\
#                 sicsector, sicindustry, famaindustry, sector, industry, \
#                 scalemarketcap, scalerevenue) VALUES (%s, %s, %s, %s, %s, %s, %s, \
#                 %s, %s, %s, %s, %s)"
#                 data = (date, timex, name, ticker.upper(), parsed_price, sicsector, \
#                 sicindustry, famaindustry, sector, industry, scalemarketcap, \
#                 scalerevenue)
#                 cur.execute(statement, data)
#                 conn.commit()
#                 print("Successfully added stock to the database.")
#             except mariadb.Error as e:
#                 print(f"Error adding entry to database: {e}")
#                 sys.exit(1)
#         else:
#             try:
#                 statement = "INSERT INTO stocks (date, time, ticker, price ,\
#                 VALUES (%s, %s, %s, %s)"
#                 data = (date, timex, ticker.upper(), parsed_price)
#                 cur.execute(statement, data)
#                 conn.commit()
#                 print("Successfully added stock to the database.")
#             except mariadb.Error as e:
#                 print(f"Error adding entry to database: {e}")
#                 sys.exit(1)
#
#
#             conn.close()
#
#
# if query != "":
#     search_ticker()
