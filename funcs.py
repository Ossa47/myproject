import string

alphabet = string.ascii_lowercase


class Encrypt():
    def encrypt(self, Text, key):
        Text = Text.lower()
        key = key
        Key = int(key)
        encrypted_message = ""

        for c in Text:
            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position + Key) % 26
                new_character = alphabet[new_position]
                encrypted_message += new_character
            else:
                encrypted_message += c
        message = str(encrypted_message)
        print(message.upper())
        return message.upper()

    def decrypt(self, Text, key):
        Text = Text.lower()
        key = key
        Key = int(key)
        encrypted_message = ""

        for c in Text:
            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - Key) % 26
                new_character = alphabet[new_position]
                encrypted_message += new_character
            else:
                encrypted_message += c
        message = str(encrypted_message)
        print(message.upper())
        return message.upper()


