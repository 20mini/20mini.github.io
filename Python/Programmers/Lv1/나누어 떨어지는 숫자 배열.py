#https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=python3

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor==0:
            answer.append(i)
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer