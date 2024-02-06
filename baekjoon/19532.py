# 출처
# https://www.acmicpc.net/problem/19532
# 입력
# 1 3 -1 4 1 7
# 출력
# 2 -1

m = [
    [1, 2],
    [2, 3]
]

def inverse_2x2(a, b, k1, c, d, k2):
    '''
    [ [ a, b ], [ c, d ] ] 's inverse => 
    1 / (a * d - b * c) [ [ d, -b ], [ -c, a ] ]
    '''
    
    k = a * d - b * c
    return [(d * k1 - b * k2) // k, (-c * k1 + a * k2) // k]
    

    

if __name__ == "__main__":

    a, b, c, d, e, f = map(int, input().split())
    eq1 = lambda x, y : a * x + b * y
    eq2 = lambda x, y : d * x + e * y

    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if eq1(x, y) == c and eq2(x, y) == f:
                print(x, y)
                break

    print(inverse_2x2(a, b, c, d, e, f))