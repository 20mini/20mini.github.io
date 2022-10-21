#https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    pos={1:(0,3),2:(1,3),3:(2,3),4:(0,2),5:(1,2),6:(2,2),7:(0,1),8:(1,1),9:(2,1),0:(1,0)} # 각 번호(문자)의 위치, *의 위치(0,0)을 기준으로 함
    left,right=(0,0),(2,0) # 왼손 엄지와 오른손 엄지의 위치
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            left=pos[i]
        elif i in [3,6,9]:
            answer+='R'
            right=pos[i]
        else:
            if abs(pos[i][0]-left[0])+abs(pos[i][1]-left[1])<abs(pos[i][0]-right[0])+abs(pos[i][1]-right[1]): # 왼손 엄지가 더 가깝다면
                answer+='L'
                left=pos[i]
            elif abs(pos[i][0]-left[0])+abs(pos[i][1]-left[1])>abs(pos[i][0]-right[0])+abs(pos[i][1]-right[1]): # 오른손 엄지가 더 가깝다면
                answer+='R'
                right=pos[i]
            elif hand=='left': # 거리 같은데, 왼손잡이일 경우
                answer+='L'
                left=pos[i] 
            else: # 거리 같은데, 오른손잡이일 경우
                answer+='R'
                right=pos[i]
    return answer