# source
# https://www.acmicpc.net/problem/1991
# input
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
# output
# ABDCEFG
# DBAECFG
# DBEGFCA


def solution(graph):
    preorder = []
    inorder = []
    postorder = []

    def recur(node):

        if node == ".":
            return

        preorder.append(node)
        recur(graph[node][0])
        inorder.append(node)
        recur(graph[node][1])
        postorder.append(node)

    recur("A")
    return (
        "".join(preorder),
        "".join(inorder),
        "".join(postorder),
    )


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    n = 7
    # n = int(input())

    data = [
        "A B C",
        "B D .",
        "C E F",
        "E . .",
        "F . G",
        "D . .",
        "G . .",
    ]
    nodes = {}
    for _ in range(n):
        a, b, c = data[_].split()  # input().split()
        nodes[a] = [b, c]

    for answer in solution(nodes):
        print(answer)
