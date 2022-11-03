#https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer=1
    clothes_dict={} # (의상의 종류:의상의 개수+1(아무것도 안 입는 경우))
    for i in clothes:
        if i[1] in clothes_dict:
            clothes_dict[i[1]]+=1
        else:
            clothes_dict[i[1]]=2
    for i in clothes_dict.values():
        answer*=i
    return answer-1 # 모든 종류의 의상을 입지 않는 경우 한 가지를 빼준다.