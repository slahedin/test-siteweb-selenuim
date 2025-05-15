import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSibtelMenu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_chargement_site_web(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accéder au site
        driver.get("https://www.sibtel.com.tn")
        time.sleep(4)

        # Trouver le bouton connexion et le cliquer via JavaScript
        bouton_connexion = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='icon-home-button' and contains(text(), 'Connexion')]")
        ))
        driver.execute_script("arguments[0].click();", bouton_connexion)
        print("boutton 'Connexion' cliqué avec succès.")
        time.sleep(3)

        # Saisir l'email et le mot de passe
        driver.find_element(By.ID, "formEmail").send_keys("slaheddine.chaabani@sibtel.com.tn")
        driver.find_element(By.ID, "password").send_keys("Sibtel@20112023+")

        # Cliquer sur le bouton "Connexion" via JS
        bouton_connexion = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='txt' and text()='Connexion']/..")
        ))
        driver.execute_script("arguments[0].click();", bouton_connexion)
        print("Connexion avec succès.")
        time.sleep(5)

        # Chercher le bouton Upload Swift puis cliquer
        upload_swift_link = driver.find_element(By.XPATH, "//li[@id='74']//a[contains(text(), 'Upload Swift')]")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_swift_link)
        time.sleep(5)
        upload_swift_link.click()
        print("Le bouton Upload est cliqué avec succès.")
        time.sleep(5)

        # Upload du fichier
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file_to_upload")))
        file_input.send_keys("C:\\Users\\Admin\\Desktop\\selenuim_tests\\test\\EXPWEB_20250309.txt")

        # Attendre que le bouton soit présent
        upload_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.upload-button")))

        # Scroller jusqu’à lui et forcer le clic
        driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)
        time.sleep(5)
        driver.execute_script("arguments[0].click();", upload_button)
        print("Le chargement est effectué avec succès.")
        time.sleep(5)

        # Déconnexion
        logout_form = driver.find_element(By.ID, "logout-form")
        driver.execute_script("arguments[0].submit();", logout_form)
        print("Déconnexion avec succès.")
        time.sleep(8)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
