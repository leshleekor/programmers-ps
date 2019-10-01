def solution(s):
    arr = list(s)
    arr[0] = arr[0].upper()
    for i in range(1, len(arr)):
        if arr[i-1] == ' ':
            arr[i] = arr[i].upper()
        else:
            arr[i] = arr[i].lower()

    answer = ''.join(arr)

    return answer

# solution('3people unFollowed me')
