from random import choice as densor
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset=True)




print(Fore.RED+""""
██╗░░░██╗██╗░██████╗░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██║░░░██║██║██╔════╝██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
╚██╗░██╔╝██║╚█████╗░███████║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░╚████╔╝░██║░╚═══██╗██╔══██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░░██║██████╔╝██║░░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                        This Tool For Visa Checker
                     [!] Coded By Vanish Now  +201286016083 [!]
""")

import random
from datetime import datetime, timedelta
from colorama import Fore, Style
import time

def progress_bar():
    """محاكاة شريط تحميل تدريجي"""
    bar_length = 30  
    for i in range(bar_length + 1):
        bar = Fore.YELLOW + '=' * i + '.' * (bar_length - i) + Style.RESET_ALL
        print(f"\r{Fore.CYAN}Generating Visa... {bar} {Fore.MAGENTA}{i * 100 // bar_length}%{Style.RESET_ALL}", end='', flush=True)
        time.sleep(0.05)
    print(f"\r{Fore.CYAN}Generating Visa... {Fore.GREEN}[DONE]{Style.RESET_ALL}                    ")

def generate_visas():
    years = range(2025, 2031)
    months = range(5, 13)
    days = range(8, 29)  # ضمان سلامة التاريخ لجميع الأشهر
    file_save = 'Densor.txt'
    balances = [69, 230, 187, 80, 280, 182]
    
    with open(file_save, 'w') as file:
        for year in years:
            for month in months:
                for day in days:
                    visa_number = ''.join(random.choices("1234567890", k=16))
                    exp_date = datetime(year, month, day).strftime("%m/%Y")
                    cvc = ''.join(random.choices("1234567890", k=3))
                    balance = random.choice(balances)
                    
                    progress_bar()
                    
                    output = f"""
{Fore.BLUE}=========================[ VISA INFO ]=========================={Style.RESET_ALL}
{Fore.CYAN}Visa Number: {Fore.WHITE}{visa_number}{Style.RESET_ALL}
{Fore.CYAN}Expiry Date: {Fore.YELLOW}{exp_date}{Style.RESET_ALL}
{Fore.CYAN}CVC Code   : {Fore.RED}{cvc}{Style.RESET_ALL}
{Fore.CYAN}Balance    : {Fore.GREEN}${balance}{Style.RESET_ALL}
{Fore.BLUE}==============================================================={Style.RESET_ALL}
"""
                    print(output)
                    file.write(f"{visa_number}|{exp_date}|{cvc}|${balance}\n")

def check_visa():
    from HamodyTools import Hamody
    file_visa = input("[+] Enter List Visa: ")
    try:
        with open(file_visa, 'r') as file:
            visas = [line.strip() for line in file]
        
        for visa in visas:
            check = Hamody.Visa(visa)
            if check:
                print(Fore.GREEN + check + Style.RESET_ALL)
                with open('visa_true.txt', 'a') as valid_file:
                    valid_file.write(check + '\n')
            else:
                print(Fore.RED + "[!] Dead Visa" + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + "[!] File not found." + Style.RESET_ALL)

ch = input(f"""
{Fore.MAGENTA}1 - Make Combo [ Visa ]{Style.RESET_ALL}
{Fore.MAGENTA}2 - Check Visa{Style.RESET_ALL}
""")

if ch == "1":
    generate_visas()
elif ch == "2":
    check_visa()
else:
    print(Fore.RED + "[!] Invalid Choice" + Style.RESET_ALL)

