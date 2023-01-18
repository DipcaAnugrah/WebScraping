import requests
from bs4 import BeautifulSoup

# URL dari halaman produk yang ingin di-scrape
url = 'https://www.tokopedia.com/nama-toko/nama-produk'

# Mengambil konten halaman produk
response = requests.get(url)

# Parsing konten halaman menjadi objek BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Mencari informasi yang diinginkan, misalnya nama produk, harga, dan deskripsi
product_name = soup.find('h1', class_='product-name').text
product_price = soup.find('span', class_='price').text
product_desc = soup.find('div', class_='product-desc').text

# Mencetak informasi yang diperoleh
print('Nama produk:', product_name)
print('Harga:', product_price)
print('Deskripsi:', product_desc)
