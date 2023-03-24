# 좌표 정렬하기 2

# 내 풀이

import sys
n = int(input())
li = []

for _ in range(n) :
    li.append(list(map(int, sys.stdin.readline().split())))

li.sort(key = lambda x: (x[1], x[0]))

for x, y in li :
    print(x, y)