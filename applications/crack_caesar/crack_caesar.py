# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open("ciphertext.txt") as f:
    text = f.read()

char_cache = {}
cipher_order = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U",
                "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

for char in text:
    if char.casefold().isalpha():
        if char not in char_cache:
            char_cache[char] = 0
        char_cache[char] += 1

sorted_chars = sorted(char_cache.items(), key=lambda x: x[1], reverse=True)

cracked_cipher = {}

for index in range(0, len(cipher_order) - 1):
    cracked_cipher[sorted_chars[index][0]] = cipher_order[index]

decoded_text = ""

# For posterity, if the text wasn't all capitalized, then I would lowercase the letter, compare, then return the
# decoded letter either upper or lower cased based off of the input letter.
for char in text:
    if char in cracked_cipher:
        char = cracked_cipher[char]

    decoded_text += char

print(decoded_text)
