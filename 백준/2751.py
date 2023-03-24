# 수 정렬하기 2

# 1. 내 풀이
# - 자꾸 시간초과가 떠서 여러줄 입력받는 부분에 sys.stdin.readline을 써주는게 정답이었다.

import sys

n = int(input())

li = [int(sys.stdin.readline()) for _ in range(n)]

li.sort()

print(*li, sep='\n')