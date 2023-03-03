# 접미사 배열

# 1. 내 풀이

li = []
s = input()

for i in range(len(s)) :
    li.append(s[i:])
    
li.sort()

for i in li :
    print(i)

# 2. 다른 사람의 풀이
# - 이게 한줄로 되는구나...

s=input()
print(*sorted(s[i:]for i in range(len(s))))