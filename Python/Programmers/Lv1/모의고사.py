# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    cnt=[0,0,0]
    sol=[[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(len(answers)):
        for j in range(3):
            if answers[i]==sol[j][i%len(sol[j])]:
                cnt[j]+=1
                
    answer=[]
    for i,v in enumerate(cnt):
        if v==max(cnt):
            answer.append(i+1)
    return answer

'''
from itertools import cycle

def solution(answers):
    cnt=[0,0,0]
    sol=[cycle([1, 2, 3, 4, 5]),cycle([2, 1, 2, 3, 2, 4, 2, 5]),cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])]

    for i in range(len(answers)):
        for j in range(3):
            if answers[i]==next(sol[j]):
                cnt[j]+=1
                
    answer=[]
    for i,v in enumerate(cnt):
        if v==max(cnt):
            answer.append(i+1)
    return answer
'''