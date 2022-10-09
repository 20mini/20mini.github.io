#https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer=[]
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        else:
            if answer[len(answer)-1]!=i:
                answer.append(i)
    return answer