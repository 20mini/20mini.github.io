#https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    possible=set() # 종이 조각을 붙여 만들 수 있는 수들의 집합
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i): # 순열 이용
            possible.add(int("".join(j)))
    
    # 소수가 아닌 수들 집합에서 제외하기
    possible-={0,1}
    for i in range(2,int(max(possible)**0.5)+1): # 에라토스테네스의 체 이용
        possible-=set(range(i**2,max(possible)+1,i))
    return len(possible)