#https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer=[0,0]
    while s!='1':
        num_of_0=s.count('0') # 0의 개수
        answer[0]+=1
        answer[1]+=num_of_0
        s=bin(len(s)-num_of_0)[2:]
    return answer