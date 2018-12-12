#!/usr/bin/python2

options='''
press  1  to  open default web browser :   
press  2  to  check currnet logined user  :   
press  3  to  ask user input  and search in google  :   
press  4  to  check number of tabs in your web browser :   
press  5  to  logout your system graphically  :   
press  6  to  login  facebook account  :   
press  7  to  send email to someone  :   
press  8  to  list all connected ip and mac in your current network  :  
''' 
print options
choice=raw_input()
import webbrowser as wb
from selenium import webdriver 
import commands 
# put your if else code here 
if choice=='1' or choice=='3' or choice=='4' or choice=='6':
	driver = webdriver.Chrome(executable_path='/home/nilesh/Downloads/chromedriver')	
	
if choice=='1':
	#wb.open_new_tab("http://www.google.com")
	driver.get('https://www.google.com/')		
elif choice=='3':
	search=raw_input("Enter the Query to search:")
	#wb.open_new_tab("https://www.google.com/search?q="+search)
	driver.get('https://www.google.com/search?='+search)
elif choice=='4':
	number_of_tabs=len(driver.window_handles)
	print number_of_tabs
elif choice=='5':
	curr_username=commands.getoutput("whoami")
	commands.getoutput("sudo pkill -u "+curr_username)
