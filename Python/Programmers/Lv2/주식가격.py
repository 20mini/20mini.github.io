#https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer=[0]*len(prices)
    stack=[] # 주식의 시점과 그때의 가격을 나타내는 스택
    for i,v in enumerate(prices):
        while stack and v<stack[-1]['value']: # 스택의 마지막 원소의 가격보다 현재 가격이 떨어졌으면 반복
            answer[stack[-1]['time']-1]=i+1-stack[-1]['time'] # 스택의 마지막 원소의 가격이 떨어지지 않은 기간을 구한다. (i+1은 현재 시각)
            stack.pop() # 그리고 그 원소를 스택에서 꺼낸다.
        stack.append({'time': i+1, 'value':v})
    for i in stack: # 남아 있는 원소들은 끝까지 가격이 떨어지지 않은 것들이다.
        answer[i['time']-1]=(len(prices)-i['time']) # len(prices)는 마지막 시점과 같음
    return answer