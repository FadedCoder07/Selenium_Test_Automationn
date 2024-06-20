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

driver.get("C:/Users/canko/Projeler/Selenium_Test_Otamasyon/iframe/sayfa1.html")

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

driver.find_element(By.ID, "email").send_keys("deneme")
time.sleep(3)

# default_content => en ana sayfaya don,, sayfanin aslina don
# parent_frame => bir ustteki frame gecis icin
# 1. ana sayfa
#   2. frame 1
#      3 frame 2
driver.switch_to.default_content()
driver.find_element(By.ID, "name").send_keys("can")
time.sleep(2)

driver.quit()






#name= driver.find_element(By.ID, "name")
#email= driver.find_element(By.ID, "email")