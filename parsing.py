import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def creating_a_folders(name):
    if not os.path.isdir(name):
         os.mkdir(name)

def get_hyperlinks(query, folder_name):
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    time.sleep(2) 
    url = f"https://yandex.ru/images/search?text={query}&isize=eq&iw=1920&ih=1080"
    driver.get(url)
    time.sleep(3)
    view_all_button = driver.find_element_by_css_selector(".cl-teaser__button")
    view_all_button.click()
    with open(f"{folder_name}/{query}.txt", "w") as f:
        time.sleep(2)
        images = driver.find_elements_by_css_selector(".serp-item__link")
        for i, image in enumerate(images):
            if i >= 1000:
                break
            link = image.get_attribute("href")
            f.write(f"{link}\n")
            image.click()
            time.sleep(2)
    
    
    driver.quit()

def download_img(folder_name, query):
    with open(f"{folder_name}/{query}.txt", "r") as f: 
        creating_a_folders(f"{folder_name}/images")
        for i, line in enumerate(f):
            if i >= 1000:
                break
            url = line.strip()
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"{folder_name}/images/{query}_{i:04d}.jpg", "wb") as img_file:
                    img_file.write(response.content)

def main():
    
    if os.path.exists("dataset"):
        for file_name in os.listdir("dataset"):
            os.remove(f"dataset/{file_name}")
        os.rmdir("dataset")
    
    creating_a_folders("dataset")
    get_hyperlinks("cat", "dataset")
    time.sleep(5)
    download_img("dataset", "cat")
    get_hyperlinks("dog", "dataset")
    time.sleep(5)
    download_img("dataset", "dog")
    time.sleep(15)
