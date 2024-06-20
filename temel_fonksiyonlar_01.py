#%%
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
#%%
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("http://www.apple.com")
baslik=driver.title
link=driver.current_url
if "apple.com" in link:
    print("suanki link:"+link)
    print("site başlığı:",baslik)
driver.maximize_window()
time.sleep(3)

driver.get("http://www.tatilbudur.com")
baslik=driver.title
link=driver.current_url
if "tatilbudur.com" in link:
    print("suanki link:"+link)
    print("site başlığı:",baslik)
driver.back()
baslik=driver.title
driver.save_screenshot("./ekrangoruntusu.png")#fonksiyonun çalıştğını görmek için
if "Apple" in baslik:
    print("dogru sayfaya donuldu")
#else:
    #driver.save_screenshot("./ekrangoruntusu.png")# anlık olarak neden yanlış sayfaya gittiğimizi ve hangi sayfada 
    #olduğumuzu test edip görebilmek için olumsuz blokta kullanıyoruz
    
#%%
