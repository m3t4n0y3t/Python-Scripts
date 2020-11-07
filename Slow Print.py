from sys import stdout
from time import sleep
import os


def SlowPrint(text):
	for char in text + '\n':
		stdout.write(char)
		stdout.flush()
		sleep(1./50) # to speed up, change 50

# colors code
yellow  = '\033[93m'
red     = '\033[91m'
green   = '\033[92m'
blue    = '\033[94m'
cyan    = '\033[96m'
white   = '\033[97m'
grey    = '\033[90m'
magenta = '\033[95m'

os.system("cls") # in linux xhange 'cls' to 'clear'

text = "print  this text"

# call the function
SlowPrint(text)