#https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    for GCD in range(min(n,m),0,-1):
        if n%GCD==0 and m%GCD==0:
            break
    LCM=n*m/GCD
    return [GCD,LCM]