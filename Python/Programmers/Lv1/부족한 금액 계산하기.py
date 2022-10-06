#https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer=(2*price+price*(count-1))*count/2-money
    if answer<=0:
        answer=0
    return answer