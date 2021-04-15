# A - Spy Detected!

"""
all the numbers except one are same
The numbers in the array are numbered from one.
"""

N = getN()
for i in range(N):
    M = getN()
    A = getList()
    d = defaultdict(int)
    for i in range(M):
        d[A[i]] += 1

    for i in range(M):
        if d[A[i]] == 1:
            print(i + 1)
            break

# B - Almost Rectangle
"""
two cells are marked.
"""

N = getN()
for _ in range(N):
    H = getN()
    maze = [list(input()) for i in range(H)]
    P = []
    for i in range(H):
        for j in range(H):
            if maze[i][j] == '*':
                P.append([i, j])

    y1, x1 = P[0]
    y2, x2 = P[1]
    if x1 == x2:
        if x1 == 0:
            maze[y1][x1 + 1] = '*'
            maze[y2][x2 + 1] = '*'
        else:
            maze[y1][x1 - 1] = '*'
            maze[y2][x2 - 1] = '*'
    elif y1 == y2:
        if y1 == 0:
            maze[y1 + 1][x1] = '*'
            maze[y2 + 1][x2] = '*'
        else:
            maze[y1 - 1][x1] = '*'
            maze[y2 - 1][x2] = '*'
    else:
        maze[y1][x2] = '*'
        maze[y2][x1] = '*'

    for m in maze:
        print(''.join(m))

# C - A-B Palindrome

"""
palindrome: 回文
have exactly a characters '0': ちょうど0をa個
Note that: 留意してください
You need to replace all the characters with '?' in the string s by '0' or '1'

まず回文にできるか判定する
"""

for ct in range(int(input())):
  a, b = map(int, input().split())
  n = a + b
  s = list(input())

  for i in range(n):
    if s[i] == '?':
      s[i] = s[n - i - 1]

  a -= s.count('0')
  b -= s.count('1')

  for i in range(n // 2 + 1):
    if i != n - i - 1 and s[i] == '?':
      if a > 1:
        s[i] = s[n - i - 1] = '0'
        a -= 2

      elif b > 1:
        s[i] = s[n - i - 1] = '1'
        b -= 2

    elif s[i] == '?':
      if a > 0:
        s[i] = '0'
        a -= 1

      elif b > 0:
        s[i] = '1'
        b -= 1

  s = ''.join(s)
  print(s) if s == s[::-1] and a == b == 0 else print(-1)

# D Corrupted Array

"""
Corrupted Array
some array a1, a2, a3... was guessed まず配列を考えます
b = aのコピー + aの総和 + 任意の数x をシャッフルしたもの
xを一つ固定すると　その中に和の1/2になる数があればOK
"""

T = getN()
for _ in range(T):
    N = getN()
    N += 2
    A = getList()
    A.sort()
    su = sum(A)
    # x = A[i]
    for i in range(N):
        target = su - A[i]
        # A[-1] = bn+1 number ?
        if i < N - 1:
            if A[-1] * 2 == target:
                print(*[A[j] for j in range(N) if j != i and j != N - 1])
                break
        # A[-2] = bn+1 number ?
        else:
            if A[-2] * 2 == target:
                print(*[A[j] for j in range(N) if j != i and j != N - 2])
                break
    else:
        print(-1)

# F - Education

"""
二分探索でしょ（適当）
4 15　positions, target
1 3 10 11 earnings
1 2 7 for stepup

最速でポジションを上げていく
"""

T = getN()
for _ in range(T):
    N, M = getNM()
    A = getList()
    B = getList()

    day = 0
    money = 0
    ans = (M + A[0] - 1) // A[0] # if you stay in level0 position

    for i in range(N - 1):
        if B[i] > money:
            # get more money enough to get a course
            need = B[i] - money
            t = (need + A[i] - 1) // A[i]
            day += t
            money += t * A[i]

        # get a course
        day += 1
        money -= B[i]
        # if you stay level i+1 position
        need = max(0, M - money)
        ans = min(ans, day + ((need + A[i + 1] - 1) // A[i + 1]))

    print(ans)

# G - Short Task

"""
denote: 示す
約数の和がcになる値を出せ
c <= 10,000,000 なので全種類出すのは調和級数でも無理そう

で通る　それはそう
tは小さいのでこれでなんとか

素数は1 + 素数
2で割れるなら 1 + 2 + 素数
全ての
約数の総和は(1 + 2 + 2^2) * (1 + 3 + 3^2) * ...みたいにやる
cの素因数分解は間に合う
それぞれの因数について(1 + n + n^2...)の形で表現できるか

まず1を引いた数は素数ですか？　いいえ

"""

lim = 10 ** 7 + 7
l = [1] * lim
for i in range(2, lim):
    j = i
    while j < lim:
        l[j] += i
        j += i

ans = [-1] * lim
for i in range(lim - 1, 0, -1):
    if l[i] < lim:
        ans[l[i]] = i

T = getN()
for _ in range(T):
    c = getN()
    print(ans[c])
