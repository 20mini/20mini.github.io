#https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    for i in range(0,len(seoul)):
        if seoul[i] == "Kim":
            break
    answer = '김서방은 '+str(i)+'에 있다'
    return answer