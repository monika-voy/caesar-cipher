def cipher(text,rot):

    ciphertxt = ''

    for character in text:
        character = ord(character)
        ciphertxt += chr(character + rot)
    print(ciphertxt)