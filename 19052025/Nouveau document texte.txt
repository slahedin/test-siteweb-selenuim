
import unittest
import time
import os
import glob
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner


class TestSibtelMenu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.uploaded_file_path = None  # On initialise le chemin ici

    def test_chargement_site_web(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accéder au site
        driver.get("https://www.sibtel.com.tn")
        time.sleep(4)

        # Connexion
        bouton_connexion = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='icon-home-button' and contains(text(), 'Connexion')]")
        ))
        driver.execute_script("arguments[0].click();", bouton_connexion)
        print(" OK Bouton 'Connexion' cliqué.")
        time.sleep(3)

        driver.find_element(By.ID, "formEmail").send_keys("slaheddine.chaabani@sibtel.com.tn")
        driver.find_element(By.ID, "password").send_keys("S@sag1+20041992+ch")

        bouton_connexion = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='txt' and text()='Connexion']/..")
        ))
        driver.execute_script("arguments[0].click();", bouton_connexion)
        print(" OK Connexion effectuée.")
        time.sleep(5)

        # Upload Swift
        upload_swift_link = driver.find_element(By.XPATH, "//li[@id='74']//a[contains(text(), 'Upload Swift')]")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_swift_link)
        time.sleep(5)
        upload_swift_link.click()
        print("OK Menu 'Upload Swift' ouvert.")
        time.sleep(5)

        # Détection du fichier .txt
        folder_path = r"C:\Users\Admin\Desktop\selenuim_tests\test"
        txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
        self.assertTrue(txt_files, " ! Aucun fichier .txt trouvé dans le dossier.")
        file_path = txt_files[0]
        self.uploaded_file_path = file_path  # Stockage du chemin pour suppression future
        print(f" OK Fichier détecté : {file_path}")

        # Upload
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file_to_upload")))
        file_input.send_keys(file_path)

        upload_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.upload-button")))
        driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)
        time.sleep(5)
        driver.execute_script("arguments[0].click();", upload_button)
        print(" OK Fichier uploadé avec succès.")
        time.sleep(5)

        # Déconnexion
        logout_form = driver.find_element(By.ID, "logout-form")
        driver.execute_script("arguments[0].submit();", logout_form)
        print(" OK Déconnexion réussie.")
        time.sleep(8)

    def tearDown(self):
        self.driver.quit()

        # Suppression du fichier uploadé
        if self.uploaded_file_path and os.path.exists(self.uploaded_file_path):
            try:
                os.remove(self.uploaded_file_path)
                print(f" Fichier supprimé : {self.uploaded_file_path}")
            except Exception as e:
                print(f"! Erreur lors de la suppression du fichier : {e}")
        else:
            print("! Aucun fichier à supprimer ou déjà supprimé.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports',
        report_name='Test_Report_Sibtel',
        report_title='Rapport de Test - Upload Swift',
        combine_reports=True,
        add_timestamp=True
    ))