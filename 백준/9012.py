# 괄호

# 1. 내 풀이
# - stack에 짝이 안 맞는 괄호가 있는지 확인하는 방법을 써봤다.

n = int(input())

for i in range(n) :
    stack = []
    li = list(input())
    for j in li :
        isLast = True
        if j == '(' : stack.append(j)
        else :
            if len(stack) != 0 : stack.pop()
            else :
                print('NO')
                isLast = False
                break
    if isLast == True and len(stack) == 0 : print('YES')
    elif isLast == True and len(stack) != 0 : print('NO')

# 2. 다른 사람의 풀이
# - while문을 계속 돌려서 replace로 괄호를 제거하고, 남는 문자가 있으면 NO, 없으면 YES를 리턴한다.

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    while '()' in s:
        s = s.replace('()','')
    print('NO') if s else print('YES')