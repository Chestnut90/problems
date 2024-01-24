# source
# https://www.acmicpc.net/problem/2589
# input
# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW
# output
# 8

import sys
from collections import deque

input = sys.stdin.readline

points = [[-1, 0], [1, 0], [0, -1], [0, 1]]
m, n = map(int, input().split())
arr = [list(input()) for _ in range(m)]

def bfs(y, x):
    visited = [[-1] * n for _ in range(m)]
    q = deque([[y, x]])
    visited[y][x] = 0
    distance = 0
    
    while q:
        cy, cx = q.popleft()
        
        for dy, dx in points:
            ny, nx = cy + dy, cx + dx
            if 0 > ny or ny >= m or 0 > nx or nx >=n or \
                visited[ny][nx] > -1 or arr[ny][nx] == "W":
                continue
            visited[ny][nx] = visited[cy][cx] + 1
            distance = max(visited[ny][nx], distance)
            q.append([ny, nx])
    return distance

def solution(m, n, arr):
    max_distance = 0
    for y in range(m):
        for x in range(n):
            if arr[y][x] == "W":
                continue
            max_distance = max(max_distance, bfs(y, x))
    return max_distance    

if __name__ == "__main__":

    m, n = map(int, input().split())
    arr = [list(input()) for _ in range(m)]    

    print(
        solution(m, n, arr),
    )
