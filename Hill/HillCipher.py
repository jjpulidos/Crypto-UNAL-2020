import numpy as np
from sympy import Matrix

class HillCipher:

    def __init__(self, message, matrix_list):
        self.alphabet = {chr(i): i - 97 for i in range(97, 123)}
        self.message = message
        self.matrix = matrix_list
        self.message_numbers = np.array([self.alphabet[x] for x in message]).reshape((-1, 2))

    def cipher_decipher(self, to_cipher):
        ciphered_message = ""
        if to_cipher:
            for vector in self.message_numbers:
                for i in (vector @ self.matrix) % 26:
                    ciphered_message += chr(i+97)
            return ciphered_message
        else:
            deciphered_message = ""
            try:
                inverse = np.array(Matrix(self.matrix).inv_mod(26))
                for vector in self.message_numbers:
                    for i in (vector @ inverse) % 26:
                        deciphered_message += chr(i + 97)
            except Exception:
                raise Exception("Not invertible matrix")
            return deciphered_message

def main():
    message = input("Insert Message:\n")
    # message = "JULY"
    matrix = []
    print("Consider the positions of the key matrix as follows: \n")
    print("(1  2")
    print(" 3  4)")
    print()
    for i in range(4):
        matrix.append(int(input("Insert Value in the position " + str(i) + " of the matrix key: \n")))
    matrix = np.array(matrix).reshape((2, 2))

    print()
    cipher = HillCipher(message.lower().replace(" ", ""), matrix)
    ciphered_message = cipher.cipher_decipher(1)
    print("Ciphered Message:", ciphered_message)

    decipher = HillCipher(ciphered_message.lower().replace(" ", ""), matrix)
    deciphered_message = decipher.cipher_decipher(0)
    print("Deciphered message:", deciphered_message)

if __name__ == '__main__':
    main()