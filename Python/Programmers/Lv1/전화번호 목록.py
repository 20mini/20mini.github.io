def solution(phone_book):
    my_set= set()
    for i in phone_book:
        for j in range(1,len(i)):
            my_set.add(i[:j])
    for i in phone_book:
        if i in my_set:
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