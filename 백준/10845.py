# 큐

# 1. 내 풀이
# - 스택의 다른 사람 풀이 코드패턴을 따라 써보았다.

import sys
n = int(input())
queue = []

for _ in range(n) :
    s=sys.stdin.readline().split()
    if s[0] == 'push': queue.append(s[1])
    elif s[0] == 'pop': print(queue.pop(0) if queue else -1)
    elif s[0] == 'size': print(len(queue))
    elif s[0] == 'empty': print(1 if not queue else 0)
    elif s[0] == 'front': print(queue[0] if queue else -1)
    elif s[0] == 'back': print(queue[-1] if queue else -1)