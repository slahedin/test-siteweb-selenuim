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

    def test_navigation_page_web(self):
        driver = self.driver

        # Accéder au site
        driver.get("https://www.sibtel.com.tn")
        time.sleep(2)

        # Survoler "À propos de SIBTEL"
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'A propos de sibtel')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Messages"
        lien_messages = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Messages')]"))
        )
        lien_messages.click()
        print("✅ Lien 'Messages' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Messages s'est bien ouverte
        self.assertIn("Messages", driver.title)
        print("✅ La page 'Messages' est bien affichée.")

        # Revenir sur le menu "À propos de SIBTEL"
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'A propos de sibtel')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Valeurs"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Valeurs')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Valeurs' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Carte d'identité s'est bien ouverte
        self.assertIn("Valeurs", driver.title)
        print("✅ La page 'Valeurs' est bien affichée.")
        
        #####################
        # Revenir sur le menu "À propos de SIBTEL"
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'A propos de sibtel')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Status et missions"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Statuts et missions')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Statuts et missions' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page statuts et missions s'est bien ouverte
        self.assertIn("Statuts et missions", driver.title)
        print("✅ La page 'Statuts et missions' est bien affichée.")


#####################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'A propos de sibtel')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Métiers"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Métiers')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Métiers' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Métiers s'est bien ouverte
        self.assertIn("Métiers", driver.title)
        print("✅ La page 'Métiers' est bien affichée.")

#################################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'A propos de sibtel')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Partenaires"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Partenaires')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Partenaires' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Partenaires s'est bien ouverte
        self.assertIn("Partenaires", driver.title)
        print("✅ La page 'Partenaires' est bien affichée.")
        
 #####################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Télécompensation')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Genèse du système"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Genèse du système')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Genèse du système' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Genèse du système s'est bien ouverte
        self.assertIn("Genèse du système", driver.title)
        print("✅ La page 'Genèse du système' est bien affichée.")
 #########################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Télécompensation')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Préalables"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Préalables')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Préalables' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Préalables s'est bien ouverte
        self.assertIn("Préalables", driver.title)
        print("✅ La page 'Préalables' est bien affichée.")
        
############################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Télécompensation')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Principes de fonctionnement"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Principes de fonctionnement')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Principes de fonctionnement' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Principes de fonctionnement s'est bien ouverte
        self.assertIn("Principes de fonctionnement", driver.title)
        print("✅ La page 'Principes de fonctionnement' est bien affichée.")
#############################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Télécompensation')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Réseau et technologie"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Réseau et technologie')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Réseau et technologie' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Réseau et technologie s'est bien ouverte
        self.assertIn("Réseau et technologie", driver.title)
        print("✅ La page 'Réseau et technologie' est bien affichée.")
        
#########################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Télécompensation')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Adhérents"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Adhérents')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Adhérents' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Adhérents s'est bien ouverte
        self.assertIn("Adhérents", driver.title)
        print("✅ La page 'Adhérents' est bien affichée.")
        
        
#######################################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Télécompensation')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Dates clés"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Dates clés')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Dates clés' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Dates clés s'est bien ouverte
        self.assertIn("Dates clés", driver.title)
        print("✅ La page 'Dates clés' est bien affichée.")



########################################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Télécompensation')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Perspectives"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Perspectives')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Perspectives' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Perspectives s'est bien ouverte
        self.assertIn("Perspectives", driver.title)
        print("✅ La page 'Perspectives' est bien affichée.")




#####################################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Swift net')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Enjeux"
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Enjeux')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Enjeux' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Enjeux s'est bien ouverte
        self.assertIn("Enjeux", driver.title)
        print("✅ La page 'Enjeux' est bien affichée.")



            

            
        



###############################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Swift net')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "La SIBTEL : « SWIFT Service Bureau »" 
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'La SIBTEL : « SWIFT Service Bureau »')]"))
        )
        lien_identite.click()
        print("✅ Lien 'La SIBTEL : « SWIFT Service Bureau »' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page La SIBTEL : « SWIFT Service Bureau » s'est bien ouverte
        self.assertIn("La SIBTEL : « SWIFT Service Bureau »", driver.title)
        print("✅ La page 'La SIBTEL : « SWIFT Service Bureau »' est bien affichée.")



################################""
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Swift net')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Infrastructure" 
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Infrastructure')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Infrastructure' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Infrastructure s'est bien ouverte
        self.assertIn("Infrastructure", driver.title)
        print("✅ La page 'Infrastructure' est bien affichée.")
  
#############################  
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Swift net')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Banques participantes" 
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Banques participantes')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Banques participantes' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Banques participantes s'est bien ouverte
        self.assertIn("Banques participantes", driver.title)
        print("✅ La page 'Banques participantes' est bien affichée.")
        
##########################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Autres services')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Cloud computing" 
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Cloud computing')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Cloud computing' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Cloud computing s'est bien ouverte
        self.assertIn("Cloud computing", driver.title)
        print("✅ La page 'Cloud computing' est bien affichée.")
############################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Autres services')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Formation" 
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Formation')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Formation' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Formation s'est bien ouverte
        self.assertIn("Formation", driver.title)
        print("✅ La page 'Formation' est bien affichée.")
        
###########################
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Actualités')]"))
        )
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)

        # Cliquer sur "Actualités" 
        lien_identite = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Actualités')]"))
        )
        lien_identite.click()
        print("✅ Lien 'Actualités' cliqué avec succès.")
        time.sleep(2)

        # Vérifier que la page Actualités s'est bien ouverte
        #self.assertIn("Actualités", driver.title)
        #print("✅ La page 'Actualités' est bien affichée.")


##############################
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
