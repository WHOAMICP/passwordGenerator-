class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

try:
    from itertools import product
    import string
    import sys
    import os
    from colorama import Fore, Back, Style
    import time
except ModuleNotFoundError:
    print(bcolors.RED + '+[+[+[ Installing modules ]+]+]+\n')
    os.system('pip install product')
    os.system('pip install sys')
    os.system('pip install colorama')
    os.system('pip install time')
    os.system('clear')
    os.system('python passListGenerator.py')

os.system('cls' if os.name == 'nt' else 'clear')

def logo(stringlogo):
    for g in stringlogo:
        sys.stdout.write(g)
        sys.stdout.flush()
        time.sleep(0.010)

def type(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.06)

logo(Fore.GREEN + '''                                 
  ______   ______  _____ ____    ____   _    _   _ ___ ____ 
 / ___\ \ / / __ )| ____|  _ \  |  _ \ / \  | \ | |_ _/ ___|
| |    \ V /|  _ \|  _| | |_) | | |_) / _ \ |  \| || | |    
| |___  | | | |_) | |___|  _ <  |  __/ ___ \| |\  || | |___ 
 \____| |_| |____/|_____|_| \_\ |_| /_/   \_\_| \_|___\____|
                                                            
''')
    
type(Fore.GREEN + '''******************************************************
*''' + Fore.BLUE + ''' Auther ''' + Fore.RED + '''   : ''' + Fore.YELLOW + '''WHO AM I''' + Fore.GREEN + '''                               *
*''' + Fore.BLUE + ''' Facebook  ''' + Fore.RED + ''': ''' + Fore.YELLOW + '''https://m.me/whoami.hacker.2 ''' + Fore.GREEN + '''          *
* ''' + Fore.BLUE +  '''Instagram ''' + Fore.RED + ''':''' + Fore.YELLOW + ''' https://www.Instagram.com/who_am_i_c_p''' + Fore.GREEN + ''' *
* ''' + Fore.BLUE +  '''github    ''' + Fore.RED + ''':''' + Fore.YELLOW +  ''' https://github.com/WHOAMICP           ''' + Fore.GREEN + ''' *
* ''' + Fore.BLUE + '''Tool ''' + Fore.RED + '''     :''' + Fore.YELLOW + ''' Password Generator ''' + Fore.GREEN + '''                    * 
******************************************************\n\n''')


type(Fore.YELLOW + "Selected password length\n")
type(Fore.GREEN + "[1]" + Fore.YELLOW + " 1 length password\n")
type(Fore.GREEN + "[2]" + Fore.YELLOW + " 2 length password\n")
type(Fore.GREEN + "[3]" + Fore.YELLOW + " 3 length password\n")
type(Fore.GREEN + "[4]" + Fore.YELLOW + " 4 length password\n")
type(Fore.GREEN + "[5]" + Fore.YELLOW + " 5 length password\n")
type(Fore.GREEN + "[6]" + Fore.YELLOW + " 6 length password\n")
type(Fore.GREEN + "[7]" + Fore.YELLOW + " 7 length password\n")
type(Fore.GREEN + "[8]" + Fore.YELLOW + " 8 length password\n")
type(Fore.GREEN + "[9]" + Fore.YELLOW + " 9 length password\n")
type(Fore.GREEN + "[10]" + Fore.YELLOW + " 10 length password\n")
type(Fore.GREEN + "[11]" + Fore.YELLOW + " CUSTOM password length\n")
type(Fore.GREEN + "[00]" + Fore.YELLOW + " EXIT\n")
type(Fore.GREEN + '>> ')
ing = int(input(Fore.RED + ''))
if int(ing) > int(12) or int(ing) < int(00):
     type('ERROR: Invalid Option. GoodBye.')
     os.system('clear')
     sys.exit(1)

if ing == int(1):
    min_len = 1
    max_len = 1
elif ing == int(2):
    min_len = 2
    max_len = 2
elif ing == int(3):
    min_len = 3
    max_len = 3
elif ing == int(4):
    min_len = 4
    max_len = 4
elif ing == int(5):
    min_len = 5
    max_len = 5
elif ing == int(6):
    min_len = 6
    max_len = 6
elif ing == int(7):
    min_len = 7
    max_len = 7
elif ing == int(8):
    min_len = 8
    max_len = 8
elif ing == int(9):
    min_len = 9
    max_len = 9
elif ing == int(10):
    min_len = 10
    max_len = 10
elif ing == int(11):
    type(Fore.GREEN + "\nEnter minimum length: ")
    min_len = int(input(Fore.RED + ''))
    type(Fore.GREEN + "Enter maximum length: ")
    max_len = int(input(Fore.RED + ''))
elif ing == int(00):
    os.system('clear')
    sys.exit()

type(Fore.GREEN + "\nEnter TEXT file name: ")    
name = str(input(Fore.RED + ''))
            
counter = 0
char = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file_open = open(name+'.txt','w')

for i in range(min_len,max_len+1):
    for j in product(char,repeat=i):
        word = "".join(j)
        list = file_open.write(word)
        file_open.write('\n')
        counter+=1
        print(Fore.RED +"["+str(counter)+"]"+Fore.YELLOW,  word)
print(Fore.GREEN + "\nwordlist of {} passwords created successfully")
        