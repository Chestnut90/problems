# source
# https://www.acmicpc.net/problem/14568
#
# inputs
# 6
# outputs
# 1


def solution(n):
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1 - i):
            k = n - i - j
            if i - j >= 2 and k % 2 == 0 and k != 0:
                answer += 1

    return answer


def solution2(n):
    """
    O(n)
    """
    answer = 0
    for i in range(2, n - 1, 2):
        answer += (n - i - 2) // 2
    return answer


if __name__ == "__main__":

    n = int(input())
    print(solution(n))
    print(solution2(n))
