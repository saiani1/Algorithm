# 거스름돈

# 1. 내 풀이
# - 기존 동전 0에서 사용한 코드를 복습하는 느낌으로 풀었다.

n = 1000-int(input())
coinLi = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in coinLi :
    cnt += n // i
    n %= i
print(cnt)