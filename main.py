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

name = input("What should the folder name be?: ")
os.mkdir(f"{name}")

print(Fore.LIGHTGREEN_EX + "Successfully created folder with the name {name}. \n" + Fore.RESET)

input("Press enter to exit...")
