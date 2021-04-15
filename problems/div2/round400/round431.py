# A. Odds and Ends

"""
# 奇数の長さの奇数で始まり奇数で終わる数列に分割する
# 奇数個の数列にできるか

# 偶数は抱き込む必要がある
もちろんDP 長さ100か
dp[i][j]: i - 1まで進んだ時にj個分割した
"""

N = getN()
A = getList()

dp = [set() for i in range(N + 1)]
dp[0].add(0)

for i in range(N):
    if A[i] % 2 == 0:
        continue
    # 次に飛べるとこ
    for j in range(i, N):
        for o in list(dp[i]):
            # 次に飛ぶとこが奇数かつ長さが奇数
            if A[j] % 2 == 1 and (j - i) % 2 == 0:
                dp[j + 1].add(o + 1)

for o in list(dp[N]):
    if o % 2 == 1:
        print('Yes')
        exit()

print('No')

# B Tell Your World

"""
5
7 5 8 6 9
(0, 7), (1, 5), (2, 8)...
coordinate plane: 直行座標系
non-overlapping: 交わらない
every point in the set lies on exactly one of them, すべての頂点がどちらかの線上にあり、
and each of them passes through at least one point in the set. ２つの線は１つ以上の
点を通る

N <= 1000
ベクトルは100万通りある　それぞれにO(1)で判定できれば
頂点0-iのグループを作る　残ったやつで頂点jのグループを作る
二度のgroupingで0になるか
"""

N = getN()
A = getList()
A = [[i, A[i]] for i in range(N)]
fir = A[0]

def vec_calc(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    if x < 0:
        x, y = -x, -y
    g = math.gcd(x, y)
    return (x // g, y // g)

def grouping(array, vec):
    group = [array[0]]
    left = []
    for i in range(1, len(array)):
        if vec_calc(array[0], array[i]) == vec:
            group.append(array[i])
        else:
            left.append(array[i])
    return group, left

for i in range(1, N):
    vec = vec_calc(A[0], A[i])
    a, left = grouping(A, vec)

    if len(left) == 0:
        print('No')
        exit()
    else:
        b, l = grouping(left, vec)
        if not l:
            print('Yes')
            exit()

a, *left = A
vec = vec_calc(left[0], left[1])
b, l = grouping(left, vec)
if not l:
    print('Yes')
    exit()

print('No')

# C From Y to Y

"""
convineするときの最小値
前からやれば...　使える文字は26個
sにあるaの数 * tにあるaの数　を足し合わせる
1+2+3...の組み合わせで表現したいが
"""

K = getN()
if K == 0:
    print('a')
    exit()
ans = ''
str = 0

while K > 0:
    now = 1
    acc = 0
    while acc + now <= K:
        acc += now
        now += 1
    K -= acc
    ans += chr(str + ord('a')) * now
    str += 1

print(ans)
