#https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    cnt=0 # 열린 상태로 닫히지 않는 괄호의 개수
    for i in s:
        cnt+=1 if i=='(' else -1
        if cnt<0: return False # 열린 괄호보다 닫은 괄호의 개수가 더 많을 경우
    if cnt==0: return True
    return False