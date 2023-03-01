# 요세푸스 문제

# 1. 내 풀이
# - 아래와 같이 풀었더니 시간초과가 떴다. 

import sys
N, K = map(int, sys.stdin.readline().split())
queue = list(range(1, N+1))
result = []

while True :
    if not queue : break
    for i in range(K) :
        queue.append(queue.pop(0))
        if i == K-1 : result.append(str(queue.pop()))
print("<", ", ".join(result), ">", sep='')

# - index를 사용해서 풀어야 시간초과가 뜨지 않는다고 해서 코드를 아래와 같이 바꿔주었다.

import sys
N, K = map(int, sys.stdin.readline().split())
queue = list(range(1, N+1))
result = []
idx = 0

while queue :
    idx = (idx + K - 1) % len(queue)
    result.append(str(queue.pop(idx)))
print("<", ", ".join(result), ">", sep='')