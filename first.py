#!/usr/bin/python2


import os,time,commands,webbrowser    #importing libraries

menu='''
Press 1 to check current time and date :
Press 2 to scan all your mac address in your currrent Connected Network : 
Press 3 to shutdown your machine after 15 min :
Press 4 to search somethig on google :
Press 5 to logout your current machine :
Press 6 to Shutdown all connected system in your current network :
Press 7 to updATE status in facebook :
Press 8 to to list ip address of given website :
'''
print menu
choice=raw_input("enter your choice: ")      #taking user input

if choice=="1":
	print "Showing Current date and time"
	time.sleep(2)
	print time.ctime()

elif choice=="2":
	print "Scanning MAC addresses of all connected machines"
	time.sleep(2)
	print commands.getoutput("arp -a | cut -d 't' -f2 | cut -d '[' -f1")
	
	
elif choice=="3":
	time.sleep(2)
	print "system is shuting down in 15 min"
	os.system("shutdown -t 15")

elif choice=="4":
	search=raw_input("Enter your Query")    #query to search on google
	time.sleep(2)
	webbrowser.open_new_tab("https://www.google.com/search?q="+search)
	
elif choice=="5":
	os.system()
	time.sleep(2)

elif choice=="6":
	os.system()
	time.sleep(2)

elif choice=="7":
	os.system()
	time.sleep(2)

elif choice=="8":
	os.system()
	time.sleep(2)

