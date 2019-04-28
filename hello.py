import pickle as pkl
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests
from lxml import html 
from bs4 import BeautifulSoup
from datetime import datetime
import urllib
import urllib.request
import json
from datetime import datetime
from bs4 import BeautifulSoup
import re

TAG_RE = re.compile(r'<[^>]+>')
driver = webdriver.Chrome(ChromeDriverManager().install())

def extract_product_info(product_url):
    time.sleep(5)
    driver.get(product_url)
    try:
        print("Got You....")
        driver.find_element_by_class_name('close-layer').click()
    except:
        print("Didn't get You....")

    time.sleep(5)
    driver.find_element_by_class_name('shipping-link').click()
    time.sleep(5)
    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")
    print("Calculating...")
    popup = soup.find('div', {'id': 'j-shipping-dialog'})
    #print(popup)
    return popup

if __name__ == '__main__':
    url = 'https://www.aliexpress.com/item/Hair-Accessories-Synthetic-Wig-Donuts-Bud-Head-Band-Ball-French-Twist-Magic-DIY-Tool-Bun-Maker/32457370321.html?scm=1007.13442.37932.0&pvid=f8b9f498-65d4-400f-a14f-38b4bba77546&tpp=1'
    row = extract_product_info(url)
    driver.quit()
    with open('C:/xampp/htdocs/WEBS/new.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(row.prettify())
    f_out.close()
    data = ""
    file1 = open("C:/xampp/htdocs/WEBS/myfile.txt","a")
    with open('C:/xampp/htdocs/WEBS/new.txt', 'r') as content_file:
        content = content_file.read()
        ss = str(TAG_RE.sub('', content))
        ss1 = ss.strip()
        if(len(ss1)>1):
            file1.write(ss1)
    content_file.close()
    file1.close()