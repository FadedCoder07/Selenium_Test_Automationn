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
#driver.implicitly_wait(20)# ilk saniyelerde istenilen elment bulunmazsa 20 sn bekleme
#bulursa kod devam edecek
#driver nesnesi ile çalışıyor bir kere başta bunu belirlememiz kodda hep driver iel beraber çalışacak
driver.get("https://pynishant.github.io/Selenium-python-waits.html")
tryit = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver, 45).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))
clickme = driver.find_element(By.XPATH, "//button[contains(text(), 'CLICK ME')]").click()

WebDriverWait(driver, 3).until(expected_conditions.alert_is_present())

uyari = Alert(driver)
time.sleep(1)
uyari.accept()











#implicit wait - gizli bekleme
#explicit wait - açıktan bekleme