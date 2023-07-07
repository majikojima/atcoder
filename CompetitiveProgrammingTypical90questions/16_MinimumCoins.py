# [https://atcoder.jp/contests/typical90/tasks/typical90_p]

# 以下はNの値がでっかい時に、Runtime Error になるので改善の余地あり

N = int(input())
ABC = list(map(int, input().split()))

dp = [0] + [float('inf')] * N
for i in range(N):
    print("\n")
    print("i", i)
    print("dp", dp)
    for c in ABC:
        print("c", c)
        if i + c <= N:
            print("i+c", i+c)
            print("dp[i+c]", dp[i+c],"dp[i]", dp[i])
            dp[i+c] = min(dp[i+c], dp[i] + 1)
            print("dp[i+c]", dp[i+c])

print(dp[-1])

"""
動的計画法（Dynamic Programming）の具体的な動きについて説明しますね。

例えば、N=15、ABC=[1, 2, 5]（それぞれ硬貨の価値が1円、2円、5円）としましょう。ちょうど15円を作るために必要な最小の硬貨の枚数を求めます。

まず、動的計画法では `dp` という配列を作成します。この配列の `i` 番目の要素は「ちょうど `i` 円を作るために必要な最小の硬貨の枚数」を表します。 `dp` 配列は以下のように初期化します。

```
dp = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
```
ここで、 `inf` は無限大を表します。`0` 円を作るためには硬貨は必要ないので `dp[0]` は `0` です。他の全ての要素は最初に無限大 (`inf`) で初期化されます。

次に、全ての `i` について（`i` は作りたい金額）、そして全ての硬貨についてループします。このループの目的は、もし `i` 円に `c` 円硬貨を足すと `N` 円を超えない場合、その硬貨を使うか使わないかで最小の枚数を選択することです。

たとえば、 `i=0`, `c=1` から始めます。 `i + c = 1` なので、 `dp[1]` を `min(dp[1], dp[0]+1)` で更新します。すなわち `min(inf, 1)` となるので、 `dp[1]` は `1` に更新されます。つまり、ちょうど1円を作るためには最小1枚の硬貨が必要という意味です。

同様に、全ての `i` と `c` の組み合わせについて上記の操作を行います。最終的に `dp` 配列は以下のようになります：

```
dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3, 4, 4, 3]
```

これを見ると、たとえば `dp[15] = 3` なので、ちょうど15円を作るためには最小で3枚の硬貨が必要ということがわかります。

以上が動的計画法の動きの一例です。このように動的計画法を使うことで、全ての可能な解を探索し、最小の硬貨の枚数を見つけ出すことができます。
"""

"""
15
1 2 5


i 0
dp [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
c 1
i+c 1
dp[i+c] inf dp[i] 0
dp[i+c] 1
c 2
i+c 2
dp[i+c] inf dp[i] 0
dp[i+c] 1
c 5
i+c 5
dp[i+c] inf dp[i] 0
dp[i+c] 1


i 1
dp [0, 1, 1, inf, inf, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
c 1
i+c 2
dp[i+c] 1 dp[i] 1
dp[i+c] 1
c 2
i+c 3
dp[i+c] inf dp[i] 1
dp[i+c] 2
c 5
i+c 6
dp[i+c] inf dp[i] 1
dp[i+c] 2


i 2
dp [0, 1, 1, 2, inf, 1, 2, inf, inf, inf, inf, inf, inf, inf, inf, inf]
c 1
i+c 3
dp[i+c] 2 dp[i] 1
dp[i+c] 2
c 2
i+c 4
dp[i+c] inf dp[i] 1
dp[i+c] 2
c 5
i+c 7
dp[i+c] inf dp[i] 1
dp[i+c] 2


i 3
dp [0, 1, 1, 2, 2, 1, 2, 2, inf, inf, inf, inf, inf, inf, inf, inf]
c 1
i+c 4
dp[i+c] 2 dp[i] 2
dp[i+c] 2
c 2
i+c 5
dp[i+c] 1 dp[i] 2
dp[i+c] 1
c 5
i+c 8
dp[i+c] inf dp[i] 2
dp[i+c] 3


i 4
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, inf, inf, inf, inf, inf, inf, inf]
c 1
i+c 5
dp[i+c] 1 dp[i] 2
dp[i+c] 1
c 2
i+c 6
dp[i+c] 2 dp[i] 2
dp[i+c] 2
c 5
i+c 9
dp[i+c] inf dp[i] 2
dp[i+c] 3


i 5
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, inf, inf, inf, inf, inf, inf]
c 1
i+c 6
dp[i+c] 2 dp[i] 1
dp[i+c] 2
c 2
i+c 7
dp[i+c] 2 dp[i] 1
dp[i+c] 2
c 5
i+c 10
dp[i+c] inf dp[i] 1
dp[i+c] 2


i 6
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, inf, inf, inf, inf, inf]
c 1
i+c 7
dp[i+c] 2 dp[i] 2
dp[i+c] 2
c 2
i+c 8
dp[i+c] 3 dp[i] 2
dp[i+c] 3
c 5
i+c 11
dp[i+c] inf dp[i] 2
dp[i+c] 3


i 7
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, inf, inf, inf, inf]
c 1
i+c 8
dp[i+c] 3 dp[i] 2
dp[i+c] 3
c 2
i+c 9
dp[i+c] 3 dp[i] 2
dp[i+c] 3
c 5
i+c 12
dp[i+c] inf dp[i] 2
dp[i+c] 3


i 8
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3, inf, inf, inf]
c 1
i+c 9
dp[i+c] 3 dp[i] 3
dp[i+c] 3
c 2
i+c 10
dp[i+c] 2 dp[i] 3
dp[i+c] 2
c 5
i+c 13
dp[i+c] inf dp[i] 3
dp[i+c] 4


i 9
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3, 4, inf, inf]
c 1
i+c 10
dp[i+c] 2 dp[i] 3
dp[i+c] 2
c 2
i+c 11
dp[i+c] 3 dp[i] 3
dp[i+c] 3
c 5
i+c 14
dp[i+c] inf dp[i] 3
dp[i+c] 4


i 10
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3, 4, 4, inf]
c 1
i+c 11
dp[i+c] 3 dp[i] 2
dp[i+c] 3
c 2
i+c 12
dp[i+c] 3 dp[i] 2
dp[i+c] 3
c 5
i+c 15
dp[i+c] inf dp[i] 2
dp[i+c] 3


i 11
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3, 4, 4, 3]
c 1
i+c 12
dp[i+c] 3 dp[i] 3
dp[i+c] 3
c 2
i+c 13
dp[i+c] 4 dp[i] 3
dp[i+c] 4
c 5


i 12
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3, 4, 4, 3]
c 1
i+c 13
dp[i+c] 4 dp[i] 3
dp[i+c] 4
c 2
i+c 14
dp[i+c] 4 dp[i] 3
dp[i+c] 4
c 5


i 13
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3, 4, 4, 3]
c 1
i+c 14
dp[i+c] 4 dp[i] 4
dp[i+c] 4
c 2
i+c 15
dp[i+c] 3 dp[i] 4
dp[i+c] 3
c 5


i 14
dp [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3, 4, 4, 3]
c 1
i+c 15
dp[i+c] 3 dp[i] 4
dp[i+c] 3
c 2
c 5
3
"""

"""
分かりやすく説明するために、日常生活の例を使ってみましょう。

まず、「イテレータ」というのは、私たちが一つ一つアイテムを取り出せるボックスのようなものと考えてみてください。例えば、お菓子の箱があったとします。その箱から一つずつお菓子を取り出すことができますよね。これがイテレータの働きです。Pythonでは、例えばリスト（例：`[1, 2, 3, 4, 5]`）から順番に要素を取り出すことができます。これを「イテレーション（反復）」と呼びます。

次に、「map」ですが、これは魔法のステッキのようなものと思ってください。この魔法のステッキは、ある物を別の物に変える能力があります。例えば、リンゴをオレンジに変えるとか、ボールを風船に変えるといった具体的なことです。

Pythonで「map」を使うと、リストなどの中にある全てのアイテムを一度に何か別のものに変えることができます。例えば、リスト`[1, 2, 3, 4, 5]`があったとき、これら全ての数字を2倍にしたいと思ったら、`map`関数を使ってそれを行うことができます。

次のように書けば、全ての数字が2倍になります：

```python
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
```

ここで`lambda x: x * 2`という部分は、"xを2倍にする魔法のステッキ"の役割を果たしています。`map`関数がこの魔法のステッキをリスト`numbers`の全ての要素に適用して、新しいリスト`doubled_numbers`を作ります。

このように、「イテレータ」は一つ一つアイテムを取り出すボックスのようなもの、そして「map」は物を別の物に変える魔法のステッキのようなもの、と覚えておくと理解しやすいかもしれません。
"""

"""
はい、その `lambda` という部分は重要です。これは「無名関数」や「ラムダ関数」とも呼ばれます。

ラムダ関数は小さな一時的な関数で、特に名前を付けずに一度きりの利用をするためによく使われます。上記の `lambda x: x * 2` の部分は、「入力された `x` を 2 倍にする」という短い関数を作っています。

`map` 関数は、第一引数に関数をとり、第二引数にイテラブル（リストなど）を取ります。それから、イテラブルの各要素に対して関数を適用します。つまり、この例の `map(lambda x: x * 2, numbers)` は「`numbers` リストの各要素を 2 倍にした新しいリストを作る」という意味になります。

一般的な関数定義を使って同じことをすると以下のようになります：

```python
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)
```

しかし、`double` 関数はこの場所でしか使わないので、代わりに `lambda` を使って一行で書くことができます。そのため、`lambda` を使うとコードが簡潔になります。

ただし、`lambda` はその特性上、複雑な処理には向いていません。簡単な一行程度の処理を行う時や、その関数が一度きりの使用になる場合に便利です。
"""