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
driver.get("https://www.imdb.com")
driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()
film_isimleri=driver.find_elements(By.XPATH,"//table/tbody//tr//td[@class='titleColumn']/a")

for i in film_isimleri:
    if i.text[-5:-1] == "2000":#click() diyerek her 20 filme tek tek tıklaaybiliriz amaca uygun burası düzenlenebilir
                                    #film_isimleri[i] bir elementtir
        print(i.text)

driver.quit()
                                
                                 