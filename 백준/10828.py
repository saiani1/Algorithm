# 스택

# 1. 내 풀이
# - 시간 초과로 입력을 sys로 바꿔주었다.

import sys
n = int(sys.stdin.readline()) 
stack = []

for i in range(n) :
    a = list(sys.stdin.readline().split())
    if a[0] == 'push' :
        stack.append(int(a[1]))
    elif a[0] == 'pop' :
        if len(stack) == 0 : print(-1)
        else :
            popNum = stack.pop()
            print(popNum)
    elif a[0] == 'size' :
        print(len(stack))
    elif a[0] == 'empty' :
        if len(stack) == 0 : print(1)
        else : print(0)
    else :
        if len(stack) == 0 : print(-1)
        else : print(stack[-1])

# 2. 다른 사람의 풀이
# - for문에서 인덱스를 굳이 쓸 필요없을 땐 변수자리에 '_'를 쓴다.
# - if문을 한 줄로도 쓸 수 있다. ex. 결과 = A if 조건 else B

import sys
N=int(input())
stk=[]
for _ in range(N):
    cmd=sys.stdin.readline().split()
    if cmd[0] == 'push': stk.append(int(cmd[1]))
    elif cmd[0] == 'pop': print(stk.pop() if stk else -1)
    elif cmd[0] == 'size': print(len(stk))
    elif cmd[0] == 'empty': print(1 if not stk else 0)
    elif cmd[0] == 'top': print(stk[-1] if stk else -1)