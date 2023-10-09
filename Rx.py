###__IMPORT__###

import os , time
from time import sleep

###__COLOURS__###

GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m' 
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"

logo = (f'''{GREEN}
                                         _                                                
                                        | |                                               
  ______ ______ ______ ______ ______    | | ___  _   _ ______ ______ ______ ______ ______ 
 |______|______|______|______|______|   | |/ _ \| | | |______|______|______|______|______|
                                   | |__| | (_) | |_| |                                   
                                    \____/ \___/ \__, |                                   
                                                  __/ |                                   
  _______                                    ____|___/  _                                 
 |__   __|                                  / ____|    | |                                
    | | ___ _ __ _ __ ___  _   ___  _______| (___   ___| |_ _   _ _ __                    
    | |/ _ \ '__| '_ ` _ \| | | \ \/ /______\___ \ / _ \ __| | | | '_ \                   
    | |  __/ |  | | | | | | |_| |>  <       ____) |  __/ |_| |_| | |_) |                  
    |_|\___|_|  |_| |_| |_|\__,_/_/\_\     |_____/ \___|\__|\__,_| .__/                   
                                                                 | |                      
                                                                 |_|                          ''')

menu = ('''
[1] ð™„ð™©-ð™„ð™¨-ð™…ð™¤ð™”-Basic Setup
'\x1b[38;5;196m' [2] Contract Me-https://www.facebook.com/profile.php?id=100024444078080&mibextid=ZbWKwL
'\x1b[38;5;196m' [3] Contract Me 01779602011
[4] Exit
''')

def setup ():
	os.system("pkg update -y && pkg upgrade -y && pkg install git -y &&pkg install python -y && pkg install python2 -y && pkg install python3 -y && pkg install curl -y && pkg install wget -y && pip install requests  mechanize bs4")
	
def join():
	os.system("xdg-open https://facebook.com/groups/763643838521570/")
	
def main():
	os.system('clear')
	print(logo)
	print('')
	print(menu)
	option = input(f'{RED}Choose Option : ')
	if option == '1':
		setup()
		main()
	elif option == '2':
		join()
		main()
	elif option == '3':
		os.system("xdg-open https://facebook.com/mesami.6T9")
		main()
	elif option =='4':
		exit()
	else:
		print('\n')
		print(f'Choose Carefully')
		time.sleep(3)
		main()

main()





#os.system('apt install git')
