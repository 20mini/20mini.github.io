#https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    bonus={'S':1,'D':2,'T':3}
    scores=[]
    start_idx=0
    for i,v in enumerate(dartResult):
        if not dartResult[i-1].isdigit() and dartResult[i].isdigit():
            start_idx=i
        elif v in bonus:
            scores.append(int(dartResult[start_idx:i])**bonus[v])
        elif v=='*':
            scores[-2:]=[i*2 for i in scores[-2:]]
        elif v=='#':
            scores[-1]*=-1
    return sum(scores)