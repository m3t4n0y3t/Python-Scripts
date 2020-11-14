
# XOR encryption in python 3 by Hossam Hamdy
# 15/11/2020

# importing area
import string
import random



# generate randome key with a Custom length
# The key consists of upper and lower case letters, numbers, and symbols
def generate_random_key(size):

    key = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + 
                                string.digits + "~!@#$%^&*()_+=*{}[]<>-,;:؛") for _ in range(0,size))
    return key


# XOR function
def enc_XOR(text, key):

    # return the encrypted text / decrypted text
    return "".join([chr(ord(c1)^ord(c2)) for (c1,c2) in zip(text,key)])


# the clear text
text = "M3T4N0Y3T Blog"

# create a random key with length 100
key = generate_random_key(100)

# encrypted text = enc_XOR(text, key)
encrypted_text = enc_XOR(text,key)

# decrypted text = enc_XOR(encrypted_text, key)
decrypted_text = enc_XOR(encrypted_text,key)

# output area
print("\n\n")
print("Clear text : ", text ,"\n")
print("Encrypted text : ", encrypted_text, "\n")
print("Decrypted text : ", decrypted_text, "\n")