#https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    p_num = int(p) # p를 정수형으로 변환한 값
    
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= p_num: # 부분 문자열을 정수형으로 변환하여 p_num과 비교
            answer+=1
            
    return answer