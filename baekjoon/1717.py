"""
# 출처
# https://www.acmicpc.net/problem/1717
# 인풋
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
# 아웃풋
# NO
# NO
# YES
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def _find(a):
    if roots[a] != a:
        roots[a] = _find(roots[a])
        return _find(roots[a])
    return a


def _union(a, b):
    a = _find(a)
    b = _find(b)

    if a == b:
        return
    elif ranks[a] > ranks[b]:
        roots[a] = b
    elif ranks[a] < ranks[b]:
        roots[b] = a
    else:
        roots[a] = b
        ranks[a] += 1


if __name__ == "__main__":

    n, m = map(int, input().split())
    roots = [i for i in range(n + 1)]
    ranks = [0 for i in range(n + 1)]

    for _ in range(m):
        c, a, b = map(int, input().split())

        if c == 0:
            _union(a, b)
        else:
            word = "YES" if _find(a) == _find(b) else "NO"
            print(word)
