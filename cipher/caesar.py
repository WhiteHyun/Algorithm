def encipher(p, k):
    c = ""
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        t = a+k
        if t > 90:
            t -= 27
        if t == 64:
            t = 32
        c += chr(t)
    return c


def decipher(p, k):
    c = ""
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        t = a - k
        if t < 64:
            t += 27
        if t == 64:
            t = 32

        c += chr(t)
    return c


# plain_text = "ABCDEFG HIJKLMN OPQRSTU VWXYZ"
plain_text = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
K = 3
print('평문: ', plain_text)
cipherText = encipher(plain_text, K)
print('암호문: ', cipherText)
decipher_text = decipher(cipherText, K)
print('다시 평문화: ', decipher_text)
