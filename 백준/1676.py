# 팩토리얼 0의 개수

# 1. 내 풀이

n = int(input())
result = 1
cnt = 0

for i in range(1, n+1) : result = result*i
li = list(str(result))
for i in li[::-1] :
    if i == '0' : cnt += 1
    else : break
print(cnt)