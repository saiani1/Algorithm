# 단어 뒤집기 2

# 1. 내 풀이
# - 덱을 이용해 풀었다. 근데 이렇게 코드가 일어질 일인가?...

S = input()
deque = []
result = []

for i in range(len(S)) :
    if S[i] == '>' :
        deque.append(S[i])
        while deque :
            result.append(deque.pop(0))
    elif S[i] == '<' and deque :
        while deque :
            result.append(deque.pop(-1))
        deque.append(S[i])
    elif S[i] == ' ' and deque[0] != '<' : 
        while deque :
            result.append(deque.pop(-1))
        result.append(S[i])        
    elif i == len(S)-1 and deque :
        result.append(S[i])        
        while deque :
            result.append(deque.pop(-1))
    else :
        deque.append(S[i])

print(''.join(result))

# 2. 다른 사람의 코드
# - 다들 'seq.replace('>', '<').split('<')'와 'if i % 2 == 1'를 많이 쓰는 경향이 있었음.
# - 덱을 사용하니 코드가 길어져서 다른 코드를 보니 굳이 덱을 사용할 필요가 있었을까 싶었다.

from sys import stdin


def sol(seq: str) -> str:
    seq: list = seq.replace('>', '<').split('<')
    ans: str = ''

    for i in range(len(seq)):
        if i % 2 == 1:
            ans += f'<{seq[i]}>'
        else:
            ans += reverse_words(seq[i])
    return ans


def reverse_words(words: str) -> str:
    return ' '.join(word[::-1] for word in words.split())


print(sol(stdin.readline().rstrip()))