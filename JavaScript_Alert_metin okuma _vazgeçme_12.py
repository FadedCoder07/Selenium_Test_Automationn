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
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

buton2=driver.find_element(By.XPATH,"(//button)[2]")
buton2.click()
time.sleep(5)
uyarı=Alert(driver)
uyarı.dismiss()

result=driver.find_element(By.ID,"result").text
print(result)

buton3=driver.find_element(By.XPATH,"(//button)[3]")
buton3.click()
WebDriverWait(driver, 3).until(expected_conditions.alert_is_present())

uyarı.send_keys("deneme")
time.sleep(5)
uyarı.accept()