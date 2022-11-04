#https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights=deque(truck_weights)
    queue=deque() # 다리 위에 있는 트럭들을 나타내는 큐
    t=0 # 현재 시간
    while truck_weights or queue: # 대기 트럭이 존재하거나 다리 위에 트럭이 아직 있을 경우 반복
        t+=1
        if queue and queue[0]['time']==t-bridge_length: # 맨 앞에 있는 트럭이 다리를 전부 건넌 경우
            weight+=queue.popleft()['weight'] # 다리가 견딜 수 있는 무게 증가
        if truck_weights and truck_weights[0]<=weight: # 첫 번째 대기 트럭이 다리가 견딜 수 있는 무게 이하일 경우
            queue.append({'time':t,'weight':truck_weights[0]}) # time은 트럭이 다리를 건너기 시작한 시간, weight는 트럭의 무게
            weight-=truck_weights.popleft() # 다리가 견딜 수 있는 무게 감소
    return t