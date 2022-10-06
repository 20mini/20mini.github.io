#https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    cost=(2*price+price*(count-1))*count/2
    if cost<=money:
        return 0
    return cost-money