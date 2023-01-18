from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi. add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

key = "holigans"
shopee_link = "https://shopee.co.id/search?keyword={}".format(key)
driver.set_window_size(1300, 800)
driver.get(shopee_link)
time.sleep(5)

driver.save_screenshot("home.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup(content, 'html.parser')
# print(data.encode("utf-8"))
list_nama, list_harga = [], []
for area in data.find_all('div', class_="col-xs-2-4 shopee-search-item-result__item"):
    # print(area)
    nama = area.find('div', class_="ie3A+n bM+7UW Cve6sh").get_text()
    harga = area.find('span', class_="ZEgDH9").get_text()
    list_nama.append(nama)
    list_harga.append(harga)

df = pd.DataFrame({'Nama Barang': list_nama, 'Harga Barang': list_harga})
writer = pd.ExcelWriter('dipca.xlsx')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
