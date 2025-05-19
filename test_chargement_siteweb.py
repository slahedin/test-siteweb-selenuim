import unittest
import time
import os
import glob
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import HtmlTestRunner


class TestSibtelMenu(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless=new")  # Important pour Jenkins

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.uploaded_file_path = None
        print(f"[INFO] Utilisateur en cours : {getpass.getuser()}")

    def test_chargement_site_web(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            driver.get("https://www.sibtel.com.tn")
            time.sleep(4)

            # Connexion
            bouton_connexion = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='icon-home-button' and contains(text(), 'Connexion')]")
            ))
            driver.execute_script("arguments[0].click();", bouton_connexion)
            print(" Bouton 'Connexion' cliqué.")
            time.sleep(2)

            driver.find_element(By.ID, "formEmail").send_keys("slaheddine.chaabani@sibtel.com.tn")
            driver.find_element(By.ID, "password").send_keys("Sibtel@20112023+")

            bouton_connexion = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='txt' and text()='Connexion']/..")
            ))
            driver.execute_script("arguments[0].click();", bouton_connexion)
            print(" Connexion effectuée.")
            time.sleep(4)

            # Upload Swift
            upload_swift_link = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//li[@id='74']//a[contains(text(), 'Upload Swift')]")
            ))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_swift_link)
            time.sleep(2)
            driver.execute_script("arguments[0].click();", upload_swift_link)
            print(" Menu 'Upload Swift' ouvert.")
            time.sleep(4)

            folder_path = r"C:\Users\Admin\Desktop\selenuim_tests\test"
            txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
            self.assertTrue(txt_files, " Aucun fichier .txt trouvé.")
            file_path = txt_files[0]
            self.uploaded_file_path = file_path
            print(f" Fichier détecté : {file_path}")

            file_input = wait.until(EC.presence_of_element_located((By.ID, "file_to_upload")))
            file_input.send_keys(file_path)

            upload_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.upload-button")))
            driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)
            time.sleep(2)
            driver.execute_script("arguments[0].click();", upload_button)
            print(" Fichier uploadé avec succès.")
            time.sleep(4)

            logout_form = wait.until(EC.presence_of_element_located((By.ID, "logout-form")))
            driver.execute_script("arguments[0].submit();", logout_form)
            print(" Déconnexion réussie.")
            time.sleep(4)

        except Exception as e:
            print(f" Erreur pendant le test : {e}")
            screenshot_path = os.path.join(os.getcwd(), "error_screenshot.png")
            driver.save_screenshot(screenshot_path)
            print(f" Capture d'écran sauvegardée : {screenshot_path}")
            raise

    def tearDown(self):
        self.driver.quit()
        if self.uploaded_file_path and os.path.exists(self.uploaded_file_path):
            try:
                os.remove(self.uploaded_file_path)
                print(f" Fichier supprimé : {self.uploaded_file_path}")
            except Exception as e:
                print(f" Erreur suppression fichier : {e}")
        else:
            print(" Aucun fichier à supprimer ou déjà supprimé.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports',
        report_name='Test_Report_Sibtel',
        report_title='Rapport de Test - Upload Swift',
        combine_reports=True,
        add_timestamp=True
    ))
