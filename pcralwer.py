### written in python 3 ###
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import time
import struct
import socket
########## Default Gateway Function ############
def get_default_gateway_linux():
	"""Read the default gateway directly from /proc."""
	with open("/proc/net/route") as fh:
		for line in fh:
			fields = line.strip().split()
			if fields[1] != '00000000' or not int(fields[3], 16) & 2:
				continue
			return str(socket.inet_ntoa(struct.pack("<L", int(fields[2], 16))))
################### Settings ###################
debug = 0 #set to 0 for no logs (aka when you're ready to deploy), 1 for logging
#If you need something to test on, use one of these portals: https://www.ironwifi.com/captive-portal-demos/
addr = str(get_default_gateway_linux())
geckopath = "" #required that you set your gecodriver path (see selenium setup)
############### Main Function ##################
def payloadz(target, debg, path):
	dcapabilities = webdriver.DesiredCapabilities.FIREFOX
	#### Uncomment to use Burp or desired proxy ####
	#proxyString = "127.0.0.1:8080"
	#dcapabilities['proxy'] = {
	#	"proxyType": "manual",
	#	"httpProxy": proxyString,
	#	"ftpProxy": proxyString,
	#	"sslProxy": proxyString
	#}
	################################################
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(capabilities=dcapabilities,options=options,executable_path=r'geckodriver')
	driver.get(target)
	time.sleep(1)
	print("***Foud Captive Portal HTML elements:***")
	try:
		text = driver.find_elements_by_xpath("//input[@type='text']")
		if not text:
			if debg == 1:
				print("[-] Text element not found")
		iftext = "thankyouverymuch"
		for s in text:
			s.send_keys(iftext)
			if debg == 1:
				print("[+] text field sent")
	except:
		if debg == 1:
			print("Could not send text element")
		pass
	try:
		email = driver.find_elements_by_xpath("//input[@type='email']")
		if not email:
			if debg == 1:
				print("[-] Email element not found")
		ifemail = "test@gmail.com"
		for x in email:
			x.send_keys(ifemail)
			if debg == 1:
				print("[+] Email element sent")
	except Exception as e:
		if debg == 1:
			print(e)
		pass
	try:
		checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")
		if not checkbox:
			if debg == 1:
				print("[-] Checkbox element not found")
		for h in checkbox:
			h.click()
			if debg == 1:
				print("[+] Checkbox element sent")
	except Exception as e:
		if debg == 1:
			print(e)
		pass
	try:
		button = driver.find_elements_by_xpath("//input[@type='button']")
		if not button:
			if debg == 1:
				print("[-] Button element not found")
		for d in button:
			d.click()
			if debg == 1:
				print("[+] Button element sent")
	except Exception as e:
		if debg == 1:
			print(e)
	try:
		radio = driver.find_elements_by_xpath("//input[@type='radio']")
		if not radio:
			if debg == 1:
				print("[-] Radio element not found")
		for r in radio:
			r.click()
			if debg == 1:
				print("[+] Radio element sent")
	except Exception as e:
		if debg == 1:
			print(e)
	try:
		tele = driver.find_elements_by_xpath("//input[@type='tel']")
		iftele = "2028675874"
		if not tele:
			if debg == 1:
				print("[-] Phone number element not found")
		for t in tele:
			t.send_keys(iftele)
			if debg == 1:
				print("[+] Phone number element sent")
	except Exception as e:
		if debg == 1:
			print(e)
	try:
		password = driver.find_elements_by_xpath("//input[@type='password']")
		if not tele:
			if debg == 1:
				print("[-] Password element not found")
		ifpass = "SomePW15$"
		for o in password:
			p.send_keys(ifpass)
			if debg == 1:
				print("[+] Password element sent")
	except Exception as e:
		if debg == 1:
			print(e)
	try:
		submit = driver.find_elements_by_xpath("//input[@type='submit']")
		if not submit:
			if debg == 1:
				print("[-] Submit element not found ¯\_(ツ)_/¯")
				print("[*] Exiting...")
				driver.quit()
				return
		for t in submit:
			if debg == 1:
				print("[+] Submit element sent")
			t.click()
	except Exception as e:
		if debg == 1:
			print(e)
			print("[-] Submit element not found ¯\_(ツ)_/¯")
			print("[*] Exiting...")
			driver.quit()
			return
	code = requests.get("https://google.com", verify=False).status_code#need to configure for proxy if debugging script
	if code != 200:
		if debg == 1:
			print("[*] Unable to reach google, check the portal source and make sure it will work with this script")
			print("[*] Exiting...")
			driver.quit()
			return
	elif code == 200:
		if debg == 1:
			print("[*] Elements submitted, you should be able to reach the internet")
	driver.quit()
	return
asciiArt = """
                  _        _ 
                 | |	  | |
 _ __   ___  _ __| |_ __ _| |
| '_ \ / _ \| '__| __/ _` | |
| |_) | (_) | |  | || (_| | |
| .__/ \___/|_|   \__\__,_|_|
| |						  
|_|  
           _     _	       
          (_)   | |		  
 ___ _ __  _  __| | ___ _ __ 
/ __| '_ \| |/ _` |/ _ \ '__|
\__ \ |_) | | (_| |  __/ |   
|___/ .__/|_|\__,_|\___|_|   
	| |					  
	|_|
         :
         :
     /\('')/\                                                    
     \      /
"""
if debug == 1:
	print(asciiArt)
req = requests.get("https://google.com", verify=False).status_code
if req != 200:
	payloadz(addr,debug,geckopath)
else:
	exit()
