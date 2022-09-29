# https://school.programmers.co.kr/learn/courses/30/lessons/12934?language=python3

def solution(n):
    answer = -1
    sqrt_n=int(n**0.5)
    if sqrt_n**2==n:
        answer=(sqrt_n+1)**2
    return answer