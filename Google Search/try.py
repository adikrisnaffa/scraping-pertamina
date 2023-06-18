import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

chrome_driver_path = 'path_to_chromedriver/chromedriver.exe'

driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hard Disk")
search_box.send_keys(Keys.RETURN)

search_results = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)

shopping_link = driver.find_element(By.LINK_TEXT, "Shopping")
shopping_link.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "rso"))
)

product= driver.find_elements(By.CLASS_NAME,'sh-dgr__content')

product_descprition_list=[]
product_price_list=[]
product_seller_url_list=[]


for items in product:
    product_descprition= items.find_element(By.CLASS_NAME,'C7Lkve').find_element(By.CLASS_NAME,'EI11Pd').find_element(By.CLASS_NAME,'tAxDx').get_attribute('innerHTML')
    product_price = items.find_element(By.CLASS_NAME,'XrAfOe').find_element(By.CLASS_NAME,'kHxwFf').find_element(By.CLASS_NAME,'QIrs8').find_element(By.TAG_NAME,'span').get_attribute('innerHTML')
    product_price=product_price.replace('&nbsp;','')
    product_seller_url= items.find_element(By.CLASS_NAME,'eaGTj.mQaFGe.shntl').find_element(By.TAG_NAME,'div').find_element(By.TAG_NAME,'a').get_attribute('href')   
    print(product_descprition, product_price, product_seller_url)

    product_descprition_list.append(product_descprition)
    product_price_list.append(product_price)
    product_seller_url_list.append(product_seller_url)

product_search_df = pd.DataFrame({'Nama Produk': product_descprition_list,'Harga Produk': product_price_list,
                                  'URLs': product_seller_url_list})
product_search_df.to_excel('Shopping.xlsx', index=False)