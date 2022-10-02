# https://school.programmers.co.kr/learn/courses/30/lessons/12935?language=python3

def solution(arr):
    answer=arr
    min=answer[0]
    for i in answer:
        if min > i:
            min=i
    answer.remove(min)
    if len(answer)==0:
        answer.append(-1)
    return answer