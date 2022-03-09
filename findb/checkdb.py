import mariadb
import datetime

date = datetime.datetime.now().date()
time = datetime.datetime.now().time()


def check():
    query = input("Which ticker would you like to look up?\n>> ")
    if query != "":
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
            print(f"Error connecting to the lookup platform: {e}")
        statement = "SELECT * FROM stocks where ticker='"+query+"'"
        cur.execute(statement)
        result = cur.fetchall()
        for row in result:
            print("On "+str(row[1])+" at "+str(row[2])+", "+row[3]+\
            " is priced at "+str(row[5]))
