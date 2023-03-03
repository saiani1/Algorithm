# 알파벳 개수

# 1. 내 풀이
# - 아스키코드 값으로 for문을 돌렸다.

S = input()

for i in range(97, 123) :
    cnt = 0
    for j in S :
        if ord(j) == i : cnt += 1
    if cnt == 0 : print(0, end=' ')
    else : print(cnt, end=' ')

# 2. 다른 사람의 풀이
# - 이렇게 한줄로 간단하게 쓸 수 있었다...
# - 리스트 앞에 별을 붙여주면 데이터를 풀어 각각으로 만들어준다고 한다.

a=[0]*26
for s in input(): a[ord(s)-97]+=1
print(*a)