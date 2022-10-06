#https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        sqrt_i=int(i**0.5)
        if sqrt_i**2==i:
            answer-=i
        else:
            answer+=i
    return answer