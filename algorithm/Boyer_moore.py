NUM=27
skip=[0]*NUM

def index(a):
    if ord(a)==32:
        return 0
    else:
        return ord(a)-64

def initSkip(a):
    n=len(a)
    for i in range(NUM):
        skip[i]=n
    for j in range(n):
        skip[index(a[j])]=n-j-1

def BM(p,t,k):
    n=len(p)
    m=len(t)
    initSkip(p)
    i=k+n-1
    j=n-1
    if i>=m:
        return m
    while j>=0:
        while t[i]!=p[j]:
            s=skip[index(t[i])]
            if n-j>s:
                i+=n-j
            else:
                i+=s
            if i>=m:
                return m
            j=n-1
        i-=1
        j-=1
    return i+1

text='VISION QUESTION ONION CAPTION GRADUATION EDUCATION'
pattern='ATION'
M=len(pattern)
N=len(text)
k=0
while True:
    pos=BM(pattern,text,k)
    k=pos+M
    if k<=N:
        print('패턴 등장 위치 : ',pos)
    else:
        break
print('탐색 종료')