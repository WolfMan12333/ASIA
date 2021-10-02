#!/bin/python3

"""
Creator: Dawid(WolfMan12333/Daredevil) Wordliczek
Example of Automation of SQL Injection Attack
"""

import subprocess
from termcolor import colored
from time import sleep

#own files
import Basic_SQL_Injection.bsi as bsi	#option nr.: 1
import Retr_Hidden_Data.rhd as rhd	#option nr.: 2
import Retr_Data_from_Other_DB_Tabl.rdfodbt as rdfodbt	#option nr.: 3
import Subverting_App_Logic.sal as sal	#option nr.: 4
import SQL_Injection_Blind.sib as sib	#option nr.: 5
import Ind_Cond_Res_by_Trig_SQL_errors.icrbtse as icr	#option nr.: 6
import Exploiting_Blind_SQL_Inj_by_Tr_Time_Delays.ebsibttd as ebs	#option nr.: 7
import login_bypass.login_bypass as logby	#option nr.: 8

#clear
def clear():
	subprocess.run('clear', shell=True)

#options/ menu
menu_options = {
	1: 'Basic Sql Injection',
	2: 'Retrieving Hidden Data',
	3: 'Retrieving Data from Other Database Tables',
	4: 'Subverting Application Logic',
	5: 'SQL Injection - Blind',
	6: 'Inducing Conditional Responses by Triggering SQL errors',
	7: 'Exploiting Blind SQL Injection by Triggering Time Delays',
	8: 'Login Bypass',
	9: 'Exit',
}

def welcome():
        print(colored("""
                Welcome in ASIA - Advanced SQL Injection Automation\n
                This program is written for demonstration purposes or for\n
                the work of an ethical hacker or pentester.\n
                I'm not responsible for its use that violates the law!!!

                Creator: Dawid(WolfMan12333/Daredevil) Wordliczek\n\n\n

                                      _.---**""**-.       
                              ._   .-'           /|`.     
                               \`.'             / |  `.   
                                V              (  ;    \  
                                L       _.-  -. `'      \ 
                               / `-. _.'       \         ;
                              :            __   ;    _   |
                              :`-.___.+-*"': `  ;  .' `. |
                               |`-/     `--*'   /  /  /`.\|
                              : :              \    :`.| ;
                              | |   .           ;/ .' ' / 
                              : :  / `             :__.'  
                               \`._.-'       /     |      
                                : )         :      ;      
                                :----.._    |     /       
                               : .-.    `.       /        
                                \     `._       /         
                                /`-            /          
                               :             .'           
                                \ )       .-'             
                                 `-----*"'    
        """, 'red'))

def print_menu():
	for key in menu_options.keys():
		print(key, '--', menu_options[key])

def menu_option():
	print_menu()

	option = ''

	try:
		option = int(input('Enter your choice: '))
	except:
		clear()
		print('Wrong input. Please enter a number ...')
		sleep(2)
		clear()

	#check choice
	if option == 1:
		clear()
		welcome()
		print('Your choice -- Basic Sql Injection\n\n')
		bsi.start_bsi()
		sleep(4)
		clear()
		welcome()
	elif option == 2:
		clear()
		welcome()
		print('Your choice -- Retrieving Hidden Data\n\n')
		rhd.start_rhd()
		sleep(4)
		clear()
		welcome()
	elif option == 3:
		clear()
		welcome()
		print('Your choice -- Retrieving Data from Other Database Tables\n\n')
		rdfodbt.start_rdfodbt()
		sleep(4)
		clear()
		welcome()
	elif option == 4:
		clear()
		welcome()
		print('Your choice -- Subverting Application Logic\n\n')
		sal.start_sal()
		sleep(4)
		clear()
		welcome()
	elif option == 5:
		clear()
		welcome()
		print('Your choice -- SQL Injection - Blind\n\n')
		sib.start_sib()
		sleep(4)
		clear()
		welcome()
	elif option == 6:
		clear()
		welcome()
		print('Your choice -- Inducing Conditional Responses by Triggering SQL error\n\n')
		icr.start_icrbtse()
		sleep(4)
		clear()
		welcome()
	elif option == 7:
		clear()
		welcome()
		print('Your choice -- Exploiting Blind SQL Injection by Triggering Time Delays\n\n')
		ebs.start_ebsibttd()
		sleep(4)
		clear()
		welcome()
	elif option == 8:
		clear()
		welcome()
		print('Your choice -- Bypass Login Page\n\n')
		logby.loginbypass()
		sleep(4)
		clear()
		welcome()
	elif option == 9:
		clear()
		print('\t\t\t\t\t\t600D 8Y3 ...')
		sleep(4)
		clear()
		exit()
	else:
		clear()
		print('Invalid option. Please enter a number between 1 and 8')
		sleep(4)
		clear()

if __name__ == '__main__':
	clear()
	welcome()

	#put here target url to check with sql injection attack script
	url = input('Enter the url you want to check: ')
	print('\n')

	#menu printing
	while(True):
		menu_option()
