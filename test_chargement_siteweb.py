import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSibtelMenu(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_chargement_site_web(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accéder au site
        driver.get("https://www.sibtel.com.tn")
        print("Site ouvert avec succès.")
        time.sleep(2)

        # Cliquer sur le bouton 'Connexion' (icône)
        bouton_connexion = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='icon-home-button' and contains(text(), 'Connexion')]")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bouton_connexion)
        driver.execute_script("arguments[0].click();", bouton_connexion)
        print("Bouton 'Connexion' cliqué avec succès.")
        time.sleep(2)

        # Saisir les identifiants
        wait.until(EC.visibility_of_element_located((By.ID, "formEmail"))).send_keys("slaheddine.chaabani@sibtel.com.tn")
        driver.find_element(By.ID, "password").send_keys("Sibtel@20112023+")

        # Cliquer sur le bouton "Connexion"
        bouton_submit_connexion = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='txt' and text()='Connexion']/..")))
        driver.execute_script("arguments[0].click();", bouton_submit_connexion)
        print("Connexion effectuée avec succès.")
        time.sleep(4)

        # Cliquer sur le menu Upload Swift
        upload_swift_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@id='74']//a[contains(text(), 'Upload Swift')]")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_swift_link)
        driver.execute_script("arguments[0].click();", upload_swift_link)
        print("Lien 'Upload Swift' cliqué avec succès.")
        time.sleep(3)

        # Upload fichier
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file_to_upload")))
        file_input.send_keys("C:\\Users\\Admin\\Desktop\\selenuim_tests\\test\\EXPWEB_20250309.txt")

        # Cliquer sur le bouton Upload
        upload_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.upload-button")))
        driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)
        driver.execute_script("arguments[0].click();", upload_button)
        print("Fichier chargé avec succès.")
        time.sleep(4)

        # Déconnexion
        logout_form = wait.until(EC.presence_of_element_located((By.ID, "logout-form")))
        driver.execute_script("arguments[0].submit();", logout_form)
        print("Déconnexion effectuée avec succès.")
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
