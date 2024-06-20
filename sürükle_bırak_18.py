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
from selenium.webdriver import ActionChains
#%%
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demoqa.com/droppable/")

kaynak = driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div")
hedef = driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div.drop-box")

print("Once: "+hedef.text)
action = ActionChains(driver)
action.drag_and_drop(kaynak, hedef).perform()
time.sleep(2)
print("Sonra: "+hedef.text)
time.sleep(2)
driver.quit()