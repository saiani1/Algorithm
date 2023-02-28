# 단어 뒤집기

# 1. 내 풀이
# - j[::-1]을 사용하여 문자열을 뒤집어 준다.

n = int(input())

for i in range(n) :
    li = list(map(str, input().split()))
    for j in li :
        if len(j) == 0 : print(j)
        else : print(j[::-1])

# 2. 다른 사람의 풀이
# - for문은 한줄로 쓸 수 있다. comprehension 공부해보기!

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(' '.join([i[::-1] for i in input().split()]))