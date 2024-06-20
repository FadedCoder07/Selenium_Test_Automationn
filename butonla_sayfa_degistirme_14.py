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

driver.get("C:/Users/canko/Projeler/Selenium_Test_Otamasyon/sayfa.html")

facebook_button = driver.find_element(By.XPATH, "//a[text()='Facebook']").click()
instagram_button = driver.find_element(By.XPATH, "//a[text()='Instagram']").click()
twitter_button = driver.find_element(By.XPATH, "//a[text()='Twitter']").click()
time.sleep(2)

def sekme_degistir(baslik):
    for sayfa in driver.window_handles:
        driver.switch_to.window(sayfa)
        if baslik.lower() in driver.title.lower():
            break


sekme_degistir("facebook")
print("facebook: "+driver.title)

sekme_degistir("twitter")
print("twitter: "+driver.title)

sekme_degistir("instagram")
print("instagram: "+driver.title)

sekme_degistir("selenium")
print("anasayfa: "+driver.title)

driver.quit()