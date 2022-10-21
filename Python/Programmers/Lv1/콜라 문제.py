#https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    while n>=a:
        n=n-a+b # 빈병 a개를 소모하여 새 콜라 b개를 받는다. 새 콜라 b개는 다시 빈 병이 된다.
        answer+=b
    return answer