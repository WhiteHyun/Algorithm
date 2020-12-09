def encipher(p, k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 0
        else:
            a-=64
        c += k[a]
    return c

def descreambling(p,k):
    c=''
    for i in range(len(p)):
        a=p[i]
        for j in range(len(k)):
            if k[j]==a:
                if j==0:
                    a=32
                else:
                    a=j+64
        c+=chr(a)
    return c

plainText='SAVE PRIVATE RYAN'
K='QHCBEJKARWSTUVD IOPXZFGLMNY'
print('평문 : ',plainText)
cipherText=encipher(plainText,K)
print('암호문 : ',cipherText)
descreambe=descreambling(cipherText,K)
print('복호문 : ',descreambe)