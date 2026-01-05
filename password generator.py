import random   # for random character selection
import string   # for ready-made sets of letters, digits, symbols

# function to generate a random password
def generate_password(length=8):
    # pool of characters: letters + digits + symbols
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # pick 'length' random characters and join them
    return ''.join(random.choice(chars) for _ in range(length))

# generate and display a 12-character password
print("Generated password:", generate_password(12))
