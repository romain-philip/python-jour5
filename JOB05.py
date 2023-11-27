def cesar(message, decalage):
    resultat = ""
    for char in message:
        if char.isalpha():
            majuscule = char.isupper()
            char_code = ord(char) + decalage
            if majuscule:
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26

            resultat += chr(char_code)
        else:
            resultat += char
    return resultat
message_original = input("Entrez votre message : ")
decalage = 3
message_chiffre = cesar(message_original, decalage)
print("Message original:", message_original)
print("Message chiffré:", message_chiffre)