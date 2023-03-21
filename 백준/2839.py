# 설탕배달

# 1. 내 풀이
# - 5키로로 나눠 떨어질 수도 있고, 3키로로만 나눠 떨어질 수 있어서
# - while문에 if문을 사용하여 처리

n = int(input())
cnt = 0

while n >= 0 :
    if n%5 == 0 :
        print(n // 5 + cnt)
        break
    n -= 3
    cnt += 1
else :
    print(-1)