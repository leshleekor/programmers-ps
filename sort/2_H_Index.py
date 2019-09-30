def solution(citations):
    h = len(citations)
    while True:
        count = 0
        for i in citations:
            if i>=h:
                count+=1

        if count>=h:
            return h

        h-=1

# print(solution([3, 0, 6, 1, 5]))
