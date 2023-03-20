# 동전 0

# 1. 내 풀이
# - 그리디 입문문제라 예제를 보고 풀었다.
# - 권종을 오름차순 한 다음, 몫을 cnt에 저장하고, total에 나머지를 저장하며 루프를 도는 풀이가 신기했음

n, total = map(int, input().split())
li = []
cnt = 0

for _ in range(n) :
    tmp = input()
    li.append(int(tmp))
li.sort(reverse=True)

for i in li :
    cnt += total // i
    total %= i
print(cnt)

# 2. 다른 사람의 풀이
# - 권종을 받자마자 리스트에 저장하는 간단한 식이 있었다.

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
m = 0
for i in range(n-1, -1, -1):
    m += k // a[i]
    k %= a[i]
print(m)