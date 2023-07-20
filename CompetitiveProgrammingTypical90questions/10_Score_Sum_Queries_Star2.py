# [https://atcoder.jp/contests/typical90/tasks/typical90_j]

# 以下はTLE

N = int(input())

C, P = [], []
for i in range(N):
    c, p = map(int, input().split())
    C.append(c)
    P.append(p)

Q = int(input())
L, R = [], []
for i in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

A = [0] * Q
B = [0] * Q

for i in range(Q):
    for j in range(L[i]-1, R[i]):
        if(C[j] == 1):
            A[i] += P[j]
        elif(C[j] == 2):
            B[i] += P[j]

for i in range(Q):
    print(A[i], B[i])