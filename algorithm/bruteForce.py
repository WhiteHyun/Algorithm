def bruteForce(p,t,c):
    M=len(p)
    N=len(t)
    i=c
    j=0
    while i<N and j<M:
        if t[i]!=p[j]:
            i-=j
            j=-1
        i+=1
        j+=1
    if j==M:
        return i-M
    else:
        return i

'''f=open("test.html",'r')
pattern='mailto:'
M=len(pattern)
while True:
    line=f.readline()
    N=len(line)
    K=0
    if not line:
        break
    while True:
        pos=bruteForce(pattern,line,K)
        K=pos+M
        if K<N:
            print('')
            while line[pos]!='\"':
                print(line[pos],end='')
                pos+=1
        else:
            break
f.close()'''

text='hosdhofafdiuhaejlwdhofhsdfjhkdhoflfdah'
pattern='dhof'
correct=0
while(True):
    a=bruteForce(pattern,text,correct)
    correct=a+len(pattern)
    c=a+len(pattern)
    if correct<len(text):
        print('패턴 등장 위치 : %d' %a)
    else:
        break
print('종료')