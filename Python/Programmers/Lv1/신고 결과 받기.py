#https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer={i:0 for i in id_list}
    report_dict={i:0 for i in id_list} # 누가 얼마만큼 신고당했는지 나타내는 dictionary
    
    for i in set(report):
        report_dict[i.split()[1]]+=1
        
    for i in set(report):
        if report_dict[i.split()[1]]>=k:
            answer[i.split()[0]]+=1
    return list(answer.values())