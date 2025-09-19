# generate_key.py
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Votre clé secrète (à copier dans .env) : {key.decode()}")
