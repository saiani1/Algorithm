# 문자열 집합

# 1. 내 풀이

n, compareN = map(int, input().split())
li = [input() for _ in range(n)]
compareLi = [input() for _ in range(compareN)]
cnt = 0

for i in compareLi :
    if i in li : cnt += 1
print(cnt)