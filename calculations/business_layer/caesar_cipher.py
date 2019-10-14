class CaesarCipher:
    def encrypt(self, text, s):
        result = ""
        key_index = 0
        for letter in text:
            result += chr((ord(letter) + ord(s[key_index])))
            if key_index == len(s)-1:
                key_index = 0
            else:
                key_index += 1
        return result

    def decode(self, text, s):
        result = ""
        key_index = 0
        for letter in text:
            result += chr((ord(letter) - ord(s[key_index])))
            if key_index == len(s)-1:
                key_index = 0
            else:
                key_index += 1
        return result