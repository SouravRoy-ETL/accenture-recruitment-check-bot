#https://india.jobs.accenture.com
from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

username = "username@hotmail.com" #Enter your accenture username
password = "username@1" #Enter your accenture password
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver", chrome_options=options)
driver.get("https://india.jobs.accenture.com")
driver.find_element_by_id("btnCandLogin").click()
driver.find_element_by_id("ContentPlaceHolder1_UsernameTextBox").send_keys(username)
driver.find_element_by_id("ContentPlaceHolder1_PasswordTextBox").send_keys(password, Keys.ENTER)
time.sleep(2)
print("[+] Start Checking Accenture - Application Status")
url = driver.current_url
previous_value = None
while(True):
    if url == driver.current_url:
        driver.refresh()
    url = driver.current_url
    current_value = driver.find_element_by_class_name("candid-message")
    if previous_value:
        time.sleep(22)
        if (len(current_value.text) != len(previous_value)):
            #a new value is present.
            #time.sleep(22)
            print("New Status :", current_value.text)
            previous_value = current_value.text
        else:
            #document_upload = "Document Upload- Active" if current_value.text.find("advanced stage") else "Check Portal"
            print("Current Status :", current_value.text)
    else:
        #first time running the loop.
        time.sleep(22)
        #document_upload = "Document Upload- Active" if current_value.text.find("advanced stage") else "Check Portal"
        print("Current Status :", current_value.text)
        previous_value = current_value.text
    time.sleep(30)
    #print("refresh")
print(status)
