# ATM

# 1. 내 풀이
# - 내림차순 정렬해서 각각의 소요시간 tmp을 sum에 더해주었다.

n = int(input())
li = list(map(int, input().split()))
li.sort()
sum = 0

for i in range(n) :
    tmp = 0
    for j in range(i+1) :
        tmp += li[j]
    sum += tmp
print(sum)

# 2. 다른 사람의 풀이
# - sorted를 쓰면 list를 쓰지 않아도 정렬이 되는구나

n = int(input())

l = sorted(map(int,input().split()))

t = 0
for i in range(n):
  t = t + (n-i)*l[i]

print(t)