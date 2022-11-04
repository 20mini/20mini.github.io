#https://school.programmers.co.kr/learn/courses/30/lessons/42577
 
def solution(phone_book):
    prefix_set= set() # 접두어들의 집합
    for i in phone_book:
        for j in range(1,len(i)):
            prefix_set.add(i[:j]) # 접두어들을 추가해준다.
    for i in phone_book:
        if i in prefix_set: # 특정 전화번호와 다른 전화번호의 접두어가 같을 경우
            return False
    return True

'''
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
'''