#https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    month=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    day_of_the_week=['THU','FRI','SAT','SUN','MON','TUE','WED']
    gap=0
    for i in range(1,a):
        gap+=month[i]
    gap+=b
    return day_of_the_week[gap%7]