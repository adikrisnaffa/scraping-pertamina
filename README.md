# Google Shopping Scraper

Proyek ini adalah scraper Python yang digunakan untuk melakukan scraping data dari Google Shopping. Menggunakan Python, Selenium, dan Pytest, proyek ini memungkinkan untuk mengumpulkan informasi produk dari halaman 1 hingga halaman 5 hasil pencarian di Google Shopping "HARD DISK"

## Persyaratan

- Python 3.11.3
- Selenium
- Webdriver (untuk browser yang diinginkan, misalnya ChromeDriver untuk Chrome)

Pastikan telah menginstal Python dan mengatur lingkungan virtual (seperti dengan menggunakan venv). Selanjutnya, instal Selenium dan ChromeDriver menggunakan perintah berikut:
```
pip install selenium
```
Pastikan juga telah mengunduh dan menginstal Webdriver yang sesuai untuk browser yang akan digunakan dalam pengujian. Pastikan versi Webdriver sesuai dengan versi browser yang gunakan.

## Instalasi
1. Clone repositori ini ke direktori lokal:

```
git clone https://github.com/adikrisnaffa/scraping-pertamina.git
```

2. Masuk ke direktori proyek:

```
cd scraping-pertamina
```
3. Instal dependensi yang diperlukan:

```
pip install -r requirements.txt
```

## Menjalankan Test Automation

1. Menjalankan tes menggunakan Pytest. Pastikan berada di dalam direktori proyek sebelum menjalankan perintah berikut:
```
pytest test_hardisk.py
```
Perintah ini akan menjalankan semua tes yang ada dalam proyek.

2. (Opsional) Jika ingin menjalankan Test Automation menggunakan Docker, pastikan telah menginstal Docker dan Docker Compose. Kemudian jalankan perintah berikut untuk membangun dan menjalankan container:

```
docker-compose up
```

## Kontribusi

Kontribusi terbuka untuk proyek ini sangat diterima! Jika ingin berkontribusi, silakan buat pull request atau buka issue baru untuk membahas perubahan yang diusulkan.
