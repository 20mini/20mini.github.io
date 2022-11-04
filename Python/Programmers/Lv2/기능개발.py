#https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    deploy=[0]*100 # 각 날 당 배포하는 기능의 수
    day=[] # 각 기능당 배포하는 데 걸리는 기간(일)
    for i,j in zip(progresses,speeds):
        day.append((100-i)//j + (1 if (100-i)%j>0 else 0))
        
    last_day=0 # 이전 기능이 배포되는 데 걸리는 기간
    for v in day:
        if last_day==0:
            deploy[v]+=1
            last_day=v
        else:
            if v<=last_day: # 이전 기능의 배포하는 데 걸리는 기간이 더 크거나 같으면
                deploy[last_day]+=1 # 이전 기능과 같은 날에 배포한다.
            else:
                deploy[v]+=1 # 이전 기능보다 배포하는 데 걸리는 기간이 더 크면 다른 날에 배포한다.
                last_day=v
    return [i for i in deploy if i >0]