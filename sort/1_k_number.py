def solution(array, commands):
    result = []
    for arr in commands:
        ars = sorted(array[arr[0]-1:arr[1]])
        result.append(ars[arr[2]-1])
        
    return result


# solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])