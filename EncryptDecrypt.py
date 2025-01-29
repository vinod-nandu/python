from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

KEY = os.urandom(32)
IV = os.urandom(16)


def encrypt_string(data: str, key: bytes, iv: bytes) -> str:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    pad_length = 16 - len(data) % 16
    padded_data = data + chr(pad_length) * pad_length
    encrypted_data = encryptor.update(padded_data.encode()) + encryptor.finalize()
    return base64.b64encode(encrypted_data.decode())


def deccrypt_string(encrypted_data: str, key: bytes, iv: bytes) -> str:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    encrypted_data_bytes = base64.b64decode(encrypted_data)
    decrypted_data_bytes = base64.b64decode(encrypted_data)
    decrypted_data = decryptor.update(encrypted_data_bytes) + decryptor.finalize()

    pad_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-pad_length]
    return decrypted_data.decode()


def main():
    original_string = "This is my secret"
    encrypted_string = encrypt_string(original_string, KEY, IV)
    print(f"Encrypted : {encrypted_string}")

    decrypted_string = decrypt_string(encrypted_string, KEY, IV)
    print(f"Decrypted : {decrypted_string}")


if __name__ == "__main__":
    main()
