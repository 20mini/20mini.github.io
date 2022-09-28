#https://school.programmers.co.kr/learn/courses/30/lessons/12932?language=python3

def solution(n):
    answer = []
    str_n=str(n)
    for i in str_n:
        answer.insert(0,int(i))
    return answer