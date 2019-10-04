# 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget-i < 0:
            return answer
        budget-=i
        answer+=1

    return answer

# print(solution([1,3,2,5,4], 9))
# print(solution([2,2,3,3], 10))
