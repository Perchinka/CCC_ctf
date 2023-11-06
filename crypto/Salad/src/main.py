from random import randint

flag = "CCC{c43SaR_S4lad}"

def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha(): 
            is_upper = char.isupper()
            char = char.lower()
            
            char_code = ord(char) - ord('a')
            char_code = (char_code + shift) % 26
            char = chr(char_code + ord('a'))
            
            if is_upper:
                char = char.upper()
        
        encrypted_text += char
    
    return encrypted_text


shift = randint(0, 26)
encrypted_text = encrypt(flag, shift)
print("Encrypted:", encrypted_text)
