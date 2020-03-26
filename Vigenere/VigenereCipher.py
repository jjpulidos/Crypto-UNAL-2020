class VigenereCipher:

    def __init__(self, message, key):
        self.message = message
        self.key = key * int(len(self.message)/len(key)) + key[:len(self.message) % len(key)]
        self.alphabet = {chr(i): i-97 for i in range(97, 123)}


    def cipher_decipher(self, to_cipher, t):
        if to_cipher:
            ciphered_message = ""
            for chr_i, chr_j in zip(self.message, self.key):
                ciphered_message += chr((self.alphabet[chr_i] + self.alphabet[chr_j]) % 26 + 97)
            return "".join(' ' * (n % int(t) == 0 and n != 0) + l for n, l in enumerate(list(ciphered_message)))
        else:
            deciphered_message = ""
            for chr_i, chr_j in zip(self.message, self.key):
                deciphered_message += chr((self.alphabet[chr_i] - self.alphabet[chr_j]) % 26 + 97)
            return deciphered_message


def main():
    message = input("Insert Message:\n")
    # message = "TO BE OR NOT TO BE THAT IS THE QUESTION"
    # message = "ksmeh zbblk smemp ogajx sejcs flzsy"
    # key = "relations"
    # t = 5
    key = input("Insert Key:\n")
    t = input("Insert t value:\n")

    cipher = VigenereCipher(message.lower().replace(" ", ""), key.lower().replace(" ", ""))
    ciphered_message = cipher.cipher_decipher(1, t)
    print("El mensaje a enviar es:", ciphered_message, "\n")

    decipher = VigenereCipher(ciphered_message.lower().replace(" ", ""), key.lower().replace(" ", ""))
    deciphered_message = decipher.cipher_decipher(0, t)
    print("El mensaje a enviar es:", deciphered_message, "\n")


if __name__ == '__main__':
    main()