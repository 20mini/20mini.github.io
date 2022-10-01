#https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    if b>a:
        answer = (a+b)*(b-a+1)/2
    else:
        answer = (a+b)*(a-b+1)/2
    return answer