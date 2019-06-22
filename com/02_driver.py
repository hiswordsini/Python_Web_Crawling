from selenium import webdriver
import time

url = "https://www.instagram.com/explore/tags/서촌/"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver.exe", options=options
)

driver.implicitly_wait(5)
driver.get(url)
time.sleep(5)

pageString = driver.page_source
print(pageString)

driver.quit()