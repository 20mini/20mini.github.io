#https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort(reverse=True) # 몸무게 내림차순으로 정렬
    min_idx=len(people)-1 # 보트에 아직 안 탄 사람 중 가장 낮은 몸무게의 인덱스
    for i,v in enumerate(people):
        if i == min_idx: # 보트에 아직 안 탄 사람이 한 명 남았을 때
            answer+=1
            break
        elif i>min_idx: # 보트에 모두 탔을 때
            break
        else:
            if v+people[min_idx]<=limit: # 보트에 아직 안 탄 사람 중 몸무게가 제일 높은 사람의 몸무게(v)와 제일 낮은 사람의 몸무게 합이 limit 이하인지 판단
                min_idx-=1 # 그럴 경우 2명이 한꺼번에 보트를 타게 한다. min_idx 1만큼 감소
            answer+=1 # 아닐 경우 몸무게가 제일 높은 사람 혼자 타게 한다.
    return answer