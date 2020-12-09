import sys


def matrix_chain_mult(d, m, p, n):
    for h in range(1, n):
        for i in range(1, n-h+1):
            j = i+h
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + d[i-1]*d[k]*d[j]
                if q < m[i][j]:
                    m[i][j] = q
                    p[i][j] = k
    return m[1][n]


N = 6
D = [4, 2, 3, 1, 2, 2, 3]
M = []
P = []

for i in range(N+1):
    m = []
    p = []
    for i in range(N+1):
        m.append(0)
        p.append(0)
    M.append(m)
    P.append(p)
result = matrix_chain_mult(D, M, P, N)
print("====================M====================")
for i in range(len(M)):
    for j in range(len(M[1])):
        print(f"{M[i][j]:^5}", end="")
    print()
print("=========================================")
print()
print("====================K====================")
for i in range(len(P)):
    for j in range(len(P[1])):
        print(f"{P[i][j]:^5}", end="")
    print()
print("=========================================")

print(f"최소 곱셈 횟수: {result}")
