#https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    month=[0,31,29,31,30,31,30,31,31,30,31,30,31] # 각 달의 일 수
    day_of_the_week=['FRI','SAT','SUN','MON','TUE','WED','THU']
    gap=0 # 1월 1일과 입력 받은 날의 차이
    for i in range(1,a):
        gap+=month[i]
    gap+=b-1
    return day_of_the_week[gap%7]