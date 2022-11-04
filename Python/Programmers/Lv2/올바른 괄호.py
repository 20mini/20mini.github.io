#https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack=[] # 열린 상태로 닫히지 않는 괄호가 들어 있는 스택
    for i in s:
        if i=='(':
            stack.append(i) # 스택에 추가
        elif len(stack)<=0: # 닫는 괄호가 열린 괄호보다 많을 경우
            return False
        else:
            stack.pop()
    if len(stack)>0: # 모든 문자를 순회했을 때 열린 상태로 닫히지 않은 괄호가 남아 있을 경우
        return False
    return True