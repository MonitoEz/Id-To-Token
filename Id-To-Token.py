# Modules importation
import os
import base64
import pydesings

try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
  ██▓▓█████▄    ▄▄▄█████▓ ▒█████     ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █
 ▓██▒▒██▀ ██▌   ▓  ██▒ ▓▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █
 ▒██▒░██   █▌   ▒ ▓██░ ▒░▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒
 ░██░░▓█▄   ▌   ░ ▓██▓ ░ ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒
 ░██░░▒████▓      ▒██▒ ░ ░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░
 ░▓   ▒▒▓  ▒      ▒ ░░   ░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒
  ▒ ░ ░ ▒  ▒        ░      ░ ▒ ▒░        ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░
  ▒ ░ ░ ░  ░      ░      ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░
  ░     ░                    ░ ░                  ░ ░  ░  ░      ░  ░         ░
""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [INPUT] USER ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGS] TOKEN FIRST PART : {encodedStr}')
os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)
