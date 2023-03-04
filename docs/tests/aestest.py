from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Encrypt a message using AES in CBC mode
def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ciphertext = base64.b64encode(ciphertext_bytes).decode('utf-8')
    return iv, ciphertext

# Decrypt a message using AES in CBC mode
def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=base64.b64decode(iv))
    ciphertext_bytes = base64.b64decode(ciphertext)
    plaintext_bytes = unpad(cipher.decrypt(ciphertext_bytes), AES.block_size)
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext

# Example usage
key = b'Sixteen byte key'
message = 'Hello, world!'
iv, ciphertext = encrypt(message, key)
decrypted_message = decrypt(ciphertext, key, iv)

print(f"Message: {message}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {decrypted_message}")
#This code should generate a random initialization vector (IV), encrypt the message using AES in CBC mode with the given key and IV, and then return the IV and ciphertext. To decrypt the ciphertext, you can pass the ciphertext, key, and IV to the decrypt() function, which should return the original plaintext message.

#gain, please let me know if you have any questions or if there are any error messages you are seeing.




