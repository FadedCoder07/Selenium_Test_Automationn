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
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")
orta_boy=driver.find_element(By.CSS_SELECTOR,"input[value='Orta']")
print(orta_boy.is_selected())
orta_boy.click()
print(orta_boy.is_selected())

zeytin=driver.find_element(By.CSS_SELECTOR,"input[value='zeytin']")
mantar=driver.find_element(By.CSS_SELECTOR,"input[value='mantar']")
zeytin.click()
mantar.click()
print(zeytin.is_selected())