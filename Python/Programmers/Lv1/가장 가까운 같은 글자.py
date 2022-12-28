#https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    letters={} # 각 글자의 가장 마지막 위치를 담은 dictionary
    
    for i,v in enumerate(s):
        if not v in letters: # 해당 글자가 letters 안에 없으면
            answer.append(-1) # 해당 글자가 처음 나왔기 때문에 자신의 앞에 같은 글자가 없음
        else:
            answer.append(i-letters[v]) # 해당 글자의 (현재 위치-마지막 위치)를 리스트에 추가
        letters[v]=i # 마지막 위치 갱신
    return answer