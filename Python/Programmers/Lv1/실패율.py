#https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    stage_player_num=[0]*(N+1) # 각 스테이지(1~N)에 멈춰있는 사람의 수
    fail_ratio=[0]*(N+1)

    for i in stages:
        if i!=N+1:
            stage_player_num[i]+=1
            
    prev=0 # i stage에 도달하지 못 한 사람의 수
    for i in range(1,N+1):
        fail_ratio[i]=stage_player_num[i]/(len(stages)-prev)
        prev+=stage_player_num[i]
        if prev==len(stages):
            break
            
    return sorted([i for i in range(1,N+1)],reverse=True,key=lambda x: fail_ratio[x])