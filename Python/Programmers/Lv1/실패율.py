#https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    pos=[0]*(N+1)
    fail_ratio=[0]*(N+1)

    for i in stages:
        if i!=N+1:
            pos[i]+=1
            
    prev=0
    for i in range(1,N+1):
        fail_ratio[i]=pos[i]/(len(stages)-prev)
        prev+=pos[i]
        if prev==len(stages):
            break
            
    return sorted([i for i in range(1,N+1)],reverse=True,key=lambda x: fail_ratio[x])