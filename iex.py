import urllib.request
from bs4 import BeautifulSoup
import mariadb
import sys
import datetime

date = datetime.datetime.now()
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
stockName = input("Which stock would you like to look up? \n>> ").upper()
query = input("What would you like to search for? \nType 'price','financials' \
\n>> ")

def search_ticker():
    if query.lower() == 'price':
        get_price_db()


def check_for_recent():
    try:
        conn = mariadb.connect(
            user = 'Win',
            password = 'birdhouse',
            host = '192.168.190.198',
            port = 3306,
            database = 'stocks'
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")
        sys.exit(1)


def get_price_db():
    n = 0
    # for ticker in tickerList:
        # stockName = tickerList[n]
    n = n+1
    url = url1+stockUrl+stockName+price+pk
    conn = urllib.request.Request(url, headers = headers)
    html = urllib.request.urlopen(conn).read()
    priceHTML = BeautifulSoup(html,features="html.parser")
    parsed_price = priceHTML.get_text()
    print("Ticker:",stockName,"; price:",parsed_price)

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

# check db for requested query
    statement = "SELECT * FROM stocks where ticker='"+stockName+"'"
    cur.execute(statement)
    row = cur.fetchone()
    if row:
        # the ticker has already been entered today
        print("\nData for "+stockName+" already exists on date "+str(date))
    else:
        # insert the date, ticker, & price into 'stocks' table
        try:
            statement = "INSERT INTO stocks (date, ticker, price) VALUES (%s, %s, %s)"
            data = (date, stockName.upper(), parsed_price)
            cur.execute(statement, data)
            conn.commit()
            print("Successfully added stock to the database.")
        except mariadb.Error as e:
            print(f"Error adding entry to database: {e}")
            sys.exit(1)



        conn.close()


if query != "":
    search_ticker()
