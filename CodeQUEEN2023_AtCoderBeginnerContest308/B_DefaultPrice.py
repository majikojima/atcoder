# [https://atcoder.jp/contests/abc308/tasks/abc308_b]
N, M = map(int, input().split())

C = input().split()

D = input().split()

P = list(map(int, input().split()))

price = 0
for color in C:
    if color in D:
        price += P[D.index(color) + 1]
    else:
        price += P[0]

print(price)

"""
PythonでリストCに含まれる文字列がリストDに存在するかどうかを判定するには、`in`演算子を使用します。以下に例を示します。

```python
C = ["red", "green", "blue"]
D = ["blue", "red"]

for color in C:
    if color in D:
        print(f"{color}はDに存在します")
    else:
        print(f"{color}はDに存在しません")
```

このコードでは、リストCの各要素を順番に取り出し、`if`文と`in`演算子を使用してリストDに含まれるかどうかを判定しています。

実行結果は次のようになります。

```
redはDに存在します
greenはDに存在しません
blueはDに存在します
```

各色に対して、Dに存在するかどうかが判定され、結果が表示されます。存在する場合は、「○はDに存在します」というメッセージが表示され、存在しない場合は、「○はDに存在しません」というメッセージが表示されます。
"""