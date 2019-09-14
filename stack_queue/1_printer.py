def move_last(array, i):
    temp = array[i]
    del array[i]
    array.append(temp)
    return array


def solution(priorities, location):
    length = len(priorities)
    cursor = 0
    while True:
        checked = False
        for j in range(cursor+1, length):
            if priorities[cursor] < priorities[j]:
                priorities = move_last(priorities, cursor)
                checked = True
                if location==cursor:
                    location = len(priorities)-1
                elif cursor<location:
                    location = location-1

                break

        if checked==False:
            cursor=cursor+1

        if cursor>len(priorities):
            break

    return location+1


# solution([2, 1, 3, 2], 2)
# solution([1, 1, 9, 1, 1, 1], 0)
