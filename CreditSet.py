from time import sleep
import MySQLdb
import AccountValidationTest 

db = MySQLdb.connect(host="", # your host
                     user="", # your username
                      passwd="", # your password
                      db="") # name of the data base
cursor = db.cursor()#Defines a cursor allowing me to execute SQL commands
adminName = raw_input("What is your username?:")
AccountValidationTest.LoginScript(adminName)
AccountValidationTest.isAdmin(adminName)
name = raw_input("What username would you like to add credits to?:")
creds = input("How many credits would you like to add to the account?")
cursor.execute("SELECT * FROM Accounts WHERE Username=%s;", (name))
for test in cursor.fetchall():
	creds = creds + test[4]
cursor.execute("""UPDATE Accounts SET Credits = %s WHERE Username = %s;""", (creds, name))
cursor.execute("SELECT * FROM Accounts WHERE Username=%s;", (name))
db.commit()# commits the changes
for test in cursor.fetchall():
	creds = creds + test[4]
	print test[4]
