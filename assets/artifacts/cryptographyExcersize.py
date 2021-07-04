import os
from pathlib import Path
from cryptography.fernet import Fernet

#Symmetric Key Encryption

"""Due to the better performance and faster speed of symmetric encryption (compared to asymmetric),
 symmetric cryptography is typically used for bulk encryption / encrypting large amounts of data, e.g. for database encryption. 
 In the case of a database, the secret key might only be available to the database itself to encrypt or decrypt."""
"""https://www.cryptomathic.com/news-events/blog/symmetric-key-encryption-why-where-and-how-its-used-in-banking"""

class KeyAccess:
    def generateKey(self):
        secretKey = Fernet.generate_key()
        self._storeKey(secretKey)

    def loadKey(self):

        f = open("secretkey.txt", "a+")
        txt = Path('secretkey.txt').read_text()
        return txt.encode()

    def _storeKey(self,key):
        if os.path.exists("secretkey.txt"):
            os.remove("secretkey.txt")
        f = open("secretkey.txt", "a+")
        f.write(key.decode())
        f.close()

class Encrypter:
    def encrpyt(self,textFile,outputFileName):
        fernet = Fernet(KeyAccess().loadKey())
        fileText= Path(textFile).read_text()
        encrypted = fernet.encrypt(fileText.encode())

        if os.path.exists(outputFileName):
            os.remove(outputFileName)
        f = open(outputFileName, "a+")
        f.write(encrypted.decode())
        f.close()

class Decrypter:
    def decrypt(self,encryptedFileName,outputFileName):
        fernet = Fernet(KeyAccess().loadKey())

        fileText= Path(encryptedFileName).read_bytes()
        decrypted = fernet.decrypt(fileText)

        if os.path.exists(outputFileName):
            os.remove(outputFileName)
        f = open(outputFileName, "a")
        f.write(decrypted.decode())
        f.close()

KeyAccess().generateKey()
Encrypter().encrpyt("testInput.txt","encrypted.txt")
Decrypter().decrypt("encrypted.txt","output.txt")