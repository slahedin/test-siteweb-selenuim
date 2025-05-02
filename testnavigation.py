from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuration du navigateur en mode headless (sans interface graphique)
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Démarre Chrome avec WebDriver Manager (plus simple sur GitHub Actions)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Accès au site
driver.get("https://www.sibtel.com.tn")

# Vérification du titre de la page
assert "SIBTEL" in driver.title, f"Titre inattendu : {driver.title}"

# Fermeture du navigateur
driver.quit()
