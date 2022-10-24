#https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=python3

def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")]) #각 단어의 첫 글자를 대문자로 바꿔줌