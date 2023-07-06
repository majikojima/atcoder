# [https://atcoder.jp/contests/abc306/tasks/abc306_a]

N = int(input())
S = input()

A = ""
for i in range(N):
    A += S[i] * 2

print(A)