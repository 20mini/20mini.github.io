#https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3

def solution(x):
    sum=0
    str_x=str(x)
    for i in str_x:
        sum+=int(i)
    if(x%sum==0):
        answer = True
    else:
        answer = False
    return answer