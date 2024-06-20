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
driver.get("https://www.apple.com")
time.sleep(1)
print(driver.title)
apple = driver.current_window_handle
driver.switch_to.new_window("tab")
driver.get("https://www.tesla.com")
time.sleep(2)
print(driver.title)
tesla = driver.window_handles[1]
driver.switch_to.window(apple)
print(driver.title)
time.sleep(2)
driver.switch_to.window(tesla)
print(driver.title)
time.sleep(2)
driver.switch_to.window(apple)
time.sleep(1)
driver.quit()