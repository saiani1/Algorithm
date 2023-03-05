# 소수 구하기

# 1. 내 풀이
# - 소수찾기 함수 쓰려다가 시간초과가 났다.
# - 소수판별에는 해당 숫자의 제곱근까지만 순회하면 된다고 해서 math.sqrt내장함수를 사용해보았다.

import math

a, b = map(int, input().split())

def trueFunc (x) :
    isTrue = True
    if x == 1 : isTrue = False
    else :
        n = int(math.sqrt(x))
        for i in range(2, n+1) :
            if x%i == 0 : 
                isTrue = False
                break
    return isTrue

for i in range(a, b+1) : 
    if trueFunc(i) : print(i)