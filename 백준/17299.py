# 오등큰수

# 1. 내 풀이
# - 풀이방법은 오큰수와 비슷하게, count함수를 썼더니 시간초과가 떠서 구글링해보니 Counter라는 컬렉션이 있길래 사용해보았다.

from collections import Counter
n = int(input())
li = list(map(int, input().split()))
cntLi = Counter(li)
answer = [str(-1) for _ in range(n)]
stack = []

for i in range(n) :
    while stack and cntLi[li[stack[-1]]] < cntLi[li[i]] :
        answer[stack.pop()] = str(li[i])
    stack.append(i)
print(' '.join(answer))