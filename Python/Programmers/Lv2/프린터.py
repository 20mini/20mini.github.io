#https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    print_order=[0]*len(priorities) # 문서의 인쇄 순서들
    queue=[] # 인쇄 대기목록
    for i,v in enumerate(priorities):
        queue.append({'initial_pos': i, 'priority': v}) # initial_pos는 문서들의 처음 대기목록에서의 위치, priority는 각 문서의 중요도
    order=1
    queue=deque(queue)
    while queue: # 인쇄 대기목록이 비어있지 않으면 반복
        J=queue.popleft() # 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼낸다.
        if queue and J['priority']<max(queue,key=lambda x: x['priority'])['priority']: # 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
            queue.append(J) #  J를 대기목록의 가장 마지막에 넣는다.
        else:
            print_order[J['initial_pos']]=order # 그렇지 않으면 J를 인쇄한다. -> 인쇄 순서가 정해진다.
            order+=1
    return print_order[location]