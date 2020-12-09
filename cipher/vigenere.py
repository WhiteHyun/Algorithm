def encipher(p, k):
    c = ''
    n = len(k)
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        b = ord(k[i % n])-64
        t = a+b
        if t > 90:
            t -= 27
        if t == 64:
            t = 32
        c += chr(t)
    return c


def decipher(p, k) -> str:
    c = ''
    n = len(k)
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        b = ord(k[i % n]) - 64
        t = a-b
        if t < 64:
            t += 27
        if t == 64:
            t = 32
        c += chr(t)
    return c


# plain_text = 'SAVE PRIVATE RYAN'
plain_text = 'ABCDEFG HIJKLMN OPQRSTU VWXYZ'
K = 'ABC'
print(f"평  문: {plain_text}")
cipher_text = encipher(plain_text, K)
print(f"암호문: {cipher_text}")
decrypted_text = decipher(cipher_text, K)
print(f"복호문: {decrypted_text}")
