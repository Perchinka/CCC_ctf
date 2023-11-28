import random
from Crypto.Cipher import AES

random.seed(ord('C'))
key = b''
for i in range(16):
    key += random.randrange(1, 255).to_bytes()

def decrypt_me(cipher_text, key_val):
    cipher = AES.new(key_val, AES.MODE_ECB)
    plain_text = cipher.decrypt(cipher_text)
    print(plain_text)

with open('files/flag_enc', 'rb') as f:
    flag_cipher_text = f.read()
    decrypt_me(flag_cipher_text, key)