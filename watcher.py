import os
import glob
import subprocess

# Dossier contenant les fichiers .txt
folder_path = r"C:\\Users\\Admin\\Desktop\\selenuim_tests\\test"

# Recherche de fichiers .txt
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

if txt_files:
    print(f"[INFO] Fichier détecté : {txt_files[0]}")
    print("[INFO] Lancement du test Selenium...")

    # Exécution du script de test via unittest directement
    subprocess.run([
        "python", "-m", "unittest",
        "test_chargement_siteweb.py"
    ])
else:
    print("[INFO] Aucun fichier .txt trouvé.")
