# 최대공약수와 최소공배수

# 1. 내 풀이
# - for문으로 2부터 max(a, b)까지 나누는 무식한 방법을 쓰다가
# - 유클리드 호제법이라는 게 있어서 적용해봤다.

a, b = map(int, '24 18'.split())
maxNum = max(a, b)
minNum = min(a, b)

while minNum != 0 :
    [maxNum, minNum] = [minNum, maxNum%minNum]

print(maxNum)
print(int(maxNum*(a/maxNum)*(b/maxNum)))

# 2. 다른 사람의 풀이
# - 파이썬에는 최소공배수와 최대공약수를 구할 수 있는 내장함수가 있다.

import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))