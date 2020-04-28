import pyDes, os, base64

with open("Sana.jpg", mode='rb') as file:
    ImageRaw = file.read()

    key = input("Introduce a Key to Cipher of length 8 bytes \n")

    encrypted = pyDes.des(key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5).encrypt(ImageRaw)
    print("First 65 bits of The Data encrypted using DES is: \n", encrypted[0:65], "\n")

    encoded64 = base64.standard_b64encode(encrypted)
    print("First 65 bits of Image Data encoded 64 is:\n", encoded64[0:65], "\n")

    to_decrypt = base64.standard_b64decode(encoded64)

    print("First 65 bits of The Data decoded 64 is: \n", to_decrypt, "\n")
    decrypted = pyDes.des(key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5).decrypt(to_decrypt,
                                                                                                          padmode=pyDes.PAD_PKCS5)
    print("First 65 bits of Image Data decrypted 64 is:\n", decrypted[0:65], "\n")
    with open("SanaDecrypted.jpg", "wb") as file:
        file.write(decrypted)
        file.close()

    os.system("xdg-open SanaDecrypted.jpg")