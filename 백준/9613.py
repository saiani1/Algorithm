# GCD합

# 1. 내 풀이
# - 내장함수를 써서 최대공약수를 구한 다음 sum에 누적시켜 print했다.

import math

n = int(input())

for _ in range(n) :
    li = list(map(int, input().split()))
    sum = 0
    for i in range(1, li[0]) :
        for j in range(i+1, li[0]+1) :
            sum += math.gcd(li[i], li[j])
    print(sum)