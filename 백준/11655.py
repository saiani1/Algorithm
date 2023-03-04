# ROT13

# 1. 내 풀이

S = 'One is 1'
result = []

for i in S :
    if ord(i) >= 65 and ord(i) <= 90 :
        if ord(i)+13 > 90 : result.append(chr(ord(i)+13-26))
        else : result.append(chr(ord(i)+13))            
    elif ord(i) >= 97 and ord(i) <= 122 :
        if ord(i)+13 > 122 : result.append(chr(ord(i)+13-26))
        else : result.append(chr(ord(i)+13))            
    else : result.append(i)

print(''.join(result))