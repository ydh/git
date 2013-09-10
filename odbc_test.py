import pyodbc

con = pyodbc.connect('DSN=username;PWD=passwd')
cur = con.cursor()
for row in con.execute("SELECT DISTINCT DATE_ID,RNC FROM table_test WHERE DATE_ID='2013-09-08' GROUP BY DATE_ID,RNC"):
	print row.DATE_ID,row.RNC



