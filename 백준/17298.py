# 오큰수

# 1. 내 풀이
# - 2중 for문으로 하니 시간초과에 걸려서 stack을 사용하여 푼 다른 사람들 풀이를 여러번 봤다. 어렵...ㅠ

import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [str(-1) for _ in range(n)]

for i in range(n) :
    while stack and li[stack[-1]] < li[i] :
        answer[stack.pop()] = str(li[i])
    stack.append(i)
print(' '.join(answer))
