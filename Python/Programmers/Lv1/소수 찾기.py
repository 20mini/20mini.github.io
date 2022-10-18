#https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    is_prime=[True for i in range(n+1)]
    for i in range(2,n+1):
        if is_prime[i]:
            answer+=1
            for j in range(2*i,n+1,i):
                is_prime[j]=False
    return answer

'''
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''