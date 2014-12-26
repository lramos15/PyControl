#Checks what OS Python is running on
import os
import sys
import subprocess
OSNum = 2
def OSCheck():
	OS = os.name
	if OS == "posix":
		global OSNum
		OSNum = 0	
	elif OS == "nt":
		global OsNum
		OSNum = 1
	else:
		print "Could not detect what python was running on."
		sys.exit()
def LockAccount(name="", time = 0):
	if OSNum == 1 and time == 0:
		subprocess.call(["Net user ", name, "/active:no"])
	elif OSNum == 0 and time == 0:
		subprocess.call(["usermod -L -e 1 " , name])
