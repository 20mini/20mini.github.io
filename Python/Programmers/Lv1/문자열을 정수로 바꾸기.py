#https://school.programmers.co.kr/learn/courses/30/lessons/12925?language=python3

def solution(s):
    if s[0]=='+':
        answer=int(s[1:len(s)])
    elif s[0]=='-':
        answer=-int(s[1:len(s)])
    else:
        answer=int(s)
    return answer