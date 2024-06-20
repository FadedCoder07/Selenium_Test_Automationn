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
from selenium.webdriver.chrome.options import Options
#%%
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
options = ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])#Tarayıcının otomasyon tarafından kontrol edildiğini belirtmemesi için gerekli ayarı yapar.
options.add_experimental_option('useAutomationExtension', False)# Otomasyon uzantısını devre dışı bırakır.

options.add_argument("--disable-infobars")#Tarayıcıda bilgi çubuklarını (infobars) devre dışı bırakır.
options.add_argument("--allow-running-insecure-content")#Güvenli olmayan içeriklerin çalıştırılmasına izin verir.
options.add_argument("--disable-notifications")#Tarayıcı bildirimlerini devre dışı bırakır.
options.add_argument("--disable-save-password")# Şifre kaydetme özelliğini devre dışı bırakır.
options.add_argument("--disable-extensions")#Tüm tarayıcı uzantılarını devre dışı bırakır.
options.add_argument("download.default_directory=C:/Users/canko/Projeler/Selenium_Test_Otamasyon")#Dosya indirme konumunu
options.add_argument("--window-size=768,1024")#Tarayıcı penceresinin boyutlarını 768x1024 piksel olarak ayarlar.
options.add_argument("--disable-popup-blocking")#Açılır pencere engelleyiciyi devre dışı bırakır.
driver = webdriver.Chrome(service=chrome_service, options=options)

# driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("http://www.google.com")
driver.get("https://www.ucuzabilet.com")
time.sleep(2)
driver.quit()
driver.get("https://www.ucuzabilet.com")
