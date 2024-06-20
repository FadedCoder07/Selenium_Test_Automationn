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

driver.get("https://the-internet.herokuapp.com/hovers")

user = driver.find_element(By.CSS_SELECTOR, "div.figure")
isim = driver.find_element(By.CSS_SELECTOR, "div.figcaption h5")
link = driver.find_element(By.CSS_SELECTOR, "div.figcaption a")
print(isim.is_displayed())
print("isim: "+isim.text)
time.sleep(2)
# önce ActionChains class ının bir nesnesini oluşturup webdriver nesnesini veriyoruz
hareket = ActionChains(driver)
# ActionChains nesnesi ile move_to_element fonksiyonuna istediğimiz webelementi veriyoruz
hareket.move_to_element(user)
# hareket.click(link) alternatif olarak linke tıklama işlemini bu şekilde de yapabilirsiniz
# en son perform fonksiyonu action chains silsilesini tamamlayacaktır.
hareket.perform()
time.sleep(2)
print("--------")
print(user.is_displayed())
print("isim: "+isim.text)
link.click()
time.sleep(2)
url = driver.current_url
print(url)
driver.quit()