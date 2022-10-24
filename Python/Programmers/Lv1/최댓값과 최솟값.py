#https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3

def solution(s):
    nums=[int(i) for i in s.split()] #공백으로 문자열 분리하여 각 문자열 int()로 정수화
    return str(min(nums))+ ' ' + str(max(nums))