#https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    genres_musiclist={} # 각 장르당 노래 리스트
    genres_rank=[] # 장르들의 수록 순위, 앞에 있는 장르부터 순위가 높다
    for i,v in enumerate(genres): # 장르당 노래 리스트 설정
        if not v in genres_musiclist:
            genres_musiclist[v]=[i]
            genres_rank.append(v)
        else:
            genres_musiclist[v].append(i)
    genres_rank.sort(key=lambda x: sum(plays[i] for i in genres_musiclist[x]),reverse=True) # 장르에 속한 노래들의 재생 횟수의 합을 기준으로 장르 순위 설정
    for i in genres_rank:
        genres_musiclist[i].sort(key=lambda x: (plays[x],-x),reverse=True) # 각 장르의 노래들을 재생 횟수와, 번호가 낮은 순으로 수록 순위 설정
        answer.append(genres_musiclist[i][0]) # 순위가 높은 장르부터 재생 횟수가 가장 많은 노래를 베스트 앨범에 추가
        if len(genres_musiclist[i])>=2:
            answer.append(genres_musiclist[i][1]) # 재생 횟수가 두 번째로 많은 노래를 추가
    return answer