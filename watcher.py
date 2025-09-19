import os
import glob
import subprocess

# Dossier où chercher les fichiers .txt
folder_path = r"C:\Users\Admin\Desktop\selenuim_tests\test"

# Rechercher les fichiers .txt
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

if txt_files:
    print(f"[INFO] Fichier détecté : {txt_files[0]}")
    print("[INFO] Lancement du test Selenium...")

    # Lancer le script principal (attention au chemin selon Jenkins)
    subprocess.run(["python", "C:\\Users\\Admin\\Desktop\\selenuim_tests\\test\\test_chargement_siteweb.py"])

else:
    print("[INFO] Aucun fichier .txt trouvé.")
