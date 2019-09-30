def solution(n):
    f = 0
    s = 1
    m = 0
    for i in range(0, n-1):
        m = f+s
        f = s
        s = m

    return m%1234567
