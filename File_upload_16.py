import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
#%%
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://the-internet.herokuapp.com/upload")

file="C:/Users/canko/Projeler/Selenium_Test_Otamasyon/chrome.exe"

upload_file=driver.find_element(By.ID,"file-upload")
upload_file.send_keys(file)

driver.find_element(By.ID,"file-submit").click()

WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

baslik=driver.find_element(By.TAG_NAME,"h3").text
print(baslik)

dosya_isim=driver.find_element(By.ID,"uploaded-files").text
print(dosya_isim)

time.sleep(2)

driver.quit()
