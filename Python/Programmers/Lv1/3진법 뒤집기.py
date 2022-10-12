#https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    arr=[]
    while n>0:
        arr.append(n%3)
        n//=3
    answer=0
    for i, k in enumerate(arr):
        answer+=k*(3**(len(arr)-1-i))
    return answer