import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#%%
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()
driver.get("https://www.homeexchange.com/")


# Arama kutusunu bulma ve yazı yazma
arama_kutusu = driver.find_element(By.XPATH, '//input[@class="form-control autocomplete search-field"]')
arama_kutusu.send_keys("top 50")

# Butonu bulma ve tıklama
buton = driver.find_element(By.XPATH, '//button[@class="btn btn-default dashboard-search-button"]')
buton.click()

driver.execute_script("window.scrollBy(0,300)", "")
time.sleep(3)
driver.execute_script("window.scrollBy(0,3000)", "")
time.sleep(3)

center_hill = driver.find_element(By.CSS_SELECTOR, 'a.ellipsis[title="Center Hill Lakehouse with Incredible Views"]')
driver.execute_script("arguments[0].scrollIntoView()", center_hill)
time.sleep(3)
driver.execute_script("window.scrollBy(0,-200)", "")
time.sleep(3)
driver.quit()