
# Ip-Tracker Script By Hossam Hamdy

import requests
import json
import time 
import sys
from os import system

Author = "Hossam Hamdy"

Logo = f"""\033[91m
  _____ _           _      ___ ____  
 |  ___(_)_ __   __| |    |_ _|  _ \ 
 | |_  | | '_ \ / _` |_____| || |_) | 
 |  _| | | | | | (_| |_____| ||  __/ 
 |_|   |_|_| |_|\__,_|    |___|_|  \033[97mBY : \033[93m{Author}\033[97m
 \033[91mGitHub : https://github.com/m3t4n0y3t\n"""

def GetIP():

    IP = str(input("\033[92m[#] IP :\033[93m "))
    while IP == "":
        IP = str(input("\033[92m[#] IP :\033[93m "))
    return IP


def GetResponse(IP):

    API = f"https://ipapi.co/{IP}/json/"
    Response = requests.get(API)
    Data = json.loads(Response.content)
    return Data

def DisplayInformation(Data):
    SlowPrinting("\033[96m\n[+] Gathering Infornation To You . . .")
    time.sleep(2)
    print("\n\n\033[94mIP INFORMATION :")
    print("===============\033[97m\n")
    try:
        print(f"IP : {Data['ip']}")
        print(f"City : {Data['city']}")
        print(f"Region : {Data['region']}")
        print(f"Region Code : {Data['region_code']}")
        print(f"Country : {Data['country']}")
        print(f"Country Code : {Data['country_code']}")
        print(f"Country Capital : {Data['country_capital']}")
        print(f"Country Name : {Data['country_name']}")
        print(f"Latitude : {Data['latitude']}")
        print(f"Longitude : {Data['longitude']}")
        print(f"Timezone : {Data['timezone']}")
        print(f"Country Calling Code : {Data['country_calling_code']}")
        print(f"Currency : {Data['currency']}")
        print(f"Currency Name : {Data['currency_name']}")
        print(f"Country Language : {Data['languages']}")
        print(f"Country Area : {Data['country_area']} KM")
        print(f"Country Population : {int(Data['country_population'])} Person")
        print(f"Asn : {Data['asn']}")
        print(f"ORG : {Data['org']}\n")
    except KeyError:
        print("We Can't Get Information\nMaybe This IP Address Doesn't Correct or it's an Internal IP Address.\n")
    print("="*50)


def SlowPrinting(Content):

    for char in Content + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3/100)


def DisplayLogo():

    SlowPrinting(Logo)

    
def Main():

    while (1):
        system('cls')
        DisplayLogo()
        IP = GetIP()
        Data = GetResponse(IP)
        DisplayInformation(Data)
        system("pause")


if __name__ == "__main__":

    Main()