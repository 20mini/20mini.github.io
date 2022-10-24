#https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    return sum(i*j for i,j in zip(sorted(A),sorted(B,reverse=True)))