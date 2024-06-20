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

driver.get("http://www.ducduckgo.com")
driver.maximize_window()
aramakutusu=driver.find_element(By.ID,"searchbox_input")
aramakutusu.send_keys("selenium")

driver.find_element(By.XPATH, '//button[@aria-label="Search"]').click()
#search_button.click()
sonuca_tıkla=driver.find_element(By.ID,"r1-3").click()

print("Araştırma yapıldı")



