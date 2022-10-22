#https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    basket=[]
    for i in moves: # i-1이 열
        for j in range(0,len(board)): #j는 행, j는 0부터~: 맨 윗 줄부터 인형 있는지 확인
            if board[j][i-1]>0:
                basket.append(board[j][i-1]) #바구니 맨 위에 꺼내온 인형 두기
                board[j][i-1]=0 #꺼내온 자리 비우기
                if len(basket)>=2 and basket[-2]==basket[-1]: #바구니 맨 위 2개가 같으면
                    basket.pop() # 맨 위 2개 꺼내기
                    basket.pop()
                    answer+=2
                break # break 까먹지 않도록 주의!!
    return answer