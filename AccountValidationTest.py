import hashlib # Imports the hashing module
import MySQLdb # Imports the database to store the hash
import sys
import getpass
db = MySQLdb.connect(host="", # your host
                     user="", # your username
                      passwd="", # your password
                      db="") # name of the data base
cursor = db.cursor()#Defines a cursor allowing me to execute SQL commands
def LoginScript(name="test"):
	cursor.execute("SELECT * FROM Accounts WHERE Username=%s;", (name))
	user_input = getpass.getpass()
	salt = ""#Input a random string of characters here
	hash = hashlib.md5(salt + user_input).hexdigest()
	for row in cursor.fetchall():
		passwd = row[2]
	attempts = 3
	while True:
		if hash == passwd:
			print "Successfully Logged in, Welcome {0}".format(name)
			break
		else:
			attempts = attempts - 1
			print "Invalid try you have {0} more attempts to guess the right password".format(attempts)
			user_input = getpass.getpass()
			salt = ""#Input a random string of characters here
			hash = hashlib.md5(salt + user_input).hexdigest()
		if attempts == 1:
			print "You have ran out of attempts get out of here!"
			sys.exit()
def isAdmin(name="test"):
	cursor.execute("SELECT * FROM Accounts WHERE Username=%s;", (name))
	for row in cursor.fetchall():
		Status = row[3]
	if Status == "Admin":
		print "{0} has Admin Privelages.".format(name)
	else:
		print "{0} does not have Admin Privelages.".format(name)
		sys.exit()

