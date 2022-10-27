#https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer=0
    i, _sum= 1, 0 # i는 연속된 자연수들의 개수, _sum은 0부터 i-1까지의 합
    while _sum<n:
        if (n - _sum)%i==0: # 연속된 자연수 i개가 k, 1+k, 2+k, ... , i-1+k 의 형태일 경우 (k는 자연수)
            answer+=1
        _sum+=i
        i+=1
    return answer