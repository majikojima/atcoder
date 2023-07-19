# [https://atcoder.jp/contests/typical90/tasks/typical90_d]

H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

# print(H,W,A)

sum_row = [0] * H
sum_col = [0] * W

for i in range(H):
    for j in range(W):
        sum_row[i] += A[i][j]
        sum_col[j] += A[i][j]

# print(sum_row)
# print(sum_col)

B = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        B[i][j] = sum_row[i] + sum_col[j] - A[i][j]

for i in range(H):
    print(' '.join(map(str, B[i])))