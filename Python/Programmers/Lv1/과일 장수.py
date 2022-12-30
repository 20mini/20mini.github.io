#https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) # 내림차순 정렬
    for i,v in enumerate(score):
        if (i+1)%m==0: # 사과의 (인덱스+1)이 m의 배수일 때
            answer+=v*m # 해당 사과가 상자에 담긴 사과들 중 최저점을 가지고 있다.
    return answer