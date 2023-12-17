import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://yandex.ru/images/"

driver.get(url=url)
time.sleep(3)

driver.close()
driver.quit()