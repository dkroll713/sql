import mariadb
import iexmodule as iex
import checkdb

k = input("What would you like to do? \nType 'check' to look up a stock in the \
database, or 'search' to add a new record to the database\n>> ")

if k == "check":
    checkdb.check()
elif k == "search":
    iex.search_ticker()
