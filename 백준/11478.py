# 서로 다른 부분 문자열의 개수

# 1. 내 풀이

n = input()
li = set()

for i in range(len(n)):
    for j in range(i, len(n)):
        li.add(n[i:j+1])
print(len(li))