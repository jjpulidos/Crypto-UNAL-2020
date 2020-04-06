class TurningGrille():

    def __init__(self, message, matrix_size, holes_number, matrix_positions, clockwise=False):

        self.alphabet = {chr(i): i - 97 for i in range(97, 123)}
        self.message = message.replace(" ", "").lower()
        self.matrix_size = matrix_size
        self.clockwise = clockwise
        diff_sizes = (len(self.message)) - (matrix_size * matrix_size)

        if diff_sizes > 0:
            raise Exception("Message doesnt fit in a matrix of size " + str(matrix_size) + "x" + str(matrix_size))
        elif diff_sizes < 0:
            print("Is going to be added '*' characters to complete the grill")
            self.message += ("*" * abs(diff_sizes))

        if holes_number * 4 >= matrix_size * matrix_size:
            print("Probably is going to be overlapping characters, they are going to be included in the last char block")

        self.matrix_pos = matrix_positions


    def cipher_decipher(self, cipher=True):
        if (cipher):
            new_matrix = []

            for i in range(self.matrix_size):
                new_matrix.append([0 for t in range(self.matrix_size)])
            print(self.matrix_pos)
            tmp_matrix_pos = self.matrix_pos
            count_char = 0
            for i in range(4):
                for tup in sorted(tmp_matrix_pos):
                    new_matrix[tup[0]][tup[1]] = self.message[count_char]
                    count_char += 1
                for idx in range(len(tmp_matrix_pos)):
                    if not self.clockwise:
                        tmp_matrix_pos[idx] = (self.matrix_size - 1 - tmp_matrix_pos[idx][1], tmp_matrix_pos[idx][0])
                    else:
                        tmp_matrix_pos[idx] = (tmp_matrix_pos[idx][1], self.matrix_size - tmp_matrix_pos[idx][0] - 1)
            print(" ".join("".join(i) for i in new_matrix))
        else:

            tmp_matrix = []
            deciphered_message = []
            for i in range(self.matrix_size):
                tmp_matrix.append([c for c in self.message[i*self.matrix_size:(i+1)*self.matrix_size]])
                deciphered_message.append([0 for t in range(self.matrix_size)])
            tmp_matrix_pos = self.matrix_pos
            idx_i = 0
            idx_j = 0

            chars_ovelapped = ""
            for i in range(4):
                for tup in sorted(tmp_matrix_pos):
                    if idx_i >= self.matrix_size:
                        chars_ovelapped += tmp_matrix[tup[0]][tup[1]]
                    else:
                        deciphered_message[idx_i][idx_j] = tmp_matrix[tup[0]][tup[1]]
                        if (idx_j == self.matrix_size-1):
                            idx_j = 0
                            idx_i += 1
                        else:
                            idx_j += 1
                for idx in range(len(tmp_matrix_pos)):
                    if not self.clockwise:
                        tmp_matrix_pos[idx] = (self.matrix_size - 1 - tmp_matrix_pos[idx][1], tmp_matrix_pos[idx][0])
                    else:
                        tmp_matrix_pos[idx] = (tmp_matrix_pos[idx][1], self.matrix_size - tmp_matrix_pos[idx][0] - 1)
                # idx_i += 1
                # idx_j = 0
                # print(deciphered_message)
            print(" ".join("".join(i) for i in deciphered_message) + " " + chars_ovelapped)





def main():
    # JIM ATTACKS AT DAWN
    # JKTD SAAT WIAM CNAT
    #

    # cipher = TurningGrille("TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM"
    #                        " TLHIE", 9, 21, [(0, 0), (0, 3), (0, 5), (1, 2), (1, 8), (2, 1), (2, 6), (3, 2), (3, 4),
    #                                          (3, 7), (4, 4), (4, 6), (4, 8), (5, 3), (5, 7), (6, 0), (6, 5), (7, 1),
    #                                          (7, 4), (7, 8), (8, 2)])

    # cipher.cipher_decipher(False)

    message = input("Insert a Message to Encrypt/Decrypt:\n")

    matrix_size = int(input("Insert Matrix Size:\n"))

    holes_num = int(input("Insert Holes Number:\n"))

    arr_pos = []
    # arr_pos= [(0, 0), (2, 1), (3, 2), (2, 3)]

    for i in range(holes_num):
        pos_0 = int(input("Insert Row Index of the Hole Number " + str(i) + " (Starting in 0):\n"))
        pos_1 = int(input("Insert Column Index of the Hole Number " + str(i) + " (Starting in 0):\n"))
        arr_pos.append((pos_0, pos_1))

    to_cipher = bool(int(input("If you want to Cipher insert 1, to decipher 0...\n")))
    clockwise = bool(int(input("If you want apply Turning Grill Clockwise insert 1, 0 to counter-clockwise...\n")))
    cipher = TurningGrille(message, matrix_size, holes_num, arr_pos, clockwise)
    cipher.cipher_decipher(to_cipher)



if __name__ == '__main__':
    main()