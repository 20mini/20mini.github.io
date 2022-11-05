#https://school.programmers.co.kr/learn/courses/30/lessons/42627

from heapq import *
from collections import deque

def solution(jobs):
    end_time_sum=0 # 각 작업 종료 시점들의 합
    job_queue=deque(sorted(jobs, key=lambda x: (x[0],x[1]))) # 요청 시점 순서대로 jobs를 정렬하여 큐에 넣는다.
    heap=[] # 현재 대기중인 작업 목록의 소요 시간
    t=0 # 다음 작업의 시작 시점
    while job_queue or heap:
        if not heap: # 현재 대기중인 작업 목록이 비어 있으면
            heap.append(job_queue[0][1]) # job 큐에서 하나를 꺼내 대기 목록에 넣는다.
            t=job_queue[0][0] # 이때 다음 작업의 시작 시점은 그 작업의 요청 시점과 같아진다.
            job_queue.popleft()
        t+=heappop(heap) # 대기 목록에서 작업을 꺼내고, 다음 작업의 시작 시점이 꺼낸 작업의 소요 시간만큼 늘어난다.
        end_time_sum+=t # 이때 작업 종료 시점은 다음 작업의 시작 시점과 같다.
        while job_queue and job_queue[0][0]<t:# 작업 종료 시점 보다 이전에 요청된 작업이 job 큐에 있을 경우 
            heappush(heap,job_queue[0][1]) # 해당 작업들을 대기 목록에 넣는다.
            job_queue.popleft()
    return (end_time_sum-sum(i[0] for i in jobs))//len(jobs) # 각 작업의 요청부터 종료까지 걸린 시간의 평균 = (각 작업이 끝난 시점들의 합 - 각 작업의 요청 시점들의 합) / 작업의 개수