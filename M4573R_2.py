#!/usr/bin/python3
import os
import time
senha = input("Qual a senha: ?")
if senha < "257":
    print("Acesso não liberado")
    exit()
elif senha == "258":  
    print("Acesso liberado")
    time.sleep(3)
    os.system("clear")
else:
    print("Bienvenido en mi script M4573R")
print("LOADING") 
time.sleep(2)
print("──▄────▄▄▄▄▄▄▄────▄───")
print("─▀▀▄─▄█████████▄─▄▀▀──")
print("─────██─▀███▀─██──────")
print("───▄─▀████▀████▀─▄────")
print("─▀█────██▀█▀██────█▀──")
print("______M4573R_Alianza______")

print("1: ZPhISHER")
print("2= PERSONALIZAR")
escolha = False
while escolha == False:
    nivel = int(input("Qual opção: "))
    if (nivel == 1):
        os.system(" pkg install tur-repo && pkg install zphisher && zphisher")
  
    elif (nivel == 2):
        os.system(" git clone https://github.com/Bhai4You/Termux-Banner && cd Termux-Banner && chmod +x requirement.sh && chmod +x t-ban.sh && bash requirement.sh && bash t-ban.sh")
      