# N*log(N)
# def solution(scoville, K):
#     answer = 0
#     while True:
#         scoville.sort()
#         if scoville[0] > K:
#             break

#         if scoville[0] < K:
#             if len(scoville)<=1:
#                 return -1
#             elif len(scoville)>1:
#                 answer+=1
#                 min1 = scoville.pop(0)
#                 min2 = scoville.pop(0)
#                 scoville.insert(0, min1+(min2*2))

#     return answer

# N
# def solution(scoville, K):
#     answer = 0
#     while True:
#         min1 = min(scoville)
#         if min1 > K:
#             break

#         if min1 < K:
#             if len(scoville)<=1:
#                 return -1
#             elif len(scoville)>1:
#                 answer+=1
#                 scoville.remove(min1)
#                 min2 = min(scoville)
#                 scoville.remove(min2)
#                 scoville.insert(0, min1+(min2*2))

#     return answer

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while True:
        if heap[0] < K:
            if len(heap) <= 1:
                return -1

            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap)*2))
            answer+=1

        if heap[0] >= K:
            break

    return answer


solution([1, 2, 3, 9, 10, 12], 7)
