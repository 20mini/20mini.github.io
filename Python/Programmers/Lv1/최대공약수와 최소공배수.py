#https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            GCD=i
    LCM=n*m/GCD
    return [GCD,LCM]