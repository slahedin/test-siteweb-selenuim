import unittest
import time
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSibtelMenu(unittest.TestCase):

    def setUp(self):
        # Configuration Chrome Headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Chargement des variables d'environnement
        load_dotenv()
        secret_key = os.getenv("SECRET_KEY")
        encrypted_password = os.getenv("ENCRYPTED_PASSWORD")
        self.email = os.getenv("EMAIL")

        # Déchiffrement du mot de passe
        fernet = Fernet(secret_key.encode())
        self.password = fernet.decrypt(encrypted_password.encode()).decode()

    def test_chargement_site_web(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Ouvrir le site
        driver.get("https://www.sibtel.com.tn")
        print("Site ouvert avec succès.")
        time.sleep(2)

        # 2. Bouton Connexion
        bouton_connexion = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='icon-home-button' and contains(text(), 'Connexion')]")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bouton_connexion)
        driver.execute_script("arguments[0].click();", bouton_connexion)
        print("Connexion bouton cliqué.")
        time.sleep(2)

        # 3. Identifiants
        wait.until(EC.visibility_of_element_located((By.ID, "formEmail"))).send_keys(self.email)
        driver.find_element(By.ID, "password").send_keys(self.password)

        # 4. Bouton Connexion (submit)
        bouton_submit = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='txt' and text()='Connexion']/..")))
        driver.execute_script("arguments[0].click();", bouton_submit)
        print("Connexion réussie.")
        time.sleep(4)

        # 5. Cliquer sur Upload Swift
        upload_swift_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@id='74']//a[contains(text(), 'Upload Swift')]")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_swift_link)
        driver.execute_script("arguments[0].click();", upload_swift_link)
        print("Upload Swift cliqué.")
        time.sleep(3)

        # 6. Upload du fichier
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file_to_upload")))
        file_input.send_keys("C:\\Users\\Admin\\Desktop\\selenuim_tests\\test\\EXPWEB_20250309.txt")

        # 7. Cliquer sur "Upload"
        upload_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.upload-button")))
        driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)
        driver.execute_script("arguments[0].click();", upload_button)
        print("Fichier chargé avec succès.")
        time.sleep(4)

        # 8. Déconnexion
        logout_form = wait.until(EC.presence_of_element_located((By.ID, "logout-form")))
        driver.execute_script("arguments[0].submit();", logout_form)
        print("Déconnexion effectuée.")
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
