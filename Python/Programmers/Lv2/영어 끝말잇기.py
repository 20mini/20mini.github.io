#https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer=[0,0]
    cnt=[0]*n # i-1번 사람이 말한 횟수
    prev=[] # 이전에 나왔던 단어들
    for i,v in enumerate(words):
        cnt[i%n]+=1
        if i==0 or (not v in prev and prev[-1][-1]==v[0]) :
            prev.append(v)
        else:
            answer= [i%n+1,cnt[i%n]]
            break
    return answer