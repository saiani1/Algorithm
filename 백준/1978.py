# 소수 찾기

# 1. 내 풀이
# - for문으로 하나하나 나눠주어서 소수를 판별했다.

n = int(input())
li = list(map(int, input().split()))
cnt = 0

def trueFunc (a) :
    isTrue = True
    if a == 1 : isTrue = False
    else :
        for j in range(2, li[i]) :
            if li[i]%j == 0: 
                isTrue = False
                break
    return isTrue

for i in range(n) :
    if trueFunc(li[i]) : cnt += 1
print(cnt)

# 2. 다른 사람의 풀이