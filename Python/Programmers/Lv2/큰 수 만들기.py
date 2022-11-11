#https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack=[] # 정답 문자열을 구성하는 문자들이 들어 있는 스택
    for i,v in enumerate(number):
        while k>0 and stack and v>stack[-1]: # 참고하는 문자가 스택의 맨 위 원소보다 크면 반복
            stack.pop() # 스택에서 원소를 꺼낸다.
            k-=1 # 제거할 수 있는 수의 개수를 하나 줄인다.
        stack.append(v) # 스택이 비어있거나 위 반복을 끝내면 스택에 원소를 넣는다.
    return "".join(stack[:len(number)-k]) # 아직 제거해야 할 수가 남았으면(k>0), 뒤에서 k개 만큼의 문자들을 제외하고 합쳐서 반환