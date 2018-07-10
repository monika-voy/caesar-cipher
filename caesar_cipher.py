def cipher(message, rot):
    ciphertxt = ""

    polishw = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
    numberspl = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for polishwords, polishnumbers in zip(polishw, numberspl):
        if rot == polishwords:
            rot = rot.replace(polishwords, polishnumbers)
            rot = int(rot)
            break

    englishw = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbersen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for englishwords, englishnumbers in zip(englishw, numbersen):
        if rot == englishwords:
            rot = rot.replace(englishwords, englishnumbers)
            rot = int(rot)
            break

    if len(message) == 0:
        return "No message to cipher!"

    if len(message) > 200:
        return "Message must be maximum 200 characters long"

    if not isinstance(rot, int):
        return "Invalid rot type!"

    elif rot < 0:
        return "Cannot cipher a message by negative rot value!"

    elif rot == 0:
        return "Message not ciphered: " + message

    else:
        for character in message:
            if character == " ":
                ciphertxt += character
                continue
            polishch = ["ó", "ą", "ę", "ć", "ń", "ś", "ż", "ź", "ł"]
            standardch = ["o", "a", "e", "c", "n", "s", "z", "z", "l"]
            for polish_char, standard_char in zip(polishch, standardch):
                character = character.replace(polish_char, standard_char)
            character = ord(character)
            if character < 32:
                return "Invalid character in the message!"
            elif character > 126:
                return "Invalid character in the message!"
            else:
                character = (character - 32 + rot) % (127 - 32) + 32
                ciphertxt += chr(character)

        return "Ciphered message: " + ciphertxt




def decipher(text, rot):
    deciphertxt = ""

    polishw = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
    numberspl = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for polishwords, polishnumbers in zip(polishw, numberspl):
        if rot == polishwords:
            rot = rot.replace(polishwords, polishnumbers)
            rot = int(rot)
            break

    englishw = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbersen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for englishwords, englishnumbers in zip(englishw, numbersen):
        if rot == englishwords:
            rot = rot.replace(englishwords, englishnumbers)
            rot = int(rot)
            break

    if len(text) == 0:
        return "No ciphered message to decode!"

    if len(text) > 200:
        return "Ciphered message must be maximum 200 characters long"

    if not isinstance(rot, int):
        return "Invalid rot type!"
    elif rot < 0:
        return "Rot value cannot be a negative number"
    elif rot == 0:
        return "Message not deciphered: " + text

    for character in text:
        if character == " ":
            deciphertxt += character
            continue
        character = ord(character)
        if character < 32:
            return "Invalid character in the ciphered message!"
        elif character > 126:
            return "Invalid character in the ciphered message!"
        else:
            character = (character - 32 - rot) % (127 - 32) + 32
            deciphertxt += chr(character)
    return "Deciphered message: " + deciphertxt


