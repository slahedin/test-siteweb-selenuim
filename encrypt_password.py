# encrypt_password.py
from cryptography.fernet import Fernet

key = b'2OtayL_Tvgu2PN4QD1RWnsvd7tEwavMebqU_Htw1BYc='  # Copie ici la clé générée dans le script précédent
fernet = Fernet(key)

password = "Sibtel@20112023+"
encrypted_password = fernet.encrypt(password.encode())
print(f"Mot de passe chiffré : {encrypted_password.decode()}")
