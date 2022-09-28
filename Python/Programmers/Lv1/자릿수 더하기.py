#https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=python3

def solution(n):
    answer = 0
    str_n=str(n)
    for i in str_n:
        answer+=int(i)
    return answer