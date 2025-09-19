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

        # Accéder au site
        driver.get("https://www.sibtel.com.tn")
        time.sleep(4)


        # Trouver le bouton connexion (ex: par son ID)
        
        bouton_connexion = driver.find_element(By.XPATH, "//span[@class='icon-home-button' and contains(text(), 'Connexion')]")
        # Cliquer sur le bouton 'connexion'
        bouton_connexion.click()
        print("boutton 'Connexion' cliqué avec succès.")
        # Attendre pour voir le résultat
        time.sleep(3)

       # Saisir l'email et le mot de passe
        driver.find_element(By.ID, "formEmail").send_keys("slaheddine.chaabani@sibtel.com.tn")
        driver.find_element(By.ID, "password").send_keys("Sibtel@20112023+")
        # Cliquer sur le bouton "Connexion"
        # On va cliquer sur le parent du <span class="txt">Connexion</span>
        bouton_connexion = driver.find_element(By.XPATH, "//span[@class='txt' and text()='Connexion']/..")
        bouton_connexion.click()
        print(" connexion avec succès.")
        time.sleep(5)
        
        
        #chercher le bouton upload swift puis cliquer
        upload_swift_link = driver.find_element(By.XPATH, "//li[@id='74']//a[contains(text(), 'Upload Swift')]")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_swift_link)
        time.sleep(5)
        upload_swift_link.click()
        print(" Le boutton upload est cliqué avec succès.")
        time.sleep(5)
        
        
        wait = WebDriverWait(driver, 10)

        # 1. Upload du fichier
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file_to_upload")))
        file_input.send_keys("C:\\Users\\Admin\\Desktop\\selenuim_tests\\test\\EXPWEB_20250309.txt")
        
        # 2. Attendre que le bouton soit présent
        upload_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.upload-button")))

        # 3. Scroller jusqu’à lui
        driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)
        time.sleep(5)  # laisser le temps au scroll

        # 4. Forcer le clic avec JavaScript pour éviter l’interception
        driver.execute_script("arguments[0].click();", upload_button)
        print("le chargement est effectué avec succès.")
        time.sleep(5)
        
        
        
        logout_form = driver.find_element(By.ID, "logout-form")
        driver.execute_script("arguments[0].submit();", logout_form)
        print(" Déconnexion avec succès.")
        time.sleep(8)
       
##############################
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()








