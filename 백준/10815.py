# 숫자 카드

# 1. 내 풀이
# - if in을 쓰면 시간초과가 나는 문제였는데 set으로 바꿔주니까 시간초과가 안 났다.

n = int(input())
li = set(map(int, input().split()))
compareN = int(input())
compareLi = list(map(int, input().split()))

answer = [0]*compareN

for i in range(compareN) :
    if compareLi[i] in li : answer[i] = 1
print(*answer)

# 2. 다른 사람의 풀이
# - 이분 탐색 문제였어서 이분탐색을 사용한 풀이를 가져왔다.

import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

def binarySearch(array, key, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            end = mid-1
        elif array[mid] < key:
            start = mid+1
    return None


for i in range(m):
    if binarySearch(card, check[i], 0, n-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
