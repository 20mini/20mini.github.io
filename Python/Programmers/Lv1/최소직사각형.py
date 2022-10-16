#https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    w=[]
    h=[]
    for i in sizes:
        w.append(max(i[0],i[1]))
        h.append(min(i[0],i[1]))
    return max(w)*max(h)