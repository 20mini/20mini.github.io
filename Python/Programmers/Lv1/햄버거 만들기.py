#https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer=0
    li=[]
    for i in ingredient: # 재료를 앞에서부터 하나씩 확인
        li.append(i)
        # li의 마지막 네 개의 원소들을 확인하여 각각 1,2,3,1 이면 그것들을 빼주고 정답을 1 더해준다.
        if len(li)>=4 and li[-4]==1 and li[-3]==2 and li[-2]==3 and li[-1]==1: 
            for _ in range(4):
                li.pop()
            answer+=1
    return answer