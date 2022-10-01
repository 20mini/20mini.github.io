#https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    n=0
    for i in range(0,len(seoul)):
        if seoul[i] == "Kim":
            n=i
            break
    answer = '김서방은 '+str(n)+'에 있다'
    return answer