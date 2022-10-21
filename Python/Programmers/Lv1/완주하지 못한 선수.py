#https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participants={} # 참여자 이름(key) : 참여자의 수(value)
    for i in participant:
        if i in participants: participants[i]+=1
        else: participants[i]=1
    for i in completion: participants[i]-=1 # 완주한 사람은 value를 -1 해준다.
    for i in participants:
        if participants[i]==1: 
            return i # value가 남아있는(value가 1인) 참여자의 이름 반환