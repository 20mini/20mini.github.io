#https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    clothes=[1]*(n+2) # 1번부터 n번까지의 학생이 가진 옷의 수
    # 인덱스 0은 1번 학생의 앞번호 확인 시, 인덱스 n+1은 n번 학생의 뒷번호 확인 시 오류 방지를 위해 생성
    clothes[0], clothes[n+1] = 0, 0 # 0번과 n+1번 학생은 없으므로
    for i in reserve: clothes[i]=2 
    for i in lost: clothes[i]-=1
    
    for i in range(1,n+1):
        if clothes[i]==0:
            if clothes[i-1]==2:
                clothes[i-1]-=1
                clothes[i]=1
            elif clothes[i+1]==2:
                clothes[i+1]-=1
                clothes[i]=1
    answer = 0
    for i in clothes: 
        if i>=1: 
            answer+=1 
    return answer