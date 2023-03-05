# 최소공배수

# 1. 내 풀이
# - 파이썬 내장함수를 써봤다.

import math

n = int(input())

for _ in range(n) :
    a, b = map(int, input().split())
    print(math.lcm(a, b))