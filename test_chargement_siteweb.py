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
        self.uploaded_file_path = None

    def test_chargement_site_web(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accès au site
        driver.get("https://www.sibtel.com.tn")
        time.sleep(4)

        # Clic sur le bouton "Connexion" (header)
        bouton_connexion = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[@class='icon-home-button' and contains(text(), 'Connexion')]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bouton_connexion)
        driver.save_screenshot("01_bouton_connexion.png")
        driver.execute_script("arguments[0].click();", bouton_connexion)
        print("OK Bouton 'Connexion' cliqué.")
        time.sleep(3)

        # Remplir formulaire de login
        driver.find_element(By.ID, "formEmail").send_keys("slaheddine.chaabani@sibtel.com.tn")
        driver.find_element(By.ID, "password").send_keys("Sibtel@20112023+")

        # Clic sur bouton de connexion dans la modal
        bouton_connexion_modal = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[@class='txt' and text()='Connexion']/.."
        )))
        driver.execute_script("arguments[0].scrollIntoView(true);", bouton_connexion_modal)
        driver.save_screenshot("02_connexion_modal.png")
        driver.execute_script("arguments[0].click();", bouton_connexion_modal)
        print("OK Connexion effectuée.")
        time.sleep(5)

        # Clic sur le menu "Upload Swift"
        upload_swift_link = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//li[@id='74']//a[contains(text(), 'Upload Swift')]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_swift_link)
        driver.save_screenshot("03_upload_swift_menu.png")
        upload_swift_link.click()
        print("OK Menu 'Upload Swift' ouvert.")
        time.sleep(5)

        # Détection du fichier .txt
        folder_path = r"C:\Users\Admin\Desktop\selenuim_tests\test"
        txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
        self.assertTrue(txt_files, "! Aucun fichier .txt trouvé dans le dossier.")
        file_path = txt_files[0]
        self.uploaded_file_path = file_path
        print(f"OK Fichier détecté : {file_path}")

        # Upload du fichier
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file_to_upload")))
        file_input.send_keys(file_path)

        upload_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.upload-button")))
        driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)
        driver.save_screenshot("04_upload_button.png")
        driver.execute_script("arguments[0].click();", upload_button)
        print("OK Fichier uploadé avec succès.")
        time.sleep(5)

        # Déconnexion
        logout_form = wait.until(EC.presence_of_element_located((By.ID, "logout-form")))
        driver.execute_script("arguments[0].submit();", logout_form)
        print("OK Déconnexion réussie.")
        time.sleep(8)

    def tearDown(self):
        self.driver.quit()
        # Suppression du fichier uploadé
        if self.uploaded_file_path and os.path.exists(self.uploaded_file_path):
            try:
                os.remove(self.uploaded_file_path)
                print(f"! Fichier supprimé : {self.uploaded_file_path}")
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
