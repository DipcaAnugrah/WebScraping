from bs4 import BeautifulSoup
import requests

url = "https://www.olx.co.id/mobil/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
judul_iklan = soup.find_all(
    'a', class_='marginright5 link linkWithHash detailsLink')
harga_mobil = soup.find_all('p', class_='price')
for iklan, harga in zip(judul_iklan, harga_mobil):
    print(iklan.get_text())
    print(harga.get_text())
