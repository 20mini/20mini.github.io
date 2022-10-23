#https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    answer=''
    x_list,y_list=[X.count(str(i)) for i in range(10)],[Y.count(str(i)) for i in range(10)] # X와 Y가 가진 0~9 숫자의 개수들
    for i in range(9,-1,-1): # 큰 숫자부터 answer에 추가해주도록 한다.
        for _ in range(min(x_list[i],y_list[i])): #x_list[i]와 y_list[i] 중 더 작은 값이 숫자 i의 공통된 개수
            answer+=str(i)
    if answer=="":
        answer='-1' # 반환된 문자열이 비어있으면 '-1' 리턴
    elif answer[0]=='0': # 첫 문자가 '0'이다 == 모든 문자가 '0'으로 이루어져 있다.
        answer='0'
    return answer