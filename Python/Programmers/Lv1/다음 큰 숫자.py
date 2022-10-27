#https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = n+1
    while bin(answer).count('1')!=bin(n).count('1'): # answer을 n+1부터 시작해서 1씩 더해가며 이진수일 때 1의 개수가 n과 같아질 때 answer 값을 반환한다.
        answer+=1
    return answer