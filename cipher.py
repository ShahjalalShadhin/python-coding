import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

# print(f"Chars: {chars}")
# print(f"keys : {keys}")

# Encrypt

plaintext = input("Enter a message to encrypt: ")
ciphertext = ""

for char in plaintext:
    index = chars.index(char)
    ciphertext += keys[index]

print(f"Original message: {plaintext}")
print(f"Encrypted message: {ciphertext}")

# Decrypt

ciphertext = input("Enter a message to decrypt: ")
plaintext = ""

for char in ciphertext:
    index = keys.index(char)
    plaintext += chars[index]

print(f"Encrypted message: {ciphertext}")
print(f"Original message: {plaintext}")
