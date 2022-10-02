# https://school.programmers.co.kr/learn/courses/30/lessons/12935?language=python3

def solution(arr):
    arr.remove(min(arr))
    if not arr:
        arr.append(-1)
    return arr