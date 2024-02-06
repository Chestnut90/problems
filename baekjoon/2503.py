# 출처
# https://www.acmicpc.net/problem/2503
# 입력
# 4
# 123 1 1
# 356 1 0
# 327 2 0
# 489 0 1
# 출력
# 2

def counter(a : list, b : list):
    ball = len(set(a).intersection(set(b)))
    strike = 0
    for _a, _b in zip(a, b):
        if _a == _b:
            strike += 1
            ball -= 1
    return [strike, ball]

if __name__ == "__main__":


    n = int(input())

    qs = []
    for _ in range(n):
        number, strike, ball = map(int, input().split())
        qs.append([list(str(number)), strike, ball])

    answer = 0
    for i in range(100, 1000):
        
        s = list(str(i))
        
        if len(set(s)) < 3 or 0 in s:
            continue

        for q in qs:
            if counter(s, q[0]) != q[1:]:
                break
        else:
            answer += 1

    print(answer)

            
