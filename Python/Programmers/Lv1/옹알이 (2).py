#https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    possible=["aya", "ye", "woo", "ma"] # 발음 가능한 단어들
    for i in babbling:
        flag=True # 연속된 단어가 없는지 판단, 없으면 True
        for j in possible:
            if j*2 in i:
                flag=False
                break
        if flag: # 연속된 단어가 없으면
            for j in possible: # 발음 가능한 단어들을 모두 '.'으로 바꿔준다.
                i=i.replace(j,'.') 
        if i.replace('.',"") == "": # '.'을 공백으로 바꿨을 때 문자열이 비어있으면 정답
            answer+=1
    return answer