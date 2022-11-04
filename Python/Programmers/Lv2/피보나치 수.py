#https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    fibo=[0,1]
    for i in range(2,n+1):
        fibo.append((fibo[i-1]+fibo[i-2])%1234567) #이전 두 항(fibo[i-1]과 fibo[i-2])을 더한 값을 구하고 나서 아예 1234567로 나눈 나머지를 fibo[i]로 한다.
    return fibo[n]