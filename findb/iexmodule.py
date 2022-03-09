import urllib.request
from bs4 import BeautifulSoup
import mariadb
import sys
import datetime
import nasdaqdatalink
nasdaqdatalink.read_key("C:/bin/api-keys/nasdaq-data-link")

date = datetime.datetime.now().date()
time = datetime.datetime.now().time()
timestr = str(time)
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


def search_ticker():
    ticker = input("Which stock would you like to look up? \n>> ").upper()
    query = input("What would you like to search for? \nType 'price','financials' \
    \n>> ")

    nasdaq_info = nasdaqdatalink.get_table('SHARADAR/TICKERS',ticker=ticker)
    nasdaq_financials = nasdaqdatalink.get_table('SHARADAR/SF1',ticker=ticker)
    company = nasdaq_info.iloc[1]
    name = company.loc['name']
    sicsector = company.loc['sicsector']
    sicindustry = company.loc['sicindustry']
    famaindustry = company.loc['famaindustry']
    sector = company.loc['sector']
    industry = company.loc['industry']
    scalemarketcap = company.loc['scalemarketcap']
    scalerevenue = company.loc['scalerevenue']
    if query.lower() == 'price':
        get_price_db(ticker)


def check_for_recent():
    try:
        conn = mariadb.connect(
            user = 'Win',
            password = 'birdhouse',
            host = '192.168.190.198',
            port = 3306,
            database = 'stocks'
        )
        cur = conn.cursor()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")
        sys.exit(1)
    statement = "SELECT * from stocks where ticker='"+ticker+"'"
    cur.execute(statement)
    rows = cur.fetchall()
    print(rows)

def get_price_db(ticker):
    n = 0
    # for ticker in tickerList:
        # ticker = tickerList[n]
    n = n+1
    url = url1+stockUrl+ticker+price+pk
    conn = urllib.request.Request(url, headers = headers)
    html = urllib.request.urlopen(conn).read()
    priceHTML = BeautifulSoup(html,features="html.parser")
    parsed_price = priceHTML.get_text()
    print("Ticker:",ticker,"; price:",parsed_price)

# connect to the database
    try:
        conn = mariadb.connect(
            user = 'Win',
            password = 'birdhouse',
            host = '192.168.190.198',
            port = 3306,
            database = 'stocks'
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()

# check db for requested query in current hour
    statement = "SELECT * FROM stocks where ticker='"+ticker+"' and date='"+\
    str(date)+"'"
    cur.execute(statement)
    rows = cur.fetchall()
    exists = False

    # checks if date & hour in entry are the same as current date & hour
    for row in rows:
        db_date = row[1]
        db_timestr = str(row[2])
        db_timesplit = db_timestr.split(":")
        db_hour = db_timesplit[0]
        if db_date == date and db_hour == hour:
            exists = True
            break
    if exists == True:
        # the ticker has already been entered today
        print("\nData for "+ticker+" already exists on date "+str(date)+\
        " in the current hour: "+hour)
    else:
        # insert the date, ticker, & price into 'stocks' table
        try:

            nasdaq_info = nasdaqdatalink.get_table('SHARADAR/TICKERS',ticker=ticker)
            nasdaq_financials = nasdaqdatalink.get_table('SHARADAR/SF1',ticker=ticker)
            company = nasdaq_info.iloc[1]
            name = company.loc['name']
            sicsector = company.loc['sicsector']
            sicindustry = company.loc['sicindustry']
            famaindustry = company.loc['famaindustry']
            sector = company.loc['sector']
            industry = company.loc['industry']
            scalemarketcap = company.loc['scalemarketcap']
            scalerevenue = company.loc['scalerevenue']

            statement = "INSERT INTO stocks (date, time, name, ticker, price ,\
            sicsector, sicindustry, famaindustry, sector, industry, \
            scalemarketcap, scalerevenue) VALUES (%s, %s, %s, %s, %s, %s, %s, \
            %s, %s, %s, %s, %s)"
            data = (date, time, name, ticker.upper(), parsed_price, sicsector, \
            sicindustry, famaindustry, sector, industry, scalemarketcap, \
            scalerevenue)
            cur.execute(statement, data)
            conn.commit()
            print("Successfully added stock to the database.")
        except mariadb.Error as e:
            print(f"Error adding entry to database: {e}")
            sys.exit(1)



            conn.close()


# if query != "":
#     search_ticker()
