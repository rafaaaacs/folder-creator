import os
import colorama
from colorama import Fore

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

print(Fore.LIGHTCYAN_EX + """

    
                                ██████╗  █████╗ ███████╗ █████╗  ██████╗███████╗      
                                ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝      
                                ██████╔╝███████║█████╗  ███████║██║     ███████╗█████╗
                                ██╔══██╗██╔══██║██╔══╝  ██╔══██║██║     ╚════██║╚════╝
                                ██║  ██║██║  ██║██║     ██║  ██║╚██████╗███████║      
                                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝      
                                                      

      """)

name = input("Folder name: ")
os.mkdir(f"{name}")

print(Fore.LIGHTGREEN_EX + "Successfully created folder {name}. \n" + Fore.RESET)
