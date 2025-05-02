from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')  # mode sans interface graphique
driver = webdriver.Chrome(options=options)

driver.get("https://www.sibtel.com.tn")

assert "SIBTEL" in driver.title  # Remplace "SIBTEL" si le titre est différent

driver.quit()
