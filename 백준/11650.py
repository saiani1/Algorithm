# 좌표 정렬하기

# 내 풀이
# - sort의 key옵션을 이용하면 sort옵션을 설정할 수 있었다.

n = int(input())
li = []

for _ in range(n) :
    li.append(list(map(int,input().split())))
    
li.sort(key = lambda x: (x[0], x[1]))

for x, y in li :
    print(x, y)