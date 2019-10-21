import pyAesCrypt

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024


def decrypt():
    password = input("Input password to decrypt file \n")
    # decrypt
    pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)

    print("File decrypted successfully \n")


def encrypt():
    password = input("Input password to encrypt file \n")
    # encrypt
    pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)

    print("File encrypted successfully \n")

def selct_option():
    type = input("Type 'D' to decrypt or 'E' to encrypt \n").upper()
    if type == 'D':
        decrypt()
    elif type == 'E':
        encrypt()
    else:
        print("Please type a valid option \n")
        selct_option()


if __name__ == "__main__":
    selct_option()
