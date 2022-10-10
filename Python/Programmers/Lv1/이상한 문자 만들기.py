# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    isEven=True
    arr=[]
    for i in s:
        if i == ' ':
            arr.append(i)
            isEven=True
        elif isEven:
            arr.append(i.upper())
            isEven=False
        else:
            arr.append(i.lower())
            isEven=True
    return "".join(arr)

"""
이렇게도 가능
def solution(s):
    return " ".join(["".join([letter.upper() if i%2==0 else letter.lower() for i,letter in enumerate(word)]) for word in s.split(' ')])
"""

