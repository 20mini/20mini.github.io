#https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer="".join(sorted([str(i) for i in numbers], key=lambda x: x*3, reverse=True)) # 숫자들을 문자열로 만든 다음 정렬한 뒤 이어 붙인다. (기존 문자열을 세 번 이어붙인 문자열을 기준으로 내림차순 정렬)
    if answer[0]=='0': # "00...00" 같은 경우 방지 
        return "0"
    else:
        return answer