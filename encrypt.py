from cryptography.fernet import Fernet

with open("secret.key", 'rb') as file:
    key = file.read()

cipher_suite = Fernet(key)

message = "Här är mitt hemliga meddelande".encode()
cipher_text = cipher_suite.encrypt(message)
print(f"Ciphertext: {cipher_text}")

with open("encrypted.enc", "wb") as file:
    file.write(cipher_text)