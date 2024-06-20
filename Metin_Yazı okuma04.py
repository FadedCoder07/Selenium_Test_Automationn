#%%
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#%%
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
driver.maximize_window()
seckin_alan=driver.find_element(By.ID,"mp-tfa")
seckin_alan_text=seckin_alan.text
seckin_alan_baslik=seckin_alan_text.split(",")[0]
print(seckin_alan_text)
print(seckin_alan_baslik)