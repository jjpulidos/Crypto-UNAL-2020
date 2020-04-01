import collections
import numpy as np


def Diff(li1, li2):
    return (list(set(li1) - set(li2)))


class PlayFair:

    def __init__(self, message, key, action):
        self.message = message.lower()
        self.message = self.message.replace(" ", "")
        self.action = action

        for i in range(0, int(len(self.message) / 2), 2):
            if self.message[i] == self.message[i + 1]:
                self.message = self.message[:i + 1] + 'x' + self.message[i + 1:]

        if (len(self.message) % 2 != 0):
            self.message += "x"

        self.key = key.lower()
        self.key = self.key.replace(" ", "")
        self.key_without_repetition = list(collections.OrderedDict.fromkeys(self.key).keys())
        self.alfabeto_no_presente = Diff(
            [chr(x) if chr(x) != 'j' else 'ij' if chr(x) == 'i' else None for x in range(97, 123)],
            self.key_without_repetition)
        self.alfabeto_no_presente = [x for x in self.alfabeto_no_presente if x is not None]
        self.alfabeto_no_presente.sort()

    def init_square(self):
        self.square = np.zeros((5, 5))
        tam_list = len(self.key_without_repetition)
        tmp_list = np.array(self.key_without_repetition[:tam_list] + self.alfabeto_no_presente[:(25 - tam_list)])
        self.square = np.reshape(tmp_list, (5, 5))
        self.dict_col = {}
        self.dict_row = {}
        for i in range(0, 5):
            for j in range(0, 5):
                self.dict_col[self.square[i][j]] = j
                self.dict_row[self.square[i][j]] = i
        self.dict_col["j"] = self.dict_col["i"]
        self.dict_row["j"] = self.dict_row["i"]

        self.alfabeto_no_presente = ['i/j' if x == 'i' else x for lst in self.alfabeto_no_presente for x in lst]
        self.key_without_repetition = ['i/j' if x == 'i' else x for lst in self.key_without_repetition for x in lst]
        tmp_list = np.array(self.key_without_repetition[:tam_list] + self.alfabeto_no_presente[:(25 - tam_list)])
        self.square = np.reshape(tmp_list, (5, 5))

    def cipher_decipher(self):
        new_msg = ""
        if(self.action==0):
            for index in range(0, len(self.message), 2):
                if (self.dict_col[self.message[index]] == self.dict_col[self.message[index + 1]]):
                    new_msg += self.square[(self.dict_row[self.message[index]] + 1) % 5][self.dict_col[self.message[index]]]
                    new_msg += self.square[(self.dict_row[self.message[index + 1]] + 1) % 5][
                        self.dict_col[self.message[index + 1]]]
                elif (self.dict_row[self.message[index]] == self.dict_row[self.message[index + 1]]):
                    new_msg += self.square[self.dict_row[self.message[index]]][(self.dict_col[self.message[index]] + 1) % 5]
                    new_msg += self.square[self.dict_row[self.message[index + 1]]][
                        (self.dict_col[self.message[index + 1]] + 1) % 5]
                else:
                    new_msg += self.square[self.dict_row[self.message[index]]][self.dict_col[self.message[index + 1]]]
                    new_msg += self.square[self.dict_row[self.message[index + 1]]][self.dict_col[self.message[index]]]
            return new_msg
        elif(self.action==1):
            new_msg = ""
            for index in range(0, len(self.message), 2):
                if (self.dict_col[self.message[index]] == self.dict_col[self.message[index + 1]]):
                    new_msg += self.square[(self.dict_row[self.message[index]] - 1) % 5][self.dict_col[self.message[index]]]
                    new_msg += self.square[(self.dict_row[self.message[index + 1]] - 1) % 5][
                        self.dict_col[self.message[index + 1]]]
                elif (self.dict_row[self.message[index]] == self.dict_row[self.message[index + 1]]):
                    new_msg += self.square[self.dict_row[self.message[index]]][(self.dict_col[self.message[index]] - 1) % 5]
                    new_msg += self.square[self.dict_row[self.message[index + 1]]][
                        (self.dict_col[self.message[index + 1]] - 1) % 5]
                else:
                    new_msg += self.square[self.dict_row[self.message[index]]][self.dict_col[self.message[index + 1]]]
                    new_msg += self.square[self.dict_row[self.message[index + 1]]][self.dict_col[self.message[index]]]

                for i in range(0, int(len(new_msg) / 2) - 1, 2):
                    if new_msg[i] == new_msg[i + 2]:
                        new_msg = new_msg[:i + 1] + new_msg[i + 2:]

                if (new_msg[-1] == "x"):
                    new_msg = new_msg[:-1]

            return new_msg
        else:
            raise Exception("Use 0 to Cypher and 1 to Decipher")


def main():

    message = "THIS SECRET MESSAGE IS ENCRYPTED"
    key = "yoan pinzon"

    print("Message to Cypher: ", message)
    to_cipher = PlayFair(message, key, 0)
    to_cipher.init_square()
    print("Square Key:")
    print(to_cipher.square)
    ciphered_message = to_cipher.cipher_decipher()
    print("Message Encrypted: " + ciphered_message)
    print()

    print("Message to Decipher: ", ciphered_message)
    to_decipher = PlayFair(ciphered_message, key, 1)
    to_decipher.init_square()
    print("Square Key:")
    print(to_decipher.square)
    print("Message Encrypted: " + to_decipher.cipher_decipher())

if __name__ == '__main__':
    main()