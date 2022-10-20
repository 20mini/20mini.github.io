#https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3

def solution(lottos, win_nums):
    correct=0 # 확정적으로 맞은 번호의 개수
    anything=lottos.count(0) # 아무거나 될 수 있는 번호의 개수
    for i in lottos:
        if i in win_nums: correct+=1
    prize={6:1,5:2,4:3,3:4,2:5,1:6,0:6} # 맞은 개수(key) :등수(value)
    return [prize[correct+anything],prize[correct]]