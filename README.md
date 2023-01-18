# WebScraping
```
NAMA    : DIPCA ANUGRAH
NIM     : 312210666
KELAS   : TI.22.A.4
```

## Pengertian dan Kegunaan PIP, Web Scraping
### PIP(Pip Install Python)
PIP (Python Package Index) adalah sistem manajemen paket yang digunakan untuk menginstal dan mengelola paket (atau modul) Python.

Kegunaan PIP:

1. PIP memudahkan proses instalasi paket Python yang dibutuhkan. Cukup dengan mengetik perintah `"pip install nama_paket"` di command prompt atau terminal, maka paket tersebut akan diunduh dan diinstal secara otomatis.
2. PIP juga memudahkan proses pengelolaan versi paket. Anda dapat mengecek versi paket yang terinstal, mengupgrade atau menurunkan versi paket, dan menghapus paket yang tidak dibutuhkan dengan perintah PIP yang sesuai.
3. PIP memudahkan pencarian paket yang tersedia di Python Package Index (PyPI) dengan perintah `"pip search"`
4. PIP memungkinkan untuk mengelola paket Python yang digunakan dalam proyek dengan menggunakan file requirements.txt, sehingga memudahkan untuk mengkonfigurasi lingkungan kerja dan mengatur dependensi.

Berikut ini adalah beberapa perintah dasar PIP yang sering digunakan:

1. pip install `<package_name>` : digunakan untuk menginstall paket Python baru. Contoh: `pip install requests`
2. pip uninstall `<package_name>` : digunakan untuk menghapus paket Python yang sudah terinstal. Contoh: `pip uninstall requests`
3. pip list : digunakan untuk melihat daftar paket Python yang sudah terinstal.
4. pip show `<package_name>` : digunakan untuk melihat informasi paket Python yang sudah terinstal, seperti nama, versi, dan lokasi instalasi. Contoh: pip show requests
5. pip search `<keyword>` : digunakan untuk mencari paket Python yang tersedia di PyPI berdasarkan kata kunci. Contoh: `pip search requests`

### Web Scraping
Web scraping adalah teknik yang digunakan untuk mengambil atau mengumpulkan data dari website secara otomatis. Data yang dihimpun dapat berupa teks, gambar, atau informasi lain yang tersedia pada website.

Kegunaan Web scraping:

1. Pengumpulan data: Web scraping digunakan untuk mengumpulkan data dari website yang tidak tersedia dalam format yang mudah diakses, seperti CSV atau Excel.
2. Analisis data: Setelah data dihimpun, dapat digunakan untuk melakukan analisis data, seperti mencari pola atau trend dari data tersebut.
3. Monitoring website: Web scraping dapat digunakan untuk memantau perubahan harga produk atau stok produk pada website e-commerce.
4. Penelitian: Web scraping dapat digunakan dalam penelitian, seperti mengumpulkan data opini publik dari website forum atau media sosial.
5. Pencarian lowongan kerja: Web scraping dapat digunakan untuk mencari lowongan kerja di website job portal.
6. Web scraping dapat digunakan untuk berbagai tujuan, namun perlu diingat bahwa scraping website tanpa izin dari pemilik website dapat melanggar hukum. Jika Anda berencana untuk melakukan web scraping, pastikan untuk mendapatkan izin dari pemilik website terlebih dahulu.

### Studi kasus
1. **Bukalapak**
* Source code
``` python
import requests
from bs4 import BeautifulSoup
import pandas as pd
     
URL = "https://www.bukalapak.com/c/komputer/laptop?from=nav_header"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
produk = soup.find_all("div", "bl-product-card__description")

data = []
for item in produk:
    nama = item.select(".bl-product-card__description-name")
    price = item.select(".bl-product-card__description-price p")
    data.append({"nama": nama[0].text.strip(), "harga": price[0].text.strip()})

#print(data)
df = pd.DataFrame(data)
print(df)
```
* Output
```
 nama         harga
0   pc817 pc 817 optocoupler sharp asli ori origin...         Rp500
1   OTG kabel usb micro kabel otg for samsung bb o...       Rp2.500
2   Kabel power Komputer Pc ups rice cooker lcd ka...      Rp10.000
3   KABEL POWER CPU PC KOMPUTER MONITOR KE LISTRIK...      Rp30.000
4   Kabel Splitter Audio 3.5mm Male to 3.5mm HiFi ...       Rp7.500
5                Laptop Hp 8440p Core i5 Sedang promo   Rp2.099.000
6   Kabel MHL Converter Micro USB to HDMI Kabel fo...      Rp50.000
7   Baterai Toshiba Satellite C600 C640 C666 L635 ...     Rp450.000
8                    Kabel Aux Audio 2in1 For Speaker       Rp5.000
9   Baterai Asus X450 X450C X450CA X450CP X450V X4...     Rp189.000
10  Baterai Asus A46 A46C A46CA A46CB A46CM A46 K4...     Rp189.000
11  Baterai Ori Acer v5 V5-431 V5-431G V5-471 V5-4...     Rp184.500
12  Baterai HP G4 430 431 G42 DV6 DM4 1000 Compaq ...     Rp164.900
13  Kabel Power VGA 6 pin female to 2 x 8 Pin male...      Rp25.000
14                         Laptop Lenovo T410 Core i5   Rp1.949.000
15               Laptop Dell 5510 Core i5 promo harga   Rp1.999.000
16  Charger Adaptor Asus Transformer Book T100 T10...     Rp130.000
17  Baterai Ori Lenovo G40 G400s G40-30 G40-45 G50...     Rp550.000
18  BAUT SEKRUP MUR SCREW LAPTOP NOTEBOOK NETBOOK ...       Rp5.000
19            APC Kabel c13 c14 2mtr 1mm cable ap9870      Rp75.000
20  Dual psu atx 24 Pin Cable Kabel PC Power Mothe...      Rp50.000
21  Laptop Dell 6510 Core i7 - Support Gaming - Bo...   Rp2.471.010
22  kabel splitter 8 pin pcie to dual 6 2 gaming m...      Rp26.000
23  Keyboard Laptop Lenovo Ideapad 110-14 110-14ib...      Rp60.000
24  Adaptor Charger Original Asus X200 X200M X200C...      Rp74.250
25  murah kabel power notebook adaptor laptop 3 lu...       Rp9.690
26  Apple Macbook Air 2020 M1 Chip 13 inch 512GB G...  Rp14.280.000
27  Baterai Acer ES1-411 ES1-431 E1-410 E1-410G E1...     Rp184.500
28  Kabel Power Cord UPS APC Rack Server C13 to Sc...     Rp125.000
29  Laptop Dell E6410 Core i5 - RAM 4GB -HDD 320GB...   Rp1.929.510
```

2. **Glints**
``` python
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://glints.com/id/opportunities/jobs/explore?keyword=jakarta&country=ID&locationName=Indonesia"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
jobs = soup.find_all('div',{'class':'ExploreTabsc__Body-sc-gs9c0s-3 fFULhl'})
data = []
for job in produk:
    title = job.select('.job card title')
    company = job.select('.job-company')
    location = job.select('.job-location')
    print(title)
    # data.append({"Title": title[0].text.strip(), "Company": company[0].text.strip(), "Location": location[0].text.strip()})

#print(data)
df = pd.DataFrame(data)
print(df)
```
3. **Shopee**
* Source code
``` python
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
    print(nama,harga)
    list_nama.append(nama)
    list_harga.append(harga)

df = pd.DataFrame({'Nama Barang': list_nama, 'Harga Barang': list_harga})
writer = pd.ExcelWriter('dipca.xlsx')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
```
* Output
```
HOOLIGANS Boardshort Academica - Black 84.000
Atasan Holigans T-shirt Premium Black Unisex Bisa COD 44.700
HOOLIGANS Hoodie Bold Speziale - Sage Green 189.000
HOOLIGANS Sweater Crewneck Bold Speziale - Sage Green 165.600
Hooligans Harrington Jacket Harry - Navy 205.000
Hooligans Jacket Tracktop Linea Lyte - Black 189.000
HOOLIGANS Hoodie Diamante - Black 189.000
HOOLIGANS Sweater Crewneck VAR Away - White 165.600
HOOLIGANS Hoodie Visione - Black 169.000
HOOLIGANS Hoodie Bold BRA Crest - Emerald Green 185.000
HOOLIGANS Sweater Crewneck Bold Netral - Light Gray 165.600
Hooligans Sandal Santos Mark - White 89.000
HOOLIGANS T-Shirt SYG Type - Black 88.800
HOOLIGANS Hoodie Bold Linea - Army Green 189.000
HOOLIGANS Hoodie Bold Analogue - Beige 189.000
```
4. **Olx**
``` python
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
```