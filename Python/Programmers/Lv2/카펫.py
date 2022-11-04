#https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    for h in range(3,int((brown+yellow)**0.5+1)): # h는 세로 길이
        if (brown+yellow)%h==0:
            w=(brown+yellow)/h # w는 가로 길이
            if (w-2)*(h-2)==yellow:
                return [w,h]