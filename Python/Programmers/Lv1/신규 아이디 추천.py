#https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = new_id.lower() # 1단계
    answer=[i for i in list(answer) if i.islower() or i.isdigit() or i=='-' or i=='_' or i=='.'] # 2단계
    answer=[v for i,v in enumerate(answer) if i==0 or v!='.' or (v=='.' and answer[i-1]!='.')] # 3단계
    answer="".join(answer).strip('.') # 4단계
    if len(answer)==0: answer='a' # 5단계
    if len(answer)>=16: answer=answer[:15].rstrip('.')# 6단계
    while len(answer)<=2: answer=answer+answer[-1] # 7단계
    return answer