# Please provide your username and password in line 29 and line 34 respectively.
# In command line (Windows) or Terminal (Linux/macOS), to run the script, enter the line in following format
# python3 CommandLineEmailer.py <To-Address> <Message> (in Linux)
# py CommandLineEmailer.py <To-Address> <Message> (in Windows)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys

if len(sys.argv) < 2:
    print('Usage: py CommandLineEmailer.py [toAddress] [message]')
    sys.exit()
    
toAddress = sys.argv[1]
messageInList = sys.argv[2:]

message = ' '.join(messageInList)

options = Options()
options.add_argument('--no sandbox')
options.add_argument('--disable-setuid-sandbox')

browser = webdriver.Chrome(options=options)

browser.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

userElem = browser.find_element_by_name('identifier')
userElem.send_keys(<enter Email ID here>)
browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
browser.implicitly_wait(4)

password_field = browser.find_element_by_name("password")
password_field.send_keys(<enter password here>)
browser.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()

browser.find_element_by_class_name("z0").click()

#To address
To = browser.find_element_by_class_name('vO')
To.send_keys(toAddress)

#Subject box
subject = browser.find_element_by_class_name('aoT')
subject.send_keys('Automated message from '+toAddress)

#Enters message in message box
subject.send_keys(Keys.TAB + message + Keys.ENTER)

browser.find_element_by_class_name("dC").click()

print('Message sent!')
browser.quit()
