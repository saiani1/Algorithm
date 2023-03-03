# 문자열 분석

# 1. 내 풀이
# - 아스키코드로 범위를 설정해서 풀었다. 입력값이 어디서 끝날지 몰라 try/except문을 사용했다.

while True :
    try :
        li = [0]*4
        s = input()
        for i in s :
            if ord(i) >= 97 and ord(i) <= 122 : li[0]+=1
            elif ord(i) >= 65 and ord(i) <= 90 : li[1]+=1
            elif ord(i) >= 48 and ord(i) <= 57 : li[2]+=1
            elif i == ' ' : li[3]+=1
        print(*li)
    except: break