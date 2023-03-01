# 덱

# 1. 내 풀이
# - append함수는 리스트 맨 마지막에 데이터를 넣는대서 insert함수를 이용해보았다.

import sys
n = int(input())
deque = []

for _ in range(n) :
    s = sys.stdin.readline().split()
    if s[0] == 'push_front': deque.insert(0, s[1])
    elif s[0] == 'push_back': deque.append(s[1])
    elif s[0] == 'pop_front': print(deque.pop(0) if deque else -1)
    elif s[0] == 'pop_back': print(deque.pop(-1) if deque else -1)
    elif s[0] == 'size': print(len(deque))
    elif s[0] == 'empty': print(1 if not deque else 0)
    elif s[0] == 'front': print(deque[0] if deque else -1)
    elif s[0] == 'back': print(deque[-1] if deque else -1)