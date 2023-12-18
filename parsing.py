import os
import requests
import time
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def creating_a_folders(name: str) -> None:
    if not os.path.isdir(name):
        os.mkdir(name)
        print("Папка создана")
    else:
        print("Папка уже существует")



def get_hyperlinks(query:str, quantity:int) -> None:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    time.sleep(2) 
    url = f"https://yandex.ru/images/search?text={query}"
    driver.get(url=url)
    time.sleep(3)
    driver.maximize_window()
    time.sleep(10)
    view_all_button = driver.find_element(By.CSS_SELECTOR, "a.Link.SimpleImage-Cover")
    view_all_button.click()
    
    with open(f"urls_{query}.txt", "w") as file:
        for i in range(quantity):
            try:
                time.sleep(2)
                link = driver.find_element(By.CSS_SELECTOR, "a.Button2_view_action").get_attribute("href")
                file.write(link + "\n")
                driver.find_element(By.CSS_SELECTOR, "div.CircleButton:nth-child(4)").click()
            except:
                continue
    driver.close()
    driver.quit()
    print("Все норм")
    

'''
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
'''



def main() -> None:
    creating_a_folders("dataset")
    request = "cat"
    get_hyperlinks(request, 10)

if __name__ == "__main__":
    main()
    
    
    
