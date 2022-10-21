#https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        result=bin(i|j)[2:] # 비트 연산(or) 이용
        result=result.rjust(n,'0')
        answer.append(result.replace('1','#').replace('0',' '))
    return answer

'''
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        answer.append(bin(i|j)[2:].rjust(n,'0').replace('1','#').replace('0',' '))
    return answer
'''