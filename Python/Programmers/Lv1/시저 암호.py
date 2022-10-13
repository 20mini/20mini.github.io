#https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    li=list(s)
    for i,j in enumerate(li):
        if j==' ':
            continue
        elif j.isupper():
            li[i]=chr(ord(j)+n) if ord(j)+n<=ord('Z') else chr(ord(j)+n-26)
        else:
            li[i]=chr(ord(j)+n) if ord(j)+n<=ord('z') else chr(ord(j)+n-26)
    return "".join(li)