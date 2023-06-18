from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.hardisk
def test(context):
    search = context.find_element(By.NAME, 'q')
    search.send_keys('HARD DISK' + Keys.ENTER)
    time.sleep(3)

    product_descprition_list = []
    product_price_list = []
    product_seller_url_list = []

    # Page 1
    shopping = context.find_element(By.XPATH, "//div[contains(text(),'Shopping')]")
    shopping.click()
    time.sleep(3)
    products = context.find_elements(By.CLASS_NAME, 'sh-dgr__content')
    extract_product_data(products, product_descprition_list, product_price_list, product_seller_url_list)

    # Page 2
    page_2 = context.find_element(By.XPATH, '//tbody/tr[1]/td[3]/a[1]')
    page_2.click()
    time.sleep(5)
    products = context.find_elements(By.CLASS_NAME, 'sh-dgr__content')
    extract_product_data(products, product_descprition_list, product_price_list, product_seller_url_list)

    # Page 3
    page_3 = context.find_element(By.XPATH, '//tbody/tr[1]/td[4]/a[1]')
    page_3.click()
    time.sleep(5)
    products = context.find_elements(By.CLASS_NAME, 'sh-dgr__content')
    extract_product_data(products, product_descprition_list, product_price_list, product_seller_url_list)

    # Page 4
    page_4 = context.find_element(By.XPATH, '//tbody/tr[1]/td[5]/a[1]')
    page_4.click()
    time.sleep(5)
    products = context.find_elements(By.CLASS_NAME, 'sh-dgr__content')
    extract_product_data(products, product_descprition_list, product_price_list, product_seller_url_list)

    # Page 5
    page_5 = context.find_element(By.XPATH, '//tbody/tr[1]/td[6]/a[1]')
    page_5.click()
    time.sleep(5)
    products = context.find_elements(By.CLASS_NAME, 'sh-dgr__content')
    extract_product_data(products, product_descprition_list, product_price_list, product_seller_url_list)

    product_search_df = pd.DataFrame({
        'Nama Produk': product_descprition_list,
        'Harga Produk': product_price_list,
        'URLs': product_seller_url_list
    })
    product_search_df.to_excel('Shopping1.xlsx', index=False)

def extract_product_data(products, description_list, price_list, url_list):
    for product in products:
        product_description = product.find_element(By.CLASS_NAME, 'C7Lkve').find_element(By.CLASS_NAME, 'EI11Pd').find_element(By.CLASS_NAME, 'tAxDx').get_attribute('innerHTML')
        product_price = product.find_element(By.CLASS_NAME, 'XrAfOe').find_element(By.CLASS_NAME, 'kHxwFf').find_element(By.CLASS_NAME, 'QIrs8').find_element(By.TAG_NAME, 'span').get_attribute('innerHTML')
        product_price = product_price.replace('&nbsp;', '')
        product_seller_url = product.find_element(By.CLASS_NAME, 'eaGTj.mQaFGe.shntl').find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'a').get_attribute('href')

        description_list.append(product_description)
        price_list.append(product_price)
        url_list.append(product_seller_url)
