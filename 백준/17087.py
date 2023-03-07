# 숨바꼭질 6

# 1. 내 풀이
# - 동생과 내 위치를 뺀 값을 배열에 넣어주고, 해당 배열의 최대공약수를 구했다.

import math

N, S = map(int, '3 3'.split())
li = list(map(int, '1 7 11'.split()))
gcdLi = []
result = 0

for i in li :
  x = S-i
  if x == 0 : continue
  else : gcdLi.append(abs(x))

for i in gcdLi :
  result = math.gcd(i, result)
print(result)

# 2. 다른 사람의 풀이
# - 리스트 앞에 별표를 붙이니 한번에 모든 리스트값의 최대공약수가 구해지는 걸 알았다.

from math import gcd
n,x  = map(int, input().split())
a_list = [abs(i-x) for i in map(int, input().split())]
print(gcd(*a_list))