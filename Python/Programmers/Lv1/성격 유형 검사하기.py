#https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    char_score={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    choice_score={1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    for i,j in zip(survey,choices):
        if j<=3:
            char_score[i[0]]+=choice_score[j]
        else:
            char_score[i[1]]+=choice_score[j]
    answer+='R' if char_score['R']>=char_score['T'] else 'T'
    answer+='C' if char_score['C']>=char_score['F'] else 'F'
    answer+='J' if char_score['J']>=char_score['M'] else 'M'
    answer+='A' if char_score['A']>=char_score['N'] else 'N'
    return answer