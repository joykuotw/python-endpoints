# Create a database

import sqlite3
import csv
from datetime import datetime
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

class createDB():

    def readCSV(self, filename):
        try:
            conn = sqlite3.connect('databaseForTest.db')
            print 'DB Creation Successful!'
            cur = conn.cursor()
            # cur.execute('''DROP TABLE PRODUCTS;''')
            cur.execute('''CREATE TABLE PRODUCTS
			              (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
				           TITLE           TEXT    NOT NULL,
				           DESCRIPTION     TEXT    NOT NULL,
				           PRICE           INTEGER     NOT NULL,
				           CREATED_AT      TIMESTAMP,
				           UPDATED_AT      TIMESTAMP);''')
            print 'Table Creation Successful!'
            with open(filename) as f:
                reader = csv.reader(f)
                for row in reader:
                    cur.execute("INSERT INTO PRODUCTS VALUES (null, ?, ?, ?, ?, ?);", (unicode(row[0]), unicode(row[1]), unicode(row[2]), datetime.now(), datetime.now()))
            print 'Successfully read data from CSV file!'
            conn.commit()
            conn.close()
        except Exception as err:
            print "Error: ", err

c = createDB().readCSV('products.csv')