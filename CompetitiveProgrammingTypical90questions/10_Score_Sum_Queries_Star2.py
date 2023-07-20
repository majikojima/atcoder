# [https://atcoder.jp/contests/typical90/tasks/typical90_j]

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

S1 = [0] * (N+1)
S2 = [0] * (N+1)

for i in range(1, N+1):
    S1[i] = S1[i-1]
    S2[i] = S2[i-1]
    if(C[i-1] == 1):
        S1[i] += P[i-1]
    elif(C[i-1] == 2):
        S2[i] += P[i-1]

print(S1,S2)
        
A = [0] * Q
B = [0] * Q

for i in range(Q):
    print(f"i:{i}, R:{R[i]}, L:{L[i-1]},S1:{S1[R[i]]}, S2:{S2[L[i-1]]}")
    A[i] = S1[R[i]] - S1[L[i]-1]
    B[i] = S2[R[i]] - S2[L[i]-1]

for i in range(Q):
    print(A[i], B[i])