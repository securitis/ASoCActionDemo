import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()
key = os.urandom(4)

iv = os.urandom(8)
cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret message") + encryptor.finalize()
print("Encrypted Data: " + base64.b64encode(ct).decode("ascii"))
decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize()


