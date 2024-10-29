letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
cipher = {letters[i]: letters[(i+6) % len(letters)] for i in range(len(letters))}

def transform_message(message, cipher):
    
    tmsg = ''

    for char in message:
        tmsg = tmsg + cipher.get(char, char)
    return tmsg

test = "It is a beautiful day in the neighborhood."

test_encoded = transform_message(test, cipher)

print(test_encoded)

decoder = {letters[i]: letters[(i-6) % len(letters)] for i in range(len(letters))}

test_decoded = transform_message(test_encoded, decoder)

print(test_decoded)