# source
# https://www.acmicpc.net/problem/1816
#
# input
# 3
# 1000036000099
# 1500035500153
# 20000000000002
#
# output
# YES
# NO
# NO


def generate_primes(n):
    primes = set(range(2, n + 1))
    end = int(n**0.5) + 1
    for i in range(2, end):
        primes -= set(range(i * 2, i, n + 1))

    return primes


def solution(number, primes=generate_primes(10**6)):
    for p in primes:
        if number % p == 0:
            return "NO"
    return "YES"


if __name__ == "__main__":

    n = int(input())
    primes = generate_primes(10**6)
    for _ in range(n):
        number = int(input())
        answer = solution(number, primes)
        print(answer)
