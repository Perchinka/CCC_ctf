import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad as padding_tool


some_bytes = b""

with open("./example_plain", "rb") as f:
    some_bytes = f.read()

with open("./flag_plain", "rb") as f:
    flag_bytes = f.read()

def encrypt_me(plain_text):
    key_val = b""
    seed_val = plain_text[0]
    random.seed(seed_val)
    for i in range(16):
        key_val += random.randrange(1, 255).to_bytes()

    cipher = AES.new(key_val, AES.MODE_ECB)
    cipher_text = cipher.encrypt(padding_tool(plain_text, 16))
    print(cipher_text)
    print(key_val)
    return cipher_text, key_val
    
def decrypt_me(cipher_text, key_val):
    cipher = AES.new(key_val, AES.MODE_ECB)
    plain_text = cipher.decrypt(cipher_text)
    print(plain_text)

example_cipher_text, example_key = encrypt_me(some_bytes)
with open("./example_enc", "wb") as f:
    f.write(example_cipher_text)

decrypt_me(example_cipher_text, example_key)

flag_cipher_text, flag_key = encrypt_me(flag_bytes)
with open("./flag_enc", "wb") as f:
    f.write(flag_cipher_text)

decrypt_me(flag_cipher_text, flag_key)