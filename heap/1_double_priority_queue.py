import heapq

def solution(operations):
    minheap = []
    maxheap = []
    for i in range(0, len(operations)):
        try:
            if operations[i][0] == 'I':
                heapq.heappush(minheap, (int(operations[i][2:])))
                heapq.heappush(maxheap, (-int(operations[i][2:]), int(operations[i][2:])))

            elif operations[i] == 'D 1':
                a = heapq.heappop(maxheap)[1]
                minheap.remove(a)

            elif operations[i] == 'D -1':
                a = heapq.heappop(minheap)
                maxheap.remove((-a, a))

        except:
            continue


    if len(minheap)==0:
        return [0,0]

    return [heapq.heappop(maxheap)[1], heapq.heappop(minheap)]

# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
# solution(["I 7", "I 5", "I -5", "D -1"])
