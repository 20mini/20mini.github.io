#https://school.programmers.co.kr/learn/courses/30/lessons/131705

def solution(number):
    answer = 0
    l=len(number)
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if number[i]+number[j]+number[k]==0:
                    answer+=1
    return answer

'''
from itertools import combinations

def solution(number):
    answer = 0
    for i in combinations(number,3):
        if sum(i)==0:
            answer+=1
    return answer
'''