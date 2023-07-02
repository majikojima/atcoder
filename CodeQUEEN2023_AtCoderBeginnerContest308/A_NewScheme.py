# [https://atcoder.jp/contests/abc308/tasks/abc308_a]
S1, S2, S3, S4, S5, S6, S7, S8 = map(int, input().split())

if S1 > S2 or S2 > S3 or S3 > S4 or S4 > S5 or S5 > S6 or S6 > S7 or S7 > S8:
    print("No")
elif S1 < 100 or S2 < 100 or S3 < 100 or S4 < 100 or S5 < 100 or S6 < 100 or S7 < 100 or S8 < 100:
    print("No")
elif S1 > 675 or S2 > 675 or S3 > 675 or S4 > 675 or S5 > 675 or S6 > 675 or S7 > 675 or S8 > 675:
    print("No")
elif S1 % 25 != 0 or S2 % 25 != 0 or S3 % 25 != 0 or S4 % 25 != 0 or S5 % 25 != 0 or S6 % 25 != 0 or S7 % 25 != 0 or S8 % 25 != 0:
    print("No")
else:
    print("Yes")