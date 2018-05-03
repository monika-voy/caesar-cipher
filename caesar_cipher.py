def cipher(text,rot):

    ciphertxt = ''

    for character in text:
        character = ord(character)
        ciphertxt += chr(character + rot)
    print(ciphertxt)

def decipher(text, rot):

    deciphertxt = ''

    for character in text:
        character = ord(character)
        deciphertxt += chr(character - rot)
    print(deciphertxt)