def solution(n):
    count = 0

    while True:
        if n%2 == 0:
            n=n/2
        elif n%2 == 1:
            count+=1
            n = n - 1

        if n == 0:
            break

    return count
