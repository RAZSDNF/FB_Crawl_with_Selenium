from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import subprocess
from fbchat import Client
import time
from fbchat.models import *
from selenium.webdriver.support import expected_conditions as EC
# chrome_options = Options()
# #chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--no-startup-window")
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# chrome_options.add_argument("--window-size=1920x1080")
# driver = webdriver.Chrome(chrome_options=chrome_options)
from selenium.webdriver.support.wait import WebDriverWait
CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"


chrome_options = Options()
chrome_options.add_argument("--headless")
# for headless to work in cloud https://stackoverflow.com/questions/60304251/unable-to-open-x-display-when-trying-to-run-google-chrome-on-centos-rhel-7-5
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH
#remove alerts
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#end remove alerts
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                          )

url = "https://www.facebook.com"

driver.get(url)
time.sleep(3)
username="xxxx"
password="xxxxx"
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('u_0_b').click()
fb_post_url="https://www.facebook.com/groups/xxxxxx/permalink/xxxxxxxx"
while True:
    try:
        time.sleep(10)
        driver.get("https://www.facebook.com/groups/xxxxxxx")
        time.sleep(10)
        driver.get(fb_post_url)
        time.sleep(10)
        ul_an1= driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul")
        print(ul_an1.text.lower())
        if ("dec" in ul_an1.text.lower()):
            p = subprocess.Popen(["google-chrome", "www.google.com"], stdout=subprocess.PIPE)
            client = Client('xxxxxx', 'xxxxxxx')
            while (True):
                time.sleep(5)
                print("Sending Message")
                sent = client.send(Message(text="Found Something"), thread_id="xxxxxxx",
                                   thread_type=ThreadType.USER)
                if sent:
                    print("Message sent successfully!")
        elif("groups/xxxxxx/permalink/" in ul_an1.text.lower()):
            fb_post_url="https://www.facebook.com/groups/xxxxxx/permalink/"+ul_an1.text.split("groups/xxxxxx/permalink/")[1].encode("utf-8").split("/")[0]
            f = open("/home/ali/PycharmProjects/fb_crwal/Crawl.py", "r")
            data = f.readlines()
            data[47]='fb_post_url='+"\""+fb_post_url+"\"\n"
            fw = open("/home/ali/PycharmProjects/fb_crwal/Crawl.py", "w")
            fw.write("".join(data))
            fw.close()
            f.close()
            driver.close()
            cmd = 'python2 '+os.path.dirname(os.path.abspath(__file__))+"/Crawl.py"
            os.system(cmd)


    finally:
        print ("Current Time: "+str(datetime.now().strftime("%H:%M:%S")))





