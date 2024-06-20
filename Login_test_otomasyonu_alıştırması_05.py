#ilk önce test edilmeli sonrasında otomasyon haline getirilmeli
#test beklenenleri karşılıyor mu?
#1. isteneni yapıyor mu?(pozitif) 2.istenmeyeni yapıyor mu?(negatif)
#%%
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#%%
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()

#internett login sayfasina git https://the-internet.herokuapp.com/login
driver.get("https://the-internet.herokuapp.com/login")
#kullanici adi gir
driver.find_element(By.ID,"username").send_keys("test")
#sifre gir
driver.find_element(By.ID,"password").send_keys("asdf")
# log in dugmesine tikla
driver.find_element(By.CLASS_NAME,"radius").click()
# yanlis kullanici adi Your username is invalid!
mesaj_user=driver.find_element(By.ID,"flash").text

if "Your username is invalid!" in mesaj_user:
    print("yanlış kullanıcı adı doğru çalışıyor ")
else:
    print("HATA:yanlış kullanıcı adı doğru çalışmıyor")

#yanlis sifre girince: Your password is invalid!
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("asdf")

driver.find_element(By.CLASS_NAME,"radius").click()
mesaj_pass=driver.find_element(By.ID,"flash").text

if "Your password is invalid!" in mesaj_pass:
    print("yanlış şifre adı doğru çalışıyor ")
else:
    print("HATA:yanlış şifre doğru çalışmıyor")

#ikisi de dogru ise: mesaj: You logged into a secure area! link secure icerecek   sayfa da secure area
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")

driver.find_element(By.CLASS_NAME,"radius").click()
mesaj_dogru=driver.find_element(By.ID,"flash").text

if "You logged into a secure area!" in mesaj_dogru:
    print("bilgiler doğru çalışıyor ")
else:
    print("HATA:bilgiler doğru çalışmıyor")

link=driver.current_url

if "secure" in link:
    print("link secure içeriyor")
else:
    print("secure içermiyor")
    
dogru_mesaj = driver.find_element(By.CSS_SELECTOR, "h2").text
print("dogru mesaj: "+dogru_mesaj)

if "Secure Area" in dogru_mesaj:
    print("Sayfa basligi dogru")
else:
    print("HATA: sayfa basligi yanlis")
    
#logout dugmesine tikla
driver.find_element(By.XPATH, "//i[contains(text(),'Logout')]").click()

#sayfa linkini dogrula
if "login" in driver.current_url:
    print("login sayfasina donduk")
else:
    print("HATA: login sayfasina donmedi")
    
#%%
def login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    mesaj = driver.find_element(By.ID, "flash").text
    return mesaj
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()


mesaj = login("asdf", "xyz")
assert  "Your username invalid!" in mesaj
    
    
    
    
    
    
    
    
    
    
    
    
    
    
