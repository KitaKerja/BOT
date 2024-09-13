import os
import zipfile
import requests
import shutil

# Fungsi untuk mendownload dan menginstall ChromeDriver
def download_chromedriver():
    chrome_driver_version = "114.0.5735.90"  # Sesuaikan dengan versi Chrome yang didukung oleh server
    chrome_driver_url = f"https://chromedriver.storage.googleapis.com/{chrome_driver_version}/chromedriver_linux64.zip"
    chrome_driver_path = "/usr/local/bin/chromedriver"  # Path tempat ChromeDriver disimpan

    if not os.path.exists(chrome_driver_path):
        print("Downloading ChromeDriver...")
        response = requests.get(chrome_driver_url, stream=True)
        with open("chromedriver.zip", "wb") as file:
            file.write(response.content)
        
        # Ekstrak file zip
        with zipfile.ZipFile("chromedriver.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
        
        # Pindahkan ChromeDriver ke /usr/local/bin
        shutil.move("chromedriver", chrome_driver_path)
        os.chmod(chrome_driver_path, 0o755)  # Berikan izin eksekusi
        
        print("ChromeDriver installed successfully!")

# Panggil fungsi untuk mendownload ChromeDriver jika belum ada
download_chromedriver()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fungsi untuk menjalankan satu bot
def run_bot(video_url):
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    try:
        # Buka URL video
        driver.get(video_url)

        # Tunggu hingga halaman dimuat
        time.sleep(5)

        # Klik elemen video. Pastikan selektor sesuai elemen video di halaman.
        video = driver.find_element(By.TAG_NAME, 'video')
        video.click()

        # Tunggu selama 3 menit (180 detik)
        time.sleep(180)

    finally:
        # Tutup browser setelah selesai
        driver.quit()

# URL video yang akan dibuka oleh bot
video_url = "https://doods.cloud/e/2SQR720YdA3x18lZBgNkXudBGjwcuyo3"

# Menjalankan 100 bot
for _ in range(100):
    run_bot(video_url)
