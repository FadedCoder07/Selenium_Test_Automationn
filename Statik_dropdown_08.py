#statik dropdownları sayfayı ilk incel dediğimizde elementler kısmında içeriğini önceden görebiliriz
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#%%
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")

dropdown = driver.find_element(By.ID, "odeme-tipi")
odeme = Select(dropdown)
odeme_tipleri = odeme.options # web element listesi, her bir option tagi

for tip in odeme_tipleri:
    print(tip.text)
    
time.sleep(2)
odeme.select_by_visible_text("Kredi Kartı")
time.sleep(2)
odeme.select_by_index(3)
time.sleep(2)
driver.quit()