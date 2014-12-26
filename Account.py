from time import sleep
import MySQLdb
import AccountValidationTest
import OSChecker
db = MySQLdb.connect(host="", # your host
                     user="", # your username
                      passwd="", # your password
                      db="") # name of the data base
cursor = db.cursor()#Defines a cursor allowing me to execute SQL commands
name = raw_input("Enter your username:")
AccountValidationTest.LoginScript(name)
OSChecker.OSCheck()
def timer(time, _print=False):
	if time == 0:
		cursor.execute("SELECT * FROM Accounts WHERE Username= %s;", (name))
		cursor.execute("UPDATE Accounts SET Credits = 0 WHERE Username = %s;", (name))
		db.commit()#commit
		OSChecker.LockAccount(name, time)
		return ''
	else:
		if _print: print time
		sleep(1)
		return timer(time - 1, _print)
cursor.execute("SELECT * FROM Accounts WHERE Username=%s;", (name))
for test in cursor.fetchall():
	creds = test[4]
	print "Credit Balance: " + `creds`
time_set = creds * 60
timer(time_set, True)
	
