
# Restoring the Permutation

"""
lexicographically: 辞書順
[3,3,4,4,7,7,7]　
permutationの縛りがなければ
[3, , 4, , 7, , ]は確定　ここから考える
3より小さい数字で埋めていく
"""

T = getN()
for _ in range(T):
    N = getN()
    A = getList()

    l = [N - i for i in range(N)]
    lower, upper = [-1] * N, [-1] * N
    low_que, up_que = [], []

    now = 0
    for i in range(N):
        if i == 0 or A[i - 1] < A[i]:
            now = A[i]
            lower[i] = upper[i] = now

        while l and l[-1] <= now:
            u = l.pop()
            if u < now:
                heappush(low_que, u)
                heappush(up_que, -u)

        if lower[i] == -1:
            lower[i] = heappop(low_que)
            upper[i] = -heappop(up_que)

    print(*lower)
    print(*upper)

# F-Triangular Paths

"""
Consider an infinite triangle made up of layers. 何艘かの三角形を考える
(r, c): r is the number of the layer, and c is the number of the point in the layer
two direct edges. only one of the edges is activated.
It is guaranteed that all n points are distinct. n個の点は全て異なる
It is guaranteed that there is always at least one way to traverse all n points.
全ての点を横切る道が一つはできることが保証されます

activateな辺をスイッチする
進む
全ての点を通るためのコスト
上から順に点1から点2までのコストを求める
もしr + cが奇数なら今ラインに乗っている
(r + i, c + i)までフリーでいける
左向き、右向き何回でいけるか
(0, 0), (a, b)の場合は
左にa - b回右にb回進む

まず左　次に右
r + c = evenならdiff r - cのラインに乗っている
これに乗りたい
diff evenのラインから一つスイッチする時コスト1かかる
近傍のラインを見つける
見るのは左を何回か　だけでいい 同じdiffの時に限ってコストが右の分だけかかる
あとはdiff // 2の差
"""

T = getN()
for _ in range(T):
    N = getN()
    R = [1] + getList()
    C = [1] + getList()
    P = [[r, c] for r, c in zip(R, C)]
    P.sort()

    ans = 0
    for i in range(N):
        diff1 = P[i][0] - P[i][1]
        diff2 = P[i + 1][0] - P[i + 1][1]
        # how many times do you select right edges
        if diff1 == diff2 and diff1 % 2 == 0:
            ans += (P[i + 1][1] - P[i][1])
            continue
        # if you are to go the same group, you don't pay for it.
        g_a = diff1 // 2
        g_b = diff2 // 2
        ans += g_b - g_a
    print(ans)

# G - Maximize the Remaining String

"""
lexicographically maximum string 辞書順最大
各文字についてインデックスを1つ選ぶ
辞書順最大になるのはどういう時？
"""

T = getN()
for _ in range(T):
    S = ord_chr(list(input()), 0)
    N = len(S)

    l = defaultdict(list)
    for i in range(N - 1, -1, -1):
        l[S[i]].append(i)

    prev = [[key, value] for key, value in l.items()]
    prev.sort(reverse = True)

    now = -1
    ans = []
    while prev:
        next = []
        # order the array
        for i in range(len(prev)):
            while prev[i][1] and prev[i][1][-1] <= now:
                prev[i][1].pop()
            if prev[i][1]:
                next.append(prev[i])

        # option
        for i in range(len(next)):
            for j in range(len(next)):
                if next[i][1][-1] > next[j][1][0]:
                    break
            else: # all ok
                now = next[i][1][-1]
                ans.append(next[i][0])
                next = [next[j] for j in range(len(next)) if j != i]
                prev = next
                break

    print(ord_chr(ans, 1))
