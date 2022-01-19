from ensurepip import version
import random
import string
import requests
from colorama import Fore, Back, Style
import os
import ctypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

os.system('mode con: cols=126 lines=30')
os.system("cls")
kernel32.SetConsoleTitleW(u"The V Nitro Gen")

version = ("v1.0.0")

print(f"""\u001b[31m 
▄▄▄█████▓ ██░ ██ ▓█████     ██▒   █▓    ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████ ▓█████  ███▄    █ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░   █▒    ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒ ▓██░ ▒░▒██▀▀██░▒███       ▓██  █▒░   ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄      ▒██ █░░   ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
  ▒██▒ ░ ░▓█▒░██▓░▒████▒      ▒▀█░     ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░      ░ ▐░     ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░      ░ ░░     ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
  ░       ░  ░░ ░   ░           ░░        ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░ 
          ░  ░  ░   ░  ░         ░              ░  ░              ░         ░ ░           ░    ░  ░         ░ 
{version}                          ░                                                                             
\ngithub.com/TheVandetta for uptdate\u001b[37m""")
a = int(input('How much code do you want ?\n'))
b = 0
Valid = 0
Invalid = 0


while b < a:
    letters = string.ascii_letters + string.digits
    f = open("Nitro.txt", "a")
    f.write('https://discord.gift/' + ''.join(random.choice(letters) for i in range(16)) + '\n')
    print('\u001b[32mhttps://discord.gift/' + ''.join(random.choice(letters) for i in range(16)) + '\u001b[37m')
    b += 1
    kernel32.SetConsoleTitleW(f"Nitro generated: {b} | Valid: {Valid} | Invalid {Invalid}")

os.system("cls")

kernel32.SetConsoleTitleW(u"The V Nitro Check")
print(f"""\u001b[31m 
▄▄▄█████▓ ██░ ██ ▓█████     ██▒   █▓    ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████      ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░   █▒    ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ 
▒ ▓██░ ▒░▒██▀▀██░▒███       ▓██  █▒░   ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ 
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄      ▒██ █░░   ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒      ▒▀█░     ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░      ░ ▐░     ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░    ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒
    ░     ▒ ░▒░ ░ ░ ░  ░      ░ ░░     ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░
  ░       ░  ░░ ░   ░           ░░        ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░         ░  ░░ ░   ░   ░        ░ ░░ ░ 
          ░  ░  ░   ░  ░         ░              ░  ░              ░         ░ ░     ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░   
{version}                          ░                                                   ░                       ░               
\ngithub.com/TheVandetta for uptdate\u001b[37m""")

Check = input('Do you want to check the codes in Nitro.txt? [Y/N]: ')

if Check in ['y', 'Y', 'yes', 'Yes', 'YES']:
    with open("Nitro.txt") as file:
        f = open("Invalid.txt", "a")
        g = open("Valid.txt", "a")
        for line in file.readlines():
            nitro = line.strip("\n")
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            r = requests.get(url)
            if r.status_code == 200:
                print(f"\u001b[37m\n\n Valid Code\u001b[37m\n | \u001b[37m{nitro}\u001b[37m")
                g.write(f'{nitro}\n')
                Valid += 1
                kernel32.SetConsoleTitleW(f"Nitro generated: {b} | Valid: {Valid} | Invalid {Invalid}")
            else:
                print(f"\u001b[31mInvalid Code\u001b[37m | \u001b[31m{nitro}\u001b[37m\n")
                f.write(f'{nitro}\n')
                Invalid += 1
                kernel32.SetConsoleTitleW(f"Nitro generated: {b} | Valid: {Valid} | Invalid {Invalid}")
    print(f"You have \u001b[32m{Valid} Valid\u001b[37m and \u001b[31m{Invalid} Invalid\u001b[37m code")
    input()
else:
    print('Your Codes are in the Nitro.txt file')
    input()