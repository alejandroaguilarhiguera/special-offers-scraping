from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configurar Selenium con Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Para que no abra el navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://scrapeme.live"
driver.get(url+"/shop")

# Extraer elementos con Selenium
titles = driver.find_elements(By.TAG_NAME, "h2")
for title in titles:
    print(title.text.strip())




driver.quit()