def editDistance(s,t,d,m,n,delta_i,delta_d,delta_s):
    d[0][0]=0
    for i in range(1,n+1):
        d[i][0]=d[i-1][0]+1
    for j in range(1,m+1):
        d[0][j]=d[0][j-1]+1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[j-1]==t[i-1]:
                cost=0
            else:
                cost=delta_s
            insertion=d[i][j-1]+delta_i
            deletion=d[i-1][j]+delta_d
            substitution=d[i-1][j-1]+cost
            minValue=insertion
            if deletion<minValue:
                minValue=deletion
            if substitution<minValue:
                minValue=substitution
            d[i][j]=minValue
    return d[n][m]

def printTable(d,m,n):
    for i in range(n+1):
        for j in range(m+1):
            print(d[i][j],end='\t')
        print()
    print()

Delta_i=Delta_d=Delta_s=1
S='GUMBO'
T='GAMBOL'
M=len(S)
N=len(T)
D=[]
for i in range(N+1):
    d=[]
    for j in range(M+1):
        d.append(0)
    D.append(d)
result=editDistance(S,T,D,M,N,Delta_i,Delta_d,Delta_s)
printTable(D,M,N)
print('스트링 편집 거리 : ',result)