# general_table = ['Q', 'H', 'C', 'B', 'E', 'J', 'K', 'A', 'R', 'W', 'S', 'T',
#                  'U', 'V', 'D', ' ', 'I', 'O', 'P', 'X', 'Z', 'F', 'G', 'L', 'M', 'N', 'Y']
general_table = "QHCBEJKARWSTUVD IOPXZFGLMNY"


def encrypt(text):
    encrypted_text = ''

    for i in text:
        t = ord(i)
        if t == 32:
            t = 0
        else:
            t -= 64

        encrypted_text += general_table[t]
    return encrypted_text


def decrypt(text):
    decrypted_text = ''

    for i in text:
        t = general_table.index(i)
        if t == 0:
            t = 32
        else:
            t += 64
        decrypted_text += chr(t)
    return decrypted_text


text = "SAVE PRIVATE RYAN"
print(encrypt(text))
print(decrypt(encrypt(text)))
