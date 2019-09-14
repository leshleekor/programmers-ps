def solution(heights):
    arrays = list(reversed(heights))
    receiver = []
    for i in range(0, len(arrays)):
        checked = False
        for j in range(i, len(arrays)):
            if arrays[i] < arrays[j]:
                receiver.append(len(arrays)-j)
                checked = True
                break

        if not checked:
            receiver.append(0)

    receiver = list(reversed(receiver))
    return receiver


# solution([6,9,5,7,4])
