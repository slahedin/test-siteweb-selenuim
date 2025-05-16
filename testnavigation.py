import unittest
import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner  # Assure-toi que 'html-testRunner' est bien installé via pip

class TestSibtelMenu(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_navigation_page_web(self):
        driver = self.driver
        driver.get("https://www.sibtel.com.tn")
        time.sleep(2)

        def cliquer_et_verifier(menu_texte, sous_menu_texte, titre_attendu):
            menu = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{menu_texte}')]"))
            )
            ActionChains(driver).move_to_element(menu).perform()
            time.sleep(2)

            lien = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{sous_menu_texte}')]"))
            )
            lien.click()
            print(f"[ok] Lien '{sous_menu_texte}' cliqué avec succès.")
            time.sleep(2)

            self.assertIn(titre_attendu, driver.title)
            print(f"[ok] La page '{titre_attendu}' est bien affichée.")

        # Liste des tests à exécuter
        tests = [
            ("A propos de sibtel", "Messages", "Messages"),
            ("A propos de sibtel", "Valeurs", "Valeurs"),
            ("A propos de sibtel", "Statuts et missions", "Statuts et missions"),
            ("A propos de sibtel", "Métiers", "Métiers"),
            ("A propos de sibtel", "Partenaires", "Partenaires"),
            ("Télécompensation", "Genèse du système", "Genèse du système"),
            ("Télécompensation", "Préalables", "Préalables"),
            ("Télécompensation", "Principes de fonctionnement", "Principes de fonctionnement"),
            ("Télécompensation", "Réseau et technologie", "Réseau et technologie"),
            ("Télécompensation", "Adhérents", "Adhérents"),
            ("Télécompensation", "Dates clés", "Dates clés"),
            ("Télécompensation", "Perspectives", "Perspectives"),
            ("Swift net", "Enjeux", "Enjeux"),
            ("Swift net", "La SIBTEL : « SWIFT Service Bureau »", "La SIBTEL : « SWIFT Service Bureau »"),
            ("Swift net", "Infrastructure", "Infrastructure"),
            ("Swift net", "Banques participantes", "Banques participantes"),
            ("Autres services", "Cloud computing", "Cloud computing"),
            ("Autres services", "Formation", "Formation")
        ]

        for menu, sous_menu, titre in tests:
            cliquer_et_verifier(menu, sous_menu, titre)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    # Dossier de sortie pour les rapports
    report_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(report_dir, exist_ok=True)

    # Nom du fichier rapport dynamique
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=report_dir,
            report_name=f"Sibtel_Test_Report_{now}",
            report_title="Rapport de test SIBTEL Navigation",
            descriptions=True
        )
    )
