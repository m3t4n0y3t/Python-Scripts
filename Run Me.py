
# Coded By : Hossam Hamdy

from os import system

system("cls")

class color:
    red     = '\033[91m'
    green   = '\033[92m'
    blue    = '\033[94m'
    white   = '\033[97m'

def get_comands():
    
    comands_list = [] # save all commands here
    counter = 1       # the number of command
    query = ""        # initial value
    while query != "##": # (##) is the termenate value
        query = str(input(f"     {color.white}[{color.blue}{counter}{color.white}] {color.green}")) # get commands from user
        if query != "##" :
            comands_list.append(query) # check f the command == termenate value or not 
        counter += 1 # increment the counter value
    return comands_list

def execute(commands):
    print(color.blue)   # chabge color of the response to blue
    for command in commands:
        system(command) # execute the command
        seperator = "-"*50
        print(f"\n\n{seperator}\n\n") 

intro = """
                         _____               __  __      
                        |  __ \             |  \/  |     
                        | |__) |   _ _ __   | \  / | ___ 
                        |  _  / | | | '_ \  | |\/| |/ _ \\
                        | | \ \ |_| | | | | | |  | |  __/
                        |_|  \_\__,_|_| |_| |_|  |_|\___ \n
                        GitHub   : /m3t4n0y3t
                        Coded By : Hossam Hamdy
                        Enter ## To termenate the input process

"""
print(color.red + intro)
get_cmd = get_comands()
execute(get_cmd)

system("pause")