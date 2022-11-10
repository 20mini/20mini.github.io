#https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True) # 내림차순 정렬
    return max(min(i,v) for i,v in enumerate(citations,start=1))
    # 해당 논문 인용 횟수 이상인 논문의 수와 해당 논문의 인용 횟수 중 더 작은 값이 문제에서의 h가 된다. 그 중 최댓값이 H-Index이다.