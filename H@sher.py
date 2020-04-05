# Coded By Hossam Hamdy
# <M3T4N0Y3T/>
# Python 3.8.2
from optparse import*
import hashlib
class hashing:
	def enc(text,hash_type):
		text = text.encode("utf-8")
		hash_hash = hashlib.new(hash_type)
		hash_hash.update(text)
		return hash_hash.hexdigest()
parser = OptionParser("""\n
  _    _                _                 
 | |  | |   ____       | |                
 | |__| |  / __ \  ___ | |__    ___  _ __ 
 |  __  | / / _` |/ __|| '_ \  / _ \| '__|
 | |  | || | (_| |\__ \| | | ||  __/| |   
 |_|  |_| \ \__,_||___/|_| |_| \___||_|   
           \____/                     \n
H@sher is a free open source hashing script
coded by : Hossam Hamdy
this script coded for personal usage so it's not an advanced one
[#] the hash types that are been supported in the script
\t[1] SHA1 [2] SHA224 [3] SHA256 [4] SHA384 [5] MD5
---------------------
> H@sher.py Options <
---------------------\n
    --e             [?] enter the clear text after to encrypt it.\n
    --a             [?] enter the hash type to en on it.\n
	example :
		enco.py --e Hossam --a md5
		>>> Text : Hossam  ALgo-Type : md5
		>>> 3448b45f85933e04fa269300e11ea1e3 """)
parser.add_option("--e",dest = "text")
parser.add_option("--a",dest = "hash_type")
(options,args) = parser.parse_args()
if options.text == None or options.hash_type == None:
	print(parser.usage)
else:
	text = str(options.text)
	hash_type = str(options.hash_type)
	encrypted_text = hashing
	test = encrypted_text.enc(text,hash_type)
	print(f"\n>>> Text : {text}  ALgo-Type : {hash_type}")
	print(f"\n>>> {test}\n")
