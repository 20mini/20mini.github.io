#https://school.programmers.co.kr/learn/courses/30/lessons/42626

from heapq import *

def solution(scoville, K):
    answer = 0
    heap=[] # Leo가 가진 음식들의 스코빌 지수를 담은 최소 힙
    for i in scoville: # 힙 구성
        heappush(heap,i)
    while heap[0]<K and len(heap)>=2: # 가장 낮은 스코빌 지수(heap[0])가 K 이상이거나 힙의 길이가 2보다 작을 때까지 가장 낮은 두 스코빌 지수의 음식을 섞는 과정을 반복한다.
        heappush(heap,heappop(heap)+heappop(heap)*2)
        answer+=1
    if heap[0]<K: # 가장 낮은 스코빌 지수가 K보다 작다 = 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없다.
        return -1
    return answer