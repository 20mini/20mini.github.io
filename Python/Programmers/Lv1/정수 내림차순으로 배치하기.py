#https://school.programmers.co.kr/learn/courses/30/lessons/12933?language=python3

def solution(n):
    li=list(str(n))
    li.sort(reverse=True)
    sorted_n=''
    for i in li:
        sorted_n+=i
    return int(sorted_n)